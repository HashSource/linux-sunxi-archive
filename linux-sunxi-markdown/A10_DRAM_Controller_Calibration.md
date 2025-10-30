# A10 DRAM Controller Calibration
## Contents
  * [1 Overview of the DRAM controller features affecting the clock speed limit and reliability][1387]
    * [1.1 DQS gate training][1388]
    * [1.2 Impedance settings, ODT and ZQ calibration][1389]
    * [1.3 CLK-DQS timing de-skew, read and write leveling][1390]
    * [1.4 DDR3 timing parameters][1391]
  * [2 Finding optimal DRAM settings for your board or device][1392]
    * [2.1 The software setup and the required tools][1393]
      * [2.1.1 The kernel, rootfs and installing the necessary userland tools][1394]
      * [2.1.2 The bootloader][1395]
      * [2.1.3 General workflow][1396]
    * [2.2 Finding good DQS gating delay settings][1397]
    * [2.3 Finding good impedance settings][1398]
  * [3 Other links][1399]

# Overview of the DRAM controller features affecting the clock speed limit and reliability
This section provides information about DDR3 memory in general and an overview of the relevant configuration features of the A10/A13/A20 DRAM controller. 
## DQS gate training
The DQ data lines and DQS/DQS# strobe lines are used both for sending data to the DRAM chips and also for receiving data back. As a result, the DRAM controller must switch between reading and writing at appropriate times. After sending a read command to the DRAM chip, we are expecting a response with a certain delay. At the time when this response arrives, we need to have the DQS gate open to let the data in. Then after the data is fully received and we need to switch back to writing, the DQS gate has to be closed. To allow a certain level of tolerance to the timing skew, every batch of read operations is surrounded by 0.9 cycle long "preamble" and the 0.3 cycle long "postamble". The gate needs to be open during "preamble" and closed during "postamble". 
An important parameter to be configured is the delay between submitting read commands and opening the DQS gate for getting the responses. It is written to the [SDR_RSLR0/SDR_RSLR1][1400] and the [SDR_RDGR0/SDR_RDGR1][1401] registers, which configure it with 1/4 cycle granularity. Luckily, **this delay can be automatically detected by the hardware** (triggered by setting the [CCR_DATA_TRAINING][1402] bit in the SDR_CCR register). Unluckily, **the automatic detection is a bit flaky and sometimes ends up with unreliable settings** , especially on cold system start (this is a problem only for high DRAM clock frequencies, low frequencies are reasonably safe). So it makes a lot of sense to just identify the optimal DQS gating delay for each board and override the hardware detection with a pre-defined delay in the 'dram_para' struct. 
Other than the delay value itself, we have two types of windowing to select from: 
  * passive (the DQS gate close time is calculated as the gate open time plus the duration of the read operation added)
  * active (the DQS gate is auto-closing, internally implemented by watching for the last rising edge on the DQS line)

The passive windowing mode is activated by setting the [CCR_DQS_GATE][1402] bit in the SDR_CCR register. However accurately hitting the 0.3 cycle long "postamble" is a bit difficult in the passive mode with just 1/4 cycle delay granularity. The active windowing mode exists to address this particular problem and should be preferred. Still there is one good use for the passive windowing mode: that's the process of hardware DQS gate training itself. Since the passive mode has more strict timing requirements, the gating delay value obtained by the hardware DQS gate training is more accurate in passive mode. 
Also the hardware supports DQS gating delay drift compensation (the [CCR_DQS_DRIFT_COMP][1402] bit in the SDR_CCR register) for automatically adjusting it at runtime if necessary. But in reality, experiments show that enabling the drift compensation feature just makes reliability worse and we should avoid it. 
## Impedance settings, ODT and ZQ calibration
The tracks on the PCB connect the DRAM controller with the DDR3 chip(s) and behave like any other wires. Signal integrity may vary really a lot depending on whether the [impedance matching][1403] has been done properly. Both output drive and termination impedance can (and should) be adjusted on both ends of the track. For the memory write operations, we deal with the DRAM controller output drive impedance and the DDR3 termination impedance. And vice versa, for the memory read operations, we deal with the DRAM controller termination impedance and the DDR3 output drive impedance. 
The [ODT][1404] abbreviation means on-die termination. The internal resistors for implementing configurable impedance are located on-die both in the SoC (for the DRAM controller) and in the DDR3 chips. But because the accuracy of the on-die resistors is not so great, they are calibrated against external high precision 240 ohm resistors at the initialization time (both on the DRAM controller side and on the DDR3 chip side) and optionally periodically re-calibrated at run time (on the DDR3 chip side, coupled with the refresh operation). This calibration process against the external resistor is called ZQ calibration. When looking at the device schematics, one can normally find at least two high precision 240 ohm resistors: one connected to the SoC and one connected to the DRAM chip. For example, [A13-OLinuXino-MICRO][1405] has these resistors connected to the DZQ and the ZQ pins. 
The purpose of the ZQ calibration is only to ensure that the configured impedance settings are applied accurately. For example, if we configure the 240/4 ohm termination impedance, then we want to be sure that it is really 60 ohm on every board, regardless of the PVT (process-voltage-temperature) differences. ZQ calibration solves this. **But the selection of optimal impedance divisors is still the responsibility of the user, because they are not configured automatically by the hardware**. For Allwinner A10/A13/A20 based devices, the impedance divisors are specified in the 'dram_para' struct in the u-boot bootloader via the following parameters: 
  * the '**zq'** and the '**odt_en'** variables (see the [SDR_ZQCR0][1406] register) for the impedance on the DRAM controller end of the wire
  * the '**emr1'** variable (see the description of the MR1 configuration register bits in the DDR3 spec or the DRAM datasheet) for the impedance on the DDR3 chip end of the wire

  
Additional references: 
  * [DDR3 Dynamic On-Die Termination][1407]
  * [DDR3 ZQ Calibration][1408]
  * [Altera - DDR2, DDR3, and DDR4 SDRAM Board Design Guidelines][1409]
  * [CTS Electronic Components - Clock Termination Techniques and Layout Considerations][1410]

## CLK-DQS timing de-skew, read and write leveling
In the case of PCB tracks length mismatch, there may be some timing skew between the CMD/ADD/CLK, DQ and/or DQS/DQS# signals. Some general overview can be found in the [New Features of DDR3 SDRAM][1411] pdf. Also the [Altera - Utilizing Leveling Techniques in DDR3 SDRAM Memory Interfaces][1412] pdf is quite interesting even though it talks about a different DRAM controller and is not directly applicable. 
The A10/A13/A20 DRAM controller has a lot of knobs to configure various delays, even up to an individual bit level. **However, the DRAM controller does not implement any hardware assistance for automatic read/write leveling at all.** So we are up to using some other method for exploring the vast space of possible configurations to find the one, which works the best. If a good configuration for the delay adjustments is identified, then we can hardcode it into the 'dram_para' struct in the u-boot bootloader for each board type. 
Right now, all the delays related configuration is exposed as the '**tpr3'** variable in the 'dram_para' struct. This variable is a hexadecimal number, composed of the following bit-fields: 
  * bits [22:20] - mapped to [MFWDLY][1413] bits of the command lane
  * bits [18:16] - mapped to [MFBDLY][1413] bits of the command lane
  * bits [15:12] - mapped to [SDPHASE][1413] bits of the byte lane 3
  * bits [11:8] - mapped to [SDPHASE][1413] bits of the byte lane 2
  * bits [7:4] - mapped to [SDPHASE][1413] bits of the byte lane 1
  * bits [3:0] - mapped to [SDPHASE][1413] bits of the byte lane 0

Basically, adjusting bits 22:16 in the 'tpr3' parameter tweaks delays on the command lane. Because the relative delay between the signals on the command lane and the signals on the byte lanes changes, this also effectively adjusts the delays for both **write** and read operations. Also adjusting bits 15:0 in the 'tpr3' parameter allows to postpone or move forward the sampling of incoming data for **read** operations (relative to the default 90 degrees phase). Since we can control both read and write delays almost independently from each other, the 'tpr3' parameter is good enough for simple de-skew adjustments. There are also other delay related knobs in the DRAM controller, but they are not exposed in the 'dram_para' struct yet. 
## DDR3 timing parameters
The description of DDR3 DRAM modules sometimes includes a sequence of 4 numbers separated by dashes, for example DDR3-1333 9-9-9-24. These four numbers are the values of tCAS-tRCD-tRP-tRAS parameters, which are most important for performance (lower is better). But there are more parameters than just these four. A complete list of timing parameters and their possible values can be found in the DDR3 spec (for the standard speed bins) and also in the datasheet of each DRAM chip in the case if the chip can support tighter timings than required by the DDR3 standard. The A10/A13/A20 DRAM controller registers [SDR_TPR0][1414], [SDR_TPR1][1415] and [SDR_TPR2][1416] are used to configure these timing parameters. Please note that the DRAM controller expects these parameters in cycles, and DRAM datasheets usually provide them in nanoseconds. So a conversion is necessary to configure this right. 
This configuration is provided by the '**tpr0'** , '**tpr1'** , '**tpr2'** parameters in the u-boot 'dram_para' struct, which are directly written to the corresponding hardware registers on DRAM initialization. 
# Finding optimal DRAM settings for your board or device
The DRAM controller overview in the previous chapters contains some parts of text, which are highlighted in red. Basically, they say that the A10/A13/A20 DRAM controller is missing decent automatic DDR3 configuration features, enjoyed by the high-end ARM or x86 desktop systems. And using a bad configuration or just keeping the defaults does not allow reaching really high DDR3 clock speeds. 
To overcome this hardware limitation and in order to allow significantly faster DRAM clock speeds, we essentially [brute-force search][1417] for a good configuration using the [lima-memtester][1418] program as a tool to evaluate and compare reliability of different settings. This method can be used by anyone and does not require any special lab equipment, simulation software or anything else. However hardcoding the impedance and delays is not a perfectly universal solution. **The optimal DRAM settings, found with this method, can be only used just for a single device model (and even limited to a single PCB revision in some cases).**
The next chapters contain the description of the exact step by step procedure. Be warned that it is a very long iterative process and may take up to a week to find something useful! But the results typically pay off and reward you with much better memory performance. 
Obviously, if somebody else has already done this work for the same device model, then you can just verify the settings with lima-memtester on your device and take them into use. Either way, sharing test results is very much welcome (both positive and negative results are useful!). So that we can collect sufficient statistics and eventually enable better DRAM settings in U-Boot. 
## The software setup and the required tools
### The kernel, rootfs and installing the necessary userland tools
It is required to have the **sunxi-3.4 kernel** (specifically for for the mali kernel module). The mainline kernel is not supported yet because it is lacking in the graphics department. Also the process of probing different dram setting involves a lot of watchdog triggered reboots, which may corrupt the file system pretty fast. So it is strongly recommended to setup **boot over the network** [using the NFS root file system][1419]. **Any other configurations are only going to bring unnecessary troubles and are completely unsupported by this guide.**
Once the system is up and running, we need to install some prerequisites: **git** , **cmake** and the **ruby** scripting language interpreter. For example, on a Debian/Ubuntu distro it would be: 
[code] 
       apt-get install git cmake ruby
    
[/code]
And then compile and install the [lima-memtester][1418] and [a10-dram-tools][1420]: 
[code] 
       cd /tmp
       git clone <https://github.com/ssvb/lima-memtester.git>
       cd lima-memtester
       cmake -DCMAKE_INSTALL_PREFIX=/usr .
       make -j2 install
    
[/code]
[code] 
       cd /tmp
       git clone <https://github.com/ssvb/a10-dram-tools.git>
       cd a10-dram-tools
       cmake -DCMAKE_INSTALL_PREFIX=/usr .
       make -j2 install
    
[/code]
Installing into /usr is not very nice, because it is the place, where software is usually installed by the distro package managers. Anyway, this whole setup is primarily intended just for the DRAM calibration process, so not a big deal. 
### The bootloader
The DRAM settings are configured in U-Boot. And we are going to use the [Mainline U-boot][1421] because it makes no sense to use anything else. In the mainline U-Boot, changing the DRAM settings needs to be done in the defconfig files for each board. For example, higher DRAM clock speed settings for the Cubieboard [(528MHz, zq=0x3B, emr1=0x04)][1422] may look like this: 
[code] 
    CONFIG_SPL=y
    CONFIG_SYS_EXTRA_OPTIONS="AXP209_POWER,SUNXI_EMAC,AHCI,SATAPWR=SUNXI_GPB(8),USB_EHCI"
    CONFIG_FDTFILE="sun4i-a10-cubieboard.dtb"
    CONFIG_ARM=y
    CONFIG_ARCH_SUNXI=y
    CONFIG_MACH_SUN4I=y
    CONFIG_DRAM_CLK=528
    CONFIG_DRAM_ODT_EN=3
    CONFIG_DRAM_ZQ=17688576
    CONFIG_DRAM_TPR3=0
    CONFIG_DRAM_EMR1=4
    CONFIG_DRAM_DQS_GATING_DELAY=0x06060606
    CONFIG_DRAM_TIMINGS_DDR3_1066F_1333H=y
    
[/code]
Additionally, the dcdc3 voltage has to be currently [patched in the U-Boot sources][1423] if the default 1.25V is too low for the high DRAM or MBUS clock speed. Modern u-boot can be configured with CONFIG_AXP_DCDC3_VOLT=1300. After changing the settings, recompiling u-boot and rebooting, be sure that the changes have in fact taken effect by running 
[code] 
       a10-meminfo
    
[/code]
If video support is enabled in U-Boot, then the sunxi-3.4 kernel appears to fail booting properly from time to time (it gets stuck after roughly 10 or 20 reboots at least on [LinkSprite pcDuino V2][1424] board). And this is a major annoyance when using the 'a10-tpr3-scan' script. In order to workaround this problem, the following line can be added to the board defconfig in U-Boot: 
[code] 
    # CONFIG_VIDEO is not set
    
[/code]
### General workflow
After all the tools are installed, network boot configured, u-boot built with some preliminary DRAM settings and the system is booted, we want to assess the reliability of the resulting configuration. Just running the lima-memtester tool for some reasonable period of time can provide only a PASS or FAIL verdict. Having just two possible states is not enough to grade the reliability of many different DRAM configurations, and this makes it difficult to select the best one. 
To provide a better insight about the reliability of the current DRAM configuration, a special **a10-tpr3-scan** script had been developed. It exploits the fact that some of the configuration knobs (the **tpr3** parameter) can be actually changed at runtime without resetting the DRAM controller, and this configuration adjustment can be done from the userspace via /dev/mem (this is actually not completely reliable, but works in most cases and is good enough for the DRAM calibration purposes). Essentially, this script needs to be set to run automatically after reboot. So that it can start probing different 'tpr3' settings, and using the lima-memtester program to verify reliability of each of these settings. This can be done by adding a shell script into some special distribution dependent place ([Debian][1425], [Gentoo][1426], ...). This script may contain something like this (assuming that 192.168.1.123 is the ip address of the device): 
[code] 
       if [ "`ifconfig | grep 192.168.1.123`" ] ; then
           mkdir /var/tpr3_results
           # If the board has LEDs, then you can also toggle one of them here (this may help troubleshooting)
           a10-tpr3-scan /var/tpr3_results "Cubietruck"
       fi
    
[/code]
The /var/tpr3_results is a directory for storing the collected data. After several hours and many automatic reboots, the data should be there. This data can be then processed by another script **a10-tpr3-html-report** to get a nicely formatted html report: 
[code] 
       a10-tpr3-html-report /var/tpr3_results > /var/tpr3_results/report.html
    
[/code]
The html report can also generated even for the partially collected data, so there it is possible to watch the progress in real time from your desktop PC (where the data is actually stored): 
[code] 
       while sleep 15 ; do a10-tpr3-html-report /nfs/exported/var/tpr3_results > /nfs/exported/var/tpr3_results/tmp.html ; mv /nfs/exported/var/tpr3_results/tmp.html /nfs/exported/var/tpr3_results/report.html ; done;
    
[/code]
Just be sure to set the permissions right for it to work. Then open /nfs/exported/var/tpr3_results/report.html in your favourite browser and keep refreshing. Here is an example of a generated report: 
**Cubietruck, (zq=0x2c, emr1=0x42), 648MHz DRAM and 600MHz MBUS, needs at least 1.325V dcdc3**
| dcdc3_vol = 1325  
dram_clk = 648  
mbus_clk = 600  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 8  
dram_bus_width = 32  
dram_cas = 9  
dram_zq = 0x2c (0x10d3900)  
dram_odt_en = 3  
dram_tpr0 = 0x429899b4  
dram_tpr1 = 0xa0a0  
dram_tpr2 = 0x2c200  
dram_tpr3 = 0x182222  
dram_emr1 = 0x42  
dram_emr2 = 0x10  
dram_emr3 = 0x0  
dqs_gating_delay = 0x07070707  
active_windowing = 1  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x072222| 0x071111| 0x070000| 0x07EEEE| 0x07DDDD  
**0x06**|  0x063333| 0x062222| 0x061111| 0x060000| 0x06EEEE| 0x06DDDD  
**0x05**|  0x0533**3** 3| 0x052222| 0x051111| 0x050000| 0x05EEEE| 0x05DDDD  
**0x04**|  0x0433**3** 3| 0x042222| 0x041111| 0x0400**0** 0| 0x04EEEE| 0x04DDDD  
**0x03**|  0x0333**3** 3| 0x032222| 0x031111| 0x0300**0** 0| 0x03EEEE| 0x03DDDD  
**0x02**|  0x0233**3** 3| 0x022222| 0x021111| 0x0200**0** 0| 0x02EEEE| 0x02DDDD  
**0x01**|  0x0133**3** 3| 0x012222| 0x011111| 0x010000| 0x01EE**E** E| 0x01DDDD  
**0x00**|  0x0033**3** 3| 0x002222| 0x001111| 0x000000| 0x00EE**E** E| 0x00DDDD  
**0x08**|  0x0833**3** 3| 0x082222| 0x081111| 0x080000| 0x08**E** EEE| 0x08DDD**D**  
**0x10**|  0x103333| 0x102222| 0x101111| 0x100000| 0x10**E** EEE| 0x10DDDD  
**0x18**|  0x183333| 0x182222| 0x181111| 0x180000| 0x18EE**E** E| 0x18DDDD  
**0x20**|  0x20**3** 333| 0x202**2** 22| 0x201111| 0x20**0** 000| 0x20EEEE| 0x20DDDD  
**0x28**|  0x28333**3**|  0x28222**2**|  0x28111**1**|  0x28000**0**|  0x28EEE**E**|  0x28DDDD  
**0x30**|  0x30333**3**|  0x3022**2****2**|  0x30111**1**|  0x30000**0**|  0x30EEEE| 0x30DDDD  
**0x38**|  0x38333**3**|  0x382222| 0x38111**1**|  0x38000**0**|  0x38EEEE| 0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [bitflip=19, solidbits=12]  
  
Total number of successful memtester runs: 235  
  
Best luminance at the height 0.5 is above 0x081111, score = 0.742  
Best luminance at the height 1.0 is above 0x081111, score = 0.634  
Best luminance at the height 2.0 is above 0x081111, score = 0.512  
Best luminance at the height 3.0 is above 0x081111, score = 0.440  
  
Read errors per lane: [3, 0, 12, 2]. Lane 1 is the most noisy/problematic.  
Errors from the lane 0 are not intersecting with the errors from the worst line 1.  
Errors from the lane 3 are not intersecting with the errors from the worst line 1.  
  
Write errors per lane: [1, 1, 2, 11]. Lane 0 is the most noisy/problematic.  
Errors from the lane 1 are 50.0% eclipsed by the worst lane 0.  
Errors from the lane 2 are not intersecting with the errors from the worst line 0.  
Errors from the lane 3 are not intersecting with the errors from the worst line 0.  
  
Collecting a few of such reports for different dram settings, we can select a more reliable configuration among them (with larger 'green' areas and higher scores). 
## Finding good DQS gating delay settings
The '**dqs_gating_delay'** parameter, reported by the 'a10-meminfo' tool, is automatically detected by the DRAM controller by default. It is usually good enough at low dram clock frequencies (around ~400MHz). However at high dram clock frequencies (getting close to ~600MHz), it may become a potential reliability hazard in the case of a possible autodetection glitch. The autodetection also happens to be sensitive to the chip temperature, so we may get substantially different values on cold start vs. the values obtained on reboot immediately after running some heavy workload. 
The unstable DQS gating delay autodetection also has some inconveniences for the 'a10-tpr3-scan' tool, which (rightfully) treats different 'dqs_gating_delay' settings as different unique dram configurations. This results in collecting statistics for multiple dram configurations instead of just one and slowing down the whole process significantly. 
As a solution, the 'dqs_gating_delay' parameter can be hardcoded in the 'dram_para' struct. The most common autodetected value (reported by 'a10-meminfo' tool) can be used for this parameter. Or alternatively, one can try to experimentally find the borderline low and borderline high 'dqs_gating_delay' values and just average them. We don't need to care about the accuracy of this selection if the 'active_windowing' parameter is set to 1, but only need to safeguard against the potential pathologically bad autodetection results. The optimal 'dqs_gating_delay' value depends on the dram clock frequency, so a bit of care still needs to be taken in the case of increasing or reducing the dram clock frequency significantly. 
The 'dqs_gating_delay' parameter does not affect reliability in any other way (does not play together or interfere with the other dram settings) as long as it is within a tolerable range. So there is no point wasting too much time selecting the best possible value, it only needs to be good enough. 
## Finding good impedance settings
First of all, we may want to configure the '**emr1'** parameter, which initializes the MR1 register (the description can be found in the DDR3 spec) and controls impedance settings on the DDR3 chip side. The 'Rtt_Nom' parameter is encoded in bits 9, 6 and 2 of the MR1 register. The 'Output Driver Impedance Control' parameter is encoded in bits 5 and 1 of the MR1 register. This provides us with a number of possible configurations (RZQ is normally 240 ohm): 
dram_emr1  | Rtt_Nom  | Output driver impedance   
---|---|---  
0x00  | disabled  | RZQ/6   
0x02  | disabled  | RZQ/7   
0x04  | RZQ/4  | RZQ/6   
0x06  | RZQ/4  | RZQ/7   
0x40  | RZQ/2  | RZQ/6   
0x42  | RZQ/2  | RZQ/7   
0x44  | RZQ/6  | RZQ/6   
0x46  | RZQ/6  | RZQ/7   
We just need to try each of these 'emr1' values from the table and get 'a10-tpr3-scan' results for them. Here is an example of doing the [ initial 'emr1' selection for cubieboard1][1427]. Starting with 'emr1' is a good idea because it has only a limited number of valid and/or interesting states (unlike somewhat more flexible 'zq' settings). 
Next we need to configure the '**zq'** parameter, which initializes impedance settings on the DRAM controller side. It is a 8-bit value, where the higher 4 bits are responsible for the termination impedance (similar to Rtt_Nom), and the lower 4 bits are responsible for the output driver impedance. These lower/higher parts of 'zq' are most likely the divisors for RZQ. We have no idea what the value of 0 would mean (is it reserved? or maybe the divisors are just encoded as 1-16 values instead of 0-15?). In any case, what we have is a space of 256 values (or a bit less if we exclude zeros) to try brute-forcing. The higher and lower 4-bit 'zq' parts can be tried with the 'a10-tpr3-scan' tool independently, starting from something around **0x2c** or **0x3b** as the initial 'zq' approximation. The default reset value **0x7b** is typically a bad choice and just regresses reliability. In order for this all to have effect, we need to also set the '**odt_en'** parameter to **3, or "y"** in the current mainline u-boot. The 'zq' parameter selection is also demonstrated in the [ impedance configuration example][1428]. 
ZQ parameter interpretation from the TI Keystone2 manual (spruhn7b.pdf)  dram_zq (ZPROG)  | On-die termination impedance  | Output driver impedance   
---|---|---  
0x2b  | 120 ohms  | 40 ohms   
0x2d  | 120 ohms  | 34 ohms   
0x5b  | 60 ohms  | 40 ohms   
0x5d  | 60 ohms  | 34 ohms   
0x8b  | 40 ohms  | 40 ohms   
0x8d  | 40 ohms  | 34 ohms   
The divisors, which are encoded in ZPROG (a two-digit hex number) are are not used directly by the hardware, but first get calibrated into ZDATA (a five-digit hex number) by the DRAM controller. One can search for ZPROG, ZDATA and ZCTRL in the [A10 DRAM Controller Register Guide][1429] to find more details. Examples of ZQ calibration results (PROG -> ZDATA conversion): 
Device  | ZPROG (two-digit 'zq' parameter)  | Calibrated ZDATA on cold start (SoC temperature is low)  | Calibrated ZDATA on hot reboot (SoC temperature is high)   
---|---|---|---  
ssvb's Cubietruck  | 0x2c  | 0x10d1800  | 0x10d3900   
ssvb's Primo73  | 0x2b  | 0x10de800  | 0x10d6900   
ssvb's Cubieboard  | 0x2b  | 0x10dcb00  | 0x10de800   
ssvb's Cubieboard  | 0x3b  | 0x199cb00  | 0x199e800   
It is possible to use ZDATA directly in the CONFIG_DRAM_ZQ U-Boot defconfig variable instead of ZPROG, skipping the calibration step. Because the calibration process is not always deterministic and depends on the temperature among other things, it may make sense to prefer the ZDATA style configuration. 
# Other links
Some links, which are not directly describing sunxi hardware, but may be useful for grasping the general concept: 
  * [Altera - Utilizing Leveling Techniques in DDR3 SDRAM Memory Interfaces][1412]
  * [Freescale - i.MX 6 Series DDR Calibration][1430]
  * [DDR3 introduction slides][1431]
  * [Samsung - Mobile DRAM’s Frequently violated parameters Application Note][1432]
  * [Altera - Using External Memory Interfaces to Achieve Efficient High-Speed Memory Solutions][1433]

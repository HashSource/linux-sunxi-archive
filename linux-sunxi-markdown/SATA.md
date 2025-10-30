# SATA
An integrated [Serial ATA][47872] interface is available on Allwinner [A10][47873], [A20][47874] and [R40][47875] SoCs. 
## Contents
  * [1 Specifications][47876]
  * [2 Performance][47877]
    * [2.1 Current state][47878]
    * [2.2 Measuring performance / interpreting numbers][47879]
  * [3 Port multipliers][47880]
    * [3.1 PMP support - using SATA port multipliers with sunxi devices][47881]
    * [3.2 Caveats][47882]
  * [4 Mechanical quality][47883]
  * [5 Devices with SATA ports][47884]
  * [6 See also][47885]

## Specifications
From **A10** EVB Manual[[1]][47886]: 
  * Supports SATA 1.5Gb/s, and SATA 3.0Gb/s
  * Compliant with SATA Spec. 2.6, and [AHCI][47887] Revision 1.3 Specifications
  * Supports industry-standard AMBA High-Performance Bus (AHB) and it is fully compliant with the AMBA Specification, Revision 2.0.
  * Supports 32-bit Little Endian
  * OOB signaling detection and generation
  * SATA 1.5Gb/s and SATA 3.0Gb/s speed negotiation when Tx OON signaling is selected
  * Supports device hot-plugging
  * Support power management features including automatic Partial to Slumber transition
  * Internal DMA Engine for Command and Data Transactions
  * Supports hardware-assisted [Native Command Queuing][47888] (NCQ) for up to 32-entries
  * Support external SATA (eSATA)

The **A20** user manual[[2]][47889] lists identical SATA/AHCI interface features. 
## Performance
This section is work in progress
### Current state
SATA sequential throughput is unbalanced for unknown reasons: With appropriate [cpufreq][47890] settings it's possible to get sequential read speeds of +200 MB/s while write speeds retain at approx. 45 MB/s. This is caused by wrong dma settings in the original allwinner driver, that was copied in the mainline kernel. See also relevant message in lkml: <https://lkml.org/lkml/2019/5/12/84>
Unlike other platforms sequential SATA transfer rates on A10/A20/R40 scale somewhat linearly with both [cpufreq settings][47890] and DRAM clock. In case you use the wrong cpufreq settings it's impossible to achieve maximum SATA performance (eg. using the _ondemand_ governor without _[io_is_busy][47891]_ setting). 
On the dual-core A20 setting both _CONFIG_SCHED_MC=y_ and _CONFIG_SCHED_SMT=y_ at kernel compile time seems to increase SATA throughput (sequential reads +10 MB/s). Please be aware that this still needs to be confirmed. 
Also worth a look are Linux' [I/O schedulers][47892]. If your SATA disk is available as _/dev/sda_ you can query _/sys/block/sda/queue/scheduler_ to get the list of available I/O schedulers (the active printed in brackets) and change the scheduler either globally by supplying _elevator=deadline_ to [bootargs][47893] environment or on a per device basis using _echo deadline >/sys/block/sdN/queue/scheduler_ (deadline seems to be the most performant scheduler on A10/A20) 
Since irqbalancing isn't working on sunxi/ARM one way to get better SATA throughput on A20/R40 devices is to assign all AHCI/SATA IRQs away from the 1st CPU core using something like 
[code]
    echo 2 >/proc/irq/$(awk -F":" '/ahci/ {print $1}' </proc/interrupts)/smp_affinity
[/code]
### Measuring performance / interpreting numbers
It should ne noted that 'passive benchmarking' especially with slow ARM devices often goes wrong ('passive' in contrast to [**active** benchmarking][47894] where the goal is to produce insights and not just numbers). You should always ensure that you have an eye on CPU utilization (use 'htop' in another shell, run 'iostat 5' in another, check cpufreq/governor) since many storage benchmarks get bottlenecked by CPU. This is somewhat different on SoCs that are made for this purpose (eg. from Marvell, please see [this thread for some numbers][47895]) but with Allwinner SoCs it's always an issue. 
This also affects how to interpret results: if you take [this comparison][47896] of A20 SATA performance and A64 [USB/UAS][47897] performance for example then random IOPS numbers look pretty close or A64's UAS mode even seems to outperform A20's SATA implementation. But by looking at CPU utilization it's obvious that this test is tampered by CPU performance/utilization since all CPU cores run with 90% or above. Pine64 has 4 cores running at 1152 MHz while A20 was running dual-core at 960 MHz. By repeating this test with R40 (quad-core up to 1.2GHz) SATA will outperform USB for sure since the CPU bottleneck is gone. And the same reason why this synthetic benchmark shows lower numbers for A20/SATA compared to A64/USB won't affect 99.9% of real-world use cases at all: since in real-world scenarios random accesses do not happen constantly but just from time to time and then SATA should always outperform USB due to less overhead. 
## Port multipliers
A [port multiplier][47898] allows to connect multiple SATA devices to a single SATA host port. Since [ sunxi devices with SATA][47899] are restricted to only one port, support for the port multiplier protocol (PMP) is a desirable feature. However, this requires suitable hardware (SATA controller) and software (AHCI driver). 
### PMP support - using SATA port multipliers with sunxi devices
  * [A10][47873] is frequently said not to support PMP due to hardware limitations and/or older SATA specification. But some documents (A10 EVB manual) indicate capabilities identical to the A20 (see above), and a [patch submission][47900] from Hans de Goede suggests he tested PMP with both A10- and A20-based devices.
  * The [A20][47874]'s SATA controller is confirmed to support PMP from a variety of sources. It only supports the slower [Command-based switching][47901] and not the faster [FIS-based mode][47902].
  * [R40/V40 also support port multipliers][47903] (it's the same simple `AHCI_HFLAG_NO_PMP` flag that has to be set/removed and performance is as low as with A20).

Originally the _sunxi_ahci_ driver derived from Allwinner sources deliberately disabled PMP by always indicating `AHCI_HFLAG_NO_PMP`. The reason probably was that while the A20 can do PMP, enabling it breaks compatibility with single drive (non-PMP) mode - so the two are mutually exclusive. (The patch mentioned above states this is due to an inability to issue a proper soft reset to a single drive after port multiplier mode gets enabled.) 
A workaround is to compile the driver as a module, and use the `enable_pmp=1` option as desired at load time (_/etc/modprobe.d/ahci-sunxi.conf_ in most distros) or adding `ahci_sunxi.enable_pmp=1` to kernel parameter with mainline kernel. 
### Caveats
If you rely exclusively on a port multiplier to access multiple drives, you're introducing a [single point of failure][47904] (SPoF). Using this technology in an attempt to increase reliability (e.g. by constructing a RAID array) therefore is questionable. 
Cheap port multipliers like JMB321/JMB393 are prone to overheating under load and then start to corrupt data or stop working at all. This adds significantly to the SPoF problem since if you build a RAID on top of such a port multiplier setup, the likelihood that you lose your whole array when you would need it will increase dramatically - as running a rebuild (after replacing a failed disk) will put significant stress on the system. Combining cheapest/unreliable components to increase reliability might work in some cases, but definitely not with PM based RAID. 
## Mechanical quality
Always keep in mind that all SATA implementations on sunxi devices rely on _internal_ SATA connectors. Unlike [eSATA][47905] these connectors are specified for only 50 matings and cheap cables/connectors die way earlier or start to corrupt data. SATA uses a relatively primitive checksum mechanism (ICRC – Interface [Cyclic Redundancy Check][47906]) to detect data corruption on the wire. The corresponding [S.M.A.R.T.][47907] attribute is 199 (unfortunately disk series exist where this counter does not increase when CRC errors occur – the value remains 0). If you exchanged cables/disks or notice that SATA performance dropped dramatically (due to a huge amount of data retransmits) it's always a good idea to check this attribute using _smartctl_ (contained in the [smartmontools][47908] package). If the counter increases something's wrong with the interconnection disk to SoC. 
## Devices with SATA ports
[Anichips PhoenixA20][47909]
[Cubietech Cubieboard][47910]
[Cubietech Cubieboard2][47911]
[Cubietech Cubietruck][47912]
[Cubietech Cubietruck Plus][47913]
[Foxconn Super Pi][47914]
[In-Circuit ICnova A20][47915]
[Itead Iteaduino Plus][47916]
[Jesurun Q5][47917]
[Lamobo R1][47918]
[LeMaker Banana Pi][47919]
[LeMaker Banana Pro][47920]
[LinkSprite pcDuino3][47921]
[LinkSprite pcDuino3 Nano][47922]
[MarsBoard A10][47923]
[MarsBoard A20][47924]
[MarsBoard A20-SOM][47925]
[Mele A1000][47926]
[Mele M5][47927]
[Merrii Hummingbird A20][47928]
[Olimex A10-OLinuXino-Lime][47929]
[Olimex A20-OLinuXino-Lime][47930]
[Olimex A20-OLinuXino-Lime2][47931]
[Olimex A20-OLinuXino-Micro][47932]
[Olimex A20-SOM][47933]
[Sinovoip Banana Pi BPI-6204][47934]
[Sinovoip Banana Pi M2 Berry][47935]
[Sinovoip Banana Pi M2 Ultra][47936]
[Sunchip CX-A99][47937]
[Xunlong Orange Pi][47938]
[Xunlong Orange Pi Mini][47939]
## See also
  * [Sata multiplier with A20][47940] thread on linux-sunxi mailing list
  * [Support status of SATA port multipliers connected to A20][47941] thread on LeMaker forum (recommended reading with some in-depth information)
  * [Sunxi devices as NAS][47942]

References: 
  1. [↑][47943] <http://dl.cubieforums.com/files/pdf/A10_development_board_user_manual--2011.9.23_English.pdf>
  2. [↑][47944] <https://github.com/allwinner-zh/documents/tree/master/A20/>

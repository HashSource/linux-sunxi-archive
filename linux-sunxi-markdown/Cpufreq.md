# Cpufreq
## Contents
  * [1 Basics][13300]
  * [2 Possible adjustments][13301]
  * [3 Performance/functionality impacts][13302]
    * [3.1 The "performance" governor][13303]
    * [3.2 The "ondemand" governor][13304]
  * [4 Practical impact on temperature/consumption][13305]
  * [5 "Overclocking"][13306]
  * [6 Troubleshooting][13307]
    * [6.1 No /sys/devices/system/cpu/cpu0/cpufreq][13308]

## Basics
Since the main market for Allwinner are mobile devices it is one of the design goals of their SoCs (System on chip) to be able to operate both performant as well as energy efficient. An important role plays 'cpu frequency scaling'. The lower the clock speed, the slower the device and the less energy it consumes (and vice versa). Even the voltage available to the ARM core(s) will be adjusted depending on the clock speed. This is done inside the kernel by defining _operating-points_ , which provide mapping between clock speeds and voltages (the higher the CPU is clocked the more voltage it needs to still operate reliable). Depending on the kernel version, the operating points can be hardcoded in the kernel sources (the sunxi-3.4 kernel on [A10][13309]), defined in the FEX file (the sunxi-3.4 kernel on [A20][13310]) or stored in the device tree blob (the mainline kernel). 
It's not enough to define a set of CPU frequency/voltage mappings and upper/lower limits but also strategies to switch between them are needed. These so called [cpufreq governors][13311] are responsible for that. If your kernel supports cpu frequency scaling you can get the list of available governors and dvfs_table-mappings/operating-points by: 
[code] 
    cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors
    cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies
[/code]
## Possible adjustments
Out of the available governors the most interesting seem to be _ondemand_ and _interactive_ since they dynamically switch cpufreq settings based on load. The _interactive_ governor is only available in the sunxi-3.4 kernel, because it is a simple pragmatic enhancement of the _ondemand_ governor, tailored for Android and shipped on millions of devices. It was [submitted to the mainline kernel][13312] but never accepted, because the _ondemand_ governor itself is [considered to be broken][13313] [by design][13314] (the "waking up to decide whether the CPU is idle" concept) and polishing a turd was not welcome. So the default with mainline kernel is now _ondemand_ (you can adjust that by writing to _scaling_governor_) and the lower/upper limits are 144000 and 960000 on sun7i (144MHz-960MHz). Since the default lower limit might be responsible for a laggy system (it takes quite a bit of time for the governor to realize that the frequency needs to be increased) it's advisable to define the lower limit yourself adjusting _/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq_ eg. 
[code] 
    echo 408000 >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq
[/code]
You can also lower the maximum value by adjusting _scaling_max_freq_. Please be aware that adjusting these values works in 48MHz steps and is not limited to the few operating-points/dvfs_table-entries. You can use any value in between min/max but have to keep in mind that the values supplied will be rounded down: you will end up with just 864MHz if you set _scaling_max_freq_ to 911999 instead of 912000 -- always compare with _cpuinfo_cur_freq_ if in doubt. 
## Performance/functionality impacts
Both the chosen governor as well as the cpufreq limits can have a huge impact on power consumption, performance and even functionality. For example in the past on sun7i (A20), the default _fantasy_ governor led to really strange behaviour (and single-threaded benchmark results for A20 devices as well) since it increased the clock speed to the max value only under certain circumstances and remained most of the time at the minimum. 
### The "performance" governor
If the lowest possible power consumption no matter the cost is not a priority, then the _performance_ governor is a very good option. The practical [tests][13315] [show][13316] that there is not much power consumption difference between idling at 60MHz and idling at 1008MHz (a ~1.5x difference on Cortex-A8, almost no difference on Cortex-A7). Modern processors implement advanced clock gating for power saving purposes and if the processor is sitting on a [WFI instruction][13317], then the power consumption is already significantly reduced regardless of the CPU clock speed. 
Please note that voltage/frequency scaling is still relevant even for the _performance_ governor. Just because we need to be able to do emergency throttling in the case of overheating. Peak power consumption of CPU, GPU and other peripherals all working at the same time may be rather high and it's best to be prepared for the worst case scenario. 
To sum it up. Idle power consumption with the _performance_ governor is almost as good as when using other governors. And if there is work to do, then finishing it quickly is not a bad option either (the "race to idle" concept). If you are unsure and the device is not battery powered, then save yourself from a lot of troubles and just use the _performance_ governor. If you are running benchmarks and want to have reproducible results without any unexpected glitches or pathological slowdowns, then the _performance_ governor is also a good choice. 
### The "ondemand" governor
If you allow very low _scaling_min_freq_ values with ondemand/interactive the system might behave laggy and some timing critical stuff (eg. reading out Dallas DS18b20 temperature sensors via 1-wire below 600MHz) won't work. Same applies to other sort of GPIO stuff when reaching the upper frequency limits (eg. reading out DHT11/DHT22 with _scaling_max_freq_ above 1008MHz). So you've to carefully adjust the cpufreq settings to your application. 
If you need maximum performance then using the governor with this name might be a good idea. But since then the CPU core(s) will always be clocked at the upper limit (speed/voltage) it's better to use ondemand with reasonable settings if you only need peak performance from time to time. A good compromise between power consumption and a responsive system being able to operate at full performance when needed is 
[code] 
    #!/bin/sh
    
    echo ondemand > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
    
    echo 1008000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq
    echo 408000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq
    
    echo 25 > /sys/devices/system/cpu/cpufreq/ondemand/up_threshold
    echo 10 > /sys/devices/system/cpu/cpufreq/ondemand/sampling_down_factor
    echo 1 > /sys/devices/system/cpu/cpufreq/ondemand/io_is_busy
    
[/code]
(can also be used with kernel 4.0 and above. And especially _io_is_busy_ is essential if you want to use your sunxi device as file server). The other parameters are explained in the governor link above. Adjust them only carefully and with a full understanding of what you're doing. 
## Practical impact on temperature/consumption
In the following 2 graphs you see the results of an experiment increasing _scaling_max_freq_ in steps of 96 MHz on an [A20-OLinuXino-Lime2][13318] with an adhesive heatsink on the A20 SoC, vertical orientation of the board, appropriate heat dissipation possible and an SSD connected via SATA: Tests were done with 816 MHz, 912 MHz, 1008 MHz, 1104 MHz and 1200 MHz (the Lime2 crashed at 1.2 GHz maybe due to insufficient voltage -- we used an unadjusted fex file from Olimex): 
[code] 
    for i in 816000 912000 1008000 1104000 1200000 ; do
            echo $i >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq
            cd /mnt/ssd && stress -t 900 -c 2 -m 2 -i 2 -d 2
            sleep 900
    done
[/code]
Each _stress_ task ran 15 minutes, after that we idled 15 min. Temperatures have been read out internally from the thermal sensors inside the A20's touchscreen controller and the [AXP209 power management unit (PMU][13319]) and verified roughly using two external DHT22 sensors measuring ambient temperature (green graph) and above SoC (purple graph). No external devices were connected to the board except network. 
  
[![Cpufreq experiment temperatures.png][13320]][13321]
Being idle (then the _ondemand_ governor decreased the CPU clock speed down to 408 MHz) SoC/PMU temperature were 13°/11° above ambient temperature, under load the temperature of the SoC raised 19°C (816 MHz) to 22°C (1104 MHz) above ambient temp. The PMU was also or even more affected (since it has to provide more voltage when the SoC is clocked higher): 19°C at 816 MHz but 24°C above surrounding temperature with the CPU running at 1104 MHz. 
Please keep in mind that these thermal values will increase considerably when your device is in a small enclosure preventing airflow and/or the PMU has to power other stuff (external USB peripherals, onboard Wi-Fi or even a SATA disk like on [Lamobo R1][13322]). 
  
[![Cpufreq experiment consumption.png][13323]][13324]
The board consumed between 270mA (idle, 408 MHz, ~1.35W), 400mA (816 MHz, ~2W) and 500mA (1104 MHz, ~2.5W). Please note that the Olimex boards like nearly all other A20 boards do not power a connected SATA disk through the PMU so the SSD's consumption doesn't show up in the graph at all and the whole system's consumption was 0.8W higher (an energy efficient SSD was used for the tests) 
Note that the ['cpuburn-a7' and 'cpuburn-a8' tools][13325] are a lot more effective for heating the CPU than the 'stress' tool. 
## "Overclocking"
As per the definition of the word "overclocking" is not possible since that would mean "frequency scaling beyond the specs". The problem with cheap ARM SoCs is that they're not subject to an expensive QA/selection process where each SoC will be tested extensively and then labeled/sold in different categories depending on the upper limits it's able to achieve (this is standard with x86 for example: chips from the same wafer will be tested individually and be sold for a few hundred bucks more or less depending on how many CPU/GPU cores work reliable at which clock speeds). 
One A20 SoC from a specific production batch might work reliable with 1.2GHz (which is rather unrealistic) while another starts to throw errors with 1.0GHz. The default cpufreq upper limits take that into account and can be considered sane/safe defaults. And while it's possible to adjust or define additional operating-points in the kernel sources to gain some more speed (with increased voltage) this should be considered experimental and is only advisable when you the user also [does QA/selection on your own][13326]: Stresstesting the device over many hours to simulate worst case conditions while keeping an eye on heat dissipation: Without appropriate airflow increasing cpufreq settings above defaults won't work. 
## Troubleshooting
### No /sys/devices/system/cpu/cpu0/cpufreq
While running test images, I noticed that I was missing cpufreq on an A20 cubietruck.  
There was no directory _cpufreq_ and the tools didn't work. 
The solution to this problem was the driver **axp20x-i2c**. It wasn't loaded, and in my case I had not build the module at all. 
See also: <http://forum.armbian.com/index.php/topic/108-no-cpufreq-support-in-cubietruck-debian-39-wheezy-405/>

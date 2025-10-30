# Hardware Reliability Tests
## Contents
  * [1 The importance of the hardware diagnostic tools][23829]
  * [2 My device is failing these reliability tests. What to do now?!][23830]
  * [3 **DRAM**][23831]
    * [3.1 Reliability][23832]
  * [4 **CPU**][23833]
    * [4.1 Reliability of cpufreq voltage/frequency settings][23834]
    * [4.2 Overheating][23835]

## The importance of the hardware diagnostic tools
Because of the diversity of various Allwinner based devices we have to deal with different DRAM, CPU clock speed and voltage settings. They are primarily derived from the fex files found in the vendor provided firmware on NAND and also based on the information retrieved by the [meminfo tool][23836]. Some dishonest sellers also happily advertise way higher specs than the hardware can actually handle (for example, unrealistic 1.5GHz CPU clock speeds). Moreover, different chips have their own individual voltage and clock frequency tolerances within a certain range. So that the borderline stable settings may be good for one unit and bad for another. 
In order to quickly identify obviously misconfigured hardware, we need some easy to use diagnostic tools. There is no magic involved. The general idea behind them is to find some real life or synthetic workloads, which are more likely to cause troubles. Then identify, which parts of these workloads are most problematic and convert them into (hopefully) user friendly test tools. Some of these tools are listed below. 
**Note:** naturally, the majority of devices are expected to pass these tests and you are likely not to get any exciting results. Still this is not a good justification for the "nah, this may happen to anyone, but me" attitude. The experience shows that there are definitely faulty/misconfigured devices out there. If you are experiencing occasional crashes or freezes once in a while, then making sure that these tests pass is strongly recommended before trying anything else. 
## My device is failing these reliability tests. What to do now?!
First of all, make sure that you are using an up to date u-boot bootloader, an up to date linux kernel and correct hardware description data (script.bin for the sunxi-3.4 kernel or a *.dtb file for the mainline kernel). It may be a matter of some hardware misconfiguration ([just like it happened with the cubieboard2/cubietruck before][23837]), and the intention is to have all of these problems ironed out eventually. 
If the tests are still failing with the up to date software, be sure to report the problem in the linux-sunxi mailing list or in the irc channel. Please also include all the relevant information (the board type, the kernel version, the bootloader version, etc.). Even if you can resolve the problem yourself (by adjusting the voltages or the clock speed), reporting the incident is still rather important to ensure that other people don't encounter the same problem in the future. Thanks! 
## **DRAM**
#### Reliability
The [Lima-memtester][23838] can be used to check if the DRAM settings are reasonable and dcdc3 voltage is sufficient. If you have a shell access to your device, then you can download a static binary compiled for ARM (or click on the 'Expand' link to see how to compile it from sources): 
[code] 
     git clone <https://github.com/ssvb/lima-memtester.git>
     cd lima-memtester
     cmake .
     make -j2
    
[/code]
[code] 
     # The wget option --no-check-certificate is only here to make it work even if the date is set wrong (no RTC battery)
     wget --no-check-certificate <https://github.com/ssvb/lima-memtester/releases/download/static-binary-20150126/lima-memtester>
     chmod +x lima-memtester
    
[/code]
The lima-memtester static binary requires only the sunxi-3.4 kernel with the mali kernel module and framebuffer enabled to run. This test does not depend on anything in the userland and should work with any Linux distribution (this also means that it does NOT require the userland [Mali binary driver][23839]). Just run lima-memtester with root privileges as: 
[code] 
     ./lima-memtester 100M
    
[/code]
If everything is working fine, there should be a spinning cube demo running indefinitely. If something is very wrong, then the test fails after just a few seconds! If something is mildly wrong, this usually gets detected in less than 15-20 minutes. However even running for a few hours can still detect some problems. In the case of troubles, the following symptoms may be observed. 
  * the system freezes
  * the display background starts glowing red (normally it is gray)

For even more confidence, it is a good idea to keep it running overnight (8-10 hours) at least once and if possible, over the weekend. 
On the [Lime2 page][23840] there are some test results. 
## **CPU**
#### Reliability of cpufreq voltage/frequency settings
The following ruby script can run basic reliability tests (correctness of jpeg decompression) for all cpufreq operating points. The kernel config needs to have support for 'userspace' cpufreq governor. 
[code] 
     cd /tmp
     git clone <https://github.com/ssvb/cpuburn-arm.git>
     cd cpuburn-arm
     ./cpufreq-ljt-stress-test
    
[/code]
Example output: 
[code] 
    Creating './whitenoise-1920x1080.jpg' ... done
    CPU stress test, which is doing JPEG decoding by libjpeg-turbo
    at different cpufreq operating points.
    
    Testing CPU 0
     1200 MHz SKIPPED
     1152 MHz SKIPPED
     1104 MHz SKIPPED
     1056 MHz SKIPPED
     1008 MHz ............................................................ OK
      960 MHz ............................................................ OK
      912 MHz ............................................................ OK
      864 MHz ............................................................ OK
      816 MHz ............................................................ OK
      768 MHz ............................................................ OK
      744 MHz ............................................................ OK
      720 MHz ............................................................ OK
      696 MHz SKIPPED
      672 MHz SKIPPED
      648 MHz SKIPPED
      600 MHz SKIPPED
      528 MHz SKIPPED
      480 MHz SKIPPED
      408 MHz SKIPPED
      384 MHz SKIPPED
      360 MHz SKIPPED
      336 MHz SKIPPED
      288 MHz SKIPPED
      264 MHz SKIPPED
      240 MHz SKIPPED
      216 MHz SKIPPED
      204 MHz SKIPPED
      192 MHz SKIPPED
      180 MHz SKIPPED
      168 MHz SKIPPED
      156 MHz SKIPPED
      144 MHz SKIPPED
      132 MHz SKIPPED
      120 MHz SKIPPED
       96 MHz SKIPPED
       84 MHz SKIPPED
       72 MHz SKIPPED
       60 MHz SKIPPED
    
[/code]
If voltage is configured wrong for one of the operating points, then data corruption may be detected and reported. 
**Be aware:** Please take the results of this script with a grain of salt. There are border cases in which extended tests show a device might not be stable at certain settings even though they pass the tests in this script. Especially on a multi-core system you may want to run CPU-intensive tasks in the background while running cpufreq-ljt-stress-test in order to keep all cores busy. The cpuburn scripts (see below) or compiling a kernel might be suitable tasks for this end. You may also want to change the duration of the tests by changing the number of test iterations per frequency setting (see line 203 of the script: the default value is 60 - feel free to set a higher value to make this script run longer). 
#### Overheating
If the CPU is overclocked and/or overvolted, then it may overheat and fail under heavy load. To check for the potential CPU overheating (with or without overclocking), it is possible to use the [cpuburn][23841] tool. 
To run this test on the Allwinner A10 hardware: 
[code] 
     git clone <https://github.com/ssvb/cpuburn-arm.git>
     cd cpuburn-arm
     gcc -o cpuburn-a8 cpuburn-a8.S
     ./cpuburn-a8
    
[/code]
Or on the Allwinner A20 hardware: 
[code] 
     git clone <https://github.com/ssvb/cpuburn-arm.git>
     cd cpuburn-arm
     gcc -o cpuburn-a7 cpuburn-a7.S
     ./cpuburn-a7
    
[/code]
The cpuburn programs are only heating the CPU and are not providing any visible feedback. It may make sense to also run some other non CPU hungry program simultaneously to monitor whether it is still alive or not. Running some Mali400 graphics demo is the best for this purpose. And the GPU is also providing an extra source of heat. 
**WARNING: if the device is recklessly overclocked/overvolted too much, then some permanent hardware damage may theoretically happen.[technical explanation][23842]**

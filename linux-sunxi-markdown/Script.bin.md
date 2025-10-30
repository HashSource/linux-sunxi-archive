# script.bin
**script.bin** is a board-specific binary "configuration file" used by Allwinner-specific drivers in the kernel (and also by the LiveSuit flashing program) with information on how to set-up various devices, ports and I/O pins on boards with Allwinner SoCs. 
The corresponding human-readable file format is [FEX][48909], it is possible to convert _.bin_ to _.fex_ and back by using [Sunxi-tools][48910]. 
## Contents
  * [1 Build script.bin][48911]
    * [1.1 Get bin2fex utility][48912]
    * [1.2 Get sunxi-boards repository][48913]
    * [1.3 Identify your fex file from your device page][48914]
    * [1.4 Edit .fex file (optional)][48915]
      * [1.4.1 Add Ethernet MAC address][48916]
    * [1.5 Build script.bin][48917]
    * [1.6 Install script.bin][48918]
    * [1.7 Configure U-Boot to load script.bin][48919]
  * [2 Modern script.bin usage][48920]
  * [3 Related Pages][48921]

# Build script.bin
[![Sticky-note-pin.png][48922]][48923] _Note:_ This is only needed for running the legacy ("sunxi") Linux kernel, or kernels provided by the board vendor or Allwinner. For running an upstream (or "mainline") kernel, you should use the included [device tree][48924] files. 
See also: [How to modify script.bin][48925]
## Get bin2fex utility
Bin2fex is part of [our sunxi-tools repository][48910]. You can get it by following [ our sunxi-tools build howto][48926]. 
## Get sunxi-boards repository
[code] 
    git clone git://github.com/linux-sunxi/sunxi-boards.git
[/code]
## Identify your fex file from your device page
The _.fex_ file should be clearly listed on [your device page][48927] under the _Manual Build_ section. 
## Edit .fex file (optional)
**This step is usually not necessary.**
The _.fex_ file uses the windows standard _.ini_ format. The entries are described in [our FEX guide][48909]. 
### Add Ethernet MAC address
To give your device a persistent MAC address, you need to add the _MAC_ directive to the _dynamic_ section, like such: 
[code] 
    [dynamic]
    MAC = "0123456789AB"
    
[/code]
If no _dynamic_ section exists, just add it to the end of the _.fex file_
## Build script.bin
[code] 
    /home/user/dir/sunxi-tools/fex2bin <your_device>.fex script.bin
[/code]
## Install script.bin
TODO
## Configure U-Boot to load script.bin
TODO
# Modern script.bin usage
On more recent BSPs (like for H6), script.bin is folded into devicetree in some weird way. Sunxi-tools has no tool yet to extract this information, as this still needs to be written up. This currently limits/prohibits extracting of script.bin on many modern Allwinner devices. 
There seems to be a decent amount of information available in the Allwinner BSP, which, amazingly, uses part of our sunxi-tools code, enough for an enterprising individual to go add the necessary tooling to sunxi-tools. 
The key here seems to be [a bash script called pack][48928], which references [a special version of the linux dtc compiler][48929] (in do_ini_to_dts()) which includes the [extra code to parse fex][48930]. 
# Related Pages
  * [How to modify script.bin][48925]

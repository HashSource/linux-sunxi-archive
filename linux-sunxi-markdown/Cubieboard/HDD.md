# Cubieboard/HDD
< [Cubieboard][14008]
 
  

## Contents
  * [1 2.5" HDD][14011]
  * [2 3.5" HDD][14012]
    * [2.1 Addon design][14013]
    * [2.2 Power brick & Molex design][14014]
      * [2.2.1 Power bricks comparison][14015]
    * [2.3 PC PSU & Molex design][14016]
    * [2.4 External HDD enclosure design][14017]

## 2.5" HDD
The Cubieboard comes with data and power SATA cable and will provide enough power if your PSU's current rating is sufficient. The **peak** current draw of HDDs from this category may be as high as 0.9A - 1.75A. For this reason make sure to use PSU with 2A or 2.5A or use separate PSU for the disk. 
## 3.5" HDD
Unlike 2.5" disks the desktop HDDs requires both 5V and 12V. They peak 1.7A - 2.8A on the 12V voltage branch (not the 5V branch as 2.5" HDDs). Using desktop HDD with Cubieboard is just matter of how you wire it up. 
### Addon design
Cubietech has released an addon package that will allow you to hook up the drive. More information can be found in their [blog post][14018]. 
The answers for a couple of comments on the post: 
Is it possible to power the cubieboard directly from this addon? Yes, you only need one 12V power adapter for that, the cubieboard can be powered by 12V-5V Subboard. 
How much Amperage is recommended for the 12V to power one HDD and the Cubietruck ? 2.5 Amperage is ok 
### Power brick & Molex design
[![][14019]][14020]
[][14021]
PSU with Molex output
[![][14022]][14023]
[][14024]
Molex-to-SATA power splitter
There is a few _power bricks_ (aka laptop's PSU) on the market with Molex power connector (precisely Molex 8981 Series Power Connector). Such a PSU will certainly provide 5V and 12V voltage branches. Then you can use [Molex to USB splitter][14025] or create your own from one of the many available Molex-to-SATA power splitters. If you choose to create your own splitter, you will cut down one of the two connectors on your splitter which will give you four cables (5V red + ground and 12V yellow + ground). Then you will use the 5V pair to create USB, miniUSB or 4.0mm/1.0mm barrel plug connector. The barrel plug is probably the easiest to solder (the 5V/positive/red cable goes in the center and ground/black cable goes to sleeve). The second unmodified connector will be used to directly supply power for the 3.5" HDD. The HDD and Cubieboard will be connect with only one cable - SATA data. 
#### Power bricks comparison
Brick | Current | Price   
---|---|---  
[Coolerguys Power Adapter][14026] | 2.0 A | $15   
[Gembird USB 3.0 to SATA adapter][14027] | 1.5 A1) | $15   
[PremiumCord Power Adapter for 3.5" HDD][14028] | 1.5 A | $19   
1) _Gembird claims 2.5 A on the box, but power brick itself 1.5 A._
### PC PSU & Molex design
This design is pretty much the same as the one above, however you won't use power brick but your PC's own PSU. I won't go in details here, but this design requires to short two cables to ensure the PSU will stay on even if you switch off your computer. The upside is you won't need to buy extra PSU (the brick). The downside is your PSU's fan will be generating noise and the power efficiency may be questionable. 
### External HDD enclosure design
I don't know details on this one, but basically you gonna use external HDD enclosure to power your HDD and with some soldering to power the Cubieboard. The upside is you get enclosure for both your HDD and Cubieboard (if you select one that is big enough).

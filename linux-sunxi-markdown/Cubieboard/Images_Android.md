# Cubieboard/Images Android
< [Cubieboard][14058]
 
## Contents
  * [1 Prebuilt images][14061]
    * [1.1 Cubieboard][14062]
      * [1.1.1 android-4.0.4][14063]
    * [1.2 Cubieboard2][14064]
      * [1.2.1 Android-4.2.2 v1.01][14065]

# Prebuilt images
**TODO: These images seem to be cubieboard specific, and not based on any sunxi code directly. Please verify, and if so, relegate this whole page to external links only.**
## Cubieboard
### android-4.0.4
These are images made for installing to NAND, and come with XBMC preinstalled. The RAM is running at 480MHz, and HDMI is enabled. 
  * [Image for rtl8192cu wifi][14066]
  * [Image for rtl8188eu wifi][14067]

To built these from scratch, please refer to [Cubieboard manifests][14068]. 
## Cubieboard2
### Android-4.2.2 v1.01
These are images made for installing to NAND. These images use the [cubieboard 3.3 kernel][14069], and with HDMI enabled. 
Note that all cubieboards and cubieboard2s seem to be happy when running their DDR3 RAM at 480MHz, but for lower power consumption, and peace of mind, the default frequency is 432MHz. 
  * For Realtek RTL8192CU wifi: 
    * [ddr432MHz][14070]
    * [ddr480MHz][14071]
  * For Realtek RTL8188EU wifi: 
    * [ddr432MHz][14072]
    * [ddr480MHz][14073]

# Dual Monitor Support
[![MBOX icon important.png][17259]][17260] | This page provides outdated set of instructions and needs to be updated to reflect current status.   
---|---  
On some hardware, it is possible to have 2 monitors display separate images. 
## Contents
  * [1 Limitations][17261]
    * [1.1 LCDCs][17262]
    * [1.2 Connectors/Encoders][17263]
      * [1.2.1 LCD][17264]
      * [1.2.2 HDMI][17265]
      * [1.2.3 VGA][17266]
      * [1.2.4 TV][17267]
  * [2 FEX changes][17268]
  * [3 Xorg Configuration][17269]
    * [3.1 Single XServer][17270]
    * [3.2 Separate XServers][17271]

# Limitations
There are a few limitations to the possible combinations. 
## LCDCs
Most SoCs have 2 LCDCs (LCD Controllers). These engines read out from the Display Backend (a sort of framebuffer compositor), and serializes the pixels, according to very specific timing (display mode timing). In order to get dual display support, you need to first have 2 CRTCs and the ability to get that serialized digital signal onto a monitor. 
## Connectors/Encoders
Not everything can be switched from one LCDC to another, so they usually end up being tied to the first LCDC, limiting the possible combinations. 
### LCD
A directly connected panel is always tied directly to an LCDC. It can therefor not be switched between LCDCs. 
### HDMI
If your SoC has a HDMI encoder, then HDMI can be freely switched between LCDCs. 
### VGA
VGA is a combination of 3 DACs (or TVECs - TV Encoders), for Red Green and Blue, and a horizontal and vertical synchronization pulse. While the DACs are freely switchable, the sync signals are wired directly to an LCDC. It is therefor not possible to switch a VGA connection between LCDCs. 
### TV
An analog TV signal is either CVBS (composite - 1 DAC), S-Video (2 DACs), RGB (3 DACs) or YCbCr (3 DACs). Timing is embedded into the DACs analog signal and analog TV connections can therefor be switched freely between LCDCs. 
# FEX changes
Currently, you will need appropriate changes to the FEX file to be able to set up dual monitor support. Our [`disp_init` section of the Fex Guide][17272] shows the possible values. 
The following example sets a dual monitor mode with the same 1280x720 resolutions to both VGA (/dev/fb0) and HDMI (/dev/fb1). 
[code] 
    [disp_init]
    disp_mode = 2
    screen0_output_type = 4
    screen1_output_type = 3
    screen0_output_mode = 11
    screen1_output_mode = 5
[/code]
This sets the dual monitor mode and the same 1280x720 screen resolution for both VGA (/dev/fb0) and HDMI (/dev/fb1) monitors. 
# Xorg Configuration
## Single XServer
You can use something like the following /etc/X11/xorg.conf file ("fbturbo" can be also replaced with "fbdev" there): 
[code] 
    Section "Device"
            Identifier      "FBDEV 0"
            Driver          "fbturbo"
            Option          "fbdev" "/dev/fb0"
    EndSection
    
    Section "Device"
            Identifier      "FBDEV 1"
            Driver          "fbturbo"
            Option          "fbdev" "/dev/fb1"
    EndSection
    
    Section "Screen"
            Identifier      "VGA"
            Device          "FBDEV 0"
            Monitor         "Monitor name 0"
    EndSection
    
    Section "Screen"
            Identifier      "HDMI"
            Device          "FBDEV 1"
            Monitor         "Monitor name 1"
    EndSection
    
    Section "ServerLayout"
            Identifier      "Default Layout"
            Screen          0 "VGA"
            Screen          1 "HDMI" RightOf "VGA"
    EndSection
[/code]
## Separate XServers
Stick the following into /etc/X11/xorg.conf 
[code] 
    Section "Device"
        Identifier "Framebuffer Graphics Driver"
        Driver "fbturbo"
        Option "fbdev" "/dev/fb0"
    EndSection
[/code]
And the following into /etc/X11/xorg2.conf 
[code] 
    Section "Device"
        Identifier "Framebuffer Graphics Driver"
        Driver "fbturbo"
        Option "fbdev" "/dev/fb1"
    EndSection
[/code]
You then need to start X with the _-config_ argument pointing to the right config file. 
For example, for XFCE: 
[code] 
    (startxfce4 -- :0 -config /etc/X11/xorg.conf -novtswitch &>/dev/null) &
[/code]
And 
[code] 
    (startxfce4 -- :1 -config /etc/X11/xorg2.conf -sharevts -novtswitch &>/dev/null) &
[/code]

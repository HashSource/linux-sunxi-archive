# SID
# Security/Chip ID
The Allwinner A-series of SoC's (A10, A10s, A12, A13, A20 and A31) feature a series of efuses used as a unique Chip ID. Other potential uses for these efuses are: 
  * MAC address
  * Encryption Key
  * Entropy seed
  * Product serial number

These 128 bits are in theory programmable, but most likely require a certain programming voltage (efuse_vddq) applied to pin T9 (on A10/A20) that is normally tied to GND. Feeding said pin with anything but GND will be hard in practice, since the BGA pin will most likely tied directly to GND. 
While these bits tend to be programmed reasonable for a lot of SoC's, there have been SoC's in the wild (mele A1000 so far) that has these efuses all set to 0! 
The following ranges appear to be available 
[code] 
    0x000  128 bit root-key (sun[457]i)
    0x010  128 bit boot-key (sun7i)
    0x020   64 bit security-jtag-key (sun7i)
    0x028   16 bit key configuration (sun7i)
    0x02b   16 bit custom-vendor-key (sun7i)
    0x02c  320 bit low general key (sun7i)
    0x040   32 bit read-control access (sun7i)
    0x064  224 bit low general key (sun7i)
    0x080 2304 bit HDCP-key (sun7i)
    0x1a0  768 bit high general key (sun7i)
    
[/code]
see also: [SID Register Guide][48224]

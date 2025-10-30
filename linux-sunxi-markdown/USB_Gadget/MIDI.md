# USB Gadget/MIDI
< [USB Gadget][57199]
 
## Contents
  * [1 USB MIDI support][57202]
    * [1.1 Kernel Configuration][57203]
    * [1.2 Loading the driver][57204]
    * [1.3 Known Error Messages][57205]

# USB MIDI support
This allows your device to act as a MIDI USB client. The connection is set up as a separate ALSA sound card with MIDI port. 
## Kernel Configuration
Enable the module in the kernel config (it's not enabled by default): 
[code] 
        Device Drivers  --->
            USB support  --->
                <*>    USB Gadget Support  --->
                    <m>    MIDI Gadget (EXPERIMENTAL)
    
[/code]
Make sure you also have the ALSA MIDI seqencer support enabled: 
[code] 
        Device Drivers  --->
            Sound Card support  --->
                Advanced Linux Sound Architecture  --->
                    <M>   Sequencer support
    
[/code]
## Loading the driver
Load the midi gadget driver with: 
[code] 
    modprobe g_midi
[/code]
If it responds with a "device or resource busy" message, then you probably already have an ALSA sound card registered with index 0. You can specify the index via the module options, simply choose the next free index: 
[code] 
    modprobe g_midi index=1
[/code]
## Known Error Messages
If you see the following message 
[code] 
    WRN:L2385(drivers/usb/sunxi_usb/udc/sw_udc.c):ERR: sw_udc_queue: inval 2
[/code]
it means that you attempted to send a MIDI message via the MIDI gadget without it being connected to a host. Just plug in the USB cable (or unplug and retry if the first registration failed) and the error should go away.

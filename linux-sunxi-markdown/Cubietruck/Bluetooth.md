# Cubietruck/Bluetooth
< [Cubietruck][15496]
 
Given that you see this in dmesg: 
[code] 
    sunxi-uart.2: ttyS1 at MMIO 0x1c28800 (irq = 35) is a U6_16550A
    
[/code]
You can upload the firmware and activate the hci device like that: 
[code] 
    ./brcm_patchram_plus -d  --patchram /lib/firmware/ap6210/bcm20710a1.hcd --enable_hci --bd_addr 11:22:33:44:55:66 --no2bytes --tosleep 1000 /dev/ttyS1
    
[/code]
You will see lots of hex dumps flying through the screen and at the end: 
[code] 
    received 7
    04 0e 04 01 03 0c 00
    writing
    01 01 fc 06 66 55 44 33 22 11
    received 7
    04 0e 04 01 01 fc 00
    Done setting line discpline
    
[/code]
The program doesn't detach itself - goes into infinite sleep. Must investigate why. 
[code] 
     The reason it doesn't detach is because of the --enable_hci flag.
     The program holds the tty open and enables bluetooth line discipline on the tty.
     The alternative is to remove the flag and use hciattach.
    
[/code]
Confirm the device has been created: 
[code] 
    root@cubietruck:~# hcitool dev
    Devices:
            hci0    11:22:33:44:55:66
    root@cubietruck:~# hciconfig -a
    hci0:   Type: BR/EDR  Bus: UART
            BD Address: 11:22:33:44:55:66  ACL MTU: 1021:8  SCO MTU: 64:1
            UP RUNNING PSCAN 
            RX bytes:4479 acl:66 sco:0 events:130 errors:0
            TX bytes:3593 acl:65 sco:0 commands:51 errors:0
            Features: 0xbf 0xfe 0xcf 0xfe 0xdb 0xff 0x7b 0x87
            Packet type: DM1 DM3 DM5 DH1 DH3 DH5 HV1 HV2 HV3 
            Link policy: RSWITCH SNIFF 
            Link mode: SLAVE ACCEPT 
            Name: 'cubietruck-0'
            Class: 0x620100
            Service Classes: Networking, Audio, Telephony
            Device Class: Computer, Uncategorized
            HCI Version: 4.0 (0x6)  Revision: 0x1000
            LMP Version: 4.0 (0x6)  Subversion: 0x220e
            Manufacturer: Broadcom Corporation (15)
    
[/code]
You might also need to preload bluetooth and hci-uart modules. 
The program can be downloaded from <https://code.google.com/p/broadcom-bluetooth/> The firmware can be grabbed from various places, e.g. cubietech images. 
  

## Update
There's been some complaints about the results being irreproducible. It is true that sometimes the firmware fails to load. And if it failed once, you most likely won't be able to activate the chip until next reboot (fixme: Someone more competent, explain how to reset the chip circuitry). 
[code] 
     Reset the chip by setting the BT-REST GPIO pin to 0.
    
[/code]
I have the following modules loaded before uploading the firmware: 
[code] 
    g2d_23 37275 2 - Live 0xbf16e000
    rfcomm 57752 14 - Live 0xbf157000
    bnep 13796 2 - Live 0xbf14f000
    hci_uart 23588 1 - Live 0xbf144000
    bluetooth 264130 31 hidp,rfcomm,bnep,hci_uart, Live 0xbf0ef000
    sunxi_cedar_mod 9600 0 - Live 0xbf0e8000
    snd_hwdep 5278 0 - Live 0xbf0e3000
    snd_usbmidi_lib 17980 0 - Live 0xbf0da000
    snd_rawmidi 18863 1 snd_usbmidi_lib, Live 0xbf0d0000
    mali_drm 2533 2 - Live 0xbf0c4000
    mali 224497 1 - Live 0xbf07d000
    drm 208545 3 mali_drm, Live 0xbf034000
    disp_ump 788 0 - Live 0xbf030000
    ump 50814 6 mali,disp_ump, Live 0xbf01d000
    lcd 3693 0 - Live 0xbf019000 
    sunxi_gmac 30577 0 - Live 0xbf00c000
    pwm_sunxi 9138 0 - Live 0xbf005000
    rtc_sun4i 5440 0 - Live 0xbf000000
    
    
[/code]
After uploading the firmware I do: 
[code] 
    modprobe hidp
    hidd --server
    hciconfig hci0 up
    
[/code]
This is probably not the cleanest way to do things, but I've been able to use a e.g. BT keyboard for a week long without any trouble. 
## Update 2
There seems to be missing gpio configuration to allow firmware download. [Re: Debian sd/nand/sata deploying bluetooth firmware][15499]
[code] 
     PH09 is for enabling WiFi. Not relevant here.
    
[/code]
## Update 3
There are two GPIO pins that are significant here. AP6210 pin 34 is BT-REST and is connected to GPIO pin PH18. AP6210 pin 6 is BT-WAKE and is connected to GPIO pin PH24. I've found that setting PH24 to 1 and then toggling PH18 (0 then 1) is required before loading the firmware using the Broadcom program. Changing the program to wait for CTS before sending also helps avoid hangs. This should be done by manually checking for CTS rather than using the RTSCTS ioctl option. Because the connection to the AP6210 is a null-modem link, RTS should be used by the program to indicate that it is ready to receive rather than it wants to send. So the modified program checks for CTS before sending and sets RTS while awaiting a reply. There are details in the link mentioned above. 
I suggest that the best place to set the pins and load the firmware is in the "start" section of the /etc/init.d/bluetooth file before it starts the daemons. I'm currently doing this and while not bullet-proof it does seem as reliable as any other approach. One change from the Broadcom suggested command to run patchram is that I do not use --enable_hci. This leaves the link in raw serial mode and is probably what hciattach expects. hciattach will set the line discipline when attaching the device. 
If you want the bluetooth script to attach the uart automatically, create the file /etc/bluetooth/uart and add the line : 
[code] 
     /dev/ttyS1 any
    
[/code]
The script looks for the file and uses the line as parameters for hciattach.

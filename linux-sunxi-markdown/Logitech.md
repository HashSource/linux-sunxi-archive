# Logitech
The logitech wireless keyboards and mouses all uses today a common receiver, the _Logitech Unifying Receiver_. This allows to use several devices with a single receiver in each computer, simplifying its use. 
The big advantage of this is when our board or tablet has only one On-The-Go USB port, because it allows to have keyboard and mouse using only one port, and without an USB hub. 
But to make this receiver to work with linux, is mandatory to enable these options in [ the kernel config][32948]: 
[code] 
       Device Drivers --->
           HID devices=Y --->
               Generic HID support=Y
                   /dev/hidraw raw HID device support=Y
               USB Human Interface Device (full HID) support=Y
               /dev/hiddev raw HID device support=Y
    
[/code]
Without them, these receivers won't work.

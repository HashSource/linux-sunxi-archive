# Advanced Power Management
Advanced Power Management is the old technology to allow PCs to suspend, hybernate, check the battery levels and so on. For the Allwinner chips there is an emulation layer for this API. 
Several devices work also with the [AXP209][6085] battery charger chip. Fortunately there is support for it in the latest 3.4 kernel. 
To enable this power management (that will allow to check the battery levels, know if the charger is connected, and shutdown via software the device) just set these options in the kernel configuration: 
[code] 
       Power management options --->
           Run-time PM core functionality=Y
           Advanced Power Management Emulation=y
       Device Drivers --->
           Power supply class support=Y --->
               AXP Power drivers=Y --->
                   AXP PMU type=AXP20 driver
                   AXP initial charging environment set=Y
                   AXP charging current set when suspendresumeshutdown=Y
               APM emulation for class batteries=Y
           Voltage and Current Regulator Support=Y --->
    
[/code]
Is mandatory to enable the _Voltage and Current Regulator Support_ option, because without it, the _AXP Power drivers_ option won't be shown.

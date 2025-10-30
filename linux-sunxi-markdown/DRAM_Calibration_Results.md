# DRAM Calibration Results
[DRAM Calibration Results/Cubietech Cubieboard][16160]
[DRAM Calibration Results/Olimex A20-OLinuXino-Micro Rev.E][16161]
## ZQ calibration table
ZQ calibration is SoC temperature dependent. The table below provides some calibration results as a reference: 
Device  | ZPROG (two-digit 'zq' parameter)  | Calibrated ZDATA on cold start (SoC temperature is low)  | Calibrated ZDATA on hot reboot (SoC temperature is high)   
---|---|---|---  
ssvb's Cubietruck  | 0x2c  | 0x10d1800  | 0x10d3900   
ssvb's Primo73  | 0x2b  | 0x10de800  | 0x10d6900   
ssvb's Cubieboard  | 0x2b  | 0x10dcb00  | 0x10de800   
ssvb's Cubieboard  | 0x3b  | 0x199cb00  | 0x199e800

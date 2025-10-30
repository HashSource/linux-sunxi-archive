# Thermal Sensor
This Wiki entry should give a basic overview about THS sensors in Allwinner Devices 
## Register Comparison H3, H5, A80, A64, A83T, H6
Device  | THS_CTRL0  | THS_CTRL1  | THS_CTRL2  | THS_INTC  | THS_STAT  | THS_FILTER  | THS_CDATA0/1  | THS_TDATA0/1/2/3   
---|---|---|---|---|---|---|---|---  
H3  | 0x00  | 0x04  | 0x40  | 0x44  | 0x48  | 0x70  | 0x74  | 0x80   
H5  | 0x00  | 0x04  | 0x40  | 0x44  | 0x48  | 0x70  | 0x74  | 0x80 0x84   
A83T  | 0x00  | 0x04  | 0x40  | 0x44  | 0x48  | 0x70  | 0x74/0x78  | 0x80 0x84 0x88   
A64  | 0x00  | 0x04  | 0x40  | 0x44  | 0x48  | 0x70  | 0x74/0x78  | 0x80 0x84 0x88   
A80  | N/A  | N/A  | 0x40  | 0x44  | 0x48  | 0x70  | 0x74/0x78  | 0x80 0x84 0x88 0x8C   
H6  | 0x00  | N/A  | 0x04 (no ACQ1)  | 0x08 - 0x18 (all separated)  | 0x20 -0x2c (all separated)  | 0x30  | 0xA0  | 0xC0 0xC4   
## Interrupts comparison THS_STAT register
Device  | ALARM OFF 2  | ALARM OFF 1  | ALARM OFF 0  | DATA3  | DATA2  | DATA1  | DATA0  | SHUT 3  | SHUT 2  | SHUT 1  | SHUT 0  | ALARM 3  | ALARM 2  | ALARM 1  | ALARM 0   
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
H3  |  |  | 12  |  |  |  | 8  |  |  |  | 4  |  |  |  | 0   
H5  |  | 13  | 12  |  |  | 9  | 8  |  |  | 5  | 4  |  |  | 1  | 0   
A83T  |  |  |  |  | 10  | 9  | 8  |  | 6  | 5  | 4  |  | 2  | 1  | 0   
A64  | 14  | 13  | 12  |  | 10  | 9  | 8  |  | 6  | 5  | 4  |  | 2  | 1  | 0   
A80  |  |  |  | 11  | 10  | 9  | 8  | 7  | 6  | 5  | 4  | 3  | 2  | 1  | 0

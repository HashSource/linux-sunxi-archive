# A10 DRAM Controller Calibration (impedance configuration example)
## Contents
  * [1 Searching for optimal "dram_emr1"][1465]
    * [1.1 **Cubieboard1, 540MHz, emr1=0x00**][1466]
    * [1.2 **Cubieboard1, 540MHz, emr1=0x04**][1467]
    * [1.3 **Cubieboard1, 540MHz, emr1=0x06**][1468]
    * [1.4 **Cubieboard1, 540MHz, emr1=0x42**][1469]
  * [2 Searching for optimal "dram_zq" (high 4 bits)][1470]
    * [2.1 **Cubieboard1, 576MHz, zq=0x1C**][1471]
    * [2.2 **Cubieboard1, 576MHz, zq=0x2C**][1472]
    * [2.3 **Cubieboard1, 576MHz, zq=0x3C**][1473]
    * [2.4 **Cubieboard1, 576MHz, zq=0x4C**][1474]
  * [3 Searching for optimal "dram_zq" (low 4 bits)][1475]
    * [3.1 **Cubieboard1, 576MHz, zq=0x3A**][1476]
    * [3.2 **Cubieboard1, 576MHz, zq=0x3B**][1477]
    * [3.3 **Cubieboard1, 576MHz, zq=0x3C**][1478]
  * [4 Additional check for "dram_emr1"][1479]
    * [4.1 **Cubieboard1, 576MHz, zq=0x3B, emr1=0x04**][1480]
    * [4.2 **Cubieboard1, 576MHz, zq=0x3B, emr1=0x06**][1481]
  * [5 528MHz with reduced dcdc3 voltage][1482]
    * [5.1 **Cubieboard1, 528MHz, zq=0x3B, emr1=0x04, dcdc3=1.25V**][1483]

# Searching for optimal "dram_emr1"
## **Cubieboard1, 540MHz, emr1=0x00**
| dcdc3_vol = 1250  
dram_clk = 540  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 7  
dram_zq = 0x7b  
dram_odt_en = 0  
dram_tpr0 = 0x36947790  
dram_tpr1 = 0xa0c0  
dram_tpr2 = 0x23600  
dram_tpr3 = 0x40000  
dram_emr1 = 0x0  
dram_emr2 = 0x8  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x07**2****2****2****2**|  0x071111| 0x070000| 0x07**E****E****E****E**|  0x07DDDD  
**0x06**|  0x063333| 0x062222| 0x061111| 0x060000| 0x06**E****E****E****E**|  0x06DDDD  
**0x05**|  0x053333| 0x052222| 0x051111| 0x050000| 0x05**E****E****E****E**|  0x05DDDD  
**0x04**|  0x04**3****3****3****3**|  0x04**2****2****2****2**|  0x041111| 0x04**0****0****0****0**|  0x04EEEE| 0x04DDDD  
**0x03**|  0x0333**3** 3| 0x032222| 0x03**1****1****1****1**|  0x03**0****0****0****0**|  0x03EEEE| 0x03**D** DDD  
**0x02**|  0x0233**3** 3| 0x022222| 0x02**1****1****1****1**|  0x02**0****0****0****0**|  0x02**E****E****E****E**|  0x02**D** DDD  
**0x01**|  0x0133**3** 3| 0x01**2****2****2****2**|  0x011111| 0x010000| 0x01**E****E****E****E**|  0x01**D** DDD  
**0x00**|  0x0033**3** 3| 0x002222| 0x00**1****1****1****1**|  0x000000| 0x00EEEE| 0x00**D** DDD  
**0x08**|  0x0833**3** 3| 0x08**2****2****2****2**|  0x08**1****1****1****1**|  0x080000| 0x08**E****E****E****E**|  0x08DDDD  
**0x10**|  0x1033**3** 3| 0x10**2****2****2****2**|  0x101111| 0x10**0****0****0****0**|  0x10EEEE| 0x10DDDD  
**0x18**|  0x1833**3** 3| 0x18**2****2****2****2**|  0x181111| 0x180000| 0x18EEEE| 0x18DDDD  
**0x20**|  0x2033**3** 3| 0x20**2****2****2****2**|  0x20**1****1****1****1**|  0x200000| 0x20**E****E****E****E**|  0x20DDDD  
**0x28**|  0x2833**3** 3| 0x282222| 0x28**1****1****1****1**|  0x28**0****0****0****0**|  0x28EEEE| 0x28DDDD  
**0x30**|  0x3033**3** 3| 0x302222| 0x30**1****1****1****1**|  0x30**0****0****0****0**|  0x30EEEE| 0x30DDDD  
**0x38**|  0x3833**3** 3| 0x38**2****2****2****2**|  0x38**1****1****1****1**|  0x380000| 0x38EEE**E**|  0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [solidbits=45, bitflip=1]  
  
Total number of successful memtester runs: 0  
  
Best luminance at the height 0.5 is above 0x000000, score = 0.000  
Best luminance at the height 1.0 is above 0x000000, score = 0.000  
Best luminance at the height 2.0 is above 0x000000, score = 0.000  
Best luminance at the height 4.0 is above 0x000000, score = 0.000  
  
Read errors per lane: [4, 0, 11, 0]. Lane 1 is the most noisy/problematic.  
Errors from the lane 3 are not intersecting with the errors from the worst lane 1.  
  
Write errors per lane: [30, 30, 30, 31]. Lane 0 is the most noisy/problematic.  
Errors from the lane 1 are 100.0% eclipsed by the worst lane 0.  
Errors from the lane 2 are 100.0% eclipsed by the worst lane 0.  
Errors from the lane 3 are 100.0% eclipsed by the worst lane 0.  
  
## **Cubieboard1, 540MHz, emr1=0x04**
| dcdc3_vol = 1250  
dram_clk = 540  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 7  
dram_zq = 0x7b  
dram_odt_en = 0  
dram_tpr0 = 0x36947790  
dram_tpr1 = 0xa0c0  
dram_tpr2 = 0x23600  
dram_tpr3 = 0x60000  
dram_emr1 = 0x4  
dram_emr2 = 0x8  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x072222| 0x071111| 0x070000| 0x07EEE**E**|  0x07DDDD  
**0x06**|  0x063333| 0x062222| 0x061111| 0x060000| 0x06EEE**E**|  0x06DDDD  
**0x05**|  0x053333| 0x052222| 0x05**1****1****1****1**|  0x050000| 0x05EEE**E**|  0x05DDDD  
**0x04**|  0x0433**3** 3| 0x042222| 0x041111| 0x040000| 0x04**E** EEE| 0x04DDDD  
**0x03**|  0x0333**3** 3| 0x03**2****2****2****2**|  0x03**1****1****1****1**|  0x030000| 0x03**E** EEE| 0x03**D** DDD  
**0x02**|  0x0233**3** 3| 0x022222| 0x021111| 0x020000| 0x02**E****E****E****E**|  0x02DDDD  
**0x01**|  0x0133**3** 3| 0x012222| 0x01**1****1****1****1**|  0x010000| 0x01EEEE| 0x01**D** DDD  
**0x00**|  0x0033**3** 3| 0x00**2****2****2****2**|  0x001111| 0x000000| 0x00EE**E** E| 0x00**D** DDD  
**0x08**|  0x0833**3** 3| 0x082222| 0x08**1****1****1****1**|  0x080000| 0x08EE**E** E| 0x08DDDD  
**0x10**|  0x1033**3** 3| 0x102222| 0x101111| 0x100000| 0x10EEE**E**|  0x10DDDD  
**0x18**|  0x1833**3** 3| 0x182222| 0x18**1****1****1****1**|  0x180000| 0x18EEEE| 0x18DDDD  
**0x20**|  0x2033**3** 3| 0x202222| 0x201111| 0x20**0****0****0****0**|  0x20EEE**E**|  0x20DDDD  
**0x28**|  0x2833**3** 3| 0x282222| 0x28**1****1****1****1**|  0x28**0****0****0****0**|  0x28EEE**E**|  0x28DDDD  
**0x30**|  0x3033**3** 3| 0x30**2****2****2****2**|  0x301111| 0x30**0****0****0****0**|  0x30EEE**E**|  0x30DDDD  
**0x38**|  0x3833**3** 3| 0x38**2****2****2****2**|  0x381111| 0x380000| 0x38EEE**E**|  0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [bitflip=24, solidbits=17]  
  
Total number of successful memtester runs: 161  
  
Best luminance at the height 0.5 is above 0x040000, score = 0.461  
Best luminance at the height 1.0 is above 0x030000, score = 0.321  
Best luminance at the height 2.0 is above 0x030000, score = 0.245  
Best luminance at the height 4.0 is above 0x020000, score = 0.203  
  
Read errors per lane: [5, 0, 14, 6]. Lane 1 is the most noisy/problematic.  
Errors from the lane 0 are not intersecting with the errors from the worst lane 1.  
Errors from the lane 3 are not intersecting with the errors from the worst lane 1.  
  
Write errors per lane: [14, 14, 14, 16]. Lane 0 is the most noisy/problematic.  
Errors from the lane 1 are 100.0% eclipsed by the worst lane 0.  
Errors from the lane 2 are 100.0% eclipsed by the worst lane 0.  
Errors from the lane 3 are 100.0% eclipsed by the worst lane 0.  
  
## **Cubieboard1, 540MHz, emr1=0x06**
| dcdc3_vol = 1250  
dram_clk = 540  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 7  
dram_zq = 0x7b  
dram_odt_en = 0  
dram_tpr0 = 0x36947790  
dram_tpr1 = 0xa0c0  
dram_tpr2 = 0x23600  
dram_tpr3 = 0x40000  
dram_emr1 = 0x6  
dram_emr2 = 0x8  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x072222| 0x07**1****1****1****1**|  0x070000| 0x07EEE**E**|  0x07DDDD  
**0x06**|  0x0633**3** 3| 0x062222| 0x061111| 0x060000| 0x06EEE**E**|  0x06DDDD  
**0x05**|  0x0533**3** 3| 0x052222| 0x051111| 0x05**0****0****0****0**|  0x05EEE**E**|  0x05DDDD  
**0x04**|  0x0433**3** 3| 0x042222| 0x041111| 0x040000| 0x04**E** EEE| 0x04DDDD  
**0x03**|  0x0333**3** 3| 0x03**2****2****2****2**|  0x03**1****1****1****1**|  0x030000| 0x03**E** EEE| 0x03**D** DDD  
**0x02**|  0x0233**3** 3| 0x022222| 0x02**1****1****1****1**|  0x02**0****0****0****0**|  0x02EEEE| 0x02**D** DDD  
**0x01**|  0x0133**3** 3| 0x01**2****2****2****2**|  0x011111| 0x01**0****0****0****0**|  0x01EEEE| 0x01**D** DDD  
**0x00**|  0x0033**3** 3| 0x002222| 0x001111| 0x000000| 0x00EE**E** E| 0x00**D** DDD  
**0x08**|  0x0833**3** 3| 0x08**2****2****2****2**|  0x081111| 0x080000| 0x08EEE**E**|  0x08**D** DDD  
**0x10**|  0x1033**3** 3| 0x102222| 0x101111| 0x100000| 0x10EEE**E**|  0x10DDD**D**  
**0x18**|  0x1833**3** 3| 0x18**2****2****2****2**|  0x181111| 0x180000| 0x18EEE**E**|  0x18DDDD  
**0x20**|  0x2033**3** 3| 0x202222| 0x20**1****1****1****1**|  0x200000| 0x20EEE**E**|  0x20DDDD  
**0x28**|  0x2833**3** 3| 0x282222| 0x281111| 0x28**0****0****0****0**|  0x28EEE**E**|  0x28DDDD  
**0x30**|  0x3033**3** 3| 0x30**2****2****2****2**|  0x301111| 0x30**0****0****0****0**|  0x30EEEE| 0x30DDDD  
**0x38**|  0x3833**3** 3| 0x382222| 0x381111| 0x380000| 0x38EEE**E**|  0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [bitflip=26, solidbits=20]  
  
Total number of successful memtester runs: 176  
  
Best luminance at the height 0.5 is above 0x040000, score = 0.444  
Best luminance at the height 1.0 is above 0x040000, score = 0.304  
Best luminance at the height 2.0 is above 0x031111, score = 0.240  
Best luminance at the height 4.0 is above 0x011111, score = 0.215  
  
Read errors per lane: [7, 0, 15, 8]. Lane 1 is the most noisy/problematic.  
Errors from the lane 0 are not intersecting with the errors from the worst lane 1.  
Errors from the lane 3 are not intersecting with the errors from the worst lane 1.  
  
Write errors per lane: [14, 14, 14, 16]. Lane 0 is the most noisy/problematic.  
Errors from the lane 1 are 100.0% eclipsed by the worst lane 0.  
Errors from the lane 2 are 100.0% eclipsed by the worst lane 0.  
Errors from the lane 3 are 100.0% eclipsed by the worst lane 0.  
  
## **Cubieboard1, 540MHz, emr1=0x42**
| dcdc3_vol = 1250  
dram_clk = 540  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 7  
dram_zq = 0x7b  
dram_odt_en = 0  
dram_tpr0 = 0x36947790  
dram_tpr1 = 0xa0c0  
dram_tpr2 = 0x23600  
dram_tpr3 = 0x60000  
dram_emr1 = 0x42  
dram_emr2 = 0x8  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x072222| 0x071111| 0x07**0****0****0****0**|  0x07EEE**E**|  0x07DDDD  
**0x06**|  0x0633**3** 3| 0x062222| 0x06**1****1****1****1**|  0x060000| 0x06EEE**E**|  0x06DDDD  
**0x05**|  0x0533**3** 3| 0x05**2****2****2****2**|  0x051111| 0x050000| 0x05EEE**E**|  0x05DDDD  
**0x04**|  0x0433**3** 3| 0x042222| 0x04**1****1****1****1**|  0x04**0****0****0****0**|  0x04**E****E****E****E**|  0x04**D** DDD  
**0x03**|  0x0333**3** 3| 0x03**2****2****2****2**|  0x031111| 0x03**0****0****0****0**|  0x03**E** EEE| 0x03**D** DDD  
**0x02**|  0x0233**3** 3| 0x022222| 0x02**1****1****1****1**|  0x020000| 0x02EEEE| 0x02**D** DDD  
**0x01**|  0x0133**3** 3| 0x012222| 0x01**1****1****1****1**|  0x01**0****0****0****0**|  0x01EEEE| 0x01**D** DDD  
**0x00**|  0x0033**3** 3| 0x002222| 0x00**1****1****1****1**|  0x00**0****0****0****0**|  0x00EE**E** E| 0x00**D** DDD  
**0x08**|  0x0833**3** 3| 0x082222| 0x081111| 0x080000| 0x08EEE**E**|  0x08**D** DDD  
**0x10**|  0x1033**3** 3| 0x10**2****2****2****2**|  0x101111| 0x10**0****0****0****0**|  0x10EEE**E**|  0x10DDD**D**  
**0x18**|  0x1833**3** 3| 0x18**2****2****2****2**|  0x18**1****1****1****1**|  0x18**0****0****0****0**|  0x18**E****E****E****E**|  0x18DDDD  
**0x20**|  0x2033**3** 3| 0x20**2****2****2****2**|  0x201111| 0x200000| 0x20EEE**E**|  0x20DDDD  
**0x28**|  0x2833**3** 3| 0x28**2****2****2****2**|  0x28**1****1****1****1**|  0x280000| 0x28EEE**E**|  0x28DDDD  
**0x30**|  0x3033**3** 3| 0x30**2****2****2****2**|  0x30**1****1****1****1**|  0x30**0****0****0****0**|  0x30EEE**E**|  0x30DDDD  
**0x38**|  0x3833**3** 3| 0x382222| 0x38**1****1****1****1**|  0x380000| 0x38EEE**E**|  0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [bitflip=34, solidbits=24]  
  
Total number of successful memtester runs: 51  
  
Best luminance at the height 0.5 is above 0x020000, score = 0.190  
Best luminance at the height 1.0 is above 0x020000, score = 0.115  
Best luminance at the height 2.0 is above 0x021111, score = 0.086  
Best luminance at the height 4.0 is above 0x021111, score = 0.069  
  
Read errors per lane: [7, 0, 15, 7]. Lane 1 is the most noisy/problematic.  
Errors from the lane 0 are not intersecting with the errors from the worst lane 1.  
Errors from the lane 3 are not intersecting with the errors from the worst lane 1.  
  
Write errors per lane: [26, 26, 26, 29]. Lane 0 is the most noisy/problematic.  
Errors from the lane 1 are 100.0% eclipsed by the worst lane 0.  
Errors from the lane 2 are 100.0% eclipsed by the worst lane 0.  
Errors from the lane 3 are 100.0% eclipsed by the worst lane 0.  
  
# Searching for optimal "dram_zq" (high 4 bits)
## **Cubieboard1, 576MHz, zq=0x1C**
| dcdc3_vol = 1325  
dram_clk = 576  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 9  
dram_zq = 0x1c  
dram_odt_en = 3  
dram_tpr0 = 0x3ab588b4  
dram_tpr1 = 0xa0d0  
dram_tpr2 = 0x2ba00  
dram_tpr3 = 0x0  
dram_emr1 = 0x4  
dram_emr2 = 0x10  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x07**2****2** 22| 0x071111| 0x07**0****0** 00| 0x07EEE**E**|  0x07DDDD  
**0x06**|  0x063333| 0x062222| 0x061111| 0x060000| 0x06EEE**E**|  0x06DDDD  
**0x05**|  0x053333| 0x052222| 0x051111| 0x050000| 0x05EEE**E**|  0x05DDDD  
**0x04**|  0x043333| 0x042222| 0x041111| 0x040000| 0x04EEE**E**|  0x04DDDD  
**0x03**|  0x033333| 0x032222| 0x031111| 0x030000| 0x03**E** EEE| 0x03**D** DDD  
**0x02**|  0x02**3****3** 33| 0x022222| 0x021111| 0x020000| 0x02EEEE| 0x02**D** DDD  
**0x01**|  0x0133**3** 3| 0x012222| 0x01**1****1** 11| 0x01**0****0** 00| 0x01EEEE| 0x01**D** DDD  
**0x00**|  0x003333| 0x002222| 0x00**1****1** 11| 0x000000| 0x00EEEE| 0x00DDD**D**  
**0x08**|  0x0833**3** 3| 0x082222| 0x081111| 0x080000| 0x08EEEE| 0x08DDD**D**  
**0x10**|  0x1033**3** 3| 0x102222| 0x101111| 0x100000| 0x10EEE**E**|  0x10DDD**D**  
**0x18**|  0x1833**3** 3| 0x182222| 0x181111| 0x180000| 0x18EEE**E**|  0x18DDD**D**  
**0x20**|  0x2033**3** 3| 0x202222| 0x201111| 0x200000| 0x20EEE**E**|  0x20DDDD  
**0x28**|  0x2833**3** 3| 0x282222| 0x281111| 0x280000| 0x28EEE**E**|  0x28DDDD  
**0x30**|  0x3033**3** 3| 0x302222| 0x301111| 0x300000| 0x30EEE**E**|  0x30DDDD  
**0x38**|  0x3833**3** 3| 0x382222| 0x381111| 0x380000| 0x38EEE**E**|  0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [solidbits=16, bitflip=16]  
  
Total number of successful memtester runs: 511  
  
Best luminance at the height 0.5 is above 0x031111, score = 0.817  
Best luminance at the height 1.0 is above 0x031111, score = 0.743  
Best luminance at the height 2.0 is above 0x031111, score = 0.666  
Best luminance at the height 4.0 is above 0x011111, score = 0.617  
  
Read errors per lane: [4, 0, 8, 11]. Lane 0 is the most noisy/problematic.  
Errors from the lane 1 are not intersecting with the errors from the worst lane 0.  
Errors from the lane 3 are not intersecting with the errors from the worst lane 0.  
  
Write errors per lane: [6, 6, 0, 3]. Lane 3 is the most noisy/problematic.  
Errors from the lane 0 are not intersecting with the errors from the worst lane 3.  
Errors from the lane 2 are 100.0% eclipsed by the worst lane 3.  
  
## **Cubieboard1, 576MHz, zq=0x2C**
| dcdc3_vol = 1325  
dram_clk = 576  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 9  
dram_zq = 0x2c  
dram_odt_en = 3  
dram_tpr0 = 0x3ab588b4  
dram_tpr1 = 0xa0d0  
dram_tpr2 = 0x2ba00  
dram_tpr3 = 0x0  
dram_emr1 = 0x4  
dram_emr2 = 0x10  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x072222| 0x071111| 0x070000| 0x07**E****E** EE| 0x07DDDD  
**0x06**|  0x063333| 0x062222| 0x061111| 0x060000| 0x06EEE**E**|  0x06DDDD  
**0x05**|  0x053333| 0x052222| 0x051111| 0x050000| 0x05**E** EEE| 0x05DDDD  
**0x04**|  0x043333| 0x042222| 0x041111| 0x040000| 0x04**E****E** EE| 0x04**D** DDD  
**0x03**|  0x03**3****3** 33| 0x03**2****2** 22| 0x03**1****1** 11| 0x03**0****0** 00| 0x03EEEE| 0x03**D** DDD  
**0x02**|  0x023333| 0x022222| 0x02**1****1** 11| 0x020000| 0x02EEEE| 0x02DDD**D**  
**0x01**|  0x013333| 0x012222| 0x011111| 0x010000| 0x01EEEE| 0x01DDD**D**  
**0x00**|  0x00**3****3** 33| 0x002222| 0x001111| 0x000000| 0x00EEEE| 0x00DDD**D**  
**0x08**|  0x083333| 0x082222| 0x081111| 0x080000| 0x08EEEE| 0x08DDD**D**  
**0x10**|  0x103333| 0x102222| 0x101111| 0x100000| 0x10EEEE| 0x10DDD**D**  
**0x18**|  0x18**3****3** 33| 0x182222| 0x181111| 0x180000| 0x18EEE**E**|  0x18DDD**D**  
**0x20**|  0x2033**3** 3| 0x202222| 0x201111| 0x200000| 0x20EEE**E**|  0x20DDD**D**  
**0x28**|  0x2833**3** 3| 0x282222| 0x281111| 0x280000| 0x28EEE**E**|  0x28DDDD  
**0x30**|  0x3033**3** 3| 0x302222| 0x301111| 0x300000| 0x30EEE**E**|  0x30DDDD  
**0x38**|  0x3833**3** 3| 0x382222| 0x381111| 0x380000| 0x38EEE**E**|  0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [bitflip=16, solidbits=13]  
  
Total number of successful memtester runs: 562  
  
Best luminance at the height 0.5 is above 0x081111, score = 0.878  
Best luminance at the height 1.0 is above 0x081111, score = 0.823  
Best luminance at the height 2.0 is above 0x081111, score = 0.755  
Best luminance at the height 4.0 is above 0x001111, score = 0.688  
  
Read errors per lane: [3, 0, 4, 12]. Lane 0 is the most noisy/problematic.  
Errors from the lane 1 are not intersecting with the errors from the worst lane 0.  
Errors from the lane 3 are not intersecting with the errors from the worst lane 0.  
  
Write errors per lane: [9, 9, 0, 1]. Lane 3 is the most noisy/problematic.  
Errors from the lane 0 are not intersecting with the errors from the worst lane 3.  
Errors from the lane 2 are 100.0% eclipsed by the worst lane 3.  
  
## **Cubieboard1, 576MHz, zq=0x3C**
| dcdc3_vol = 1325  
dram_clk = 576  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 9  
dram_zq = 0x3c  
dram_odt_en = 3  
dram_tpr0 = 0x3ab588b4  
dram_tpr1 = 0xa0d0  
dram_tpr2 = 0x2ba00  
dram_tpr3 = 0x0  
dram_emr1 = 0x4  
dram_emr2 = 0x10  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x07**3****3** 33| 0x072222| 0x071111| 0x070000| 0x07**E** EEE| 0x07DDDD  
**0x06**|  0x06**3****3** 33| 0x062222| 0x061111| 0x060000| 0x06**E** EEE| 0x06DDDD  
**0x05**|  0x05**3****3** 33| 0x052222| 0x051111| 0x050000| 0x05**E** EEE| 0x05DDDD  
**0x04**|  0x043333| 0x042222| 0x041111| 0x040000| 0x04EEEE| 0x04**D** DDD  
**0x03**|  0x033333| 0x032222| 0x031111| 0x030000| 0x03EEEE| 0x03DDDD  
**0x02**|  0x023333| 0x02**2****2** 22| 0x021111| 0x020000| 0x02EEEE| 0x02DDDD  
**0x01**|  0x013333| 0x012222| 0x011111| 0x01**0****0** 00| 0x01EEEE| 0x01DDDD  
**0x00**|  0x003333| 0x00**2****2** 22| 0x001111| 0x000000| 0x00**E****E****E****E**|  0x00**D****D** DD  
**0x08**|  0x083333| 0x082222| 0x08**1****1** 11| 0x080000| 0x08EEEE| 0x08DDD**D**  
**0x10**|  0x103333| 0x102222| 0x101111| 0x100000| 0x10EEEE| 0x10DDD**D**  
**0x18**|  0x183333| 0x182222| 0x181111| 0x180000| 0x18EEEE| 0x18DDD**D**  
**0x20**|  0x203333| 0x202222| 0x201111| 0x200000| 0x20EEE**E**|  0x20DDD**D**  
**0x28**|  0x2833**3** 3| 0x282222| 0x281111| 0x280000| 0x28EEE**E**|  0x28DDDD  
**0x30**|  0x3033**3** 3| 0x302222| 0x301111| 0x300000| 0x30EEE**E**|  0x30DDDD  
**0x38**|  0x3833**3** 3| 0x382222| 0x381111| 0x380000| 0x38EEE**E**|  0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [bitflip=14, solidbits=10]  
  
Total number of successful memtester runs: 571  
  
Best luminance at the height 0.5 is above 0x181111, score = 0.850  
Best luminance at the height 1.0 is above 0x181111, score = 0.786  
Best luminance at the height 2.0 is above 0x101111, score = 0.723  
Best luminance at the height 4.0 is above 0x001111, score = 0.686  
  
Read errors per lane: [4, 0, 3, 7]. Lane 0 is the most noisy/problematic.  
Errors from the lane 1 are not intersecting with the errors from the worst lane 0.  
Errors from the lane 3 are not intersecting with the errors from the worst lane 0.  
  
Write errors per lane: [9, 9, 1, 2]. Lane 3 is the most noisy/problematic.  
Errors from the lane 0 are 50.0% eclipsed by the worst lane 3.  
Errors from the lane 1 are 100.0% eclipsed by the worst lane 3.  
Errors from the lane 2 are 100.0% eclipsed by the worst lane 3.  
  
## **Cubieboard1, 576MHz, zq=0x4C**
| dcdc3_vol = 1325  
dram_clk = 576  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 9  
dram_zq = 0x4c  
dram_odt_en = 3  
dram_tpr0 = 0x3ab588b4  
dram_tpr1 = 0xa0d0  
dram_tpr2 = 0x2ba00  
dram_tpr3 = 0x0  
dram_emr1 = 0x4  
dram_emr2 = 0x10  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x07**3****3** 33| 0x07**2****2** 22| 0x07**1****1** 11| 0x07**0****0** 00| 0x07**E** EEE| 0x07DDDD  
**0x06**|  0x06**3****3** 33| 0x06**2****2** 22| 0x06**1****1** 11| 0x06**0****0** 00| 0x06**E** EEE| 0x06DDDD  
**0x05**|  0x05**3****3** 33| 0x05**2****2** 22| 0x05**1****1** 11| 0x05**0****0** 00| 0x05**E****E** EE| 0x05DDDD  
**0x04**|  0x043333| 0x04**2****2** 22| 0x04**1****1** 11| 0x04**0****0** 00| 0x04**E****E** EE| 0x04DDDD  
**0x03**|  0x033333| 0x03**2****2** 22| 0x031111| 0x030000| 0x03**E****E** EE| 0x03**D** DDD  
**0x02**|  0x023333| 0x02**2****2** 22| 0x021111| 0x02**0****0** 00| 0x02EEEE| 0x02DDDD  
**0x01**|  0x01**3****3** 33| 0x012222| 0x01**1****1****1****1**|  0x01**0****0** 00| 0x01**E****E** EE| 0x01DDDD  
**0x00**|  0x00**3****3** 33| 0x00**2****2** 22| 0x001111| 0x000000| 0x00**E****E** EE| 0x00**D** DDD  
**0x08**|  0x083333| 0x082222| 0x081111| 0x080000| 0x08EEEE| 0x08DDD**D**  
**0x10**|  0x103333| 0x10**2****2** 22| 0x10**1****1** 11| 0x100000| 0x10EEEE| 0x10DDD**D**  
**0x18**|  0x18**3****3** 33| 0x182222| 0x181111| 0x180000| 0x18EEEE| 0x18DDD**D**  
**0x20**|  0x203333| 0x20**2****2** 22| 0x201111| 0x200000| 0x20EEEE| 0x20DDDD  
**0x28**|  0x283333| 0x282222| 0x281111| 0x280000| 0x28EEE**E**|  0x28DDDD  
**0x30**|  0x303333| 0x302222| 0x301111| 0x300000| 0x30EEE**E**|  0x30DDDD  
**0x38**|  0x3833**3** 3| 0x382222| 0x381111| 0x380000| 0x38EEE**E**|  0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [solidbits=26, bitflip=17]  
  
Total number of successful memtester runs: 428  
  
Best luminance at the height 0.5 is above 0x180000, score = 0.775  
Best luminance at the height 1.0 is above 0x201111, score = 0.692  
Best luminance at the height 2.0 is above 0x181111, score = 0.625  
Best luminance at the height 4.0 is above 0x181111, score = 0.558  
  
Read errors per lane: [4, 0, 1, 6]. Lane 0 is the most noisy/problematic.  
Errors from the lane 1 are not intersecting with the errors from the worst lane 0.  
Errors from the lane 3 are not intersecting with the errors from the worst lane 0.  
  
Write errors per lane: [32, 32, 1, 1]. Lane 3 is the most noisy/problematic.  
Errors from the lane 0 are 100.0% eclipsed by the worst lane 3.  
Errors from the lane 1 are 100.0% eclipsed by the worst lane 3.  
Errors from the lane 2 are 100.0% eclipsed by the worst lane 3.  
  
# Searching for optimal "dram_zq" (low 4 bits)
## **Cubieboard1, 576MHz, zq=0x3A**
| dcdc3_vol = 1325  
dram_clk = 576  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 9  
dram_zq = 0x3a  
dram_odt_en = 3  
dram_tpr0 = 0x3ab588b4  
dram_tpr1 = 0xa0d0  
dram_tpr2 = 0x2ba00  
dram_tpr3 = 0x31111  
dram_emr1 = 0x4  
dram_emr2 = 0x10  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x072222| 0x071111| 0x070000| 0x07EEE**E**|  0x07DDDD  
**0x06**|  0x063333| 0x062222| 0x061111| 0x060000| 0x06EEE**E**|  0x06DDDD  
**0x05**|  0x053333| 0x052222| 0x051111| 0x050000| 0x05**E** EEE| 0x05DDDD  
**0x04**|  0x043333| 0x042222| 0x041111| 0x040000| 0x04**E** EEE| 0x04DDDD  
**0x03**|  0x033333| 0x032222| 0x031111| 0x030000| 0x03EEEE| 0x03**D** DDD  
**0x02**|  0x023333| 0x022222| 0x021111| 0x020000| 0x02EEEE| 0x02**D** DDD  
**0x01**|  0x013333| 0x012222| 0x011111| 0x010000| 0x01EEEE| 0x01**D** DDD  
**0x00**|  0x003333| 0x002222| 0x001111| 0x000000| 0x00EEEE| 0x00DDD**D**  
**0x08**|  0x083333| 0x08**2****2** 22| 0x081111| 0x08**0****0** 00| 0x08EEEE| 0x08DDD**D**  
**0x10**|  0x10**3****3** 33| 0x10**2****2** 22| 0x10**1****1** 11| 0x10**0****0** 00| 0x10EEEE| 0x10DDD**D**  
**0x18**|  0x18**3****3** 33| 0x18**2****2** 22| 0x18**1****1** 11| 0x18**0****0** 00| 0x18**E****E** EE| 0x18DDD**D**  
**0x20**|  0x20**3****3** 33| 0x20**2****2** 22| 0x20**1****1** 11| 0x20**0****0** 00| 0x20**E****E** EE| 0x20**D****D** DD  
**0x28**|  0x28**3****3** 33| 0x28**2****2** 22| 0x28**1****1** 11| 0x28**0****0** 00| 0x28**E****E** EE| 0x28DDDD  
**0x30**|  0x30**3****3** 33| 0x30**2****2** 22| 0x30**1****1** 11| 0x30**0****0** 00| 0x30**E****E** EE| 0x30DDDD  
**0x38**|  0x38**3****3** 33| 0x38**2****2** 22| 0x38**1****1** 11| 0x38**0****0** 00| 0x38**E****E** EE| 0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [solidbits=25, bitflip=18]  
  
Total number of successful memtester runs: 419  
  
Best luminance at the height 0.5 is above 0x021111, score = 0.869  
Best luminance at the height 1.0 is above 0x021111, score = 0.808  
Best luminance at the height 2.0 is above 0x021111, score = 0.725  
Best luminance at the height 4.0 is above 0x031111, score = 0.620  
  
Read errors per lane: [5, 0, 0, 6]. Lane 0 is the most noisy/problematic.  
Errors from the lane 3 are not intersecting with the errors from the worst lane 0.  
  
Write errors per lane: [32, 32, 0, 0]. Lane 3 is the most noisy/problematic.  
Errors from the lane 2 are 100.0% eclipsed by the worst lane 3.  
  
## **Cubieboard1, 576MHz, zq=0x3B**
| dcdc3_vol = 1325  
dram_clk = 576  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 9  
dram_zq = 0x3b  
dram_odt_en = 3  
dram_tpr0 = 0x3ab588b4  
dram_tpr1 = 0xa0d0  
dram_tpr2 = 0x2ba00  
dram_tpr3 = 0x101111  
dram_emr1 = 0x4  
dram_emr2 = 0x10  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x072222| 0x071111| 0x070000| 0x07EEE**E**|  0x07DDDD  
**0x06**|  0x063333| 0x062222| 0x061111| 0x060000| 0x06**E** EEE| 0x06DDDD  
**0x05**|  0x053333| 0x052222| 0x051111| 0x050000| 0x05**E** EEE| 0x05DDDD  
**0x04**|  0x043333| 0x042222| 0x041111| 0x040000| 0x04**E** EEE| 0x04DDDD  
**0x03**|  0x033333| 0x032222| 0x031111| 0x030000| 0x03EEEE| 0x03**D** DDD  
**0x02**|  0x023333| 0x022222| 0x021111| 0x020000| 0x02EEEE| 0x02**D** DDD  
**0x01**|  0x013333| 0x012222| 0x011111| 0x010000| 0x01EEEE| 0x01**D** DDD  
**0x00**|  0x003333| 0x002222| 0x001111| 0x000000| 0x00EEEE| 0x00DDD**D**  
**0x08**|  0x083333| 0x082222| 0x081111| 0x080000| 0x08EEEE| 0x08DDD**D**  
**0x10**|  0x103333| 0x102222| 0x101111| 0x100000| 0x10EEEE| 0x10DDD**D**  
**0x18**|  0x183333| 0x182222| 0x181111| 0x180000| 0x18EEEE| 0x18DDD**D**  
**0x20**|  0x203333| 0x202222| 0x201111| 0x200000| 0x20EEE**E**|  0x20DDD**D**  
**0x28**|  0x283333| 0x282222| 0x281111| 0x280000| 0x28EEE**E**|  0x28DDDD  
**0x30**|  0x3033**3** 3| 0x302222| 0x30**1****1** 11| 0x30**0****0** 00| 0x30EEE**E**|  0x30DDDD  
**0x38**|  0x3833**3** 3| 0x38**2****2** 22| 0x38**1****1** 11| 0x38**0****0** 00| 0x38EEE**E**|  0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [bitflip=16, solidbits=7]  
  
Total number of successful memtester runs: 616  
  
Best luminance at the height 0.5 is above 0x001111, score = 0.923  
Best luminance at the height 1.0 is above 0x001111, score = 0.888  
Best luminance at the height 2.0 is above 0x001111, score = 0.839  
Best luminance at the height 4.0 is above 0x001111, score = 0.777  
  
Read errors per lane: [6, 0, 2, 7]. Lane 0 is the most noisy/problematic.  
Errors from the lane 1 are not intersecting with the errors from the worst lane 0.  
Errors from the lane 3 are not intersecting with the errors from the worst lane 0.  
  
Write errors per lane: [5, 5, 0, 3]. Lane 3 is the most noisy/problematic.  
Errors from the lane 0 are not intersecting with the errors from the worst lane 3.  
Errors from the lane 2 are 100.0% eclipsed by the worst lane 3.  
  
## **Cubieboard1, 576MHz, zq=0x3C**
| dcdc3_vol = 1325  
dram_clk = 576  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 9  
dram_zq = 0x3c  
dram_odt_en = 3  
dram_tpr0 = 0x3ab588b4  
dram_tpr1 = 0xa0d0  
dram_tpr2 = 0x2ba00  
dram_tpr3 = 0x0  
dram_emr1 = 0x4  
dram_emr2 = 0x10  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x07**3****3** 33| 0x072222| 0x071111| 0x070000| 0x07**E** EEE| 0x07DDDD  
**0x06**|  0x06**3****3** 33| 0x062222| 0x061111| 0x060000| 0x06**E** EEE| 0x06DDDD  
**0x05**|  0x05**3****3** 33| 0x052222| 0x051111| 0x050000| 0x05**E** EEE| 0x05DDDD  
**0x04**|  0x043333| 0x042222| 0x041111| 0x040000| 0x04EEEE| 0x04**D** DDD  
**0x03**|  0x033333| 0x032222| 0x031111| 0x030000| 0x03EEEE| 0x03DDDD  
**0x02**|  0x023333| 0x02**2****2** 22| 0x021111| 0x020000| 0x02EEEE| 0x02DDDD  
**0x01**|  0x013333| 0x012222| 0x011111| 0x01**0****0** 00| 0x01EEEE| 0x01DDDD  
**0x00**|  0x003333| 0x00**2****2** 22| 0x001111| 0x000000| 0x00**E****E****E****E**|  0x00**D****D** DD  
**0x08**|  0x083333| 0x082222| 0x08**1****1** 11| 0x080000| 0x08EEEE| 0x08DDD**D**  
**0x10**|  0x103333| 0x102222| 0x101111| 0x100000| 0x10EEEE| 0x10DDD**D**  
**0x18**|  0x183333| 0x182222| 0x181111| 0x180000| 0x18EEEE| 0x18DDD**D**  
**0x20**|  0x203333| 0x202222| 0x201111| 0x200000| 0x20EEE**E**|  0x20DDD**D**  
**0x28**|  0x2833**3** 3| 0x282222| 0x281111| 0x280000| 0x28EEE**E**|  0x28DDDD  
**0x30**|  0x3033**3** 3| 0x302222| 0x301111| 0x300000| 0x30EEE**E**|  0x30DDDD  
**0x38**|  0x3833**3** 3| 0x382222| 0x381111| 0x380000| 0x38EEE**E**|  0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [bitflip=14, solidbits=10]  
  
Total number of successful memtester runs: 571  
  
Best luminance at the height 0.5 is above 0x181111, score = 0.850  
Best luminance at the height 1.0 is above 0x181111, score = 0.786  
Best luminance at the height 2.0 is above 0x101111, score = 0.723  
Best luminance at the height 4.0 is above 0x001111, score = 0.686  
  
Read errors per lane: [4, 0, 3, 7]. Lane 0 is the most noisy/problematic.  
Errors from the lane 1 are not intersecting with the errors from the worst lane 0.  
Errors from the lane 3 are not intersecting with the errors from the worst lane 0.  
  
Write errors per lane: [9, 9, 1, 2]. Lane 3 is the most noisy/problematic.  
Errors from the lane 0 are 50.0% eclipsed by the worst lane 3.  
Errors from the lane 1 are 100.0% eclipsed by the worst lane 3.  
Errors from the lane 2 are 100.0% eclipsed by the worst lane 3.  
  
# Additional check for "dram_emr1"
## **Cubieboard1, 576MHz, zq=0x3B, emr1=0x04**
| dcdc3_vol = 1325  
dram_clk = 576  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 9  
dram_zq = 0x3b  
dram_odt_en = 3  
dram_tpr0 = 0x3ab588b4  
dram_tpr1 = 0xa0d0  
dram_tpr2 = 0x2ba00  
dram_tpr3 = 0x101111  
dram_emr1 = 0x4  
dram_emr2 = 0x10  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x072222| 0x071111| 0x070000| 0x07EEE**E**|  0x07DDDD  
**0x06**|  0x063333| 0x062222| 0x061111| 0x060000| 0x06**E** EEE| 0x06DDDD  
**0x05**|  0x053333| 0x052222| 0x051111| 0x050000| 0x05**E** EEE| 0x05DDDD  
**0x04**|  0x043333| 0x042222| 0x041111| 0x040000| 0x04**E** EEE| 0x04DDDD  
**0x03**|  0x033333| 0x032222| 0x031111| 0x030000| 0x03EEEE| 0x03**D** DDD  
**0x02**|  0x023333| 0x022222| 0x021111| 0x020000| 0x02EEEE| 0x02**D** DDD  
**0x01**|  0x013333| 0x012222| 0x011111| 0x010000| 0x01EEEE| 0x01**D** DDD  
**0x00**|  0x003333| 0x002222| 0x001111| 0x000000| 0x00EEEE| 0x00DDD**D**  
**0x08**|  0x083333| 0x082222| 0x081111| 0x080000| 0x08EEEE| 0x08DDD**D**  
**0x10**|  0x103333| 0x102222| 0x101111| 0x100000| 0x10EEEE| 0x10DDD**D**  
**0x18**|  0x183333| 0x182222| 0x181111| 0x180000| 0x18EEEE| 0x18DDD**D**  
**0x20**|  0x203333| 0x202222| 0x201111| 0x200000| 0x20EEE**E**|  0x20DDD**D**  
**0x28**|  0x283333| 0x282222| 0x281111| 0x280000| 0x28EEE**E**|  0x28DDDD  
**0x30**|  0x3033**3** 3| 0x302222| 0x30**1****1** 11| 0x30**0****0** 00| 0x30EEE**E**|  0x30DDDD  
**0x38**|  0x3833**3** 3| 0x38**2****2** 22| 0x38**1****1** 11| 0x38**0****0** 00| 0x38EEE**E**|  0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [bitflip=16, solidbits=7]  
  
Total number of successful memtester runs: 616  
  
Best luminance at the height 0.5 is above 0x001111, score = 0.923  
Best luminance at the height 1.0 is above 0x001111, score = 0.888  
Best luminance at the height 2.0 is above 0x001111, score = 0.839  
Best luminance at the height 4.0 is above 0x001111, score = 0.777  
  
Read errors per lane: [6, 0, 2, 7]. Lane 0 is the most noisy/problematic.  
Errors from the lane 1 are not intersecting with the errors from the worst lane 0.  
Errors from the lane 3 are not intersecting with the errors from the worst lane 0.  
  
Write errors per lane: [5, 5, 0, 3]. Lane 3 is the most noisy/problematic.  
Errors from the lane 0 are not intersecting with the errors from the worst lane 3.  
Errors from the lane 2 are 100.0% eclipsed by the worst lane 3.  
  
## **Cubieboard1, 576MHz, zq=0x3B, emr1=0x06**
| dcdc3_vol = 1325  
dram_clk = 576  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 9  
dram_zq = 0x3b  
dram_odt_en = 3  
dram_tpr0 = 0x3ab588b4  
dram_tpr1 = 0xa0d0  
dram_tpr2 = 0x2ba00  
dram_tpr3 = 0x31111  
dram_emr1 = 0x6  
dram_emr2 = 0x10  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x072222| 0x071111| 0x070000| 0x07**E** EEE| 0x07DDDD  
**0x06**|  0x063333| 0x062222| 0x061111| 0x060000| 0x06**E** EEE| 0x06DDDD  
**0x05**|  0x053333| 0x052222| 0x051111| 0x050000| 0x05**E** EEE| 0x05DDDD  
**0x04**|  0x043333| 0x042222| 0x041111| 0x040000| 0x04EEEE| 0x04DDDD  
**0x03**|  0x033333| 0x032222| 0x031111| 0x030000| 0x03EEEE| 0x03DDDD  
**0x02**|  0x023333| 0x022222| 0x021111| 0x020000| 0x02EEEE| 0x02DDDD  
**0x01**|  0x013333| 0x012222| 0x011111| 0x010000| 0x01EEEE| 0x01**D** DDD  
**0x00**|  0x003333| 0x002222| 0x001111| 0x000000| 0x00EEEE| 0x00DDD**D**  
**0x08**|  0x083333| 0x082222| 0x081111| 0x080000| 0x08EEEE| 0x08DDD**D**  
**0x10**|  0x103333| 0x102222| 0x101111| 0x100000| 0x10EEEE| 0x10DDD**D**  
**0x18**|  0x183333| 0x182222| 0x181111| 0x180000| 0x18EEEE| 0x18DDD**D**  
**0x20**|  0x2033**3** 3| 0x202222| 0x201111| 0x200000| 0x20EEE**E**|  0x20DDDD  
**0x28**|  0x2833**3** 3| 0x28**2****2** 22| 0x281111| 0x280000| 0x28EEE**E**|  0x28DDDD  
**0x30**|  0x3033**3** 3| 0x30**2****2** 22| 0x30**1****1** 11| 0x30**0****0** 00| 0x30EEE**E**|  0x30DDDD  
**0x38**|  0x3833**3** 3| 0x38**2****2** 22| 0x38**1****1** 11| 0x38**0****0** 00| 0x38EEE**E**|  0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [bitflip=20, solidbits=3]  
  
Total number of successful memtester runs: 597  
  
Best luminance at the height 0.5 is above 0x011111, score = 0.922  
Best luminance at the height 1.0 is above 0x011111, score = 0.886  
Best luminance at the height 2.0 is above 0x011111, score = 0.836  
Best luminance at the height 4.0 is above 0x011111, score = 0.770  
  
Read errors per lane: [4, 0, 4, 8]. Lane 0 is the most noisy/problematic.  
Errors from the lane 1 are not intersecting with the errors from the worst lane 0.  
Errors from the lane 3 are not intersecting with the errors from the worst lane 0.  
  
Write errors per lane: [7, 7, 0, 0]. Lane 3 is the most noisy/problematic.  
Errors from the lane 2 are 100.0% eclipsed by the worst lane 3.  
  
# 528MHz with reduced dcdc3 voltage
## **Cubieboard1, 528MHz, zq=0x3B, emr1=0x04, dcdc3=1.25V**
| dcdc3_vol = 1250  
dram_clk = 528  
mbus_clk = 0  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 7  
dram_zq = 0x3b  
dram_odt_en = 3  
dram_tpr0 = 0x36947790  
dram_tpr1 = 0xa0c0  
dram_tpr2 = 0x23600  
dram_tpr3 = 0x0  
dram_emr1 = 0x4  
dram_emr2 = 0x8  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x072222| 0x071111| 0x070000| 0x07**E** EEE| 0x07DDDD  
**0x06**|  0x063333| 0x062222| 0x061111| 0x060000| 0x06**E** EEE| 0x06DDDD  
**0x05**|  0x053333| 0x052222| 0x051111| 0x050000| 0x05**E** EEE| 0x05DDDD  
**0x04**|  0x043333| 0x042222| 0x041111| 0x040000| 0x04EEEE| 0x04DDDD  
**0x03**|  0x033333| 0x032222| 0x031111| 0x030000| 0x03EEEE| 0x03**D** DDD  
**0x02**|  0x023333| 0x022222| 0x021111| 0x020000| 0x02EEEE| 0x02DDDD  
**0x01**|  0x013333| 0x012222| 0x011111| 0x010000| 0x01EEEE| 0x01**D** DDD  
**0x00**|  0x003333| 0x002222| 0x001111| 0x000000| 0x00EEEE| 0x00**D** DDD  
**0x08**|  0x083333| 0x082222| 0x081111| 0x080000| 0x08EEEE| 0x08**D** DDD  
**0x10**|  0x103333| 0x102222| 0x101111| 0x100000| 0x10EEEE| 0x10DDD**D**  
**0x18**|  0x183333| 0x182222| 0x181111| 0x180000| 0x18EEEE| 0x18DDD**D**  
**0x20**|  0x203333| 0x202222| 0x201111| 0x200000| 0x20EEEE| 0x20**D** DDD  
**0x28**|  0x283333| 0x282222| 0x281111| 0x280000| 0x28EEE**E**|  0x28DDDD  
**0x30**|  0x303333| 0x302222| 0x301111| 0x300000| 0x30EEE**E**|  0x30DDDD  
**0x38**|  0x383333| 0x382222| 0x381111| 0x380000| 0x38EEE**E**|  0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [bitflip=7, solidbits=6]  
  
Total number of successful memtester runs: 614  
  
Best luminance at the height 0.5 is above 0x081111, score = 0.917  
Best luminance at the height 1.0 is above 0x081111, score = 0.879  
Best luminance at the height 2.0 is above 0x081111, score = 0.829  
Best luminance at the height 4.0 is above 0x081111, score = 0.767  
  
Read errors per lane: [8, 0, 0, 5]. Lane 3 is the most noisy/problematic.  
Errors from the lane 0 are not intersecting with the errors from the worst lane 3.  
  
Write errors per lane: [0, 0, 0, 0]. Lane 3 is the most noisy/problematic.

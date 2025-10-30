# DRAM Calibration Results/Olimex A20-OLinuXino-Micro Rev.E
< [DRAM Calibration Results][16121]
 
DRAM calibration results for [Olimex A20-OLinuXino-Micro][16124] **rev. E** board. 
## Contents
  * [1 dram_emr1][16125]
    * [1.1 **432MHz, emr1=0x4**][16126]
    * [1.2 **432MHz, emr1=0x44**][16127]
    * [1.3 **432MHz, emr1=0x40**][16128]
  * [2 zq][16129]
    * [2.1 **A20-new-u-boot**][16130]

# dram_emr1
## **432MHz, emr1=0x4**
| dcdc3_vol = 1300  
dram_clk = 432  
mbus_clk = 300  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 7  
dram_zq = 0x7f (0x5294a00)  
dram_odt_en = 0  
dram_tpr0 = 0x2a906690  
dram_tpr1 = 0xa068  
dram_tpr2 = 0x22e00  
dram_tpr3 = 0x0  
dram_emr1 = 0x4  
dram_emr2 = 0x8  
dram_emr3 = 0x0  
dqs_gating_delay = 0x05060505  
active_windowing = 0  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x0733**3** 3| 0x072222| 0x071111| 0x070000| 0x07EEE**E**|  0x07DDDD  
**0x06**|  0x0633**3** 3| 0x062222| 0x061111| 0x060000| 0x06EEE**E**|  0x06DDDD  
**0x05**|  0x0533**3** 3| 0x052222| 0x051111| 0x050000| 0x05EEE**E**|  0x05DDDD  
**0x04**|  0x0433**3** 3| 0x042222| 0x041111| 0x040000| 0x04EEE**E**|  0x04DDDD  
**0x03**|  0x0333**3** 3| 0x032222| 0x031111| 0x030000| 0x03EE**E** E| 0x03DDD**D**  
**0x02**|  0x0233**3** 3| 0x022222| 0x021111| 0x020000| 0x02EE**E** E| 0x02DDDD  
**0x01**|  0x0133**3** 3| 0x012222| 0x011111| 0x010000| 0x01EE**E** E| 0x01DDDD  
**0x00**|  0x0033**3** 3| 0x0022**2****2**|  0x001111| 0x0000**0****0**|  0x00EE**E** E| 0x00DDD**D**  
**0x08**|  0x0833**3** 3| 0x082222| 0x0811**1****1**|  0x0800**0****0**|  0x08EE**E****E**|  0x08DDD**D**  
**0x10**|  0x1033**3** 3| 0x1022**2****2**|  0x1011**1****1**|  0x100000| 0x10EEEE| 0x10DDD**D**  
**0x18**|  0x1833**3** 3| 0x182222| 0x1811**1****1**|  0x1800**0****0**|  0x18EE**E****E**|  0x18DDD**D**  
**0x20**|  0x203333| 0x202222| 0x2011**1****1**|  0x200000| 0x20EEEE| 0x20DDDD  
**0x28**|  0x283333| 0x282222| 0x2811**1****1**|  0x280000| 0x28EE**E****E**|  0x28DDDD  
**0x30**|  0x303333| 0x302222| 0x301111| 0x300000| 0x30EEEE| 0x30DDDD  
**0x38**|  0x383333| 0x382222| 0x381111| 0x380000| 0x38EE**E****E**|  0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [solidbits=20, bitflip=18]  
  
Total number of successful memtester runs: 309  
  
Best luminance at the height 0.5 is above 0x021111, score = 0.760  
Best luminance at the height 1.0 is above 0x021111, score = 0.662  
Best luminance at the height 2.0 is above 0x021111, score = 0.559  
Best luminance at the height 4.0 is above 0x021111, score = 0.462  
  
Read errors per lane: [0, 0, 15, 9]. Lane 1 is the most noisy/problematic.  
Errors from the lane 0 are not intersecting with the errors from the worst lane 1.  
  
Write errors per lane: [0, 0, 14, 14]. Lane 1 is the most noisy/problematic.  
Errors from the lane 0 are 100.0% eclipsed by the worst lane 1.  
  
  

## **432MHz, emr1=0x44**
| dcdc3_vol = 1300  
dram_clk = 432  
mbus_clk = 300  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 7  
dram_zq = 0x7f (0x5294a00)  
dram_odt_en = 0  
dram_tpr0 = 0x2a906690  
dram_tpr1 = 0xa068  
dram_tpr2 = 0x22e00  
dram_tpr3 = 0x21111  
dram_emr1 = 0x44  
dram_emr2 = 0x8  
dram_emr3 = 0x0  
dqs_gating_delay = 0x05060605  
active_windowing = 0  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x0733**3** 3| 0x072222| 0x071111| 0x070000| 0x07EEE**E**|  0x07DDDD  
**0x06**|  0x0633**3****3**|  0x062222| 0x061111| 0x060000| 0x06EEE**E**|  0x06DDDD  
**0x05**|  0x0533**3** 3| 0x052222| 0x051111| 0x050000| 0x05EEE**E**|  0x05DDDD  
**0x04**|  0x0433**3** 3| 0x042222| 0x041111| 0x040000| 0x04EE**E** E| 0x04DDDD  
**0x03**|  0x0333**3** 3| 0x032222| 0x031111| 0x030000| 0x03EE**E** E| 0x03DDDD  
**0x02**|  0x0233**3** 3| 0x022222| 0x021111| 0x020000| 0x02EE**E** E| 0x02DDDD  
**0x01**|  0x0133**3** 3| 0x012222| 0x011111| 0x010000| 0x01EEEE| 0x01DDDD  
**0x00**|  0x0033**3** 3| 0x002222| 0x0011**1****1**|  0x0000**0****0**|  0x00EEEE| 0x00DDD**D**  
**0x08**|  0x0833**3** 3| 0x0822**2****2**|  0x0811**1****1**|  0x0800**0****0**|  0x08EEEE| 0x08DDD**D**  
**0x10**|  0x1033**3** 3| 0x102222| 0x101111| 0x100000| 0x10EE**E****E**|  0x10DDDD  
**0x18**|  0x1833**3** 3| 0x1822**2****2**|  0x1811**1****1**|  0x180000| 0x18EEEE| 0x18DDDD  
**0x20**|  0x203333| 0x2022**2****2**|  0x201111| 0x20**0****0****0****0**|  0x20EEEE| 0x20DDDD  
**0x28**|  0x283333| 0x282222| 0x281111| 0x280000| 0x28EE**E****E**|  0x28DDDD  
**0x30**|  0x303333| 0x302222| 0x3011**1****1**|  0x300000| 0x30EE**E****E**|  0x30DDDD  
**0x38**|  0x383333| 0x382222| 0x381111| 0x380000| 0x38EEEE| 0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [solidbits=20, bitflip=12]  
  
Total number of successful memtester runs: 267  
  
Best luminance at the height 0.5 is above 0x031111, score = 0.745  
Best luminance at the height 1.0 is above 0x031111, score = 0.640  
Best luminance at the height 2.0 is above 0x031111, score = 0.528  
Best luminance at the height 4.0 is above 0x031111, score = 0.421  
  
Read errors per lane: [0, 0, 13, 6]. Lane 1 is the most noisy/problematic.  
Errors from the lane 0 are 16.7% eclipsed by the worst lane 1.  
  
Write errors per lane: [1, 1, 14, 13]. Lane 1 is the most noisy/problematic.  
Errors from the lane 0 are 100.0% eclipsed by the worst lane 1.  
Errors from the lane 2 are 100.0% eclipsed by the worst lane 1.  
Errors from the lane 3 are 100.0% eclipsed by the worst lane 1.   
## **432MHz, emr1=0x40**
| dcdc3_vol = 1300  
dram_clk = 432  
mbus_clk = 300  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 7  
dram_zq = 0x7f (0x5294a00)  
dram_odt_en = 0  
dram_tpr0 = 0x2a906690  
dram_tpr1 = 0xa068  
dram_tpr2 = 0x22e00  
dram_tpr3 = 0x21111  
dram_emr1 = 0x40  
dram_emr2 = 0x8  
dram_emr3 = 0x0  
dqs_gating_delay = 0x05060606  
active_windowing = 0  
---  
| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x0733**3** 3| 0x072222| 0x071111| 0x070000| 0x07EEE**E**|  0x07DDDD  
**0x06**|  0x0633**3** 3| 0x062222| 0x061111| 0x060000| 0x06EEE**E**|  0x06DDDD  
**0x05**|  0x0533**3** 3| 0x052222| 0x051111| 0x050000| 0x05EEE**E**|  0x05DDDD  
**0x04**|  0x0433**3** 3| 0x042222| 0x041111| 0x040000| 0x04EE**E** E| 0x04DDDD  
**0x03**|  0x0333**3** 3| 0x032222| 0x031111| 0x030000| 0x03EE**E** E| 0x03DDDD  
**0x02**|  0x0233**3** 3| 0x022222| 0x021111| 0x020000| 0x02EE**E** E| 0x02DDD**D**  
**0x01**|  0x0133**3** 3| 0x012222| 0x011111| 0x010000| 0x01EEEE| 0x01DDD**D**  
**0x00**|  0x0033**3** 3| 0x0022**2****2**|  0x001111| 0x000000| 0x00EE**E****E**|  0x00DDD**D**  
**0x08**|  0x0833**3** 3| 0x0822**2****2**|  0x081111| 0x080000| 0x08EE**E****E**|  0x08DDD**D**  
**0x10**|  0x1033**3** 3| 0x102222| 0x101111| 0x1000**0****0**|  0x10EE**E****E**|  0x10DDD**D**  
**0x18**| | |  0x18**1****1****1****1**| | |   
**0x20**| | | | | |   
**0x28**| | | | | |   
**0x30**| | | | | |   
**0x38**| | | | | |   
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [solidbits=17, bitflip=11]  
  
Total number of successful memtester runs: 264  
  
Best luminance at the height 0.5 is above 0x031111, score = 0.746  
Best luminance at the height 1.0 is above 0x031111, score = 0.642  
Best luminance at the height 2.0 is above 0x031111, score = 0.529  
Best luminance at the height 4.0 is above 0x031111, score = 0.421  
  
Read errors per lane: [0, 0, 12, 8]. Lane 1 is the most noisy/problematic.  
Errors from the lane 0 are not intersecting with the errors from the worst lane 1.  
  
Write errors per lane: [1, 1, 8, 7]. Lane 1 is the most noisy/problematic.  
Errors from the lane 0 are 100.0% eclipsed by the worst lane 1.  
Errors from the lane 2 are 100.0% eclipsed by the worst lane 1.  
Errors from the lane 3 are 100.0% eclipsed by the worst lane 1.  
  
# zq
<tbody></tbody>dcdc3_vol = 1300  
dram_clk = 432  
mbus_clk = 300  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 7  
dram_zq = 0x4e (0x199cb00)  
dram_odt_en = 3  
dram_tpr0 = 0x2a906690  
dram_tpr1 = 0xa068  
dram_tpr2 = 0x22e00  
dram_tpr3 = 0x41111  
dram_emr1 = 0x4  
dram_emr2 = 0x8  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
<tbody></tbody>mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x072222| 0x071111| 0x070000| 0x07EEEE| 0x07DDDD  
**0x06**|  0x063333| 0x062222| 0x061111| 0x060000| 0x06EEEE| 0x06DDDD  
**0x05**|  0x053333| 0x052222| 0x051111| 0x050000| 0x05EEEE| 0x05DDD**D**  
**0x04**|  0x0433**3****3**|  0x042222| 0x0411**1****1**|  0x0400**0****0**|  0x04EEEE| 0x04DDD**D**  
**0x03**|  0x0333**3****3**|  0x032222| 0x0311**1****1**|  0x0300**0****0**|  0x03EE**E****E**|  0x03**D****D** DD  
**0x02**|  0x023333| 0x0222**2****2**|  0x0211**1****1**|  0x0200**0****0**|  0x02**E****E** EE| 0x02DDDD  
**0x01**|  0x01**3****3** 33| 0x012222| 0x011111| 0x010000| 0x01EEEE| 0x01DD**D****D**  
**0x00**|  0x003333| 0x0022**2****2**|  0x00**1****1****1****1**|  0x000000| 0x00EEEE| 0x00DD**D****D**  
**0x08**|  0x083333| 0x0822**2****2**|  0x081111| 0x080000| 0x08EEEE| 0x08**D****D****D****D**  
**0x10**|  0x103333| 0x102222| 0x10**1****1** 11| 0x100000| 0x10EEEE| 0x10DDDD  
**0x18**|  0x183333| 0x182222| 0x181111| 0x180000| 0x18EEEE| 0x18DDDD  
**0x20**|  0x203333| 0x202222| 0x201111| 0x200000| 0x20EEEE| 0x20DDDD  
**0x28**|  0x283333| 0x282222| 0x281111| 0x280000| 0x28EEEE| 0x28DDDD  
**0x30**|  0x303333| 0x302222| 0x301111| 0x300000| 0x30EEEE| 0x30DDDD  
**0x38**|  0x383333| 0x382222| 0x381111| 0x380000| 0x38EEEE| 0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [solidbits=18, bitflip=4]  
  
Total number of successful memtester runs: 180  
  
Best luminance at the height 0.5 is above 0x061111, score = 0.709  
Best luminance at the height 1.0 is above 0x061111, score = 0.587  
Best luminance at the height 2.0 is above 0x061111, score = 0.451  
Best luminance at the height 4.0 is above 0x061111, score = 0.324  
  
Read errors per lane: [1, 1, 0, 2]. Lane 0 is the most noisy/problematic.  
Errors from the lane 2 are not intersecting with the errors from the worst lane 0.  
Errors from the lane 3 are not intersecting with the errors from the worst lane 0.  
  
Write errors per lane: [5, 5, 16, 16]. Lane 1 is the most noisy/problematic.  
Errors from the lane 0 are 100.0% eclipsed by the worst lane 1.  
Errors from the lane 2 are 40.0% eclipsed by the worst lane 1.  
Errors from the lane 3 are 40.0% eclipsed by the worst lane 1.  
</tbody>
## **A20-new-u-boot**
<tbody></tbody> <tbody></tbody>| dcdc3_vol = 1300  
dram_clk = 432  
mbus_clk = 400  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 7  
dram_zq = 0x5e (0x31deb00)  
dram_odt_en = 3  
dram_tpr0 = 0x2a906690  
dram_tpr1 = 0xa068  
dram_tpr2 = 0x22e00  
dram_tpr3 = 0x41111  
dram_emr1 = 0x4  
dram_emr2 = 0x8  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
<tbody></tbody>| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x072222| 0x071111| 0x070000| 0x07EEEE| 0x07DDD**D**  
**0x06**|  0x063333| 0x062222| 0x061111| 0x060000| 0x06EEEE| 0x06DDD**D**  
**0x05**|  0x053333| 0x052222| 0x051111| 0x050000| 0x05EEEE| 0x05DDD**D**  
**0x04**|  0x043333| 0x042222| 0x041111| 0x040000| 0x04EEEE| 0x04DDD**D**  
**0x03**|  0x033333| 0x032222| 0x031111| 0x030000| 0x03EEEE| 0x03DDDD  
**0x02**|  0x023333| 0x022222| 0x021111| 0x020000| 0x02EEEE| 0x02DDDD  
**0x01**|  0x013333| 0x012222| 0x011111| 0x010000| 0x01EEEE| 0x01DDDD  
**0x00**|  0x003333| 0x002222| 0x00**1****1** 11| 0x0000**0****0**|  0x00EEEE| 0x00DD**D****D**  
**0x08**|  0x0833**3****3**|  0x0822**2****2**|  0x081111| 0x0800**0****0**|  0x08EEEE| 0x08DD**D****D**  
**0x10**|  0x1033**3****3**|  0x1022**2****2**|  0x10**1****1****1****1**|  0x10**0****0****0****0**|  0x10EE**E****E**|  0x10DD**D****D**  
**0x18**|  0x18**3****3****3****3**|  0x1822**2****2**|  0x18**1****1** 11| 0x1800**0****0**|  0x18EE**E****E**|  0x18DD**D****D**  
**0x20**|  0x203333| 0x2022**2****2**|  0x20**1****1** 11| 0x2000**0****0**|  0x20EEEE| 0x20DDDD  
**0x28**| | | | | |   
**0x30**| | | | | |   
**0x38**| | | | | |   
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [solidbits=15, bitflip=11]  
  
Total number of successful memtester runs: 436  
  
Best luminance at the height 0.5 is above 0x031111, score = 0.890  
Best luminance at the height 1.0 is above 0x031111, score = 0.838  
Best luminance at the height 2.0 is above 0x031111, score = 0.763  
Best luminance at the height 4.0 is above 0x031111, score = 0.656  
  
Read errors per lane: [0, 0, 0, 4]. Lane 0 is the most noisy/problematic.  
  
Write errors per lane: [6, 6, 19, 19]. Lane 1 is the most noisy/problematic.  
Errors from the lane 0 are 100.0% eclipsed by the worst lane 1.  
Errors from the lane 2 are 50.0% eclipsed by the worst lane 1.  
Errors from the lane 3 are 50.0% eclipsed by the worst lane 1.  
  
**A20-new-u-boot**
<tbody></tbody> <tbody></tbody>| dcdc3_vol = 1300  
dram_clk = 432  
mbus_clk = 300  
dram_type = 3  
dram_rank_num = 1  
dram_chip_density = 4096  
dram_io_width = 16  
dram_bus_width = 32  
dram_cas = 7  
dram_zq = 0x6e (0x31deb00)  
dram_odt_en = 3  
dram_tpr0 = 0x2a906690  
dram_tpr1 = 0xa068  
dram_tpr2 = 0x22e00  
dram_tpr3 = 0x41111  
dram_emr1 = 0x4  
dram_emr2 = 0x8  
dram_emr3 = 0x0  
dqs_gating_delay = 0x06060606  
active_windowing = 1  
---  
<tbody></tbody>| mfxdly| phase=36| phase=54| phase=72| phase=90| phase=108| phase=126  
---|---|---|---|---|---|---  
**0x07**|  0x073333| 0x072222| 0x071111| 0x070000| 0x07EEEE| 0x07DDDD  
**0x06**|  0x063333| 0x062222| 0x061111| 0x060000| 0x06EEEE| 0x06DDDD  
**0x05**|  0x053333| 0x052222| 0x051111| 0x050000| 0x05EEEE| 0x05DDD**D**  
**0x04**|  0x043333| 0x042222| 0x041111| 0x040000| 0x04EEEE| 0x04DDD**D**  
**0x03**|  0x033333| 0x032222| 0x031111| 0x030000| 0x03EEEE| 0x03DDDD  
**0x02**|  0x023333| 0x022222| 0x021111| 0x020000| 0x02EEEE| 0x02DDDD  
**0x01**|  0x013333| 0x012222| 0x011111| 0x010000| 0x01**E****E****E****E**|  0x01DDDD  
**0x00**|  0x003333| 0x002222| 0x00**1****1****1****1**|  0x000000| 0x00EEEE| 0x00DDDD  
**0x08**|  0x08**3** 333| 0x08**2****2****2****2**|  0x0811**1****1**|  0x0800**0****0**|  0x08EEEE| 0x08DD**D****D**  
**0x10**|  0x1033**3****3**|  0x10**2****2** 22| 0x1011**1****1**|  0x1000**0****0**|  0x10**E****E** EE| 0x10DD**D****D**  
**0x18**|  0x1833**3****3**|  0x18**2****2** 22| 0x1811**1****1**|  0x180000| 0x18**E****E****E****E**|  0x18**D****D****D****D**  
**0x20**|  0x20**3****3** 33| 0x20**2****2****2****2**|  0x20**1****1** 11| 0x200000| 0x20**E****E****E****E**|  0x20DDDD  
**0x28**|  0x283333| 0x2822**2****2**|  0x28**1****1** 11| 0x280000| 0x28**E****E****E****E**|  0x28DDDD  
**0x30**|  0x303333| 0x302222| 0x301111| 0x30**0****0** 00| 0x30EEEE| 0x30**D****D****D****D**  
**0x38**|  0x383333| 0x382222| 0x381111| 0x380000| 0x38EEEE| 0x38DDDD  
Lane phase adjustments: [0, 0, 0, 0]  
Error statistics from memtester: [solidbits=22, bitflip=6, bitspread=1]  
  
Total number of successful memtester runs: 470  
  
Best luminance at the height 0.5 is above 0x031111, score = 0.905  
Best luminance at the height 1.0 is above 0x031111, score = 0.859  
Best luminance at the height 2.0 is above 0x031111, score = 0.791  
Best luminance at the height 4.0 is above 0x031111, score = 0.692  
  
Read errors per lane: [0, 0, 0, 2]. Lane 0 is the most noisy/problematic.  
  
Write errors per lane: [17, 16, 19, 19]. Lane 1 is the most noisy/problematic.  
Errors from the lane 0 are 100.0% eclipsed by the worst lane 1.  
Errors from the lane 2 are 56.2% eclipsed by the worst lane 1.  
Errors from the lane 3 are 52.9% eclipsed by the worst lane 1.  
  
##

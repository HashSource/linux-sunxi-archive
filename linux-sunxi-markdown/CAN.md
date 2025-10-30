# CAN
The CAN controller in sunxi devices supports RX, TX and filtering. Currently the controller is almost identical across each chip with small variations. 
# Versions
There are three variants of the CAN controller: 
  1. A10: Present in the [A10][11113] and [A20][11114]
  2. R40: Present in the [R40][11115] and [T3][11116]
  3. D1: Present in the [D1][11117] and [T113-s3][11118]

The R40 variant is identical to the A10 variant but requires a clock reset. 
The D1 variant is identical to the R40 variant but has moved the filter registers. 
The D1 variant introduces a version register but on the D1 it seems to read 0 rather than 1 as described in the datasheet. 
# Datasheets
Information about this controller is scattered across multiple datasheets: Make sure to check all available revisions if the controller registers are not listed for a device. 
  * The A10, A20 datasheets specify pins and interrupts
  * [Allwinner A20 Manual v1.40][11119] gives a register map for the A10 and A20 CAN controller
  * [File:Sun7i-CANbus.pdf][11120] is just the register map for the A10 and A20 CAN controller
  * [File:Allwinner T3 User Manual V1.0 cleaned.pdf][11121] specifies pins, interrupts and the register map for the T3. Applies to the R40 too
  * [File:T113-s3 datasheet v1.6.pdf][11122] specifies pins but not interrupts for the T113-s3. Applies to the D1 too
  * [Allwinner T113-S3 User Manual v1.1][11123] gives the register map and filter algorithm. Applies to the D1 too

Information not included: 
  * The D1's CAN registers (found to be 53 for CAN0 and 54 for CAN1)
  * Does the filtering algorithm on the D1 appply to the A10 and R40 variants? (Likely yes)

# Filtering
The controllers support a complex input filtering algorithm. This algorithm by default rejects all traffic aside from empty traffic from address 000. 
Set CAN_ACPC to 0x00000000 and CAN_ACPM to 0xFFFFFFFF to allow all traffic. 
This algorithm is described in the T113-S3 user manual v1.1 using various diagrams with somewhat unclear diagrams and graphs. Some light reverse engineering may be required to document this properly. 
The user manual heavily implies that filtered traffic is not stored in the RX buffer but this is not the case (on the D1 at least), filtered traffic only avoids an interrupt.

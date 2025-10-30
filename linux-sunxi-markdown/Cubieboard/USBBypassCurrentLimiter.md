# Cubieboard/USBBypassCurrentLimiter
< [Cubieboard][14519]
 
# Introduction
Normally the maximum current provided by the two USB ports of the Cubieboard is limited by the ICs U10 and U11. One of these ICs (U11) can easily bridged by a 0805 0-Ohm-resistor, a piece of wire or a soldering blob. In the schematic, the "not connected" resistor pads for this is marked with "R89". This completely disables the current limiting feature for USB port 1 (the lower one). This might be needed in case of connecting a 2,5"-HDD to the USB port, which will not be supplied externally. 
# How it is done
[![][14522]][14523]
[][14524]
Location of the R89 pads on the bottom side
  1. First, you have to locate the free "R89" pads on the board. There is very less printing on the board, so you have to find them either by measuring or by logical thinking. The "R89"-pads are located 
     * on the bottom side
     * more or less between the NAND IC and the USB solderings
     * in this whole area, these pads are the only ones where a 0805 resistor would fit
     * the IC directly next to the pads is U11
  2. After locating the pads, you can start soldering. The easiest way to bridge these pads is to produce a liquid solder blob on one of the pads and then pull it carefully to the other pad with the soldering iron. If it does not cover both pads automatically, more solder might be needed.
  3. Job finished.

[![][14525]][14526]
[][14527]
Location of the R89 pads on the bottom side
# Warning
  * When the bridge is inserted, there will be no protection against wrong polarity on the USB port! The board itself is protected, but not the USB port.
  * If a short circuit on the USB device occures and the power supply is strong enough, the whole board can be damaged!

# CubietechKernel
Please explain the purpose of the commits: 
[rtp: rename sun4i-ts to sunxi-ts][14826]
sun4i-ts seems doesn't work fine with tslib. We want to see if sunxi-ts from new SDK is better. just at debug stage, and not recommend to use it now. 
  
[gmac: use mac address from chipid][14827]
Some users complain about the MAC address keep changing after reboot. the CHIPID is unique from chip to chip, we may generate unique MAC address from it.

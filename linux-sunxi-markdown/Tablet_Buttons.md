# Tablet Buttons
The buttons of a tablet are handled by two different drivers and exposed by different event devices. 
## Contents
  * [1 Power Button][54220]
  * [2 Other Buttons][54221]
  * [3 Testing][54222]
  * [4 Sunxi 3.4][54223]
  * [5 Mainline][54224]

### Power Button
Since the power button is relevant for power control, it is attached to the power management hardware. Install acpid for controlled shutdown using this button. Note the [FEX][54225] _power_start_ setting, which has an effect on reboot/halt, when connected to AC power. 
### Other Buttons
These are all other buttons like Vol+, Menu, etc. 
### Testing
For testing use the _evtest_ utility. 
### Sunxi 3.4
For non-power buttons use the sun4i_keyboard module. 
### Mainline
Buttons are currently hot in the pipelines, but work well. See this [thread][54226] for references to patches. 
The non-power keys additionally need some special device tree entries. This is a funny device, an ADC actually, where each key is identified by a particular voltage, naturally the values are device depend.

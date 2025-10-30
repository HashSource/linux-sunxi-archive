# Windowmanager
## TabletWM and TabletLauncher
TabletWM is a window manager for the X Window System designed specifically for tablets. Its main characteristic is that it keeps all windows maximized and without decorations, allowing to work with classic linux apps in a tablet-style. 
It also includes an on-screen keyboard, and a bar with buttons that allows to close the current application, change to the next... 
[![Tabletwm.png][59402]][59403]
The picture above shows LibreOffice and the on-screen keyboard working with TabletWM. 
By default both the bar and the on-screen are hidden, until the user presses Ctrl+MENU keys. This combination shows both the bar and the on-screen keyboard. This combination is emulated by the [GSL1680][59404] touch driver when the user touches with three fingers. This allows to work with classic desktop applications without a physical keyboard and mouse. 
By pressing MENU key, or moving the mouse cursor to the bottom of the screen, only the bar will be shown. This allows to work better when using an external keyboard and mouse. 
There is also TabletLauncher, an application launcher designed to be used with TabletWM: 
[![Tabletlauncher.png][59405]][59406]
All this code can be downloaded from the author's homepage: 
[[TabletWM][59407]] [[TabletLauncher][59408]]

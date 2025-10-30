# VNC
## Remote administration using VNC from boot with Linaro
In this page we see how to use setup our Linux bootable image so that it is automatically accessible remotely through VNC from the login-screen. The following instructions have been tested with Ubuntu/Linaro. Other GNU/Linux distributions may require modifications. 
  * Run the commands

[code] 
    sudo apt-get update
    sudo apt-get install lightdm-gtk-greeter x11vnc
    sudo x11vnc -storepasswd /etc/x11vnc.pass
[/code]
The first command will update the package list (requires Internet connection) and the second command installs two packages. The third command creates a password for VNC. 
  * Then, edit /etc/lightdm/lightdm.conf with

[code] 
    sudo nano /etc/lightdm/lightdm.conf
[/code]
  

  * and adjust as follows to disable autologin / enable login screen for VNC

[code] 
    [SeatDefaults]
    greeter-session=lightdm-gtk-greeter
    user-session=Lubuntu
    #autologin-user=linaro
[/code]
  * Note, that you can select whether you want to enable autologin. The above example disables autologin to get the login-session-start event for VNC. To enable, remove the comment # character from the start of the line. But Re-enabling autologin will prevent VNC from launching automatic.

  * Now create a new file with

[code] 
    sudo nano /etc/init/x11vnc.conf
[/code]
  * and add the following content:

[code] 
    start on login-session-start
    script
    /usr/bin/x11vnc -xkb -auth /var/run/lightdm/root/:0 -noxrecord -noxfixes -noxdamage -rfbauth /etc/x11vnc.pass -forever -bg -rfbport 5900 -o /var/log/x11vnc.log
    end script
[/code]
  * Save and exit. Then, you can start vnc by typing:

[code] 
    start x11vnc
[/code]
Note that x11vnc will be automatically started after each boot until you remove this `/etc/init/x11vnc.conf` script. 
You should then be able to login with any VNC-viewer (like **remmina** , **vncviewer** , etc… in Ubuntu) with your given password @ port 5900 and can login with any user available. 
(Thanks to Martin Wild for the above instructions)

# Packages
The linux-sunxi community provides a repository with packages for various distributions at <http://packages.linux-sunxi.org/> This mostly contains packages specific for sunxi hardware. 
## Contents
  * [1 Available packages][43982]
  * [2 debian/ubuntu][43983]
  * [3 fedora][43984]
  * [4 Possible issues][43985]

# Available packages
The following packages are available: 
  * [fbturbo X driver][43986]: a sped up version of the fbdev driver, which also supports 3D acceleration.
  * [libump][43987]: ARMs Universal Memory Provider, as needed by the fbturbo driver.
  * Mesa with SDK: needed for building and running the lima mesa driver.

# debian/ubuntu
There are specific repositories available for debian and ubuntu. 
Add the repository to your /etc/apt/sources.list: 
[code] 
    deb http://packages.linux-sunxi.org/ubuntu/ quantal main
    deb-src http://packages.linux-sunxi.org/ubuntu/ quantal main
    
[/code]
The above is for ubuntu, quantal quetzal (12.10), replace this with your own distribution and distribution version codename. 
To have apt prefer packages from linux-sunxi over the distributions own, you need to set linux-sunxi to a higher preference than the standard packages. Create /etc/apt/preferences.d/00-linux-sunxi with the following content: 
[code] 
    Package: *
    Pin: origin packages.linux-sunxi.org
    Pin-Priority: 990
    
[/code]
You should now be able to apt-get install packages from this repository. If you want to re-install packages but this time round from the sunxi repos, use: 
[code] 
    apt-get install --reinstall packagename
    
[/code]
  

# fedora
... 
# Possible issues

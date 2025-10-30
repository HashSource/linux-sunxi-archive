# Cubietech Cubieboard/Android TV image
< [Cubietech Cubieboard][13505](Redirected from [Cubieboard/Android TV image][13506])
 
The system running on Cubieboard can be customized,and this page is going to tell you how to build android operating system by yourself. Here I suggest you using Ubuntu 12.04(x86_64) as your building environment. If you have not setup your android buiding environment before, you should reference to [Setting up build environment][13509]
## Contents
  * [1 simple way][13510]
    * [1.1 Download the source code][13511]
    * [1.2 Compiling][13512]
    * [1.3 Generating final image][13513]
  * [2 google way][13514]
    * [2.1 Download the source code using git/repo][13515]
    * [2.2 Compiling][13516]
    * [2.3 Generating final image][13517]
  * [3 See also][13518]

# simple way
## Download the source code
[code] 
    $wget <http://dl.cubieboard.org/software/a10-cubieboard/android/cubieboard_opentv.tar.gz>
    
[/code]
## Compiling
[code] 
    $tar -zxf cubieboard_opentv.tar.gz
    $cd cubieboard_opentv/
    $source build/envsetup.sh && lunch #select cubieboard
    $make -j5 # 5 if quadcore, 3 if dualcore.
    
[/code]
## Generating final image
[code] 
    $tools/pack-cm.sh
    
[/code]
# google way
## Download the source code using git/repo
[code] 
    $mkdir ~/bin
    $curl <https://raw.github.com/cubieboard/git-repo/stable/repo> > ~/bin/repo
    $export PATH=$PATH:~/bin 
    $chmod +x ~/bin/repo
    $mkdir openbox && cd openbox
    $repo init --no-repo-verify -u <git://github.com/cubieboard/manifests> -b cb -m openbox.xml  
    $repo sync
    
[/code]
## Compiling
[code] 
    $source build/envsetup.sh && lunch #select cubieboard
    $make -j4
    
[/code]
## Generating final image
[code] 
    $tools/pack-cm.sh
    
[/code]
by now, we can flash the image to your cubieboard using livesuilt tool. 
# See also
  * [Android (operating system)][13519]
  * [Cubieboard][13520]

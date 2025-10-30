# Cubieboard/Building Jellybean
< [Cubieboard][13551]
 
Instruction to build jellybean for cubieboard 
## Contents
  * [1 Download the source code][13554]
  * [2 Start to build][13555]
  * [3 Generate firmware image][13556]
  * [4 Known Issues][13557]
  * [5 See also][13558]

## Download the source code
[code] 
    $ mkdir openbox && cd openbox
    $ repo init --no-repo-verify -u <git://github.com/cubieboard/manifests> -b cb -m openbox.xml  
    $ repo sync
    
[/code]
or see <https://github.com/cubieboard/manifests> for up-to-date instructions. 
Note: you may need to edit manifest.xml after this to say **git:// instead of https://**. Http downloads from github tend to fail. 
## Start to build
On 64bit system you need 32bit build environment. 
You will need **g++-4.4**
g++-4.7 is too new at this moment. 
You will need **lib32z1** (x86 32bit libz.so.1) - the prebuilt android tools are linked with it but it is not included in the repo. 
[code] 
    $source build/envsetup.sh
    $lunch 4
    $make
    
[/code]
[http://linux-sunxi.org/Cubieboard][13559]
## Generate firmware image
[code] 
     $tools/pack-cm.sh
    
[/code]
## Known Issues
  * Ethernet is not supported currently

# See also
  * [Android (operating system)][13560]
  * [Cubieboard][13551]

# OpenixCard
OpenixCard is a Open Source Version of Allwinner PhoenixCard to Dump, Unpack, Flash Allwinner IMG Files on Linux 
## Contents
  * [1 Building from Source][41969]
    * [1.1 Prerequisites][41970]
      * [1.1.1 cmake, autoconf, libconfuse-dev][41971]
        * [1.1.1.1 Debian/Ubuntu][41972]
        * [1.1.1.2 ArchLinux][41973]
    * [1.2 Repository][41974]
    * [1.3 Building][41975]
  * [2 Usage][41976]
  * [3 See also][41977]

# Building from Source
[![Information.png][41978]][41979] See also [Instructions in the README][41980]
## Prerequisites
### cmake, autoconf, libconfuse-dev
#### Debian/Ubuntu
[code] 
    apt install cmake autoconf libconfuse-dev pkg-config
[/code]
#### ArchLinux
[code] 
    pacman -S cmake autoconf confuse pkg-config
[/code]
## Repository
The repository is located on [GitHub][41981]. 
Change to the directory that you would like to clone the repository into and use: 
[code] 
    apt-get install git
    git clone --recursive https://github.com/YuzukiTsuru/OpenixCard
    
[/code]
## Building
Make new build directory 
[code] 
    mkdir build
    cd build
    
[/code]
Make 
[code] 
    cmake .. && make -j
    
[/code]
The compiled application is in the dist directory in the build directory. 
# Usage
[code] 
     _____             _     _____           _ 
    |     |___ ___ ___|_|_ _|     |___ ___ _| |
    |  |  | . | -_|   | |_'_|   --| .'|  _| . |
    |_____|  _|___|_|_|_|_,_|_____|__,|_| |___|
          |_| 
    Copyright (c) 2022, YuzukiTsuru <[[email protected]][41982]>
    
    Usage: OpenixCard [options] 
    
    Optional arguments:
    -h --help       shows help message and exits [default: false]
    -v --version    prints version information and exits [default: false]
    -u --unpack     Unpack Allwinner Image to folder [default: false]
    -d --dump       Convert Allwinner image to regular image [default: false]
    -c --cfg        Get Allwinner image partition table cfg file [default: false]
    -p --pack       Pack dumped Allwinner image to regular image from folder [default: false]
    -i --input      Input Allwinner image file [required]
    
    eg.
    
    OpenixCard                  - TUI Interface -> NOT AVALIABLE
    OpenixCard -u -i <img>      - Unpack Allwinner image to target
    OpenixCard -u -c -i <img>   - Unpack Allwinner image to target and generate Allwinner image partition table cfg
    OpenixCard -d -i <img>      - Convert Allwinner image to regular image
    OpenixCard -p -i <dir>      - Pack dumped Allwinner image to regular image from folder
    
[/code]
# See also
  * [Sunxi-tools][41983]
  * [Git Repository][41981]

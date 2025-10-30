# CedarX/RE Toolkit
< [CedarX][11715]
 
This page collects all information to create a suitable environment, as a start with reverse engineering the video engine. 
  

## Contents
  * [1 armhf/armel rootfs?][11718]
    * [1.1 .a libraries from the android sdk can be used in gnu/linux?][11719]
    * [1.2 Howto bootstrap a minimal debian armel rootfs from inside armhf.][11720]
  * [2 Old][11721]
  * [3 Laundry][11722]
  * [4 Tracing][11723]
    * [4.1 valgrind-ammt][11724]
      * [4.1.1 tracecatcher.py][11725]
      * [4.1.2 ltv][11726]

# armhf/armel rootfs?
This is a question of personal preference. Only needed to be aware is that android is armel as for this fact the availability of close source binaries blobs is greater. There is also some armhf binaries blobs, but have some caveats: only decoder, older versions and with bugs. 
Another option is the use of [libhybris][11727]. 
## .a libraries from the android sdk can be used in gnu/linux?
The android sdk release contains .a variants of the close blob libraries, and as this is only a archive of .o objects. They should link, only is needed to be aware that they are compiled with android specifics, and workarounds are required for unresolved symbols, by implementing stubs or by other means. 
**Further investigation required.** Only up to now was tested libjpegenc.a with a usable result. 
## Howto bootstrap a minimal debian armel rootfs from inside armhf.
Chrooting into a armel roofs is also a solution. 
Variant buildd installs build-essential packages: 
[code] 
    debootstrap --verbose --arch armel --variant=buildd wheezy ./armelroot <http://ftp.debian.org/debian>
    
[/code]
Chrooting to: 
[code] 
    mount -t proc proc armelroot/proc
    mount -t devtmpfs devtmpfs armelroot/dev
    chroot --userspec=USER:GROUP armelroot
    
[/code]
# Old
  * **VLC** [compile instructions and usage][11728].

To not skip frames, and to have control of the play speed, some optional arguments are useful. Putting them in a shell script to facilitate the reuse, can be as example: 
[code] 
    #!/bin/sh
    cvlc ?????
    
[/code]
Encoding is spread in multiples libraries, each with one function. 
  * **h264** [github.com/patrickhwood/h264encoder][11729] a minimal example of h264 encoding, takes raw video frames as input, and outputs a h264 mkv video file.

  * **jpeg** There was made a initial trial to get working [libjpegenc.a][11730] in a A13, which result in success.

# Laundry
  * Minimal examples [[1]][11731]
  * Use the most recent [allwinner blobs][11732] and [header files][11733]

# Tracing
## valgrind-ammt
This is a tracer in the form of valgrind tool, that uses valgrind instrument capabilities to trace memory access and functions of interest. As valgrind is a virtual cpu, the traced program will run considerable slower. 
For compile instructions see [ammt][11734] directory. If using a release version of valgrind, after applied this patch is required to also run autogen.sh. Example usage: 
[code] 
    /dir/to/valgrind/vg-in-place    \
    -q                              \
    --vgdb=no                       \
    --trace-children=yes            \
    --log-file=trace.log            \
    --tool=ammt                     \
    --trace-file=/dev/cedar_dev     \
    --show-stack-fnnames=yes        \
    program_to_be_traced
    
[/code]
### tracecatcher.py
tracecatcher.py is helper script to catch traces files. Is a tcp server listening for connections, and if recognizes an AMMT trace, will name and save the trace to a file in the current directory. 
Usage, Run valgrind-ammt with the option --log-socket=ipaddress:port 
[code] 
    ./tracecatcher.py ipaddress port
    
[/code]
### ltv
This is a viewer of traces made in format outputted from valgrind-ammt. For usage see README.

# CedarX/Reverse Engineering
< [CedarX][11764]
 
# Current status
[![MBOX icon important.png][11767]][11768] | **FIRST NOTE: Allwinner's[video de-/encoding engine][11769] is successfully reverse engineered in the most common parts (HEVC, H264, MPEG1/2, MPEG4).** The results of this reverse engineering are bundled in a [vdpau driver backend][11770] since January 2014. To do hardware accelerated video decoding on sunxi devices nowadays, you don't need any software provided by Allwinner, which is either (partly) closed sourced and/ or violating the GPL. Instead you should use the result of the community's reverse engineering work, called [Cedrus][11771]. As this is only proof of concept code, the goal is a [mainlined video engine driver][11772] in the end. To take full advantage of such a driver, the other bits (display, hdmi, sound ...) also have to be rewritten in ongoing [mainline process][11773].   
  
---|---  
# Hardware registers
The closed source blob uses direct access to hardware registers using mmap to userspace. Currently known register usage is documented: 
  * [VE Register guide][11774]
  * [ACE Register guide][11775]

There's ongoing register documentation effort using [envytools][11776]. 
# Progress history
15 June 2012
    Iain Bullard [started reverse engineering the proprietary libraries][11777]. 
  * [open_cdxalloc][11778] as an free reimplementation of [Allwinner][11779]'s `libcederxalloc.a`.
  * [CedarXWrapper][11780] as a `LD_PRELOAD`ed wrapper to help understanding the proprietary libraries.
  * [CedarXPlayerTest][11781] as a basic player to use when testing.

3 May 2013
    wingrime and oliver started work on register guide, JPEG, MPEG decoding manuals and [binary analysis][11782].
20 May 2013
    nove introduced new MMIO tracer based on Valgrind 
  * [ReCedro][11783] has similar tools as those from IanB above, but with a different angle, works really well.

22 June 2013
    JPEG decoding proof-of-concept was introduced by Jemk [JPEG/MPEG-12 Decoding PoC][11784]
30 August 2013
    Workable proof-of-concept VDPAU decoder was introduced by Jemk support MPEG-1/2 and MPEG-4 AVC/h.264 decoding [libvdpau-sunxi][11785]
24 August ~ 12 September 2013
    Paullo612 worked in documenting vp8 decoding.
12 January 2014
    First MPEG-4 AVC/h.264 encoder proof-of-concept from Jemk
15 January 2014
    Jpeg encoding proof-of-concept by nove [jepoc][11786]
31 January 2014
    Jemk added to libvdpau-sunxi the first support for decoding (some) mpeg4 videos
28 November 2015
    Jemk added [initial H.265 support][11787] to libvdpau-sunxi
12 July 2016
    ubobrov modified Jemk's proof-of-concept h264 encoder sources making them workable on [H3 platform][11788]
A first proof at the end ...

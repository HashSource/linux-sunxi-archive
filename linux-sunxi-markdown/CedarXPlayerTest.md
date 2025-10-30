# CedarXPlayerTest
CedarXPlayerTest is a testing video player for Allwinner A10, from the [Mele Ubuntu Image][12053]. 
It can play almost all video formats because of linked in LAVF demuxer (GPL violation). It also seem to have broken support online playback by http (connection and caching seems to work, but it crashes before playback start). Relative seek by J and K keys is supported, but no absolute seek support. SPACE is pause, Q is exit 
CPU load is very low: can smoothly play video with sound when CPU is underclocked to 48 MHz. Audio seems to be decoded with CedarA 
You can get it from <https://github.com/iainb/CedarXPlayerTest/>
Only 1.4.1 version seems to work. 
# Usage
CedarXPlayerTest compiled for armel systems, but can be run on armhf: 
[code] 
    cd /path/to/CedarXPlayerTest
    /lib/ld-linux-armhf.so.3 --library-path . /path/to/file >/dev/null
    
[/code]
By default, only fullscreen (with no aspect ratio keeping) playback on screen0 is supported, but output can be resized through disp driver by other applications, and screen can be overriden by ioctl wrappers 
CedarXPlayerTest requres root because it is trying to change thread scheduling mode to SCHED_RR. It also can be fixed by some wrappers. 
# GUI
There is a simple X11 gui for this player: 
<https://github.com/mittorn/cedarxplayertest-gui>
Supported features: 
  * Video in window
  * Keep aspect ratio
  * Crop/Resize video
  * Seek by arrow keys
  * Seek by scroll
  * Simple mouse control
  * ColorKey (video can be overlapped by other windows)
  * Onscreen buttons
  * Fullscreen mode by doubleclick or F key
  * Screen1 suport (by preloadable library with wrappers)
  * Work without root (by preloadable library with wrappers)
  * Display current position and duration
  * Smart seeker (emulate absolute seeker using relative)
  * Can work with audio too
  * External subtitle support (srt)

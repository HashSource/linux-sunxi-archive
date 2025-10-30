# CedarX/Misc Docs
< [CedarX][11683]
 
## Overlays
[code] 
    <tomee^> meanwhile, any of you tried (wrote? :>) the vdpau driver?
    <arokux> tomee^: you should ask wingrime, ssvb rellla jemk etc.
    <mnemoc> tomee^: jemk is one of the care cedarx devs
    <tomee^> anyway, I got it working, but now I am wondering if there's any way to use overlays with it
    <tomee^> already implemented/planned or vlc->demux->vdpau->vram->memcpy->ram->overlays/compositing->memcpy->vram ...
    <jemk> tomee^: overlays aren't possible yet, i had tried it, but it needs a lot of memcpy which kills performance
    <jemk> tomee^: or it needs some way to interact with the xorg driver (or ignore it and take the whole screen)
    <tomee^> jemk: neither with "pure" libcedarx?
    <jemk> tomee^: i don't work on libcedarx, but it doesn't have overlays either
    <tomee^> jemk: i see. so what's rendered inside the program window/fb coords cannot be in any way changed.
    <tomee^> jemk: only possibility is to f*ck with memcpys which will bring the performance back to softdecoding or draw other stuff aside (e.g. subtitles below the video, given the video is not full-screen)
    <tomee^> jemk: did I get that right?
    <Turl> maybe you can use disp layers for that
    <jemk> tomee^: yes, thats one way, the other would be to figure out some inteligent way of using disp layers, but as only two layers can be blended and the video layer already is the second one...
    <jemk> for fullscreen it would be no problem at all, there video is back layer and subtitles front layer
    <jemk> but in window mode desktop is back layer and video front and nothing left for overlay
    <torbenh3> mnemoc: i have other things todo.... testing it in the evening.
    <tomee^> jemk: hmm, so in fullscreen 2 layers can be blended...
    <jemk> for fully visible windows same as fullscreen, but such things can only be decided by xorg driver
    <tomee^> jemk: you mean that 2 RGBA framebuffers are composited into one?
    <jemk> tomee^: disp can blend two layers without copy, but only two
    <tomee^> ok
    <tomee^> so that would require 3 or 4 framebuffers?
    <tomee^> 1 for widgets, 1 for video, another one for off-screen widget redraw = 3 ?
    <tomee^> and then swapping 3->1 then compositing 1+2 ?
    <jemk> tomee^: in vdpau those are all handled by VideoSurfaces and OutputSurfaces, so that's no problem, the only problem is to bring those surfaces to display without copying them around
    <tomee^> but that's not yet implemented, right? :)
    <jemk> right, because it is nearly impossible to get fully compatible vdpau. it would be easy to write it for special needs like fullscreen, but not universal
    <tomee^> yeah, I know
    <jemk> well, not impossible if you allow copying, but that makes watching 1080p not very funny
    <tomee^> but vdpau is already somewhat more promising than cedarx... since VDPAU is at least SOMEWHAT of an abstraction layer
    <jemk> but it's an abstraction layer that has too many possible ways of doing things that can't be represented by the limited hardware in arm socs.
    <tomee^> yup
    <tomee^> I cannot argue with the fact that you are right and more your knowledge is more comprehensive that mine
    <tomee^> still, from my point of view, mplayer+vdpau/sunxi=no subtitles ;-)
    <tomee^> while, I think, the stagefright android binaries somehow do support subtitle rendering in hardware
    <jemk> possible, but android hasn't have to handle obscured windows. if the vdpau window is allways on top the same as for fullscreen works
    <Turl> you could composite all desktop and subtitles by software to a layer and have the video on the 2nd one
    <jemk> Turl: i talked with ssvb some months ago about possible tricks, but they all need much work and xorg driver interaction
    <jemk> like only copying the part of the video that is used for subtitles
    <tomee^> Turl: couldn't that be done with acceleration? the compositing I mean.
    <tomee^> I don't care about playback in a window as long as I can draw something on the video
    <Turl> I'm not much into the graphics stack, but I think there's two alpha layers that get blended by sw
    <Turl> if you can put the subtitles onto the desktop layer, then they could be overlayed over the video
    <tomee^> jemk: when I played with mxplayer, I managed to get 2 sets of subtitles (one s/w, one h/w I guess), plus the top menu bar visible... this is far from Xorg complexity, but shows that the hardware can cope with that
    <tomee^> Turl: say, an mplayer playing transparent video file + subtitles overlaid on top of the proper vdpau-drawn video?
    <Turl> tomee^: I mean one layer with your desktop, mplayer window, a hole instead of video, and subtitles inside the hole
    <Turl> and a second layer with the video
    <jemk> Turl: possible, but not nice, especially as vdpau redraws all layers each frame, so the subtitles get redrawn too
    <juanfont> tomee^, jemk these overlay problems also affect xbmc when running standalone?
    <jemk> juanfont_: if you have xbmc running fullscreen or even without xorg it is much easier
    <jemk> juanfont_: but xthe upstream bmc uses opengl for rendering, so it's totaly different there anyways
    <juanfont_> jemk but, XBMC+VDPUA is not possible due to the lack of the required OpenGL extension in OpenGLES, is it? 
    <jemk> juanfont_: think so, but i didn't look too deep into xbmc
    
[/code]

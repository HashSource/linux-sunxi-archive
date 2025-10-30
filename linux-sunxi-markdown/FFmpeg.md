# FFmpeg
[![MBOX icon edit-clear.png][19123]][19124] | **This ffmpeg fork is without an active maintainer and its hardware h264 encoding implemention is based from an older version of the proof of concept source-code.** Per this reason this implementation doesn't represent the actual state of knowledge about the workings of h264 encoding in the hardware. Moreover because the vendor's kernel doesn't have any future, the little time available by the people working in the [Cedrus project][19125] is concentrated in pushing the mainlineable driver forward, meaning any work in the encoding side will always be second priority. Anyone that wishes to work in improving the use of h264 encoding with the vendor's kernel, is very welcome to join [Cedrus project][19125], we will be very glad to help make this possible.   
---|---  
[![MBOX icon important.png][19126]][19127] | **The following is only _working_ with 3.4 kernel and in A10/A10s/A13/A20 SOCs.**  
---|---  
## FFmpeg for sunxi
This is an FFmpeg implementation for sunxi devices based on great work by jemk & alcantor (i.e cedrus ). 
Here is the git address: <https://github.com/stulluk/FFmpeg-Cedrus>
The repository contains a *deb file for easy installation trial. 
( Please see readme) 
Typical usage to capture from CSI camera and encode to h264 via Cedrus library and output as RTSP: 
ffmpeg -f v4l2 -video_size 640x480 -i /dev/video0 -pix_fmt nv12 -r 25 -c:v cedrus264 -f mpegts - | cvlc - --sout "#:rtp{sdp=rtsp://:8554/}" 
( TBD)

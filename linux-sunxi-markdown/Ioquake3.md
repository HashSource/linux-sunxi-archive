# Ioquake3
## Contents
  * [1 Porting][28023]
  * [2 Building][28024]
  * [3 Running][28025]
  * [4 Benchmark results][28026]
  * [5 TODO][28027]
  * [6 Links][28028]

## Porting
Mali-400 port was done by Luc libv Verhaegen. Purpose of this port is only testing the OpenGL ES libraries, no playable experience is available yet. 
## Building
Remove X11 Mali-400 libraries if you installed them, install framebuffer ones! (make framebuffer in mali-libs) Current ioquake3 uses only framebuffer output, nothing else. 
[code] 
    git clone https://github.com/libv/ioquake3
    cd ioquake3
    git checkout remotes/origin/mali_fb
    nano Makefile.local # change DEFAULT_BASEDIR to directory where you have Quake 3 Arena game files
    make ARCH=arm
    cd build/release-linux-arm
    
[/code]
## Running
Run 
[code] 
    ./ioquake3.arm
    
[/code]
in your build/release-linux-arm directory 
You should get something like this: 
[code] 
    root@linaro-alip:~/ioquake3-mali_fb/build/release-linux-arm# ./ioquake3.arm
    ioq3 1.36 linux-arm Dec  6 2012
    ----- FS_Startup -----
    Current search path:
    /root/.q3a/baseq3
    /home/linaro/ioquake3//baseq3/twpak0.pk3 (116 files)
    /home/linaro/ioquake3//baseq3/pak8.pk3 (9 files)
    /home/linaro/ioquake3//baseq3/pak7.pk3 (4 files)
    /home/linaro/ioquake3//baseq3/pak6.pk3 (64 files)
    /home/linaro/ioquake3//baseq3/pak5.pk3 (7 files)
    /home/linaro/ioquake3//baseq3/pak4.pk3 (272 files)
    /home/linaro/ioquake3//baseq3/pak3.pk3 (4 files)
    /home/linaro/ioquake3//baseq3/pak2.pk3 (148 files)
    /home/linaro/ioquake3//baseq3/pak1.pk3 (26 files)
    /home/linaro/ioquake3//baseq3/pak0.pk3 (3510 files)
    /home/linaro/ioquake3//baseq3
     
    ----------------------
    4160 files in pk3 files
    execing default.cfg
    execing q3config.cfg
    com_zoneMegs will be changed upon restarting.
    couldn't exec autoexec.cfg
    Hunk_Clear: reset the hunk ok
    ----- Client Initialization -----
    Couldn't read q3history.
    ----- Initializing Renderer ----
    -------------------------------
    QKEY found.
    ----- Client Initialization Complete -----
    ----- R_Init -----
    Initializing OpenGL subsystem
    FB dimensions 1920x1080
    Initializing OpenGL extensions
    ...GL_EXT_texture_compression_s3tc not found
    ...GL_S3_s3tc not found
    ...using GL_ARB_multitexture
    ...GL_EXT_compiled_vertex_array not found
    ...GL_EXT_texture_filter_anisotropic not found
    ------------------
     
    GL_VENDOR: ARM
    GL_RENDERER: Mali-400 MP
    GL_VERSION: OpenGL ES-CM 1.1
    GL_EXTENSIONS: 
     GL_OES_byte_coordinates GL_OES_fixed_point
     GL_OES_single_precision GL_OES_matrix_get
     GL_OES_read_format GL_OES_compressed_paletted_texture
     GL_OES_point_size_array GL_OES_point_sprite
     GL_OES_texture_npot GL_OES_query_matrix
     GL_OES_matrix_palette GL_OES_extended_matrix_palette
     GL_OES_compressed_ETC1_RGB8_texture GL_OES_EGL_image
     GL_OES_draw_texture GL_OES_depth_texture
     GL_OES_packed_depth_stencil GL_EXT_texture_format_BGRA8888
     GL_OES_framebuffer_object GL_OES_stencil8 
     GL_OES_depth24 GL_ARM_rgba8 
     GL_OES_EGL_image_external GL_OES_EGL_sync
     GL_EXT_multisampled_render_to_texture
     GL_OES_texture_cube_map GL_EXT_discard_framebuffer
    GL_MAX_TEXTURE_SIZE: 4096
    GL_MAX_TEXTURE_UNITS_ARB: 8
     
    PIXELFORMAT: color(0-bits) Z(0-bit) stencil(0-bits)
    MODE: 8, 1920 x 1080 fullscreen hz:N/A
    GAMMA: software w/ 0 overbright bits
    rendering primitives: single glDrawElements
    texturemode: GL_LINEAR_MIPMAP_LINEAR
    picmip: 0
    texture bits: 32
    multitexture: enabled
    compiled vertex arrays: enabled
    texenv add: enabled
    compressed textures: disabled
    HACK: using vertex lightmap approximation
    Initializing Shaders
    ----- finished R_Init -----
    ------ Initializing Sound ------
    SDL_Init( SDL_INIT_AUDIO )... OK
    SDL audio driver is "alsa".
    SDL_AudioSpec:
      Format:   AUDIO_S16LSB
      Freq:     22050
      Samples:  2048
      Channels: 2
    Starting SDL audio callback...
    SDL audio initialized.
    ----- Sound Info -----
        1 stereo
    65536 samples
       16 samplebits
        1 submission_chunk
    22050 speed
    0x4241a008 dma buffer
    No background file.
    ----------------------
    Sound initialization successful.
    --------------------------------
    Sound memory manager started
    Loading vm file vm/ui.qvm...
    Architecture doesn't have a bytecode compiler, using interpreter
    ui loaded in 2348480 bytes on the hunk
    38 arenas parsed
    32 bots parsed
    --- Common Initialization Complete ---
    IP: 127.0.0.1
    IP: 192.168.1.151
    IP6: ::1
    IP6: fe80::986e:5cff:fef9:cae0%eth0
    Opening IP6 socket: [::]:27960
    Opening IP socket: 0.0.0.0:27960
    
[/code]
Then enter this to run the demo benchmark: 
[code] 
    timedemo 1
    demo four
    
[/code]
ioquake3 is not wired with any input system (game will not recognize any keyboard or mouse input), this lines will go stright to Quake 3 console that will run under the renderer output. 
## Benchmark results
Resolution | Frame rate | Misc.   
---|---|---  
1920x1080 | 4.5 fps | 1260 frames 279.7 seconds 31.0/222.0/320.0/14.5 ms   
1280x720 | 39.4 fps | 1260 frames 32.0 seconds 10.0/25.4/80.0/8.2 ms   
## TODO
  * Add input system (evdev?)
  * Add X11 support

## Links
  * linux-sunxi.org: quake 3 arena timedemo - <http://www.youtube.com/watch?v=k4LbQGdwslA>

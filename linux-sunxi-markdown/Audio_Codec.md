# Audio Codec
## Contents
  * [1 Sound / Audio][8028]
    * [1.1 Configuring the analog output as default][8029]
    * [1.2 Testing the sound][8030]
    * [1.3 Troubleshooting][8031]
  * [2 Technical details][8032]

## Sound / Audio
The [A10][8033] supports two audio outputs and two audio inputs: 
  1. HDMI digital audio output (through HDMI port)
  2. Analog stereo (jack) audio output
  3. Analog Line-In (stereo) audio input
  4. Microphone audio input

### Configuring the analog output as default
By default, if you install a Linux image, the HDMI (digital) audio output is the first audio output device. Thus, if you try to play a sound file without specifying the output device, the sound will be send to the HDMI output. 
  * But in last Cubian,by default, the Analog stereo (jack) audio output is the first audio output device.

In order to configure the ALSA sound subsystem to use the analog (jack) audio output, add the following file /etc/asound.conf 
[code] 
    pcm.!default {
      type hw
      card 1
      device 0
    }
    ctl.!default {
      type hw
      card 1
    }
    
[/code]
### Testing the sound
You can test the sound output by running the command 
[code] 
    speaker-test -twav -c2
    
[/code]
You will hear a voice saying in turns _Left_ and _Right_ , and the sound for each word will come from each The default device will be selected. You can use the -D parameter to select the other sound output device. With **aplay -l** you can view the available audio output devices. 
### Troubleshooting
Mainline kernel (4.5-rc3)/[A20][8034]: if audio doesn't play remember to ENABLE both in alsamixer: "Power Amplifier DAC" and "Power Amplifier Mute". 
## Technical details
**PDF Documentation:** More information can be found in the document here: <https://mchehab.fedorapeople.org/kernel_docs_latex/sound.pdf>
**Works with:** A10 with mainline and sunxi kernels, {more details here}. 
**Playback:** (internal 24 bits Digital to Analog Converter) 
  * HPL Headphone Left channel output AO
  * HPR Headphone Right channel output AO
  * HPCOM Headphone amplifier output A
  * HPCOM_FB Headphone amplifier Feedback A

  
**Recorder:** (internal 24 bits Analog to Digital Converter) 
  * FMINL Audio ADC(24bit) Input for Left channel of FM radio AI
  * FMINR Audio ADC(24bit) Input for Right channel of FM radio AI
  * LINEINL Audio ADC(24bit) Input for Left channel of Line In AI
  * LINEINR Audio ADC(24bit) Input for Right channel of Line In AI
  * MICINL Audio ADC(24bit) Input for Left channel of Microphone AI
  * MICINR Audio ADC(24bit) Input for Right channel of Microphone AI

micin has an internal pre-amplifier. 
Only one 2-channel input port can be used at the same time. 
To select the intput port you have to set the mixer control called **ADC Input Mux**
**ADC Input Mux Value:** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7   
---|---|---|---|---|---|---|---|---  
**Input Port** | linein | fmin | mic1 | mic2 | mic1,mic2 | mic1+mic2 | output mixer | linein,mic1   
To change the ADC muxer you have to use the amixer tool from the "alsa-utils" package: 
**amixer -c <"card"> cset numid=<"control#"> <"input_port">**
  
where: 
<"card"> is the card, 0 for the sunxi-codec and 1 for the hdmi audio output 
<"input_port"> is the input port from the table 
<"control#"> is the control # showed using: aximer contents 
  
To install the alsa-utils from debian based distros: "apt-get install alsa-utils". Inside the package you have the aplay and arecord tools to test it. 
  

Command example to use the linein port: 
**amixer -c 0 cset numid=16 0**
  
Use **"amixer contents"** to get the contents and controls of your Alsa driver: 
[code] 
    numid=1,iface=MIXER,name='Master Playback Volume'
      ; type=INTEGER,access=rw------,values=1,min=0,max=63,step=0
      : values=51
    numid=10,iface=MIXER,name='LineL Switch'
      ; type=BOOLEAN,access=rw------,values=1
      : values=on
    numid=11,iface=MIXER,name='LineR Switch'
      ; type=BOOLEAN,access=rw------,values=1
      : values=on
    numid=5,iface=MIXER,name='Line Volume'
      ; type=BOOLEAN,access=rw------,values=1
      : values=on
    numid=15,iface=MIXER,name='Mic Input Mux'
      ; type=INTEGER,access=rw------,values=1,min=0,max=15,step=0
      : values=0
    numid=6,iface=MIXER,name='MicL Volume'
      ; type=INTEGER,access=rw------,values=1,min=0,max=3,step=0
      : values=1
    numid=7,iface=MIXER,name='MicR Volume'
      ; type=INTEGER,access=rw------,values=1,min=0,max=3,step=0
      : values=2
    numid=16,iface=MIXER,name='ADC Input Mux'
      ; type=INTEGER,access=rw------,values=1,min=0,max=7,step=0
      : values=0
    numid=3,iface=MIXER,name='Capture Volume'
      ; type=INTEGER,access=rw------,values=1,min=0,max=7,step=0
      : values=7
    numid=2,iface=MIXER,name='Playback Switch'
      ; type=BOOLEAN,access=rw------,values=1
      : values=off
    numid=4,iface=MIXER,name='Fm Volume'
      ; type=INTEGER,access=rw------,values=1,min=0,max=7,step=0
      : values=3
    numid=8,iface=MIXER,name='FmL Switch'
      ; type=BOOLEAN,access=rw------,values=1
      : values=off
    numid=9,iface=MIXER,name='FmR Switch'
      ; type=BOOLEAN,access=rw------,values=1
      : values=off
    numid=12,iface=MIXER,name='Ldac Left Mixer'
      ; type=BOOLEAN,access=rw------,values=1
      : values=off
    numid=14,iface=MIXER,name='Ldac Right Mixer'
      ; type=BOOLEAN,access=rw------,values=1
      : values=off
    numid=13,iface=MIXER,name='Rdac Right Mixer'
      ; type=BOOLEAN,access=rw------,values=1
      : values=off
    
[/code]

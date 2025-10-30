# Intenso TAB744/prep.sh
< [Intenso TAB744][27861]
 
[code] 
    # for *bootimg, *ramdisk tools see e.g. [xda-developers.com][27864]
    # clone [pctools/linux/mod_update][27865] ([alternative][27866]), [sunxi-tools][27867] for update* tools
    
[/code]
Usage: ./prep.sh [ pack | unpack ] [ fw.img | fw.img.dump ] 
[code] 
    #!/bin/bash
    #This file is PD.
    #Use it at your own risk.
    
    D="$(realpath "$0")"
    D="${D%/*}"
    IR="$D/TWRP/image.repacker/imgrepacker"
    
    function unpack() {
      $IR "$1"
      cd "$1.dump"
    
      mv -f home/imgrepacker/* .
      sed -i -e 's/home.imgrepacker.//' image.cfg
      sed -i -e 's/.home.imgrepacker.//' _*/*txt
    
      rm Vdiskfs.fex
      for f in image.cfg _img.files/Filelist.txt
      do sed -i -e '/Vdiskfs.fex/d' $f
      done
      
      f=sys_partition.fex  b=${f/.fex/.bin}
      sed -i -e '/diskfs.fex/,$ s/;\(verify *= *0\)/\1/' $f
      unix2dos $f 
      "$D"/mod_update/script $f  # fex2bin $f $b
      "$D"/mod_update/update_mbr $b 4
    
      "$D"/simg2img/simg2img system.fex system.bin
      mkdir -p s
      sudo mount -o loop system.bin s
    
      "$D"/mod_bootimg/umkbootimg boot.fex
      "$D"/mod_bootimg/unpack_ramdisk initramfs.cpio.gz
    }
    
    function pack() {
      IMG="$1"
      [[ -z "$IMG" || "${IMG%/}" == "." ]] && IMG="$PWD"
      IMG="${IMG%/}" IMG="${IMG##*/}" IMG="${IMG%.dump}"
    
      pushd .
      cd $IMG.dump &>/dev/null
    
      if [[ -f zImage ]]
      then
        [[ -d ramdisk/ ]] && "$D"/mod_bootimg/repack_ramdisk ramdisk/
        "$D"/mod_bootimg/mkbootimg --kernel zImage --ramdisk \
          new-ramdisk.cpio.gz --base 0x40000000 -o boot.fex \
        #&& rm -rf ramdisk/ zImage || exit 1
        rm -rf *ram*cpio.gz
      fi
    
      if [[ -f system.bin ]]
      then
        [[ -d s/ && -f s/build.prop ]] && sudo umount s
    
        rm -rf system.fex
        "$D"/make_ext4fs/ext2simg system.bin system.fex || \
        { echo "building sparse ext4 filesystem image failed.." >&2 ; exit 1 ; }
    
        sudo mount system.bin s
      fi
    
      "$D"/awtools/bins/FileAddSum boot.fex Vboot.fex
      "$D"/awtools/bins/FileAddSum system.fex Vsystem.fex
    
      "$D"/sunxi-tools/fex2bin     sys_config.fex   config.fex && \
      "$D"/mod_update/update_fes1  fes1.fex         config.fex && \
      "$D"/mod_update/update_boot0 boot0_nand.fex   config.fex NAND && \
      "$D"/mod_update/update_boot0 boot0_sdcard.fex config.fex SDMMC_CARD && \
      "$D"/mod_update/update_uboot u-boot.fex       config.fex || \
      { echo "updating with sys_config.fex / config.fex failed.." >&2 ; exit 1 ; }
    
      cd ..
      rm -f "$IMG"
      $IR $IMG.dump
      #rm -rvf $IMG.dump
    
      popd
    }
    
    function remove() {
      sudo umount $1/s
      rm -rvf ${1##/}
    }
    
    # Standard methods:
    [[ "$1" == "pack" || "$1" == "unpack" || "$1" == "remove" ]] && $1 "$2"
    
    # If first arg, or, if no arg is given, the current working directory
    # end with ".dump", packing is performed:
    [[ "${1##*.img.dump}" != "$1" \
    || "${1##*.img.dump/}" != "$1" \
    || -z "$1" && -z "${PWD##*.dump}" ]] && pack "$1"
    
    # If first arg ends in ".img", unpacking:
    [[ "${1##*.img}" != "$1" ]] && unpack "$1"
    
    # Usage hint is printed if no args are given and we're not inside an unpacked directory.
    [[ -z "$1" && -n "${PWD##*.dump}" ]] && echo "Usage: $0 [ pack [dir | ] | unpack [file] | remove [dir] ] (in *dump/ directory runs pack . without args)"
    
[/code]

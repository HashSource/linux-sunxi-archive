# Benchmarks
This page is not too useful as is, and needs to be fully split/removed/reworked to feature in the modern device->components centric wiki logic.
## Contents
  * [1 A10 Benchmarks][9833]
    * [1.1 CPU][9834]
      * [1.1.1 Linpack][9835]
        * [1.1.1.1 Build][9836]
        * [1.1.1.2 Results][9837]
      * [1.1.2 Whetstone/Dhrystone][9838]
        * [1.1.2.1 Building][9839]
        * [1.1.2.2 Results][9840]
      * [1.1.3 OpenSSL][9841]
        * [1.1.3.1 How to test][9842]
        * [1.1.3.2 Results][9843]
      * [1.1.4 SciMark][9844]
        * [1.1.4.1 Build][9845]
        * [1.1.4.2 Results][9846]
      * [1.1.5 nbench][9847]
        * [1.1.5.1 build][9848]
        * [1.1.5.2 results][9849]
      * [1.1.6 Linux kernel build][9850]
        * [1.1.6.1 setup][9851]
        * [1.1.6.2 tests][9852]
      * [1.1.7 OpenBenchmark Phoronix Test Suite][9853]
    * [1.2 GPU][9854]
      * [1.2.1 ioquake3][9855]
      * [1.2.2 es2_gears][9856]
      * [1.2.3 glx_gears][9857]
      * [1.2.4 glmark2-es2][9858]
    * [1.3 Video decoding][9859]
    * [1.4 IO][9860]
      * [1.4.1 SATA][9861]
      * [1.4.2 SD Card][9862]
      * [1.4.3 NAND][9863]
      * [1.4.4 Ethernet][9864]
    * [1.5 Power consumption][9865]
  * [2 A13 Benchmarks][9866]
    * [2.1 nbench][9867]
  * [3 A10S Benchmarks][9868]
  * [4 A20 Benchmarks][9869]
    * [4.1 CPU][9870]
      * [4.1.1 OpenSSL][9871]
      * [4.1.2 Linpack][9872]
      * [4.1.3 lmbench][9873]
    * [4.2 GPU][9874]

## A10 Benchmarks
### CPU
#### Linpack
Download this[[1]][9875], rename it to linpack.c 
##### Build
[code] 
    root@linaro-alip:~/benchmarks# cc -Ofast -o linpack linpack.c -lm -mcpu=cortex-a8 -march=armv7-a -mfpu=neon -mfloat-abi=hard -funsafe-math-optimizations -fno-fast-math
    linpack.c: In function ‘main’:
    linpack.c:78:14: warning: ignoring return value of ‘fgets’, declared with attribute warn_unused_result [-Wunused-result]
    
[/code]
##### Results
-mcpu=cortex-a8 -march=armv7-a -mfpu=neon -mfloat-abi=hard -funsafe-math-optimizations -fno-fast-math 
[code] 
    Memory required:  315K.
    
    
    LINPACK benchmark, Double precision.
    Machine precision:  15 digits.
    Array size 200 X 200.
    Average rolled and unrolled performance:
    
        Reps Time(s) DGEFA   DGESL  OVERHEAD    KFLOPS
    ----------------------------------------------------
          16   0.61  88.52%   6.56%   4.92%  37885.057
          32   1.21  85.12%   2.48%  12.40%  41459.119
          64   2.43  93.83%   2.47%   3.70%  37561.254
         128   4.86  91.77%   2.47%   5.76%  38381.368
         256   9.70  92.06%   2.89%   5.05%  38173.000
         512  19.41  91.29%   2.47%   6.23%  38634.432
    
[/code]
mcpu=cortex-a8 -mtune=cortex-a8 -march=armv7-a -mfpu=neon -mfloat-abi=hard -funsafe-math-optimizations -fomit-frame-pointer -ffast-math -funroll-loops -funsafe-loop-optimizations 
[code] 
    Memory required:  315K.
    
    
    LINPACK benchmark, Double precision.
    Machine precision:  15 digits.
    Array size 200 X 200.
    Average rolled and unrolled performance:
    
        Reps Time(s) DGEFA   DGESL  OVERHEAD    KFLOPS
    ----------------------------------------------------
          16   0.53  90.57%   1.89%   7.55%  44843.537
          32   1.05  90.48%   3.81%   5.71%  44390.572
          64   2.13  90.14%   2.35%   7.51%  44615.905
         128   4.23  90.54%   3.07%   6.38%  44390.572
         256   8.46  90.19%   2.84%   6.97%  44672.596
         512  17.03  90.55%   2.76%   6.69%  44250.892
    
[/code]
#### Whetstone/Dhrystone
<http://www.roylongbottom.org.uk/linux%20benchmarks.htm> (requires [File:Classic benchmarks.patch][9876]) 
##### Building
[code] 
    linaro@linaro-alip:~/tmp$ wget 'http://www.roylongbottom.org.uk/classic_benchmarks.tar.gz'
    linaro@linaro-alip:~/tmp$ wget 'http://linux-sunxi.org/images/a/a1/Classic_benchmarks.patch'
    linaro@linaro-alip:~/tmp$ tar -xzf classic_benchmarks.tar.gz 
    linaro@linaro-alip:~/tmp$ patch -p0 < Classic_benchmarks.patch 
    linaro@linaro-alip:~/tmp$ cd classic_benchmarks/source_code/
    linaro@linaro-alip:~/tmp/classic_benchmarks/source_code$ make
    
[/code]
##### Results
    ./whets (gcc-4.7 -static -O3 -mcpu=cortex-a8 -mtune=cortex-a8 -mfpu=neon -funroll-loops)
[code] 
              Single Precision C/C++ Whetstone Benchmark
    
    Loop content                   Result              MFLOPS      MOPS   Seconds
    
    N1 floating point      -1.12475013732910156       104.038               0.041
    N2 floating point      -1.12274742126464844       105.829               0.282
    N3 if then else         1.00000000000000000               14575.397     0.002
    N4 fixed point         12.00000000000000000                 418.942     0.167
    N5 sin,cos etc.         0.49911010265350342                   3.906     4.729
    N6 floating point       0.99999982118606567        98.848               1.211
    N7 assignments          3.00000000000000000                2254.666     0.018
    N8 exp,sqrt etc.        0.75110864639282227                   2.335     3.537
    
    MWIPS                                             222.285               9.987
    
[/code]
    ./dhry1 (gcc-4.7 -static -O3 -mcpu=cortex-a8 -mtune=cortex-a8 -mfpu=neon -funroll-loops)
[code] 
    Microseconds for one run through Dhrystone:         0.22 
    Dhrystones per Second:                         4518788 
    VAX  MIPS rating =                               2571.88 
    
[/code]
    ./dhry2 (gcc-4.7 -static -O3 -mcpu=cortex-a8 -mtune=cortex-a8 -mfpu=neon -funroll-loops)
[code] 
    Microseconds for one run through Dhrystone:         0.30 
    Dhrystones per Second:                         3336166 
    VAX  MIPS rating =                               1898.79 
    
[/code]
Adding -Ofast and -flto: 
    ./whets (gcc-4.7 -static -Ofast -mcpu=cortex-a8 -mtune=cortex-a8 -mfpu=neon -funroll-loops -flto)
[code] 
              Single Precision C/C++ Whetstone Benchmark
    
    Loop content                  Result              MFLOPS      MOPS   Seconds
    
    N1 floating point     -1.12367534637451172       103.565              0.004
    N2 floating point     -1.12167263031005859       105.531              0.028
    N3 if then else        1.00000000000000000               14852.924    0.000
    N4 fixed point        12.00000000000000000                6970.390    0.001
    N5 sin,cos etc.        0.49911010265350342                   3.933    0.465
    N6 floating point      0.99999982118606567        98.786              0.120
    N7 assignments         3.00000000000000000                2211.433    0.002
    N8 exp,sqrt etc.       0.75110864639282227                   2.698    0.303
    
    MWIPS                                            238.120              0.924
    
[/code]
    ./dhry1 (gcc-4.7 -static -Ofast -mcpu=cortex-a8 -mtune=cortex-a8 -mfpu=neon -funroll-loops -flto)
[code] 
    Microseconds for one run through Dhrystone:         0.19 
    Dhrystones per Second:                         5185531 
    VAX  MIPS rating =                               2951.36 
    
[/code]
    ./dhry2 (gcc-4.7 -static -Ofast -mcpu=cortex-a8 -mtune=cortex-a8 -mfpu=neon -funroll-loops)
[code] 
    Microseconds for one run through Dhrystone:         0.19 
    Dhrystones per Second:                         5262435 
    VAX  MIPS rating =                               2995.13 
    
[/code]
#### OpenSSL
##### How to test
run 
[code] 
    openssl speed
[/code]
##### Results
Linaro-alip soft-float 
[code] 
    OpenSSL 1.0.1 14 Mar 2012
    built on: Tue Aug 21 05:35:49 UTC 2012
    options:bn(64,32) rc4(ptr,char) des(idx,cisc,16,long) aes(partial) blowfish(ptr)
    compiler: cc -fPIC -DOPENSSL_PIC -DZLIB -DOPENSSL_THREADS -D_REENTRANT -DDSO_DLFCN -DHAVE_DLFCN_H -DL_ENDIAN -DTERMIO -g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Wformat-security -Werror=format-security -D_FORTIFY_SOURCE=2 -Wl,-Bsymbolic-functions -Wl,-z,relro -Wa,--noexecstack -Wall -DOPENSSL_NO_TLS1_2_CLIENT -DOPENSSL_MAX_TLS1_2_CIPHER_LENGTH=50
    The 'numbers' are in 1000s of bytes per second processed.
    type             16 bytes     64 bytes    256 bytes   1024 bytes   8192 bytes
    md2                  0.00         0.00         0.00         0.00         0.00
    mdc2                 0.00         0.00         0.00         0.00         0.00
    md4               4539.13k    23584.98k    68988.33k   133520.04k   184363.69k
    md5               5140.49k    17237.58k    46162.43k    79220.05k   100848.98k
    hmac(md5)         6296.96k    20580.39k    51788.37k    83395.93k   101282.91k
    sha1              5056.81k    15672.85k    36537.09k    54699.01k    64102.40k
    rmd160            4733.01k    14162.58k    31460.95k    45231.10k    51950.93k
    rc4              67049.00k    74935.98k    78372.86k    79348.39k    79623.51k
    des cbc          17689.04k    18793.72k    19138.82k    19248.13k    19292.16k
    des ede3          6748.10k     6951.38k     6998.10k     7015.77k     6950.87k
    idea cbc             0.00         0.00         0.00         0.00         0.00
    seed cbc         20640.20k    21906.09k    22347.52k    22450.52k    22500.69k
    rc2 cbc          13089.00k    13998.74k    14224.73k    14294.36k    14164.76k
    rc5-32/12 cbc        0.00         0.00         0.00         0.00         0.00
    blowfish cbc     26759.62k    29755.75k    30726.06k    30958.59k    31053.14k
    cast cbc         25870.12k    28393.51k    29254.23k    29501.78k    29570.39k
    aes-128 cbc      19582.69k    20855.45k    21258.07k    21348.35k    21392.04k
    aes-192 cbc      16902.33k    17731.03k    18009.26k    18094.42k    18117.97k
    aes-256 cbc      14778.66k    15419.55k    15636.82k    15683.58k    15712.26k
    camellia-128 cbc    26162.67k    28201.17k    28923.31k    29136.90k    28918.58k
    camellia-192 cbc    20555.46k    22316.52k    22863.19k    22990.17k    23046.83k
    camellia-256 cbc    20704.67k    22316.39k    22846.72k    23003.48k    23044.10k
    sha256            4130.87k     9683.05k    17185.11k    21408.43k    23093.25k
    sha512             804.45k     3218.84k     4525.99k     6147.07k     6873.09k
    whirlpool         1201.69k     2457.88k     3979.18k     4716.20k     4917.93k
    aes-128 ige      18517.42k    19858.50k    20280.58k    20406.61k    20838.75k
    aes-192 ige      15950.20k    17003.69k    17323.18k    17393.32k    17408.00k
    aes-256 ige      14102.48k    14868.65k    15100.93k    15172.95k    15174.31k
    ghash            14806.49k    15383.55k    15564.03k    15625.22k    15652.18k
                      sign    verify    sign/s verify/s
    rsa  512 bits 0.002293s 0.000203s    436.1   4920.6
    rsa 1024 bits 0.012441s 0.000617s     80.4   1621.2
    rsa 2048 bits 0.075263s 0.002055s     13.3    486.7
    rsa 4096 bits 0.499048s 0.007148s      2.0    139.9
                      sign    verify    sign/s verify/s
    dsa  512 bits 0.002058s 0.002299s    485.9    435.0
    dsa 1024 bits 0.006101s 0.006964s    163.9    143.6
    dsa 2048 bits 0.020326s 0.023641s     49.2     42.3
                                  sign    verify    sign/s verify/s
     160 bit ecdsa (secp160r1)   0.0010s   0.0045s    977.2    222.1
     192 bit ecdsa (nistp192)   0.0011s   0.0046s    950.8    218.4
     224 bit ecdsa (nistp224)   0.0014s   0.0062s    739.1    160.2
     256 bit ecdsa (nistp256)   0.0016s   0.0079s    613.0    126.5
     384 bit ecdsa (nistp384)   0.0036s   0.0184s    281.4     54.3
     521 bit ecdsa (nistp521)   0.0096s   0.0510s    103.9     19.6
     163 bit ecdsa (nistk163)   0.0021s   0.0080s    473.6    125.3
     233 bit ecdsa (nistk233)   0.0044s   0.0155s    228.5     64.3
     283 bit ecdsa (nistk283)   0.0067s   0.0286s    150.2     35.0
     409 bit ecdsa (nistk409)   0.0178s   0.0667s     56.3     15.0
     571 bit ecdsa (nistk571)   0.0426s   0.1538s     23.5      6.5
     163 bit ecdsa (nistb163)   0.0021s   0.0086s    472.9    116.0
     233 bit ecdsa (nistb233)   0.0043s   0.0173s    230.3     57.9
     283 bit ecdsa (nistb283)   0.0067s   0.0320s    149.7     31.2
     409 bit ecdsa (nistb409)   0.0178s   0.0759s     56.1     13.2
     571 bit ecdsa (nistb571)   0.0428s   0.1760s     23.3      5.7
                                  op      op/s
     160 bit ecdh (secp160r1)   0.0038s    264.8
     192 bit ecdh (nistp192)   0.0038s    263.9
     224 bit ecdh (nistp224)   0.0052s    191.9
     256 bit ecdh (nistp256)   0.0066s    151.4
     384 bit ecdh (nistp384)   0.0152s     66.0
     521 bit ecdh (nistp521)   0.0422s     23.7
     163 bit ecdh (nistk163)   0.0040s    253.0
     233 bit ecdh (nistk233)   0.0077s    130.0
     283 bit ecdh (nistk283)   0.0142s     70.6
     409 bit ecdh (nistk409)   0.0331s     30.2
     571 bit ecdh (nistk571)   0.0760s     13.2
     163 bit ecdh (nistb163)   0.0042s    235.8
     233 bit ecdh (nistb233)   0.0085s    117.0
     283 bit ecdh (nistb283)   0.0158s     63.1
     409 bit ecdh (nistb409)   0.0378s     26.5
     571 bit ecdh (nistb571)   0.0879s     11.4
    
[/code]
ArchLinux-ARM hard-float 
[code] 
    OpenSSL 1.0.1c 10 May 2012
    built on: Sat May 12 16:58:09 UTC 2012
    options:bn(64,32) md2(int) rc4(ptr,char) des(idx,cisc,16,long) aes(partial) idea(int) blowfish(ptr)
    compiler: gcc -fPIC -DOPENSSL_PIC -DZLIB -DOPENSSL_THREADS -D_REENTRANT -DDSO_DLFCN -DHAVE_DLFCN_H -Wa,--noexecstack -march=armv7-a -mfloat-abi=hard -mfpu=vfpv3-d16 -O2 -pipe -fstack-protector --param=ssp-buffer-size=4 -D_FORTIFY_SOURCE=2 -DOPENSSL_NO_TLS1_2_CLIENT -DTERMIO -O3 -Wall -DOPENSSL_BN_ASM_MONT
    -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DAES_ASM -DGHASH_ASM
    The 'numbers' are in 1000s of bytes per second processed.
    type             16 bytes     64 bytes    256 bytes   1024 bytes   8192 bytes
    md2               1010.38k     2071.59k     2919.79k     3215.08k     3322.59k
    mdc2              2238.70k     2724.06k     2915.34k     3063.91k     3044.11k
    md4               8261.57k    28911.65k    81103.94k   148492.57k   200026.24k
    md5               6456.03k    20979.84k    54995.08k    89176.35k   111244.43k
    hmac(md5)         6319.94k    21289.87k    54631.79k    89444.75k   110983.92k
    sha1              6633.24k    20150.08k    47302.98k    70280.66k    82581.21k
    rmd160            5493.36k    15627.12k    34127.48k    48159.05k    54297.05k
    rc4              66233.79k    74331.73k    77396.54k    77693.81k    78829.52k
    des cbc          18532.54k    19769.99k    20273.26k    20313.14k    20323.82k
    des ede3          7169.37k     7346.22k     7416.20k     7478.53k     7461.20k
    idea cbc         15485.30k    16443.47k    16683.46k    16698.54k    16758.24k
    seed cbc         20667.10k    22857.28k    23349.77k    23677.72k    23609.99k
    rc2 cbc          13686.09k    14637.63k    14956.66k    15077.94k    14912.37k
    rc5-32/12 cbc        0.00         0.00         0.00         0.00         0.00
    blowfish cbc     27451.80k    30338.11k    31082.36k    31144.23k    31523.17k
    cast cbc         27317.50k    30075.42k    31215.36k    31145.33k    31403.65k
    aes-128 cbc      35895.60k    40605.48k    43274.31k    43880.05k    44219.12k
    aes-192 cbc      30897.64k    35908.66k    37676.55k    38116.09k    38425.23k
    aes-256 cbc      27594.10k    31650.74k    33180.37k    33427.34k    33498.80k
    camellia-128 cbc    26308.13k    29661.26k    31114.20k    31346.19k    31582.08k
    camellia-192 cbc    21422.53k    23395.33k    24418.24k    24554.27k    24599.57k
    camellia-256 cbc    21457.81k    23333.78k    24369.82k    24582.58k    24617.25k
    sha256           10078.10k    24314.98k    43970.03k    55573.89k    59677.84k
    sha512            4133.94k    16576.53k    25365.00k    35504.81k    40002.80k
    whirlpool         1216.98k     2492.34k     4065.11k     4781.12k     5059.59k
    aes-128 ige      31316.97k    38357.40k    41833.06k    43101.16k    43264.37k
    aes-192 ige      27502.07k    34078.09k    36575.95k    37367.50k    37251.58k
    aes-256 ige      24869.69k    30543.02k    32333.16k    32777.21k    33054.87k
    ghash            52904.92k    62310.47k    66025.17k    66775.11k    66985.81k
                      sign    verify    sign/s verify/s
    rsa  512 bits 0.001042s 0.000104s    960.0   9587.7
    rsa 1024 bits 0.005983s 0.000327s    167.2   3060.2
    rsa 2048 bits 0.038947s 0.001188s     25.7    841.7
    rsa 4096 bits 0.280000s 0.004561s      3.6    219.2
                      sign    verify    sign/s verify/s
    dsa  512 bits 0.001062s 0.001161s    942.0    861.4
    dsa 1024 bits 0.003206s 0.003716s    311.9    269.1
    dsa 2048 bits 0.011507s 0.013283s     86.9     75.3
                                  sign    verify    sign/s verify/s
     160 bit ecdsa (secp160r1)   0.0006s   0.0023s   1620.6    438.5
     192 bit ecdsa (nistp192)   0.0008s   0.0033s   1259.9    304.1
     224 bit ecdsa (nistp224)   0.0010s   0.0043s    991.3    232.9
     256 bit ecdsa (nistp256)   0.0013s   0.0058s    790.4    173.8
     384 bit ecdsa (nistp384)   0.0030s   0.0151s    338.2     66.2
     521 bit ecdsa (nistp521)   0.0062s   0.0346s    161.1     28.9
     163 bit ecdsa (nistk163)   0.0019s   0.0064s    536.1    157.0
     233 bit ecdsa (nistk233)   0.0039s   0.0116s    257.6     85.9
     283 bit ecdsa (nistk283)   0.0059s   0.0214s    169.2     46.8
     409 bit ecdsa (nistk409)   0.0161s   0.0469s     62.0     21.3
     571 bit ecdsa (nistk571)   0.0385s   0.1089s     25.9      9.2
     163 bit ecdsa (nistb163)   0.0018s   0.0069s    544.3    145.1
     233 bit ecdsa (nistb233)   0.0038s   0.0128s    259.9     78.3
     283 bit ecdsa (nistb283)   0.0059s   0.0238s    169.3     42.0
     409 bit ecdsa (nistb409)   0.0161s   0.0533s     62.1     18.8
     571 bit ecdsa (nistb571)   0.0385s   0.1241s     25.9      8.1
                                  op      op/s
     160 bit ecdh (secp160r1)   0.0019s    515.5
     192 bit ecdh (nistp192)   0.0027s    374.3
     224 bit ecdh (nistp224)   0.0036s    278.7
     256 bit ecdh (nistp256)   0.0049s    203.8
     384 bit ecdh (nistp384)   0.0126s     79.2
     521 bit ecdh (nistp521)   0.0288s     34.7
     163 bit ecdh (nistk163)   0.0031s    319.4
     233 bit ecdh (nistk233)   0.0057s    176.9
     283 bit ecdh (nistk283)   0.0105s     94.9
     409 bit ecdh (nistk409)   0.0231s     43.2
     571 bit ecdh (nistk571)   0.0538s     18.6
     163 bit ecdh (nistb163)   0.0033s    300.7
     233 bit ecdh (nistb233)   0.0063s    158.9
     283 bit ecdh (nistb283)   0.0118s     85.1
     409 bit ecdh (nistb409)   0.0263s     38.1
     571 bit ecdh (nistb571)   0.0615s     16.3
    
[/code]
#### SciMark
##### Build
[code] 
    wget http://math.nist.gov/scimark2/scimark2_1c.zip
    unzip -o scimark2_1c.zip -d scimark2_files
    cd scimark2_files/
    g++ -o scimark2 -O *.c -mcpu=cortex-a8 -mtune=cortex-a8 -march=armv7-a -mfpu=neon -mfloat-abi=hard -funsafe-math-optimizations -fomit-frame-pointer -ffast-math -funroll-loops -funsafe-loop-optimizations -fno-tree-vectorize
    ./scimark2 -large
    
[/code]
##### Results
[code] 
    **                                                              **
    ** SciMark2 Numeric Benchmark, see http://math.nist.gov/scimark **
    ** for details. (Results can be submitted to [[email protected]][9877])     **
    **                                                              **
    Using       2.00 seconds min time per kenel.
    Composite Score:           29.32
    FFT             Mflops:    13.57    (N=1048576)
    SOR             Mflops:    48.51    (1000 x 1000)
    MonteCarlo:     Mflops:    23.30
    Sparse matmult  Mflops:    34.22    (N=100000, nz=1000000)
    LU              Mflops:    26.97    (M=1000, N=1000)
    
[/code]
#### nbench
<http://www.tux.org/~mayer/linux/bmark.html>
##### build
[code] 
    linaro@linaro-alip:~/tmp$ wget http://www.tux.org/~mayer/linux/nbench-byte-2.2.3.tar.gz
    [...]
    linaro@linaro-alip:~/tmp$ tar -xzf nbench-byte-2.2.3.tar.gz 
    linaro@linaro-alip:~/tmp$ cd nbench-byte-2.2.3
    linaro@linaro-alip:~/tmp/nbench-byte-2.2.3$ vi Makefile 
    linaro@linaro-alip:~/tmp/nbench-byte-2.2.3$ make
    [...]
    linaro@linaro-alip:~/tmp/nbench-byte-2.2.3$ ./nbench 
    
[/code]
##### results
    CC=gcc-4.7
    CFLAGS=-s -static -Wall -O3 -mfpu=neon -mcpu=cortex-a8 -mtune=cortex-a8 -fomit-frame-pointer -marm -funroll-loops
[code] 
    BYTEmark* Native Mode Benchmark ver. 2 (10/95)
    Index-split by Andrew D. Balsa (11/97)
    Linux/Unix* port by Uwe F. Mayer (12/96,11/97)
    
    TEST                : Iterations/sec.  : Old Index   : New Index
                        :                  : Pentium 90* : AMD K6/233*
    --------------------:------------------:-------------:------------
    NUMERIC SORT        :          583.28  :      14.96  :       4.91
    STRING SORT         :          58.353  :      26.07  :       4.04
    BITFIELD            :      2.6754e+08  :      45.89  :       9.59
    FP EMULATION        :          108.48  :      52.05  :      12.01
    FOURIER             :          1866.1  :       2.12  :       1.19
    ASSIGNMENT          :          9.0228  :      34.33  :       8.91
    IDEA                :          1226.3  :      18.76  :       5.57
    HUFFMAN             :          744.22  :      20.64  :       6.59
    NEURAL NET          :            1.96  :       3.15  :       1.32
    LU DECOMPOSITION    :          87.325  :       4.52  :       3.27
    ==========================ORIGINAL BYTEMARK RESULTS==========================
    INTEGER INDEX       : 27.658
    FLOATING-POINT INDEX: 3.115
    Baseline (MSDOS*)   : Pentium* 90, 256 KB L2-cache, Watcom* compiler 10.0
    ==============================LINUX DATA BELOW===============================
    CPU                 : 
    L2 Cache            : 
    OS                  : Linux 3.4.19-a10-aufs+
    C compiler          : gcc-4.7
    libc                : libc-2.15.so
    MEMORY INDEX        : 7.010
    INTEGER INDEX       : 6.822
    FLOATING-POINT INDEX: 1.728
    Baseline (LINUX)    : AMD K6/233*, 512 KB L2-cache, gcc 2.7.2.3, libc-5.4.38
    * Trademarks are property of their respective holder.
    
[/code]
    CC=gcc-4.7
    CFLAGS=-s -static -Wall -Ofast -mfpu=neon -mcpu=cortex-a8 -mtune=cortex-a8 -fomit-frame-pointer -marm -funroll-loops
[code] 
    BYTEmark* Native Mode Benchmark ver. 2 (10/95)
    Index-split by Andrew D. Balsa (11/97)
    Linux/Unix* port by Uwe F. Mayer (12/96,11/97)
    
    TEST                : Iterations/sec.  : Old Index   : New Index
                        :                  : Pentium 90* : AMD K6/233*
    --------------------:------------------:-------------:------------
    NUMERIC SORT        :          586.72  :      15.05  :       4.94
    STRING SORT         :          58.217  :      26.01  :       4.03
    BITFIELD            :      2.6871e+08  :      46.09  :       9.63
    FP EMULATION        :           108.2  :      51.92  :      11.98
    FOURIER             :          1895.2  :       2.16  :       1.21
    ASSIGNMENT          :          9.0192  :      34.32  :       8.90
    IDEA                :          1226.8  :      18.76  :       5.57
    HUFFMAN             :          804.24  :      22.30  :       7.12
    NEURAL NET          :          2.0692  :       3.32  :       1.40
    LU DECOMPOSITION    :          87.325  :       4.52  :       3.27
    ==========================ORIGINAL BYTEMARK RESULTS==========================
    INTEGER INDEX       : 27.988
    FLOATING-POINT INDEX: 3.188
    Baseline (MSDOS*)   : Pentium* 90, 256 KB L2-cache, Watcom* compiler 10.0
    ==============================LINUX DATA BELOW===============================
    CPU                 : 
    L2 Cache            : 
    OS                  : Linux 3.4.19-a10-aufs+
    C compiler          : gcc-4.7
    libc                : libc-2.15.so
    MEMORY INDEX        : 7.014
    INTEGER INDEX       : 6.962
    FLOATING-POINT INDEX: 1.768
    Baseline (LINUX)    : AMD K6/233*, 512 KB L2-cache, gcc 2.7.2.3, libc-5.4.38
    * Trademarks are property of their respective holder.
    
[/code]
#### Linux kernel build
##### setup
[code] 
    root@debian:~$ wget '[http://www.kernel.org/pub/linux/kernel/v3.0/linux-3.1.tar.bz2'][9878]
    root@debian:~$ md5sum linux-3.1.tar.bz2
    8d43453f8159b2332ad410b19d86a931  linux-3.1.tar.bz2
    root@debian:~$ tar -xjf linux-3.1.tar.bz2
    root@debian:~$ cd linux-3.1
    root@debian:~/linux-3.1$ gcc --version
    gcc (Debian 4.7.2-5) 4.7.2
    Copyright (C) 2012 Free Software Foundation, Inc.
    This is free software; see the source for copying conditions.  There is NO
    warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    
[/code]
##### tests
[code] 
    root@debian:~/linux-3.1$ time make -s vexpress_defconfig bzImage 
    [...] 
    real    45m26.121s 
    user    43m6.080s 
    sys     2m8.370s
    
[/code]
[code] 
    root@debian:~$ time md5sum linux-3.1.tar.bz2  
    8d43453f8159b2332ad410b19d86a931  linux-3.1.tar.bz2 
    real    0m0.797s
    user    0m0.610s
    sys     0m0.180s
    
[/code]
[code] 
    root@debian:~$ time bzip2 -t linux-3.1.tar.bz2  
    real    1m47.884s
    user    1m47.250s
    sys     0m0.290s
    
[/code]
#### OpenBenchmark Phoronix Test Suite
Comparisons with Debian and Raspian on r-Pi vs. Cubieboard 1 and 2 <http://openbenchmarking.org/result/1308083-UT-1302242BY19> <http://openbenchmarking.org/result/1308084-UT-1301189RA85>
### GPU
Results for X11 libraries and framebuffer libraries may differ. 
#### ioquake3
See [ioquake3][9879]
#### es2_gears
X11 libraries: 
  * 131FPS

  * r3p0: 195-200 FPS
  * r3p0: 58-75 FPS - fullscreen (1024x768)

Framebuffer libraries: ? 
#### glx_gears
X11 libraries + mesa: 
  * 117 FPS
  * ~25 FPS - fullscreen (1024x768)

#### glmark2-es2
X11 libraries: 
[code] 
    =======================================================
        glmark2 2012.08
    =======================================================
        OpenGL Information
        GL_VENDOR:     ARM
        GL_RENDERER:   Mali-400 MP
        GL_VERSION:    OpenGL ES 2.0
    =======================================================
    [build] use-vbo=false: FPS: 48 FrameTime: 20.833 ms
    [build] use-vbo=true: FPS: 55 FrameTime: 18.182 ms
    [texture] texture-filter=nearest: FPS: 56 FrameTime: 17.857 ms
    [texture] texture-filter=linear: FPS: 56 FrameTime: 17.857 ms
    [texture] texture-filter=mipmap: FPS: 57 FrameTime: 17.544 ms
    [shading] shading=gouraud: FPS: 50 FrameTime: 20.000 ms
    [shading] shading=blinn-phong-inf: FPS: 50 FrameTime: 20.000 ms
    [shading] shading=phong: FPS: 47 FrameTime: 21.277 ms
    [bump] bump-render=high-poly: FPS: 37 FrameTime: 27.027 ms
    [bump] bump-render=normals: FPS: 58 FrameTime: 17.241 ms
    [bump] bump-render=height: FPS: 57 FrameTime: 17.544 ms
    [effect2d] kernel=0,1,0;1,-4,1;0,1,0;: FPS: 30 FrameTime: 33.333 ms
    [effect2d] kernel=1,1,1,1,1;1,1,1,1,1;1,1,1,1,1;: FPS: 19 FrameTime: 52.632 ms
    [pulsar] light=false:quads=5:texture=false: FPS: 59 FrameTime: 16.949 ms
    [desktop] blur-radius=5:effect=blur:passes=1:separable=true:windows=4: FPS: 16 FrameTime: 62.500 ms
    [desktop] effect=shadow:windows=4: FPS: 43 FrameTime: 23.256 ms
    Error: Requested MapBuffer VBO update method but GL_OES_mapbuffer is not supported!
    [buffer] columns=200:interleave=false:update-dispersion=0.9:update-fraction=0.5:update-method=map: Unsupported
    [buffer] columns=200:interleave=false:update-dispersion=0.9:update-fraction=0.5:update-method=subdata: FPS: 18 FrameTime: 55.556 ms
    Error: Requested MapBuffer VBO update method but GL_OES_mapbuffer is not supported!
    [buffer] columns=200:interleave=true:update-dispersion=0.9:update-fraction=0.5:update-method=map: Unsupported
    [ideas] speed=duration: FPS: 48 FrameTime: 20.833 ms
    [jellyfish] <default>: FPS: 43 FrameTime: 23.256 ms
    Error: SceneTerrain requires Vertex Texture Fetch support, but GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS is 0
    [terrain] <default>: Unsupported
    [conditionals] fragment-steps=0:vertex-steps=0: FPS: 59 FrameTime: 16.949 ms
    [conditionals] fragment-steps=5:vertex-steps=0: FPS: 54 FrameTime: 18.519 ms
    [conditionals] fragment-steps=0:vertex-steps=5: FPS: 58 FrameTime: 17.241 ms
    [function] fragment-complexity=low:fragment-steps=5: FPS: 57 FrameTime: 17.544 ms
    [function] fragment-complexity=medium:fragment-steps=5: FPS: 43 FrameTime: 23.256 ms
    [loop] fragment-loop=false:fragment-steps=5:vertex-steps=5: FPS: 56 FrameTime: 17.857 ms
    [loop] fragment-steps=5:fragment-uniform=false:vertex-steps=5: FPS: 57 FrameTime: 17.544 ms
    [loop] fragment-steps=5:fragment-uniform=true:vertex-steps=5: FPS: 56 FrameTime: 17.857 ms
    =======================================================
                                      glmark2 Score: 47 
    =======================================================
    
[/code]
### Video decoding
See [CedarXVideoRenderingChart][9880]
### IO
#### SATA
[code] 
    root@debian:~% sudo dd if=/dev/sda of=/dev/null bs=32M count=100 iflag=direct
    100+0 records in
    100+0 records out
    3355443200 bytes (3.4 GB) copied, 15.3565 s, 219 MB/s
    
[/code]
This may be limited by the comparatively old, cheap SSD being used. 
#### SD Card
#### NAND
#### [Ethernet][9881]
### Power consumption
## A13 Benchmarks
A13 needs own CPU benchmarks because DDR3 bus is crippled. 
### nbench
Tested on A13-olinuxino, debian wheezy. 
CC=gcc-4.7 CFLAGS= -s -static -O3 -mfpu=neon -mcpu=cortex-a8 -mtune=cortex-a8 -fomit-frame-pointer -marm -munroll-loops 
[code] 
    BYTEmark* Native Mode Benchmark ver. 2 (10/95)
    Index-split by Andrew D. Balsa (11/97)
    Linux/Unix* port by Uwe F. Mayer (12/96,11/97)
    
    TEST                : Iterations/sec.  : Old Index   : New Index
                        :                  : Pentium 90* : AMD K6/233*
    --------------------:------------------:-------------:------------
    NUMERIC SORT        :           578.4  :      14.83  :       4.87
    STRING SORT         :          53.536  :      23.92  :       3.70
    BITFIELD            :      2.5697e+08  :      44.08  :       9.21
    FP EMULATION        :          105.84  :      50.79  :      11.72
    FOURIER             :          1754.5  :       2.00  :       1.12
    ASSIGNMENT          :          8.8536  :      33.69  :       8.74
    IDEA                :          1206.5  :      18.45  :       5.48
    HUFFMAN             :          719.14  :      19.94  :       6.37
    NEURAL NET          :          1.9275  :       3.10  :       1.30
    LU DECOMPOSITION    :          85.326  :       4.42  :       3.19
    ==========================ORIGINAL BYTEMARK RESULTS==========================
    INTEGER INDEX       : 26.768
    FLOATING-POINT INDEX: 3.011
    Baseline (MSDOS*)   : Pentium* 90, 256 KB L2-cache, Watcom* compiler 10.0
    ==============================LINUX DATA BELOW===============================
    CPU                 : 
    L2 Cache            : 
    OS                  : Linux 3.4.61stage+
    C compiler          : gcc-4.7
    libc                : libc-2.13.so
    MEMORY INDEX        : 6.679
    INTEGER INDEX       : 6.681
    FLOATING-POINT INDEX: 1.670
    Baseline (LINUX)    : AMD K6/233*, 512 KB L2-cache, gcc 2.7.2.3, libc-5.4.38
    * Trademarks are property of their respective holder.
    
    
[/code]
## A10S Benchmarks
Should be the same as A13. 
## A20 Benchmarks
### CPU
#### OpenSSL
[code] 
    OpenSSL 1.0.1c 10 May 2012
    built on: Sun May 26 10:09:49 UTC 2013
    options:bn(64,32) rc4(ptr,char) des(idx,cisc,16,long) aes(partial) blowfish(ptr)
    compiler: cc -fPIC -DOPENSSL_PIC -DZLIB -DOPENSSL_THREADS -D_REENTRANT -DDSO_DLFCN -DHAVE_DLFCN_H -DL_ENDIAN -DTERMIO -g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -D_FORTIFY_SOURCE=2 -Wl,-Bsymbolic-functions -Wl,-z,relro -Wa,--noexecstack -Wall -DOPENSSL_NO_TLS1_2_CLIENT -DOPENSSL_MAX_TLS1_2_CIPHER_LENGTH=50 -DOPENSSL_BN_ASM_MONT -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DAES_ASM -DBSAES_ASM -DGHASH_ASM
    The 'numbers' are in 1000s of bytes per second processed.
    type             16 bytes     64 bytes    256 bytes   1024 bytes   8192 bytes
    md2                  0.00         0.00         0.00         0.00         0.00
    mdc2                 0.00         0.00         0.00         0.00         0.00
    md4               2536.46k    20273.86k    52285.78k    85916.01k   106042.42k
    md5               4658.85k    15543.72k    40538.41k    67159.72k    83646.07k
    hmac(md5)         4977.63k    16353.73k    41931.60k    69000.08k    84975.62k
    sha1              4701.95k    13683.01k    28788.78k    40693.55k    46074.54k
    rmd160            3908.94k    10874.84k    22251.01k    30578.56k    34138.79k
    rc4              48278.43k    54375.70k    56301.51k    57160.09k    53712.21k
    des cbc          11529.27k    12242.68k    12399.79k    12450.82k    12465.49k
    des ede3          4163.83k     4113.26k     4434.71k     4462.30k     3923.97k
    idea cbc             0.00         0.00         0.00         0.00         0.00
    seed cbc         15233.77k    16166.74k    16474.46k    16540.33k    16561.49k
    rc2 cbc           8235.71k     8122.28k     9262.39k     9267.03k     9287.92k
    rc5-32/12 cbc        0.00         0.00         0.00         0.00         0.00
    blowfish cbc     18124.43k    19772.31k    20277.09k    20431.03k    20400.81k
    cast cbc         17256.97k    17877.53k    20460.48k    20543.36k    20561.92k
    aes-128 cbc      20783.69k    22336.55k    23158.58k    23271.08k    23328.09k
    aes-192 cbc      16915.78k    17387.43k    19564.65k    19736.49k    16523.73k
    aes-256 cbc      16038.03k    17123.52k    15135.01k    16914.49k    17337.45k
    camellia-128 cbc    17164.96k    18374.83k    18757.21k    18865.92k    18882.56k
    camellia-192 cbc    13680.37k    14486.59k    14760.33k    14803.97k    14824.79k
    camellia-256 cbc    13662.32k    14485.67k    14743.13k    14816.15k    14827.52k
    sha256            5340.42k    12254.95k    21022.63k    25548.63k    27282.68k
    sha512            2550.36k    10262.62k    15025.92k    20669.44k    23343.09k
    whirlpool         1401.77k     2917.73k     4762.11k     5679.58k     5982.89k
    aes-128 ige      18517.31k    18765.50k    21879.30k    22013.26k    22099.22k
    aes-192 ige      17356.40k    18653.29k    19075.34k    19152.21k    19177.47k
    aes-256 ige      15542.49k    16533.78k    16846.17k    16933.33k    17005.93k
    ghash            24851.30k    27019.22k    28001.93k    28195.84k    28265.13k
                      sign    verify    sign/s verify/s
    rsa  512 bits 0.001276s 0.000122s    783.7   8212.9
    rsa 1024 bits 0.006676s 0.000382s    149.8   2617.3
    rsa 2048 bits 0.045991s 0.001380s     21.7    724.6
    rsa 4096 bits 0.334000s 0.005418s      3.0    184.6
                      sign    verify    sign/s verify/s
    dsa  512 bits 0.001230s 0.001300s    813.1    769.2
    dsa 1024 bits 0.003737s 0.004349s    267.6    229.9
    dsa 2048 bits 0.013634s 0.015876s     73.3     63.0
                                  sign    verify    sign/s verify/s
     160 bit ecdsa (secp160r1)   0.0008s   0.0031s   1319.3    322.7
     192 bit ecdsa (nistp192)   0.0010s   0.0042s   1010.7    236.5
     224 bit ecdsa (nistp224)   0.0013s   0.0056s    797.9    179.9
     256 bit ecdsa (nistp256)   0.0016s   0.0074s    637.6    135.0
     384 bit ecdsa (nistp384)   0.0035s   0.0178s    287.7     56.1
     521 bit ecdsa (nistp521)   0.0073s   0.0393s    136.1     25.4
     163 bit ecdsa (nistk163)   0.0025s   0.0094s    402.0    106.5
     233 bit ecdsa (nistk233)   0.0055s   0.0163s    183.2     61.3
     283 bit ecdsa (nistk283)   0.0085s   0.0316s    117.3     31.7
     409 bit ecdsa (nistk409)   0.0209s   0.0644s     47.7     15.5
     571 bit ecdsa (nistk571)   0.0539s   0.1527s     18.6      6.5
     163 bit ecdsa (nistb163)   0.0026s   0.0096s    378.9    103.9
     233 bit ecdsa (nistb233)   0.0056s   0.0192s    178.7     52.2
     283 bit ecdsa (nistb283)   0.0088s   0.0336s    113.9     29.7
     409 bit ecdsa (nistb409)   0.0223s   0.0772s     44.7     13.0
     571 bit ecdsa (nistb571)   0.0538s   0.1719s     18.6      5.8
                                  op      op/s
     160 bit ecdh (secp160r1)   0.0026s    385.4
     192 bit ecdh (nistp192)   0.0037s    270.4
     224 bit ecdh (nistp224)   0.0048s    208.8
     256 bit ecdh (nistp256)   0.0062s    162.2
     384 bit ecdh (nistp384)   0.0152s     65.9
     521 bit ecdh (nistp521)   0.0334s     30.0
     163 bit ecdh (nistk163)   0.0044s    226.9
     233 bit ecdh (nistk233)   0.0078s    128.5
     283 bit ecdh (nistk283)   0.0147s     68.1
     409 bit ecdh (nistk409)   0.0321s     31.2
     571 bit ecdh (nistk571)   0.0755s     13.2
     163 bit ecdh (nistb163)   0.0048s    209.1
     233 bit ecdh (nistb233)   0.0088s    113.7
     283 bit ecdh (nistb283)   0.0161s     62.2
     409 bit ecdh (nistb409)   0.0364s     27.5
     571 bit ecdh (nistb571)   0.0858s     11.7
    
[/code]
#### Linpack
Compile: 
[code] 
    linaro@localhost:~/bench$ cc -Ofast -o linpack linpack.c -lm -mcpu=cortex-a7 -mfpu=vfpv4 -mfloat-abi=hard -funsafe-math-optimizations -fomit-frame-pointer -ffast-math -funroll-loops -funsafe-loop-optimizations
    
[/code]
Results 
[code] 
    Enter array size (q to quit) [200]:  
    Memory required:  315K.
     
     
    LINPACK benchmark, Double precision.
    Machine precision:  15 digits.
    Array size 200 X 200.
    Average rolled and unrolled performance:
     
        Reps Time(s) DGEFA   DGESL  OVERHEAD    KFLOPS
    ----------------------------------------------------
          32   0.73  87.67%   4.11%   8.22%  65592.040
          64   1.70  89.41%   2.94%   7.65%  55983.015
         128   1.19  90.76%   3.36%   5.88%  156952.381
         256   2.36  88.56%   3.39%   8.05%  162015.361
         512   5.03  89.86%   2.78%   7.36%  150889.843
        1024  10.19  89.99%   2.75%   7.26%  148814.109
    
[/code]
Note: The linpack results suggest that the floating performance of the Cortex A7 core in the A20 is signficantly faster (up to 3x more KFLOPS) than the Cortex A8 used in the A10. Running a flioating-point intensive application (3D geometry processing) seems to confirm that the A20 is significantly faster. 
#### lmbench
lmbench (lmbench-3.0-a9) is an older and not very well known benchmark, but can provides some interesting low-level architectural details as well as memory speed benchmarks. 
[code] 
    $ cache -N 2 -M 4M -L 64
    L1 cache: 32768 bytes 2.99 nanoseconds 64 linesize 1.73 parallelism
    L2 cache: 262144 bytes 14.36 nanoseconds 64 linesize 2.34 parallelism
    Memory latency: 158.86 nanoseconds 1.75 parallelism
    
[/code]
The reported latency and parallelism is not consistent between runs, but the L1 data cache and L2 cache size is probably correct. The L2 cache size is not large, but that is not surprising for a 55nm manufactured SoC (modern higher-end ARM socs manufactured at 28nm for smartphones and tablets have up to 2MB of L2 cache; RK3188 has 512KB L2 cache). 
[code] 
    $ echo -n 'CPU speed: '
    $ mhz
    $ lat_ops -N 100
    $ par_ops -N 10
    CPU speed: 1008 MHz, 0.9921 nanosec clock
    integer bit: 1.00 nanoseconds
    integer add: 0.99 nanoseconds
    integer mul: 2.98 nanoseconds
    integer div: 73.66 nanoseconds
    integer mod: 23.93 nanoseconds
    int64 bit: 2.00 nanoseconds
    uint64 add: 2.14 nanoseconds
    int64 mul: 5.02 nanoseconds
    int64 div: 311.98 nanoseconds
    int64 mod: 195.88 nanoseconds
    float add: 3.97 nanoseconds
    float mul: 3.98 nanoseconds
    float div: 17.88 nanoseconds
    double add: 3.98 nanoseconds
    double mul: 6.96 nanoseconds
    double div: 31.81 nanoseconds
    float bogomflops: 28.14 nanoseconds
    double bogomflops: 45.05 nanoseconds
    integer bit parallelism: 1.03
    integer add parallelism: 1.43
    integer mul parallelism: 2.78
    integer div parallelism: 1.01
    integer mod parallelism: 1.05
    int64 bit parallelism: 1.00
    int64 add parallelism: 1.14
    int64 mul parallelism: 1.01
    int64 div parallelism: 1.03
    int64 mod parallelism: 1.02
    float add parallelism: 3.98
    float mul parallelism: 1.60
    float div parallelism: 1.20
    double add parallelism: 3.98
    double mul parallelism: 1.27
    double div parallelism: 1.10
    
[/code]
This gives interesting info about the CPU instruction characteristics of the ARM Cortex A7 core used in the A20. 
  * As with most ARM architectures, integer divide slow.
  * Integer multiply is relatively fast.
  * Floating performance is OK, and single precision (float) is faster than double precision (double).

Memory latencies: 
[code] 
    $ lat_mem_rd -N 8 16 128
    0.00049 3.013
    0.00098 3.009
    0.00195 3.014
    0.00293 3.009
    0.00391 3.019
    0.00586 3.009
    0.00781 3.018
    0.01172 3.009
    0.01562 2.996
    0.02344 6.636
    0.03125 5.792
    0.04688 9.009
    0.06250 10.178
    0.09375 9.222
    0.12500 10.254
    0.18750 21.143
    0.25000 27.971
    0.37500 42.014
    0.50000 46.024
    0.75000 46.074
    1.00000 46.855
    1.50000 57.570
    2.00000 58.869
    3.00000 60.061
    4.00000 60.225
    6.00000 60.892
    8.00000 61.057
    12.00000 61.355
    16.00000 61.225
    
[/code]
This confirms the cache sizes of the A20, the L1 (data) cache size is 32KB, latency seems to about 3ns, and as buffer size approaches 32KB the latency reported by the test starts to increase due to cache associativity effects (cache line conflicts). A similar transition is seen for the L2 cache, latency is about 9.3ns, and latency starts to increase as the buffer size approaches 256KB. DRAM latency is about 60ns on the test configuration (1008 MHz CPU, 432 MHz DRAM clock, 432 MHz MBUS clock, 6 cycle CAS timing). With 9 cycle CAS timing latency at 16MB buffer size is 63.8ns. 
Memory bandwidth: 
[code] 
    One CPU core:
    4K read  0.004000 5889.70
    4K write 0.004000 10083.91
    4K rdwr  0.004000 4401.45
    4K copy  0.004000 8441.78
    64K read  0.064000 4488.56
    64K write 0.064000 6251.16
    64K rdwr  0.064000 2420.51
    64K copy  0.064000 2821.57
    1M read  1.00 1273.65
    1M write 1.00 542.30
    1M rdwr  1.00 592.77
    1M copy  1.00 293.34
    16M read  16.00 1136.36
    16M write 16.00 513.89
    16M rdwr  16.00 549.53
    16M copy  16.00 288.14
    Two CPU cores:
    4K read  0.004000 11623.95
    4K write 0.004000 20121.14
    4K rdwr  0.004000 8693.74
    4K copy  0.004000 16691.51
    64K read  0.064000 8449.77
    64K write 0.064000 10443.66
    64K rdwr  0.064000 3063.00
    64K copy  0.064000 2790.98
    1M read  1.00 1791.39
    1M write 1.00 588.36
    1M rdwr  1.00 595.09
    1M copy  1.00 409.95
    16M read  16.00 1533.03
    16M write 16.00 719.84
    16M rdwr  16.00 630.88
    16M copy  16.00 413.78
    
[/code]
Each core has its own L1 data cache, so the L1 cache bandwidth doubles with two cores active. WIth two cores active, the shared L2 cache bandwidth (64K buffer result above) increases compared to when using only one core except in the case of copy when one core already saturates the L2 cache bandwidth. With DRAM access (16M buffer), two active cores are able to utilize more DRAM bandwidth compared to when using only one core (may depend on the lmbench implementation, but is probably a good sign for multi-tasking performance). With a CAS timing of 9 cycles instead of 6, performance is only slightly slower. However, with lower DRAM or MBUS clock, performance will be lower. 
### GPU
The Mali-400MP2 GPU in the A20 has two pixel processors instead of only one in the A10 (Mali-400MP). Because of that especially fillrate (i.e. high resolution) performance should be higher with proper drivers. You need the newer Mali r3p2 drivers (standard is r3p0) to really take advantage of the improved features of the Mali-400MP2. See the section [Optimizing system performance][9882] for advanced instructions for using the r3p2 Mali drivers. 
The following benchmarks were performed with 1280x720 60 Hz HDMI output (32bpp). The window size of of glmark2 is the default 800x600. The device has the memory clock set to 408 MHz (which is lower than some other devices which may impact performance). The CPU governor was set to ondemand with custom settings. The SwapbuffersWait option was set to "false" in the xorg.conf to eliminate the effect of vsync. The fb0_framebuffer_num in script.bin was set to 3 so that xf86-video-fbturbo can optimally provide Mali GLES integration. 
The version of glmark2 (glmark2-es2) used is 2013.08.07. Source: <https://github.com/ssvb/glmark2.git>. Configure with 
[code] 
    apt-get install libgles2-mesa-dev && ./waf configure --with-flavors x11-glesv2
    
[/code]
You might need to apply a patch like this to the GLES header files for a clean compile: 
[code] 
    *** /usr/include/GLES2/gl2.h-old	2013-11-25 22:00:09.287711308 +0100
    --- /usr/include/GLES2/gl2.h	2013-11-25 22:00:45.147711324 +0100
    ***************
    *** 32,37 ****
    --- 32,38 ----
      typedef khronos_float_t  GLfloat;
      typedef khronos_float_t  GLclampf;
      typedef khronos_int32_t  GLfixed;
    + typedef char             GLchar;
      
      /* GL types for handling large vertex buffer objects */
      typedef khronos_intptr_t GLintptr;
    
[/code]
Performance with standard Mali r3p0 drivers/kernel: 
[code] 
    =======================================================
        glmark2 2013.08.07
    =======================================================
        OpenGL Information
        GL_VENDOR:     ARM
        GL_RENDERER:   Mali-400 MP
        GL_VERSION:    OpenGL ES 2.0
    =======================================================
    [build] use-vbo=false: FPS: 190 FrameTime: 5.263 ms
    [build] use-vbo=true: FPS: 225 FrameTime: 4.444 ms
    [texture] texture-filter=nearest: FPS: 257 FrameTime: 3.891 ms
    [texture] texture-filter=linear: FPS: 226 FrameTime: 4.425 ms
    [texture] texture-filter=mipmap: FPS: 200 FrameTime: 5.000 ms
    [shading] shading=gouraud: FPS: 174 FrameTime: 5.747 ms
    [shading] shading=blinn-phong-inf: FPS: 161 FrameTime: 6.211 ms
    [shading] shading=phong: FPS: 131 FrameTime: 7.634 ms
    [bump] bump-render=high-poly: FPS: 74 FrameTime: 13.514 ms
    [bump] bump-render=normals: FPS: 229 FrameTime: 4.367 ms
    [bump] bump-render=height: FPS: 182 FrameTime: 5.495 ms
    [effect2d] kernel=0,1,0;1,-4,1;0,1,0;: FPS: 37 FrameTime: 27.027 ms
    [effect2d] kernel=1,1,1,1,1;1,1,1,1,1;1,1,1,1,1;: FPS: 22 FrameTime: 45.455 ms
    [pulsar] light=false:quads=5:texture=false: FPS: 279 FrameTime: 3.584 ms
    [desktop] blur-radius=5:effect=blur:passes=1:separable=true:windows=4: FPS: 16 FrameTime: 62.500 ms
    [desktop] effect=shadow:windows=4: FPS: 61 FrameTime: 16.393 ms
    [buffer] columns=200:interleave=false:update-dispersion=0.9:update-fraction=0.5:update-method=map: Unsupported
    [buffer] columns=200:interleave=false:update-dispersion=0.9:update-fraction=0.5:update-method=subdata: FPS: 32 FrameTime: 31.250 ms
    [buffer] columns=200:interleave=true:update-dispersion=0.9:update-fraction=0.5:update-method=map: Unsupported
    [ideas] speed=duration: FPS: 156 FrameTime: 6.410 ms
    [jellyfish] <default>: FPS: 52 FrameTime: 19.231 ms
    [terrain] <default>: Unsupported
    [shadow] <default>: FPS: 27 FrameTime: 37.037 ms
    [refract] <default>: FPS: 15 FrameTime: 66.667 ms
    [conditionals] fragment-steps=0:vertex-steps=0: FPS: 249 FrameTime: 4.016 ms
    [conditionals] fragment-steps=5:vertex-steps=0: FPS: 85 FrameTime: 11.765 ms
    [conditionals] fragment-steps=0:vertex-steps=5: FPS: 256 FrameTime: 3.906 ms
    [function] fragment-complexity=low:fragment-steps=5: FPS: 119 FrameTime: 8.403 ms
    [function] fragment-complexity=medium:fragment-steps=5: FPS: 58 FrameTime: 17.241 ms
    [loop] fragment-loop=false:fragment-steps=5:vertex-steps=5: FPS: 118 FrameTime: 8.475 ms
    [loop] fragment-steps=5:fragment-uniform=false:vertex-steps=5: FPS: 118 FrameTime: 8.475 ms
    [loop] fragment-steps=5:fragment-uniform=true:vertex-steps=5: FPS: 118 FrameTime: 8.475 ms
    =======================================================
                                      glmark2 Score: 133 
    =======================================================
    
[/code]
Performance with Mali r3p2 drivers/kernel: 
[code] 
    =======================================================
        glmark2 2013.08.07
    =======================================================
        OpenGL Information
        GL_VENDOR:     ARM
        GL_RENDERER:   Mali-400 MP
        GL_VERSION:    OpenGL ES 2.0
    =======================================================
    [build] use-vbo=false: FPS: 181 FrameTime: 5.525 ms
    [build] use-vbo=true: FPS: 199 FrameTime: 5.025 ms
    [texture] texture-filter=nearest: FPS: 224 FrameTime: 4.464 ms
    [texture] texture-filter=linear: FPS: 216 FrameTime: 4.630 ms
    [texture] texture-filter=mipmap: FPS: 244 FrameTime: 4.098 ms
    [shading] shading=gouraud: FPS: 159 FrameTime: 6.289 ms
    [shading] shading=blinn-phong-inf: FPS: 163 FrameTime: 6.135 ms
    [shading] shading=phong: FPS: 129 FrameTime: 7.752 ms
    [bump] bump-render=high-poly: FPS: 67 FrameTime: 14.925 ms
    [bump] bump-render=normals: FPS: 265 FrameTime: 3.774 ms
    [bump] bump-render=height: FPS: 234 FrameTime: 4.274 ms
    [effect2d] kernel=0,1,0;1,-4,1;0,1,0;: FPS: 87 FrameTime: 11.494 ms
    [effect2d] kernel=1,1,1,1,1;1,1,1,1,1;1,1,1,1,1;: FPS: 42 FrameTime: 23.810 ms
    [pulsar] light=false:quads=5:texture=false: FPS: 356 FrameTime: 2.809 ms
    [desktop] blur-radius=5:effect=blur:passes=1:separable=true:windows=4: FPS: 29 FrameTime: 34.483 ms
    [desktop] effect=shadow:windows=4: FPS: 114 FrameTime: 8.772 ms
    [buffer] columns=200:interleave=false:update-dispersion=0.9:update-fraction=0.5:update-method=map: Unsupported
    [buffer] columns=200:interleave=false:update-dispersion=0.9:update-fraction=0.5:update-method=subdata: FPS: 36 FrameTime: 27.778 ms
    [buffer] columns=200:interleave=true:update-dispersion=0.9:update-fraction=0.5:update-method=map: Unsupported
    [ideas] speed=duration: FPS: 159 FrameTime: 6.289 ms
    [jellyfish] <default>: FPS: 114 FrameTime: 8.772 ms
    [terrain] <default>: Unsupported
    [shadow] <default>: FPS: 95 FrameTime: 10.526 ms
    [refract] <default>: FPS: 15 FrameTime: 66.667 ms
    [conditionals] fragment-steps=0:vertex-steps=0: FPS: 334 FrameTime: 2.994 ms
    [conditionals] fragment-steps=5:vertex-steps=0: FPS: 145 FrameTime: 6.897 ms
    [conditionals] fragment-steps=0:vertex-steps=5: FPS: 298 FrameTime: 3.356 ms
    [function] fragment-complexity=low:fragment-steps=5: FPS: 197 FrameTime: 5.076 ms
    [function] fragment-complexity=medium:fragment-steps=5: FPS: 104 FrameTime: 9.615 ms
    [loop] fragment-loop=false:fragment-steps=5:vertex-steps=5: FPS: 192 FrameTime: 5.208 ms
    [loop] fragment-steps=5:fragment-uniform=false:vertex-steps=5: FPS: 196 FrameTime: 5.102 ms
    [loop] fragment-steps=5:fragment-uniform=true:vertex-steps=5: FPS: 193 FrameTime: 5.181 ms
    =======================================================
                                      glmark2 Score: 165 
    =======================================================
    
[/code]
Note that several sub-benchmarks show doubled performance or better. This includes 2D compositing and fillrate-limited tests. 
After tweaking the memory controller parameters (DRAM frequency 432 MHz, MBUS frequency 432 MHz, CAS timing 6 cycles) the gl2mark2 score increases to 189. 
Another benchmark of r3p2 drivers, done on Cubietruck, with r3p2 kernel module, binary drivers and patched xf86-video-fbturbo: 
[code] 
    root@cubietruck:/sata/build/xf86-video-fbturbo# DISPLAY=:0 glmark2-es2
    =======================================================
        glmark2 2012.08
    =======================================================
        OpenGL Information
        GL_VENDOR:     ARM
        GL_RENDERER:   Mali-400 MP
        GL_VERSION:    OpenGL ES 2.0
    =======================================================
    [build] use-vbo=false: FPS: 204 FrameTime: 4.902 ms
    [build] use-vbo=true: FPS: 262 FrameTime: 3.817 ms
    [texture] texture-filter=nearest: FPS: 291 FrameTime: 3.436 ms
    [texture] texture-filter=linear: FPS: 282 FrameTime: 3.546 ms
    [texture] texture-filter=mipmap: FPS: 315 FrameTime: 3.175 ms
    [shading] shading=gouraud: FPS: 195 FrameTime: 5.128 ms
    [shading] shading=blinn-phong-inf: FPS: 208 FrameTime: 4.808 ms
    [shading] shading=phong: FPS: 167 FrameTime: 5.988 ms
    [bump] bump-render=high-poly: FPS: 75 FrameTime: 13.333 ms
    [bump] bump-render=normals: FPS: 341 FrameTime: 2.933 ms
    [bump] bump-render=height: FPS: 299 FrameTime: 3.344 ms
    [effect2d] kernel=0,1,0;1,-4,1;0,1,0;: FPS: 93 FrameTime: 10.753 ms
    [effect2d] kernel=1,1,1,1,1;1,1,1,1,1;1,1,1,1,1;: FPS: 43 FrameTime: 23.256 ms
    [pulsar] light=false:quads=5:texture=false: FPS: 438 FrameTime: 2.283 ms
    [desktop] blur-radius=5:effect=blur:passes=1:separable=true:windows=4: FPS: 33 FrameTime: 30.303 ms
    [desktop] effect=shadow:windows=4: FPS: 138 FrameTime: 7.246 ms
    Error: Requested MapBuffer VBO update method but GL_OES_mapbuffer is not supported!
    [buffer] columns=200:interleave=false:update-dispersion=0.9:update-fraction=0.5:update-method=map: Unsupported
    [buffer] columns=200:interleave=false:update-dispersion=0.9:update-fraction=0.5:update-method=subdata: FPS: 40 FrameTime: 25.000 ms
    Error: Requested MapBuffer VBO update method but GL_OES_mapbuffer is not supported!
    [buffer] columns=200:interleave=true:update-dispersion=0.9:update-fraction=0.5:update-method=map: Unsupported
    [ideas] speed=duration: FPS: 182 FrameTime: 5.495 ms
    [jellyfish] <default>: FPS: 126 FrameTime: 7.937 ms
    Error: SceneTerrain requires Vertex Texture Fetch support, but GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS is 0
    [terrain] <default>: Unsupported
    [conditionals] fragment-steps=0:vertex-steps=0: FPS: 386 FrameTime: 2.591 ms
    [conditionals] fragment-steps=5:vertex-steps=0: FPS: 163 FrameTime: 6.135 ms
    [conditionals] fragment-steps=0:vertex-steps=5: FPS: 401 FrameTime: 2.494 ms
    [function] fragment-complexity=low:fragment-steps=5: FPS: 226 FrameTime: 4.425 ms
    [function] fragment-complexity=medium:fragment-steps=5: FPS: 114 FrameTime: 8.772 ms
    [loop] fragment-loop=false:fragment-steps=5:vertex-steps=5: FPS: 226 FrameTime: 4.425 ms
    [loop] fragment-steps=5:fragment-uniform=false:vertex-steps=5: FPS: 227 FrameTime: 4.405 ms
    [loop] fragment-steps=5:fragment-uniform=true:vertex-steps=5: FPS: 227 FrameTime: 4.405 ms
    =======================================================
                                      glmark2 Score: 211 
    =======================================================
    
[/code]

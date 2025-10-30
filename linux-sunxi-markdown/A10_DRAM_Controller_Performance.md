# A10 DRAM Controller Performance
## Tests with the lima-memspeed program on a Cubietruck with a 1920x1080-32@60Hz monitor
The [lima-memspeed][1513] program is a tool, which tries to simulate different memory intensive workloads and measure how much of the memory bandwidth is really available to be consumed by the CPU, GPU and other peripherals. Basically, it should provide an answer to the question about the optimal relationship between the MBUS and DRAM clock frequencies and whether increasing the DRAM clock speed provides any practical improvements. The systems with a 32-bit dram bus width can't be analyzed well by just the tinymembench program, because tinymembench only focuses on the memory bandwidth available to a single CPU core. And a single CPU core alone can't consume all the DRAM bandwidth, but may benefit from some help from the other peripherals and other CPU cores. 
[code] 
    Usage: lima-memspeed [workload1] [workload2] ... [workloadN]
    
    Where the 'workload' arguments are the identifiers of different
    memory bandwidth consuming workloads. Each workload is run in its
    own thread.
    
    The list of available workload identifiers:
    	fb_blank                       (blank the screen in order not to drain memory bandwidth)
    	fb_scanout                     (take the framebuffer scanout bandwidth into account)
    	gpu_write                      (use the lima driver to solid fill the screen)
    	gpu_copy                       (use the lima driver to copy a texture to the screen)
    	neon_write                     (use ARM NEON to fill a memory buffer)
    	neon_write_backwards           (use ARM NEON to fill a memory buffer)
    	neon_read_pf32                 (use ARM NEON to read from a memory buffer)
    	neon_read_pf64                 (use ARM NEON to read from a memory buffer)
    	neon_copy_pf64                 (use ARM NEON to copy a memory buffer)
    
[/code]
Cubietruck (standard 32-bit dram bus width)  MBUS clock  | DRAM clock  | fb_scanout gpu_write  | fb_scanout neon_write  | fb_scanout neon_copy_pf64 (*)  | fb_blank gpu_write  | fb_blank neon_write  | fb_blank neon_write neon_read_pf64  | fb_blank neon_write gpu_write   
---|---|---|---|---|---|---|---|---  
300 MHz | 432 MHz | 2209.3 MB/s | 2343.2 MB/s | 1826.3 MB/s | 1935.1 MB/s | 2035.5 MB/s | 2270.5 MB/s | 2018.0 MB/s   
400 MHz | 432 MHz | 2301.6 MB/s | 2765.3 MB/s | 1835.9 MB/s | 2045.8 MB/s | 2703.7 MB/s | 2615.1 MB/s | 2610.4 MB/s   
400 MHz | 528 MHz | 2448.0 MB/s | 3064.1 MB/s | 2096.7 MB/s | 2073.4 MB/s | 2713.5 MB/s | 2882.8 MB/s | 2673.7 MB/s   
528 MHz | 528 MHz | 2461.8 MB/s | 3298.6 MB/s | 2107.1 MB/s | 2098.3 MB/s | 3288.1 MB/s | 3172.1 MB/s | 3370.1 MB/s   
400 MHz | 600 MHz | 2511.5 MB/s | 3094.4 MB/s | 2146.1 MB/s | 2073.4 MB/s | 2717.7 MB/s | 2940.8 MB/s | 2675.7 MB/s   
400 MHz | 648 MHz | 2542.7 MB/s | 3106.7 MB/s | 2243.0 MB/s | 2073.4 MB/s | 2721.9 MB/s | 2978.5 MB/s | 2683.2 MB/s   
600 MHz | 648 MHz | 2543.3 MB/s | 3451.5 MB/s | 2262.7 MB/s | 2102.4 MB/s | 3293.7 MB/s | 3600.8 MB/s | 3630.9 MB/s   
Cubietruck (artificially configured 16-bit dram bus width)  MBUS clock  | DRAM clock  | fb_scanout gpu_write  | fb_scanout neon_write  | fb_scanout neon_copy_pf64 (*)  | fb_blank gpu_write  | fb_blank neon_write  | fb_blank neon_write neon_read_pf64  | fb_blank neon_write gpu_write   
---|---|---|---|---|---|---|---|---  
300 MHz | 528 MHz | 1354.0 MB/s | 1873.6 MB/s | 1268.5 MB/s | 1188.7 MB/s | 1979.5 MB/s | 1627.1 MB/s | 1712.5 MB/s   
400 MHz | 528 MHz | 1354.3 MB/s | 1903.0 MB/s | 1278.1 MB/s | 1181.7 MB/s | 1981.7 MB/s | 1637.7 MB/s | 1707.8 MB/s   
528 MHz | 528 MHz | 1352.3 MB/s | 1892.6 MB/s | 1269.3 MB/s | 1188.7 MB/s | 1979.6 MB/s | 1626.0 MB/s | 1702.0 MB/s   
300 MHz | 648 MHz | 1464.1 MB/s | 2219.9 MB/s | 1403.5 MB/s | 1256.4 MB/s | 2046.7 MB/s | 1923.1 MB/s | 1892.5 MB/s   
400 MHz | 648 MHz | 1463.3 MB/s | 2332.0 MB/s | 1403.5 MB/s | 1258.1 MB/s | 2415.7 MB/s | 1925.5 MB/s | 1993.0 MB/s   
600 MHz | 648 MHz | 1464.3 MB/s | 2348.3 MB/s | 1403.5 MB/s | 1255.0 MB/s | 2382.0 MB/s | 1926.9 MB/s | 1993.6 MB/s   
(*) copying 1 MB from one memory location to another memory location per second means 2 MB/s bandwidth in this table, because both reads and writes are accounted. 
**Based on the benchmark results above, looks like the systems with a full 32-bit memory interface want to have both MBUS and DRAM clocked at high speed. While the Allwinner A20 systems with only a 16-bit memory interface (such as[Olimex A20-OLinuXino-Lime][1514]) should not have any obvious extra bandwidth penalties even if MBUS is clocked slower than DRAM.**
## Tests with the tinymembench program on a A13-OLinuXino-Micro and screen blanked
The Allwinner A13 user manual tells us about the 300MHz clock speed limit for MBUS. And indeed, when having only 16-bit external DDR3 memory interface to deal with, clocking MBUS at a very high speed may be unnecessary (assuming that MBUS internally has the same width as in the A10/A20 siblings). So it is quite interesting to check if running MBUS at half-speed of DRAM is fast enough for A13. 
Benchmarks have been run on [Olimex_A13-OLinuXino-Micro][1515] for different MBUS/DRAM clock settings. The CPU clock speed was 1008MHz, AXI clock speed 504MHz (overclocked). The screen was blanked in order not to drain memory bandwidth. The performance numbers are obtained using a [tinymembench][1516] tool for the 'NEON read prefetched (64 bytes step)', 'NEON fill', 'NEON copy prefetched (64 bytes step)' subtests. The DRAM timings are accurately calculated for each clock frequency, assuming JEDEC Speed Bin 1333H (DDR3 1333 9-9-9). 
Please note that the DRAM clock speeds above 533 MHz (and MBUS above 300 MHz) may be considered overclocking if we trust the Allwinner manuals!
Original old u-boot-sunxi settings (with the wastful DDR3-1333 timings)  MBUS clock  | DRAM clock  | Read  | Write  | Copy  | Random read in 64MiB block   
---|---|---|---|---|---  
204 MHz | 408 MHz | 709.1 MB/s | 1026.7 MB/s | 475.4 MB/s | 311.8 ns   
Half speed MBUS  MBUS clock  | DRAM clock  | Read  | Write  | Copy  | Random read in 64MiB block   
---|---|---|---|---|---  
204 MHz | 408 MHz | 738.0 MB/s | 1027.1 MB/s | 512.7 MB/s | 286.3 ns   
216 MHz | 432 MHz | 762.6 MB/s | 1095.4 MB/s | 544.4 MB/s | 274.8 ns   
300 MHz MBUS  MBUS clock  | DRAM clock  | Read  | Write  | Copy  | Random read in 64MiB block   
---|---|---|---|---|---  
300 MHz | 408 MHz | 785.7 MB/s | 1450.3 MB/s | 511.3 MB/s | 262.2 ns   
300 MHz | 432 MHz | 825.2 MB/s | 1474.6 MB/s | 544.1 MB/s | 259.2 ns   
300 MHz | 456 MHz | 854.3 MB/s | 1486.8 MB/s | 576.3 MB/s | 244.3 ns   
300 MHz | 480 MHz | 880.2 MB/s | 1491.6 MB/s | 606.7 MB/s | 241.8 ns   
300 MHz | 504 MHz | 889.8 MB/s | 1499.9 MB/s | 637.7 MB/s | 238.6 ns   
300 MHz | 528 MHz | 936.2 MB/s | 1507.4 MB/s | 671.0 MB/s | 232.1 ns   
300 MHz | 552 MHz | 921.0 MB/s | 1508.3 MB/s | 659.7 MB/s | 236.2 ns   
300 MHz | 576 MHz | 943.8 MB/s | 1512.8 MB/s | 689.3 MB/s | 231.2 ns   
300 MHz | 600 MHz | 988.3 MB/s | 1517.5 MB/s | 719.1 MB/s | 224.3 ns   
300 MHz | 624 MHz | 979.5 MB/s | 1518.9 MB/s | 743.6 MB/s | 226.6 ns   
300 MHz | 648 MHz | 1012.8 MB/s | 1522.5 MB/s | 770.1 MB/s | 221.2 ns   
Balanced speed MBUS (2/3 of DRAM)  MBUS clock  | DRAM clock  | Read  | Write  | Copy  | Random read in 64MiB block   
---|---|---|---|---|---  
272 MHz | 408 MHz | 770.2 MB/s | 1345.8 MB/s | 512.2 MB/s | 270.7 ns   
288 MHz | 432 MHz | 816.6 MB/s | 1421.0 MB/s | 545.4 MB/s | 259.9 ns   
304 MHz | 456 MHz | 857.3 MB/s | 1504.8 MB/s | 576.4 MB/s | 245.3 ns   
320 MHz | 480 MHz | 897.5 MB/s | 1584.6 MB/s | 606.8 MB/s | 239.5 ns   
336 MHz | 504 MHz | 933.5 MB/s | 1663.9 MB/s | 643.5 MB/s | 232.8 ns   
352 MHz | 528 MHz | 954.4 MB/s | 1742.0 MB/s | 669.1 MB/s | 226.6 ns   
368 MHz | 552 MHz | 979.4 MB/s | 1797.8 MB/s | 665.3 MB/s | 228.7 ns   
384 MHz | 576 MHz | 1014.1 MB/s | 1789.7 MB/s | 689.1 MB/s | 222.6 ns   
400 MHz | 600 MHz | 1039.7 MB/s | 1836.8 MB/s | 719.3 MB/s | 215.9 ns   
416 MHz | 624 MHz | 1069.6 MB/s | 1819.2 MB/s | 747.5 MB/s | 219.1 ns   
432 MHz | 648 MHz | 1092.5 MB/s | 1869.2 MB/s | 777.8 MB/s | 210.3 ns   
Full speed MBUS (the same as DRAM)  MBUS clock  | DRAM clock  | Read  | Write  | Copy  | Random read in 64MiB block   
---|---|---|---|---|---  
408 MHz | 408 MHz | 833.6 MB/s | 1460.8 MB/s | 513.0 MB/s | 252.3 ns   
432 MHz | 432 MHz | 863.1 MB/s | 1555.5 MB/s | 543.2 MB/s | 243.8 ns   
456 MHz | 456 MHz | 911.5 MB/s | 1647.3 MB/s | 576.7 MB/s | 233.2 ns   
480 MHz | 480 MHz | 954.2 MB/s | 1727.3 MB/s | 609.5 MB/s | 231.5 ns   
504 MHz | 504 MHz | 983.0 MB/s | 1813.1 MB/s | 638.3 MB/s | 220.6 ns   
528 MHz | 528 MHz | 1030.9 MB/s | 1913.3 MB/s | 676.4 MB/s | 220.8 ns   
552 MHz | 552 MHz | 1033.2 MB/s | 1943.4 MB/s | 623.4 MB/s | 217.8 ns   
576 MHz | 576 MHz | 1065.7 MB/s | 1989.1 MB/s | 691.3 MB/s | 211.3 ns   
600 MHz | 600 MHz | Reliability is poor   
624 MHz | 624 MHz | Reliability is poor   
648 MHz | 648 MHz | Reliability is poor   
Exotic MBUS configurations (no practical use, just for the sake of research)  MBUS clock  | DRAM clock  | Read  | Write  | Copy  | Random read in 64MiB block  | Random non-cached read in 4KiB block   
---|---|---|---|---|---|---  
50 MHz | 600 MHz | 303.1 MB/s | 255.7 MB/s | 236.4 MB/s | 505.3 ns | 335.6 ns   
100 MHz | 600 MHz | 535.0 MB/s | 516.3 MB/s | 389.3 MB/s | 316.0 ns | 215.7 ns   
150 MHz | 600 MHz | 700.8 MB/s | 773.2 MB/s | 594.1 MB/s | 261.1 ns | 166.3 ns   
200 MHz | 600 MHz | 818.1 MB/s | 1018.9 MB/s | 686.9 MB/s | 258.4 ns | 142.7 ns   
The non-cached read latency numbers from the table above should have no TLB misses and exactly one DRAM access per read. They seem to fit the _(12 * mbus_cycle_time + 95 ns)_ formula quite nicely. It might be that MBUS contributes 12 its cycles to the memory access latency.

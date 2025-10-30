# SBROM
## SBROM Error Codes
The SBROM performs several verification steps before executing the loaded [TOC0][47976] image, so there are many ways it can fail and dump you to [FEL][47977]. Thankfully, the SBROM records an error code in most failure paths, and these can help you debug your [TOC0][47976] image generation process. 
Obviously, these error codes are meant for internal debugging, so they are not neatly organized. The location, encoding, and granularity of these error codes vary from chip to chip. There may be more than one set of codes recorded by a single SBROM implementation. Some error codes may be used multiple places within the SBROM, making them ambiguous. Finally, the descriptions provided below are reverse-engineered from the SBROM code, so they may not always be accurate. 
The BROMs do not contain any human-readable log messages, but they use use several methods of reporting integer status and error codes: 
  * Storing information in SRAM. This usually includes the contents of various [eFuses][47978], such as `BROM_CONFIG` and `ROTPK_HASH`.
  * Reading from or writing to an "dummy" or unmapped address in MMIO space. Presumably this is visible to JTAG.
  * Toggling a bit in MMIO space (usually in the SYSCON region), with the number of pulses or the width of each pulse varying based on the status/error code. Presumably this is visible to JTAG or a logic analyzer.
  * Writing to a MMIO register in the SYSCON or RTC region. Sometimes the BROM splits the register into two 16-bit words and alternates between them on consecutive boots.

### H5 SBROM
The H5 SBROM writes the following codes to the SYSCON at 0x1c000f0, using the functions at 0x033c (low word) and 0x0374 (high word), roughly in the order listed below. 
[![Sticky-note-pin.png][47979]][47980] _Note:_ Bit 31 of this register controls which BROM (SBROM or NBROM) is visible, and will be set by the time you read this register from FEL. 
Value | Location | Type | Description   
---|---|---|---  
`0x..01....` | 0x2364 | Status | Beginning normal (i.e. not standby) boot process   
`0x..02....` | 0x2274 | Status | Beginning boot device selection   
`0x....0301` | 0x087c | Error | MMC: TOC0 4-byte magic mismatch   
`0x....0341` | 0x4f1c | Error | MMC: TOC0 8-byte name mismatch   
`0x....0342` | 0x4f4c | Error | MMC: TOC0 length too large (> 0x20000) or not aligned (0x200)   
`0x....0343` | 0x4fc0 | Error | MMC: TOC0 checksum mismatch   
`0x..03....` | 0x20d0 | Status | Beginning cryptographic verification   
`0x..14....` | 0x212c | Status | Successfully read TOC0 header   
`0x..15....` | 0x2168 | Status | Found certificate item in TOC0   
`0x..16....` | 0x2184 | Status | Finished parsing certificate item   
`0x..**....` | 0x7dec | Status | Certificate signature status (see below)   
`0x..27....` | 0x21a4 | Status | Verified certificate key (ROTPK hash) and signature   
`0x..28....` | 0x21d4 | Status | Found firmware item in TOC0   
`0x..03....` | 0x220c | Status | Firmware matches certificate, copied code to SRAM, ready to boot   
These are the possible values for the certificate signature status: 
** | Meaning   
---|---  
0xf0 | Certificate is exactly 3072 bytes long (probably should have used >= instead of ==)   
0x00 | Bad RSA signature   
0x01 | Good RSA signature   
The H5 SBROM also contains a dummy MMIO read function at 0x202c, and a SYSCON bit toggle function at 0x0264. Neither of these are interesting.

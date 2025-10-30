# ACE Register guide
# Audio Codec Engine Registers
ACE does not exist on hardware beyond A10. 
Base address: 0x01c1a000 
## ACE Registers
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`[ACE_MODE_SELECTOR][5071]` | `0x0000` | `4B` | ``  
`[ACE_ACE_RESET][5072]` | `0x0004` | `4B` | ``  
## AE Registers
Register Name  | Offset  | Size  | Description   
---|---|---|---  
`[ACE_AE_INT_EN_REG][5073]` | `0x0108` | `4B` | ``  
`[ACE_AE_STATUS_REG][5074]` | `0x0124` | `4B` | ` Status register`  
## ACE_MODE_SELECTOR
Default value: 0x00000000  
Offset: 0x0000 
Name  | Bit  | Read/Write  | Default (Hex)  | Values  | Description   
---|---|---|---|---|---  
`` | `31:5` | `Read/Write` | `` | `` | unknown   
`ACE_CE_ENABLE_MASK` | `4` | `Read/Write` | `0x0` | ` `
[code]
        0x0 = Disable
        0x1 = Enable
      
    
[/code]
| Codec engine enable 
[code]
      Can offload zlib's deflate 
      and can be used with TSCC,
      PNG decoding
    
[/code]  
`` | `3:1` | `Read/Write` | `` | `` | unknown   
`ACE_AE_ENABLE_MASK` | `0` | `Read/Write` | `0x0` | ` `
[code]
        0x0 = Disable
        0x1 = Enable
      
    
[/code]
| Audio engine enable 
[code]
      can offload DTS and 
      AC3
    
[/code]

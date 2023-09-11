# **CAPYBARA**
## **Challenge**
What a cute picture of a capybara!

Flag format: PCTF{}

Author: @txnner
## **Writeup**
Extracting the given image using `binwalk`, I get a `.wav` file:
```console
agj1ss@agj1ss:/Desktop$ binwalk -e capybara.jpeg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
151174        0x24E86         Zip archive data, at least v2.0 to extract, compressed size: 6902, uncompressed size: 919160, name: audio.wav
158170        0x269DA         End of Zip archive, footer length: 22
```
Listening to this, it seems like morse code so I'm using a website to decode it to plain text:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/e0687578-7c57-407b-92fb-3bbbf6ff696b)

Using CyberChef to decode from Base64 and get the flag:
![Screenshot 2023-09-10 001056](https://github.com/agj1ss/CTF_Write_up/assets/108376735/2c5be057-b276-42f5-b87a-f7cc3b761cd1)


Flag: `PCTF{d0_y0U_kN0W_h0W_t0_R34D_m0r53_C0d3?}`

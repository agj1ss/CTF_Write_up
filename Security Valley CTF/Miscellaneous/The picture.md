![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/eb8c373f-a834-4062-a6b5-82633f980ee2)# **THE PICTURE**
## **Challenge**
WTF... we need a forensic specialist here

## **Writeup**
The challenge gave us a picture, maybe this is steganography?
![challenge](https://github.com/agj1ss/CTF_Write_up/assets/108376735/dbac3b61-dec4-4118-a8fc-6e26bb9e2f15)

So I tried `exiftool`, `binwalk`, `steghide`, etc. and I found the flag when using `zsteg`!
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/943c6c38-7c40-42a8-b6be-8626659cf25c)


Flag `SecVal{pH0R3N51C_m3}`

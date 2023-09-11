# **CONGRATULATIONS**
## **Challenge**
Congratulations on making it this far, here's an email attatchment.

Flag format: PCTF{}

Author: @elbee#3779
## **Writeup**
The file given is a `.docm`, which means a document has macro in it, so I analyze it using `olevba`:
![Screenshot 2023-09-10 001737](https://github.com/agj1ss/CTF_Write_up/assets/108376735/e400ac2a-4304-463f-8882-b25c57637b43)

The `x49` variable has a Hexadecimal string, so I get this and decode using CyberChef and get the flag:
![Screenshot 2023-09-10 001752](https://github.com/agj1ss/CTF_Write_up/assets/108376735/0c76fff5-2835-4549-a052-180ed07bda2b)


Flag: `PCTF{3n4bl3_m4cr05_plz_27315670}`

# **THE ARCHIVE**
## **Challenge**
I've forgotten my archive password. Help me restore it

## **Writeup**
The challenge gave us a `.zip` file, and when I tried to unzip it, it required me a password:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/34edb054-1204-4053-8f2d-970d6e63b745)

Of course I didn't know the password so I tried to crack it using `zip2john` and `john`:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/39b82e2d-93eb-45ae-b3d6-60f9cbdbe2c8)

Open the flag.txt and got the flag:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/9b2597ac-7b97-432b-b49c-b8232590083b)


Flag `SecVal{not_that_bad_for_a_zip}`

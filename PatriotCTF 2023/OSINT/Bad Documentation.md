# **BAD DOCUMENTATION**
## **Challenge**
I heard that this security researcher accidentally leaked his password in his documentation, but he deleted all the files in his repository so now we don't have access to it anymore! I'm pretty sure it's hopeless, but if you think you can find it here's the link to the repo: https://github.com/Th3Burn1nat0r/vuln.

Flag format: PCTF{}

Author: @necktie5740
## **Writeup**
Go to the given website, there is a repository that was deleted, so I check the history:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/043a4ec7-7ff0-4438-b7fd-48f7cf25e3c3)

Go to `J-Link` directory, I found this:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/0a5b80d0-dccc-4478-b7eb-442f9ccdf6d4)

I see the suspicious .png file and this is a base64 string in the `Authorization`:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/35b6222e-e44b-4722-836f-239a56bd411b)

Decode the string and get the flag:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/1097fee2-780e-4357-af73-081e25f365a1)

Flag: `PCTF{t0_c0D3's_3VuR}_R3aLlY_G0n3}`

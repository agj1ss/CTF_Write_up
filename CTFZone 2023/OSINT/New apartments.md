# Challenge:
Hamster Lenya moved to a new apartment. Look at the view from his window. Determine where Lenya lives. The response came in the format ctfzone{md5(00.0000,00.0000)} (Lat and Long with 4 digits after the decimal point, md5 digest in lower case)

# Solution:
The challenge gave me a picture of a building: 
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/a729f7b0-6776-4f55-9c36-deb54e356200)

I Upload this to `Google Lens` and found the building with its name "Cirkon Dental Lab" in a Facebook post:
![Screenshot 2023-08-13 104753](https://github.com/agj1ss/CTF_Write_up/assets/108376735/93e07930-9a4c-415c-90f4-8648c31da5c8)

![Screenshot 2023-08-13 104839](https://github.com/agj1ss/CTF_Write_up/assets/108376735/5cd1a033-fd3c-49cd-80c1-8383ee63b2e4)

The post's given me the address already so I entered the address into `Google Maps` to find the exact latitude and longitude:
![Screenshot 2023-08-13 104939](https://github.com/agj1ss/CTF_Write_up/assets/108376735/b9ed57c7-64a4-4327-a472-a6d1746de714)

According to the angle of the given image, I have pinned the assumed location of Lenya's apartment:
![Screenshot 2023-08-13 105043](https://github.com/agj1ss/CTF_Write_up/assets/108376735/161a1c64-6cdb-4b3a-ab62-a8636da0484f)

The flag came with the format `ctfzone{md5(00.0000,00.0000)}` so I used an online MD5 hash generator and used latitude and longitude that I had pinned in Google Maps to create the hash:
![Screenshot 2023-08-13 105059](https://github.com/agj1ss/CTF_Write_up/assets/108376735/69595702-a145-4308-816f-4b6a147d0677)

And we get the flag 🚩
# ENJOY 🤡

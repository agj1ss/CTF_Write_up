# Challenge:
5 years ago, Ray the hamster flew to see the world and bought a random plane ticket. Where he went can be found on the scoreboard at gate C15 at the airport.

Flag format: ctfzone{destination}

Note: the flag is case sensitive

# Solution:
The challenge gave me an image with `.heic` format, so I converted to `.jpg` to make it easier to upload to tools:
![image1](https://github.com/agj1ss/CTF_Write_up/assets/108376735/83d653b9-a379-4c23-a4c0-0de9730bdf85)

I uploaded this to `Google Lens` and after selecting every corner of this image, I found an image in Flickr that has similar buildings from afar like the given image:
![Screenshot 2023-08-13 104358](https://github.com/agj1ss/CTF_Write_up/assets/108376735/2328409e-5d67-483e-a701-65882863217e)

And this location is LaGuardia Airport in New York:
![Screenshot 2023-08-13 104439](https://github.com/agj1ss/CTF_Write_up/assets/108376735/95b03b73-a72f-4bd6-9917-a04137450852)

The challenge mentioned about `gate C15`, so I tried to google it:
![Screenshot 2023-08-13 103918](https://github.com/agj1ss/CTF_Write_up/assets/108376735/e1d87d9b-dc87-4ce8-812d-907b5d9255b1)

And there was a result quite below mentioned about it that I captured above, so I clicked on it and it has the exact location with minimap on it too:
![Screenshot 2023-08-13 103947](https://github.com/agj1ss/CTF_Write_up/assets/108376735/c5256f9a-9fe6-4a26-8e79-5cbda4c95673)

So I using Google Maps to the Terminal C of the airport, and using the only Google Street View that available at Terminal C and voilà:
![Screenshot 2023-08-13 104022](https://github.com/agj1ss/CTF_Write_up/assets/108376735/6b6e46d7-d146-4d85-b277-a81653e87af9)

There were two flights on the screen, so I tried to enter the one on the left

And we get the flag 🚩
# ENJOY 🤡

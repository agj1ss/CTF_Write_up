# **SATELLITE KILLER**
## **Challenge**
Most satellites get to live out a relatively peaceful existence in space until their orbit eventually decays and they fall back to Earth.

Most.

Back in the 80's, one poor satellite met a premature end at the hands of an ASM-135.

I would like you to find the date that the second-to-last piece of its debris fell back down to Earth (Or more realistically, its decay date).

In addition, please give me its object ID/International Code.

*Flag format: PCTF{OBJECTID_YEAR-MONTH-DAY} *

For example, for a piece of debris from the Falcon 9, the flag would look like this: PCTF{2023-028BG_2023-3-15}

Author: necktie5740
## **Writeup**
Using the given information, I google it and get the name of the poor satellite:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/6feaebcc-8461-45f2-9644-c2dda698cbec)

I google for the COSPAR ID of this too:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/5e175aa4-4472-42cf-8177-422317ee0ae2)

After searching through many pages using its COSPAR ID, I find this page is kinda helpful:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/247a56d7-9636-4a58-82a7-fa6f15698b0f)

But this page only displays information of only a debris, so I change the COSPAR ID and find in this page:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/13ecf76a-4298-4dc4-a0f2-1755bd44841c)

There is a really long list, so I pick some decay date and using `Ctrl + F` to find the latest date and I find it:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/1351879f-0314-414f-9293-fed30314c5d8)


Flag: `PCTF{1979-017AN_2002-12-06}`

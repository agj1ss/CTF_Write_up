# **UH OH!**
## **Challenge**
Uh Oh! While trying to add passwords to my wordlist, I accidentally added my own phone number! Can you tell me what line it's on?

https://en.wikipedia.org/wiki/North_American_Numbering_Plan#Modern_plan

Make sure the phone number follows this format: (NPA) XXX-XXXX

For example (123) 456-7890

Flag format: PCTF{linenumber_phonenumonlynumbers}

Author: @angr404
## **Writeup**
The challenge give me `rockyou.txt` file it looks like a normal `rockyou`, which is kinda large so I wrote a Python script to find it using the NANP format in the above link:

```console
agj1ss@agj1ss:/Desktop$ python3 get_pnumber.py
Line 7731484: (404) 303-7283
```

Flag: `PCTF{7731484_4043037283}`

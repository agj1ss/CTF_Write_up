# **KARTER**
## **Challenge**
In 2021, Flipkart added a new director. Your task is to find:

1. his last name (UPPERCASE)
2. his Director Identification Number
3. And the URL of the primary source from where you found his name (URL format: scheme://subdomain.rootdomain.tld) paths excluded
Flag Format: PCTF{LASTNAME_IdentificationNumber_URL}

Example: PCTF{SMITH_123456_https://www.google.com}

Author: @sau_12
## **Writeup**
With the help of Google, I know that Flipkart is a company from India:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/6f177857-7131-4fa4-8192-a49213b759d7)

And with the given information, I think I need to find the primary source first, so I google it:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/d3f2fc8a-3628-4b3c-ad44-4c623045c7d8)

So we have the primary source is `https://www.mca.gov.in`, so now I need to find Director's name. Go to Flipkart homepage, I find this:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/3f0fd816-6a01-452c-b5cd-ed13fbccb720)

Using this information to find in the primary source, I find it CIN code:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/ab2b7c7f-eb6e-461e-a1d4-d7d03baa2130)

I google again and find Director's name:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/ef38a1e0-cd44-4711-9ef5-e6a97ad3b425)

Now all I need is his DIN:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/005552d2-c7a4-4743-b2a0-88a335eefd2f)


Flag: `PCTF{COLLINS_09075331_https://www.mca.gov.in}`

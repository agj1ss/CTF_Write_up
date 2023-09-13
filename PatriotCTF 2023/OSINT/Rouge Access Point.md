# **ROUGE ACCESS POINT**
## **Challenge**
We've received a notice from our companies EDR software that a laptop was attacked while they were on WFH. The employee says they were at home when it happened, but we suspect they were using public wifi. Our EDR software managed to capture the BSSID of the wifi (46:D1:FA:63:BC:66) network before it got disconnected, but not the SSID. Can you still find the network they were connected to?

Flag format: PCTF{SSID}

Author: @meatball5201
## **Writeup**
With the given BSSID, all I can think about is `WiGLE`. WiGLE (or Wireless Geographic Logging Engine) is a website for collecting information about the different wireless hotspots around the world. Users can register on the website and upload hotspot data like GPS coordinates, SSID, MAC address and the encryption type used on the hotspots discovered. In addition, cell tower data is uploaded and displayed.

Login to WiGLE.net and go to Network Search -> WiFi/Cell Detail:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/4d3c7a32-8f6d-435d-8a3a-182cc7f2e95a)

Querying with the given BSSID and get the SSID of that router:
![image](https://github.com/agj1ss/CTF_Write_up/assets/108376735/8feb926f-8b75-448a-9d7a-d5c1b869bd0c)


Flag: `PCTF{Red's Table Free Wifi}`

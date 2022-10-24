# Get-Domain-All-Information-Using-Python
Get Domain All Information Using Python

## Before Run this code install :
```
pip install python-whois
```

## Run this code
```
import whois
domain = input("Please, Enter Your Domain Name: ")
domainInfo = whois.whois(domain)
for key, value in domainInfo.items():
    print(key, ':', value)
```

## Code. 
![Code](https://github.com/NowshadRuhan/Get-Domain-All-Information-Using-Python/blob/main/photos.png?raw=true) 

import whois
domain = input("Please, Enter Your Domain Name: ")
domainInfo = whois.whois(domain)
for key, value in domainInfo.items():
    print(key, ':', value)
import whois
 
# w = whois.whois('google.com')

data = input("Enter a domain: ")
w = whois.whois(data)
print (w)
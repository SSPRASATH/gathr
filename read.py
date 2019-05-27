import nltk
import re
import socket

    
def input_drive(inp):
    #find the domain name
    ValidIpAddressRegex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
    domain_name= inp.split('.')
    print(domain_name)
    if(len(domain_name) >= 2):
        if(len(domain_name) == 3):
            if((domain_name[0] == 'www') or (domain_name[0] == 'https://www') or (domain_name[0] == 'http://www') or (domain_name[0] == 'https://') or (domain_name[0] == 'http://')):
                domain_name_ip1= 'www.'+domain_name[1]+'.'+domain_name[2]
                domain_name_ip2= 'www.'+domain_name[1]+'.'+domain_name[2]
                dip1= re.search(ValidIpAddressRegex,socket.gethostbyname(domain_name_ip1))
                dip2= re.search(ValidIpAddressRegex,socket.gethostbyname(domain_name_ip2))
                print(dip1)
                print("its the website")
        else:
                print("its the 2 website")
                dip= socket.gethostbyname(inp)
                print(dip)
    #tokenizer
    nltk_tokens = nltk.word_tokenize(inp)
    print(nltk_tokens)
    #email finder
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", inp)
    print(emails)
    #urlfinder
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', inp)
    print(urls)
    #ip address finder
    ValidIpAddressRegex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
    ip=re.search(ValidIpAddressRegex,inp)
    print(ip)
    ValidIpAddressRegex = r"^https?://(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
    ip=re.search(ValidIpAddressRegex,inp)
    print(ip)

if __name__ == "__main__":
    inp=input("enter iput :")
    input_drive(inp)
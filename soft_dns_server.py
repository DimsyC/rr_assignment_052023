import socket
import sys
import tldextract
from validators import url as is_url,ipv4 as is_ipv4, domain as is_domain

class SoftDnsServer:
    def __init__(self, cache=None):
        self.cache = cache or {}

    #https://www.pythonforbeginners.com/code-snippets-source-code/dns-lookup-python
    def dns_lookup(self, hostname):
        try:
            ip_address = socket.gethostbyname(hostname)
            self.cache[hostname] = ip_address
            return ip_address
        except socket.gaierror:
            raise Exception('Hostname cannot be resolved to an IP address')

    # https://stackoverflow.com/questions/19867548/how-to-perform-a-reverse-dns-lookup-in-python
    def reverse_dns_lookup(self, ip_address):
        try:
            hostname, alias_list, ip_list = socket.gethostbyaddr(ip_address)
            return hostname
        except socket.herror:
            raise Exception('IP address cannot be resolved to a hostname')

    def register(self, domain, ipv4):
        self.cache[domain] = ipv4
        print(f"{domain}:{ipv4} have been cached")

    def ip_to_url(self, ipv4):
        # Check cache first to see if IPv4 address is present and return it if so
        url = next((key for key, value in self.cache.items() if ipv4 == value), None)
        if url is not None:
            return url
        # Else If ipv4 address not in cache perform Reverse DNS lookup
        else:
            return self.reverse_dns_lookup(ipv4)

    def url_to_ip(self, url):
        # Normalize all URLS to a lowercased domain name.
        # reference: https://pypi.org/project/tldextract/
        domain = tldextract.extract(url).registered_domain.lower()
        # Check cache first to see if URL is present and return it if so
        if domain in self.cache:
            return self.cache[domain]
        # Else If URL address not in cache perform DNS lookup
        else:
            return self.dns_lookup(domain)

    def resolve(self, input):
        if is_ipv4(input):
            return self.ip_to_url(input)
        elif is_url(input) or is_domain(input):
            return self.url_to_ip(input)


    def run(self):
        while True:
            print("\nSoft DNS Server running...")
            print("1. Register a domain")
            print("2. Resolve a URL or IPv4 address")
            print("3. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                domain = input("Enter the domain: ")
                ip = input("Enter the IP address: ")
                self.register(domain, ip)
            elif choice == "2":
                url_or_ip_input = input("Enter the URL or IP address: ")
                result = self.resolve(url_or_ip_input)
                print(f"{url_or_ip_input} resolves to: {result}")
            elif choice == "3":
                sys.exit("Exiting...")
            else:
                print("Invalid choice. Try again.")




if __name__ == "__main__":
    server = SoftDnsServer()
    try:
        server.run()
    except KeyboardInterrupt:
        sys.exit(0)

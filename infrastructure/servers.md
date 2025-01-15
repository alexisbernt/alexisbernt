# Servers

## DNS Server
Def DNS Server: The Domain Name System (DNS) Server is a server that is specifically used for matching website hostnames (like lexiscyberclub.com) to their corresponding Internet Protocol or IP addresses. 
The DNS server contains a database of public IP addresses and their corresponding domain names.

Maps human readable host names to the IP Address that hosts that site. 

DNS Recursive Resolver - makes multiple requests to other servers. Starts with the root name server.
Root server will respond with the address of a top level domain DNS server which stores data about top level domains (like .com or .io or .site).
The resolver (Recursive Resolver) then makes a request to the TLD Server which will respond with the IP Address of the Authoritative name server. This will contain the requested website's IP address. 
The IP address gets sent to the client and cached (in computer memory) for future use. 

When you have a domain name it is handled by a registrar. 
Record of registration for the domain name is handled by a registry operator who stores your DNS settings and propogates them to other DNS servers around the world. 
Registrants have zone files to configure domain settings. 
The A record is important.

Def 'A' File: Means address and maps a domain or subdomain to the IP address of its host. 

Def 'CNAME': Known as a canonical name which is for forwarding a domain to another domain on the internet (instead of using an IP address).

Def 'MX' Record: For email.

Def 'TXT' Record: For storing arbitrary (exsisting) data with text record to communicate with parties to verify ownership of the domain.

Def 'NS' Record: Internet can ping to find our IP address. 

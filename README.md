# Assignment submission
## Detailed instructions on how to run your assignment
Navigate to the directory where you have cloned or downloaded the repository:
1. Create a new virtual environment :  
`python -m venv rr_assignment_env`
2. Activate the new virtual environment :  
`rr_assignment_env\Scripts\activate` #Windows OS  
`source rr_assignment_env/bin/activate` #LinuxOS  
3. Install the necessary dependencies from the requirements.txt file:  
`pip install -r requirements.txt`  
4. Run Server or Tests  
`python main.py`  # Run Server  
`python test_soft_dns_server.py` # Run Tests

## Justification of selected approach
Upon reading the brief and  task requirements,I decided to brush up on my DNS knowledge and read through https://www.cloudflare.com/learning/dns/what-is-dns/.  

Initially, I wanted to develop a recursive DNS resolver, but due to the complexity and extensive effort required for handling DNS packets and data parsing, I opted to focus on a more basic solution.

I decided to minimize reliance on external libraries and used only the following:

- `validators` library for efficient validation of domains, URLs, and IPv4 addresses.
- `tldextract` library for effective normalization and extraction of domain names.
- `socket` library to implement DNS lookup and reverse DNS lookup functionalities.  
   These DNS functionalities were inspired by solutions found on Google searches and Stack Overflow.
   

Furthermore, while reading the Cloudflare website, I was reminded of the concept of caching, which inspired me to incorporate a simple cache using a dictionary data structure.  

I followed a Test-Driven Development by writing a test file before development and adjusting it.  

I also utilized an object-oriented approach by designing a class that includes a cache parameter and the necessary methods for the requested features. 

To simulate a running server, I implemented an infinite while loop with basic user input handling to provide an interface for registering domains and resolving URLs or IP addresses.
## Solution limitations 
- The solution is a simplified implementation and does not encompass the full complexity of production-grade DNS servers.
- Reliance on the socket module for DNS lookup may be unreliable in certain environments or with specific DNS configurations.
- There is limited user input validation and error handling, meaning the server is vulnerable.
- The simple in-memory cache used in the solution is lost upon server restart or exit. There is no persistence.
- The solution only supports IPv4 addresses and lacks proper functionality for resolving IPv6 addresses.
- Reverse DNS lookup results may not always provide meaningful or recognizable URLs due to custom DNS configurations.

## Possible improvements
- Support for IPv6
- Persistence
- Better (and more) error handling
- Implementation of propre `A Records` structure and other records (AAAA, CNAME, etc.)

# The Soft-DNS server
## Objective
Your assignment is to implement domain URL to IP resolver service (DNS Server) using Python and no framework.
## Brief
The Domain Name System (DNS) is the phonebook of the Internet. Humans access information online through domain names, like nytimes.com or espn.com. Web browsers interact through Internet Protocol (IP) addresses. DNS translates domain names to IP addresses so browsers can load Internet resources.

Each device connected to the Internet has a unique IP address which other machines use to find the device. DNS servers eliminate the need for humans to memorize IP addresses such as 192.168.1.1 (in IPv4)

## Tasks
Implement assignment using:  
- Language: Python  
- Framework: no framework  

Two features are required:  
- **register** – register domain with IPv4  
- **resolve** – resolve domain-based URL to IPv4 and vice versa  

Provide a markdown file with the following:  
- Detailed instructions on how to run your assignment
- Justification of selected approach
- Solution limitations 
- Possible improvements  

Provide tests for both solutions and their use cases using Python Unit Testing framework (or similar).
## Evaluation Criteria
**Completeness:** Did you complete the features? Are all the tests running?  
**Correctness:** Does the functionality act in sensible, thought-out ways?  
**Maintainability:** Is it written in a clean, maintainable way?  

## Sample domains
| Domain      | URL         | IPv4 | 
| ----------- | ----------- | ---- |
| google.com      | https://www.google.com      |  172.217.1.110    |
| Yahoo.com   | https://www.yahoo.com       |   74.6.231.21  |
| NHL.com   | https://www.nhl.com       |   104.18.17.236   |
| Python.org   | https://www.python.org       |  151.101.193.168   |

# AWS Notes as of 4/12/25

### What does AWS do?
AWS is a cloud computing platform which means it provides servers, storage, networking, remote computing, email, and security.
### What is a cloud computing platform?
Cloud computing is a service that gives you access to computing resources (like storage, processing power, or databases) on demand. This way you just use what you need and pay for that (like electricity or water).
So instead of buying a server to store files or run a website, you use a cloud platform.

### IN AWS:
On the Console Home:

Main thing to use is the EC2. EC2 is like a virtual machine (software version of a computer (for example if you want to run a different OS on your computer) that runs on your actual computer).

Everything goes inside a VPC (Virtual Private Cloud) which handles all your connections and networking. 

#### SSH 
You need a key for the SSH login. SSH stands for Secure Shell. Secure shell is how you remotely access another computer over a network (like the internet). 

An SSH login means you're logging into a remote computer or server using the SSH protocol.

🔒 Why SSH is important:
It encrypts your data so no one can eavesdrop.You can run commands, move files, or even manage servers from anywhere. It's commonly used by developers, sysadmins, and anyone working with cloud servers.

🧠 Real-world example:
Let’s say you’re working on a website hosted on a Linux server in the cloud. You’d open a terminal and type:
in bash:
ssh username@server-address
Boom — you’re now "inside" that server, just like if you were sitting at it.

You get an IP of it essentially and then you get the panel of servers essentially (you get a public IP address as well). 

Look at your Global View which will show where your servers are running. 

You can view all your servers. 

Servers have their own IP addresses!!!!!!

Def IP address = home address for a computer or device on a network. So a server (which is just a powerful computer) needs an IP address so other computers can find it and talk to it.
- For example: when you visit www.google.com, your computer looks up Google’s IP address (like 142.250.190.78), and connects to one of their servers.

DNS provider can help you connect domain name to the IP address.

Then you get a Connect Button which gives you the commands to connect to the instance.

You then have to secure shell into the instance. Then open up command prompt inside of the directory (structure that organizes files and resources on a computer) as the key for access. Then SSH into the server. Update.

Nginx is used for many things (serving web files - like html files). Makes it super easy and fast to set up a website.

AWS can get in-depth. Lots of things that you can do with it. You can quickly spin up an EC2 instance.



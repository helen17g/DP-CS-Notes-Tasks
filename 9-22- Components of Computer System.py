print("""Todays date is 9/22/2022, Components of a Computer System
-- MENU --
''''''''''
Please choose on of the options below, and press enter.
1) Components of a Computer System
2) Next set of terms and concepts:

""")

answer = "empty"

while (answer == "empty"):
  userchoice = input()
  if(userchoice == "1"):
    print("""Components of a Computer System 
    
    We are switching into a new section of the curriculum now. Some of this terminology is probably second nature to you, but you do need to know the terminology. This will include some terminology related to computer hardware, but we'll go into it in more detail in the next unit. 
    
    Terms/Concepts:
Hardware: Hardware consist of the physical parts of the system

Software:

Peripheral Devices: These are hardware devices that are outside the computer processor. Typically connected to the computer by cables. Printer is the obvious example. Hard disk is also a perpheral.
Even if its is in the same box as the computer
This is because it is ouside the thing that does all the work, the processor.
      Input Device
        Allows data to be transmitted to the computer processor
        - E.G, keyboard, mouse, mircophone
      Output Device
       This is a deivce that allows the comouter processor to output information
       - Eg printer, monitor, headphones/speakers
       note vibrations features on a device would be an output device
       Does this mean a vibrating controller is an inout or output device?

      Storage
       This is any piece of hardware which can store data outside the processor in a form which is a suitable for input back into the processor. This is needed as data must be saved for future use if the processor is swithed off. Also for the transfer of data from one machine to another.

Computer Network: A set of computer systems that are interconnected and share resources, as well as data. For example: Local Area Network, Wide Area Network, etc.

Human Resources: people who are part of (or could be part of) an organization, business, or economy.
We'll go a little bit into network related terminology next, but we'll go into in much more detail later.
""")

  elif(userchoice == "2"):
    print("""
Patches: used by software companies to update applications by fixing known bugs and vulnerabilities. Be aware that patches may introduce new bugs.
    
Upgrades: contain a novel function or characteristic, as well as cumulative bug fixes. Upgrades often require an additional purchase.

Updates: improve a product in a minor way, adding some new functionality or fixing a bug. Updates are usually free. Updates may be obtained manually, or may also be automatic through an internet connection.

Releases: final, working versions of software applications. Prior to release, they should undergo alpha and beta testing. A release is a new product, or an upgraded product.
    
Dumb Terminal: a terminal that does not performing local processing of entered information, but serves only as an input/output device for an attached or network-linked processor.

Thin Client: In computer networking, a thin client is a simple computer that has been optimized for establishing a remote connection with a server-based computing environment. They are sometimes known as network computers, or in their simplest form as zero clients.

Client: In computing, a client is a piece of computer hardware or software that accesses a service made available by a server as part of the client–server model of computer networks. The server is often on another computer system, in which case the client accesses the service by way of a network. 

Email Server: An email server, also called a mail server, is essentially a computer system that sends and receives emails. When you send an email, it goes through a series of servers to reach its final destination

Router: A router is a networking device that forwards data packets between computer networks. Routers perform the traffic directing functions on the Internet. Data sent through the internet, such as a web page or email, is in the form of data packets.

DNS Server: The Domain Name System (DNS) Server is a server that is specifically used for matching website hostnames (like example.com)to their corresponding Internet Protocol or IP addresses. The DNS server contains a database of public IP addresses and their corresponding domain names.

Firewall: In computing, a firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. A firewall typically establishes a barrier between a trusted network and an untrusted network, such as the Internet

Client-server: Client-server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients. 
""")
    print("")
    print(""" """)

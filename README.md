# Python Packet Sniffer

## Project Overview

This project is a Python-based packet sniffer developed to capture and analyze network traffic. The purpose of the project is to understand how network packets are transmitted across a network and to examine important information contained within those packets.

The project was completed as part of a cybersecurity practical exercise. It demonstrates the basic process of capturing network packets, identifying their structure, and analyzing information such as source and destination IP addresses, protocols, ports, and packet contents.

## Objectives

The main objectives of this project were to:

* Build a Python program capable of capturing network packets.
* Understand the basic structure of network packets.
* Identify the source and destination IP addresses.
* Identify the protocols used by captured packets.
* Examine TCP and UDP traffic.
* Analyze packet information after capturing network traffic.
* Develop practical experience with network monitoring and packet analysis.
* Understand how packet information can be useful in cybersecurity investigations.

## Tools and Technologies Used

* **Kali Linux** — Operating system used for the cybersecurity practical.
* **Python 3** — Programming language used to develop the packet sniffer.
* **Scapy** — Python library used to capture and inspect network packets.
* **Git/GitHub** — Used to store and document the completed source code.

## How the Packet Sniffer Works

The packet sniffer listens to network traffic on a selected network interface. When packets are detected, the Python program captures them and extracts useful information.

For IP packets, the program can examine information such as:

* Source IP address
* Destination IP address
* Transport protocol
* Source port
* Destination port
* Packet length
* Other packet information provided by Scapy

The basic flow of the program is:

1. Start the Python program.
2. The program begins listening for network packets.
3. Network packets are captured as they pass through the selected interface.
4. The program examines the captured packets.
5. Relevant packet information is displayed.
6. The sniffer is stopped when enough packets have been captured.
7. The captured information is analyzed to understand the traffic.

## Running the Program

First, make sure Python and Scapy are installed.

Scapy can be installed on Kali Linux using:

```bash
sudo apt install python3-scapy
```

Navigate to the project directory:

```bash
cd ~/packet-sniffer
```

Run the program:

```bash
sudo python3 packet_sniffer.py
```

Administrative privileges may be required because packet capture involves access to network interfaces.

To stop the packet capture, press:

```text
Ctrl + C
```

## Packet Capture and Analysis

During testing, the packet sniffer captured different types of network traffic.

Captured packets may use different protocols depending on the network activity taking place. For example, TCP and UDP packets can appear during normal network communication.

### Source and Destination IP Addresses

Each IP packet contains a source and destination IP address.

The source IP represents the device sending the packet, while the destination IP represents the device receiving it.

For example:

```text
Source IP:      192.168.1.10
Destination IP: 142.250.x.x
```

The exact addresses depend on the network traffic generated during testing.

### TCP Traffic

TCP is a connection-oriented protocol. It establishes a connection between devices before transferring data.

TCP is commonly used by services such as:

* HTTPS
* HTTP
* SSH
* FTP

When TCP packets were captured, information such as the source port and destination port could be examined.

### UDP Traffic

UDP is a connectionless transport protocol. Unlike TCP, it does not establish a connection before sending data.

UDP is commonly used for services such as:

* DNS
* DHCP
* Streaming
* Some online games and real-time applications

The presence of UDP packets during testing is normal and depends on the network activity taking place.

## Understanding Packet Structure

A network packet can be thought of as information divided into different layers.

A simplified packet structure is:

```text
Ethernet
   ↓
IP
   ↓
TCP/UDP
   ↓
Application Data
```

### Ethernet Layer

The Ethernet layer contains information used for communication on the local network, including MAC addresses.

### IP Layer

The IP layer contains information used to identify the sending and receiving devices.

Important fields include:

* Source IP
* Destination IP
* Protocol
* TTL
* Packet length

### TCP/UDP Layer

The transport layer provides information about the type of transport protocol being used.

For TCP and UDP traffic, important information can include:

* Source port
* Destination port

### Application Data

Some packets may contain data associated with the application communicating over the network.

The amount and visibility of application data depends on the protocol and whether encryption is being used.

## What I Learned

Through this practical exercise, I learned that network communication is made up of individual packets that contain information about how data is being transferred between devices.

I learned how to:

* Capture network packets using Python.
* Use Scapy for packet analysis.
* Identify source and destination IP addresses.
* Identify different network protocols.
* Understand the difference between TCP and UDP traffic.
* Examine packet fields.
* Analyze captured traffic after stopping the sniffer.
* Understand how packet analysis can support cybersecurity monitoring.

## Cybersecurity Relevance

Packet analysis is an important cybersecurity skill. Security analysts can examine network traffic to identify unusual or potentially suspicious communication.

Packet information can help analysts investigate:

* Unexpected connections
* Suspicious IP addresses
* Unusual ports
* Unexpected protocols
* Communication between systems
* Possible reconnaissance activity
* Indicators of compromise

However, packet information should always be interpreted in context. A packet using a particular protocol or port is not automatically malicious.

## Ethical Considerations

This packet sniffer should only be used on networks and systems where the user has permission to monitor traffic.

Capturing network traffic without authorization can expose sensitive information and may violate privacy laws, organizational policies, or acceptable-use rules.

Testing was therefore performed in a controlled environment for educational and cybersecurity learning purposes.

## Conclusion

The Python packet sniffer provided practical experience with network traffic capture and packet analysis. By examining packets and their fields, I developed a better understanding of how devices communicate across networks.

The project also demonstrated how Python and Scapy can be used as basic cybersecurity tools for network monitoring and investigation.

This practical exercise provides a foundation for more advanced topics such as intrusion detection, network forensics, Security Operations Center (SOC) monitoring, and automated network traffic analysis.

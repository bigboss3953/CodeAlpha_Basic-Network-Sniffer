from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime


def analyze_packet(packet):

    if IP not in packet:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    source = packet[IP].src
    destination = packet[IP].dst
    protocol = packet[IP].proto
    size = len(packet)

    print("\n" + "=" * 65)
    print("NETWORK PACKET")
    print("=" * 65)

    print(f"Time            : {timestamp}")
    print(f"Source IP       : {source}")
    print(f"Destination IP  : {destination}")
    print(f"Packet Size     : {size} bytes")

    if TCP in packet:
        print("Protocol        : TCP")
        print(f"Source Port     : {packet[TCP].sport}")
        print(f"Destination Port: {packet[TCP].dport}")

    elif UDP in packet:
        print("Protocol        : UDP")
        print(f"Source Port     : {packet[UDP].sport}")
        print(f"Destination Port: {packet[UDP].dport}")

    elif ICMP in packet:
        print("Protocol        : ICMP")

    else:
        print(f"Protocol Number : {protocol}")

    if Raw in packet:
        payload = packet[Raw].load

        print(f"Payload Length  : {len(payload)} bytes")
        print(f"Payload         : {payload[:100]}")

    print("=" * 65)


print("""
=========================================
          BASIC NETWORK SNIFFER
=========================================
Capturing network packets...
Press CTRL+C to stop.
""")

try:
    sniff(
        prn=analyze_packet,
        store=False
    )

except KeyboardInterrupt:
    print("\n\nPacket capture stopped.")

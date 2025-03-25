from scapy.all import sniff
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP

# Sets to store unique MAC and IP addresses
seen_macs = set()
seen_ips = set()

def packet_callback(packet):
    # Process Ethernet layer
    if packet.haslayer(Ether):
        src_mac = packet[Ether].src
        dst_mac = packet[Ether].dst

        if src_mac not in seen_macs:
            seen_macs.add(src_mac)
            print(f"Detected Source MAC: {src_mac}")

        if dst_mac not in seen_macs:
            seen_macs.add(dst_mac)
            print(f"Detected Destination MAC: {dst_mac}")

    # Process IP layer
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if src_ip not in seen_ips:
            seen_ips.add(src_ip)
            print(f"Detected Source IP: {src_ip}")

        if dst_ip not in seen_ips:
            seen_ips.add(dst_ip)
            print(f"Detected Destination IP: {dst_ip}")

# Start sniffing packets (change 'iface' to your network interface if needed)
print("Listening for MAC and IP addresses...")
sniff(prn=packet_callback, store=False)

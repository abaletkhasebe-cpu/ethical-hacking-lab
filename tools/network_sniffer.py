#!/usr/bin/env python3
"""
Network Packet Sniffer Tool
For authorized network analysis only - requires root/admin privileges
"""

import sys
import struct
import textwrap

class PacketSniffer:
    def __init__(self):
        self.packet_count = 0
        self.protocol_map = {
            1: 'ICMP',
            6: 'TCP',
            17: 'UDP'
        }

    def format_multi_line(self, *, bytes_data, name='', num_per_line=16):
        """
        Format data for printing
        """
        size = len(bytes_data)
        if size == 0:
            return name
        
        first_line = f'{name}:'
        subsequent_lines = []
        
        for i in range(0, size, num_per_line):
            chunk = bytes_data[i:i + num_per_line]
            hex_part = ' '.join(f'{b:02x}' for b in chunk)
            ascii_part = ''.join(f'{chr(b):>3}' if 32 <= b < 127 else ' . ' for b in chunk)
            subsequent_lines.append(f'  {hex_part:<{num_per_line*3}}  {ascii_part}')
        
        return first_line + '\n' + '\n'.join(subsequent_lines)

    def parse_ipv4_packet(self, data):
        """
        Parse IPv4 packet
        """
        version_header_length = data[0]
        version = version_header_length >> 4
        header_length = (version_header_length & 15) * 4
        ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
        return self.format_ipv4(src, target), proto, ttl

    def format_ipv4(self, bytes_addr):
        """
        Format IPv4 address
        """
        bytes_iter = iter(bytes_addr)
        return '.'.join(map(lambda b: str(b), bytes_iter))

    def parse_tcp_segment(self, data):
        """
        Parse TCP segment
        """
        src_port, dest_port, sequence, acknowledgment, offset_reserved_flags = struct.unpack('! H H L L H', data[:14])
        offset = (offset_reserved_flags >> 12) * 4
        flag_urg = (offset_reserved_flags & 32) >> 5
        flag_ack = (offset_reserved_flags & 16) >> 4
        flag_psh = (offset_reserved_flags & 8) >> 3
        flag_rst = (offset_reserved_flags & 4) >> 2
        flag_syn = (offset_reserved_flags & 2) >> 1
        flag_fin = offset_reserved_flags & 1
        
        return src_port, dest_port, sequence, acknowledgment, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin

    def format_tcp_segment(self, src_port, dest_port, sequence, acknowledgment, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin):
        """
        Format TCP segment info
        """
        flags = ''
        if flag_syn:
            flags += 'SYN '
        if flag_ack:
            flags += 'ACK '
        if flag_fin:
            flags += 'FIN '
        if flag_rst:
            flags += 'RST '
        if flag_psh:
            flags += 'PSH '
        if flag_urg:
            flags += 'URG '
        
        return f'TCP Segment:\n  Src Port: {src_port}, Dest Port: {dest_port}\n  Sequence: {sequence}, Acknowledgment: {acknowledgment}\n  Flags: {flags}'

    def parse_udp_segment(self, data):
        """
        Parse UDP segment
        """
        src_port, dest_port, size = struct.unpack('! H H 2x H', data[:8])
        return src_port, dest_port, size

    def format_udp_segment(self, src_port, dest_port, size):
        """
        Format UDP segment info
        """
        return f'UDP Segment:\n  Src Port: {src_port}, Dest Port: {dest_port}, Size: {size}'

    def demo_sniffer(self):
        """
        Demonstrate packet sniffing (simulated packets)
        """
        print("\n📡 Network Packet Sniffer (DEMO MODE)")
        print("="*60)
        print("Note: Actual sniffing requires root/admin privileges")
        print("="*60)
        
        # Simulate captured packets
        demo_packets = [
            {
                'src_ip': '192.168.1.100',
                'dest_ip': '192.168.1.1',
                'protocol': 'TCP',
                'src_port': 54321,
                'dest_port': 80,
                'flags': 'SYN',
                'length': 60
            },
            {
                'src_ip': '192.168.1.1',
                'dest_ip': '192.168.1.100',
                'protocol': 'TCP',
                'src_port': 80,
                'dest_port': 54321,
                'flags': 'SYN-ACK',
                'length': 60
            },
            {
                'src_ip': '8.8.8.8',
                'dest_ip': '192.168.1.100',
                'protocol': 'UDP',
                'src_port': 53,
                'dest_port': 53232,
                'flags': 'N/A',
                'length': 512
            }
        ]
        
        print(f"\n🔍 Captured {len(demo_packets)} Simulated Packets\n")
        
        for i, packet in enumerate(demo_packets, 1):
            print(f"\nPacket #{i}")
            print("-" * 60)
            print(f"Source IP:      {packet['src_ip']}")
            print(f"Destination IP: {packet['dest_ip']}")
            print(f"Protocol:       {packet['protocol']}")
            print(f"Src Port:       {packet['src_port']}")
            print(f"Dest Port:      {packet['dest_port']}")
            print(f"Flags:          {packet['flags']}")
            print(f"Length:         {packet['length']} bytes")
        
        print("\n" + "="*60)
        print("✅ Packet capture simulation complete")

def main():
    print("\n" + "="*60)
    print("🛡️  Network Packet Sniffer Tool")
    print("For Authorized Network Analysis Only")
    print("="*60)
    
    sniffer = PacketSniffer()
    
    if len(sys.argv) > 1:
        interface = sys.argv[1]
        print(f"\nStarting packet capture on interface: {interface}")
        print("(This requires administrator/root privileges)")
        print("\nNote: For demo purposes, showing simulated output\n")
        sniffer.demo_sniffer()
    else:
        sniffer.demo_sniffer()
        print("\n💡 USAGE: python3 network_sniffer.py [interface]")
        print("Example: python3 network_sniffer.py eth0")
        print("\nNote: Requires root/administrator privileges!")

if __name__ == "__main__":
    main()

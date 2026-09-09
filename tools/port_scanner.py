#!/usr/bin/env python3
"""
Network Port Scanner Tool
For authorized network reconnaissance only
"""

import socket
import sys
import threading
from datetime import datetime

class PortScanner:
    def __init__(self, target, timeout=2):
        self.target = target
        self.timeout = timeout
        self.open_ports = []
        self.common_ports = {
            21: 'FTP',
            22: 'SSH',
            23: 'Telnet',
            25: 'SMTP',
            53: 'DNS',
            80: 'HTTP',
            110: 'POP3',
            143: 'IMAP',
            443: 'HTTPS',
            465: 'SMTP-SSL',
            587: 'SMTP-TLS',
            993: 'IMAP-SSL',
            995: 'POP3-SSL',
            3306: 'MySQL',
            5432: 'PostgreSQL',
            6379: 'Redis',
            27017: 'MongoDB',
            3389: 'RDP',
            8080: 'HTTP-Alt'
        }

    def scan_port(self, port):
        """
        Scan a single port
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))
            sock.close()
            
            if result == 0:
                service = self.common_ports.get(port, 'Unknown')
                self.open_ports.append((port, service))
                print(f"✅ Port {port:5d} - OPEN ({service})")
            else:
                print(f"❌ Port {port:5d} - CLOSED")
        except socket.gaierror:
            print(f"❌ Hostname {self.target} could not be resolved")
        except socket.error:
            print(f"❌ Could not connect to {self.target}")

    def scan_common_ports(self):
        """
        Scan the most common ports
        """
        print(f"\n🔍 Scanning Common Ports on {self.target}")
        print(f"Started: {datetime.now()}")
        print("-" * 50)
        
        for port in sorted(self.common_ports.keys()):
            self.scan_port(port)
        
        self.print_summary()

    def scan_range(self, start_port, end_port):
        """
        Scan a range of ports
        """
        print(f"\n🔍 Scanning Ports {start_port}-{end_port} on {self.target}")
        print(f"Started: {datetime.now()}")
        print("-" * 50)
        
        threads = []
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=self.scan_port, args=(port,))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        self.print_summary()

    def print_summary(self):
        """
        Print scan summary
        """
        print("\n" + "="*50)
        print("📊 SCAN SUMMARY")
        print("="*50)
        print(f"Target: {self.target}")
        print(f"Open Ports: {len(self.open_ports)}")
        
        if self.open_ports:
            print("\nOpen Services:")
            for port, service in sorted(self.open_ports):
                print(f"  - Port {port}: {service}")
        else:
            print("\nNo open ports found")
        
        print(f"Completed: {datetime.now()}")

def main():
    print("\n" + "="*50)
    print("🔎 Network Port Scanner")
    print("For Authorized Network Reconnaissance Only")
    print("="*50)
    
    if len(sys.argv) < 2:
        print("\n📌 DEMO MODE - Scanning localhost")
        target = 'localhost'
        scanner = PortScanner(target)
        scanner.scan_common_ports()
        
        print("\n💡 USAGE: python3 port_scanner.py <target> [start_port] [end_port]")
        print("Examples:")
        print("  python3 port_scanner.py example.com")
        print("  python3 port_scanner.py example.com 1 1000")
    else:
        target = sys.argv[1]
        
        if len(sys.argv) == 4:
            start_port = int(sys.argv[2])
            end_port = int(sys.argv[3])
            scanner = PortScanner(target)
            scanner.scan_range(start_port, end_port)
        else:
            scanner = PortScanner(target)
            scanner.scan_common_ports()

if __name__ == "__main__":
    main()

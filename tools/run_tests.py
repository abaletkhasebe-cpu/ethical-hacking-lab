#!/usr/bin/env python3
"""
Integrated Security Testing Framework
Run all security tools in one place
"""

import sys
import os
import subprocess
from datetime import datetime

class SecurityTestingFramework:
    def __init__(self):
        self.tools_dir = os.path.dirname(os.path.abspath(__file__))
        self.results = []
        self.tools = {
            '1': {'name': 'SQL Injection Tool', 'file': 'sql_injection_tool.py'},
            '2': {'name': 'Password Cracker', 'file': 'password_cracker.py'},
            '3': {'name': 'Port Scanner', 'file': 'port_scanner.py'},
            '4': {'name': 'Network Sniffer', 'file': 'network_sniffer.py'},
            '5': {'name': 'Web Vulnerability Scanner', 'file': 'web_scanner.py'},
            '6': {'name': 'JWT Security Analyzer', 'file': 'jwt_analyzer.py'},
            '7': {'name': 'Credential Tester', 'file': 'credential_tester.py'},
        }

    def display_menu(self):
        """
        Display main menu
        """
        print("\n" + "="*70)
        print("🔒 ETHICAL HACKING LAB - Security Testing Framework")
        print("="*70)
        print("\n💻 Available Tools:\n")
        
        for key, tool in self.tools.items():
            print(f"  [{key}] {tool['name']}")
        
        print(f"  [8] Run All Tools (Demo)")
        print(f"  [9] View Reports")
        print(f"  [0] Exit")
        print("\n" + "-"*70)

    def run_tool(self, tool_key, *args):
        """
        Run a specific tool
        """
        if tool_key not in self.tools:
            print(f"\n❌ Invalid tool selection")
            return
        
        tool = self.tools[tool_key]
        tool_path = os.path.join(self.tools_dir, tool['file'])
        
        print(f"\n🚀 Starting: {tool['name']}")
        print("-" * 70)
        
        try:
            cmd = ['python3', tool_path] + list(args)
            subprocess.run(cmd, check=True)
            self.results.append({
                'tool': tool['name'],
                'status': 'SUCCESS',
                'timestamp': datetime.now()
            })
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Error running tool: {e}")
            self.results.append({
                'tool': tool['name'],
                'status': 'FAILED',
                'timestamp': datetime.now()
            })
        except FileNotFoundError:
            print(f"\n❌ Tool file not found: {tool_path}")
            print(f"Make sure you're in the tools directory")

    def run_all_demos(self):
        """
        Run all tools in demo mode
        """
        print("\n🚀 Running all tools in DEMO mode...\n")
        
        for key in sorted(self.tools.keys()):
            print(f"\n{'='*70}")
            self.run_tool(key)
            print(f"{'='*70}")

    def show_reports(self):
        """
        Display test results
        """
        if not self.results:
            print("\n⚠️  No test results yet")
            return
        
        print("\n" + "="*70)
        print("📊 TEST RESULTS REPORT")
        print("="*70)
        
        for result in self.results:
            status_icon = "✅" if result['status'] == 'SUCCESS' else "❌"
            print(f"{status_icon} {result['tool']}: {result['status']} at {result['timestamp'].strftime('%H:%M:%S')}")
        
        successful = len([r for r in self.results if r['status'] == 'SUCCESS'])
        total = len(self.results)
        print(f"\nSummary: {successful}/{total} tools executed successfully")

    def interactive_mode(self):
        """
        Interactive tool selection
        """
        while True:
            self.display_menu()
            choice = input("\n👉 Select option: ").strip()
            
            if choice == '0':
                print("\n👋 Exiting... Goodbye!\n")
                break
            elif choice == '8':
                self.run_all_demos()
            elif choice == '9':
                self.show_reports()
            elif choice in self.tools:
                args = input("Enter arguments (optional): ").strip().split()
                self.run_tool(choice, *args)
            else:
                print("\n❌ Invalid selection. Please try again.")

def main():
    framework = SecurityTestingFramework()
    
    if len(sys.argv) > 1:
        # Command-line mode
        tool_key = sys.argv[1]
        args = sys.argv[2:]
        framework.run_tool(tool_key, *args)
    else:
        # Interactive mode
        framework.interactive_mode()

if __name__ == "__main__":
    main()

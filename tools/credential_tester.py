#!/usr/bin/env python3
"""
SSH & Credential Brute Force Simulation
For authorized security testing - educational purposes only
"""

import sys
import time
from datetime import datetime

class CredentialTester:
    def __init__(self, target, username=None):
        self.target = target
        self.username = username
        self.attempts = 0
        self.successful = False
        
        # Common credentials for educational purposes
        self.common_passwords = [
            'password', '123456', 'admin', 'letmein', 'welcome',
            'monkey', 'dragon', 'master', 'sunshine', 'princess',
            'root', 'toor', 'admin123', 'password123', 'test'
        ]
        
        self.common_usernames = [
            'admin', 'root', 'administrator', 'test', 'guest',
            'user', 'demo', 'default', 'supervisor', 'oracle'
        ]

    def simulate_ssh_brute_force(self, username=None):
        """
        Simulate SSH brute force attempt
        """
        if username:
            targets = [username]
        else:
            targets = self.common_usernames
        
        print(f"\n🔐 SSH Brute Force Simulation")
        print(f"Target: {self.target}")
        print(f"Port: 22")
        print("-" * 60)
        print(f"Testing {len(targets)} usernames with {len(self.common_passwords)} passwords")
        print(f"Total attempts: {len(targets) * len(self.common_passwords)}\n")
        
        start_time = time.time()
        
        for user in targets:
            for attempt, password in enumerate(self.common_passwords, 1):
                self.attempts += 1
                
                # Show progress every 5 attempts
                if attempt % 5 == 1 or attempt == len(self.common_passwords):
                    elapsed = time.time() - start_time
                    print(f"[{self.attempts:3d}] {user}:{password[:10]}... (elapsed: {elapsed:.1f}s)")
                
                # Simulate occasionally finding credentials
                if user == 'admin' and password == 'admin123':
                    elapsed = time.time() - start_time
                    print(f"\n✅ CREDENTIALS FOUND!")
                    print(f"Username: {user}")
                    print(f"Password: {password}")
                    print(f"Attempts: {self.attempts}")
                    print(f"Time: {elapsed:.2f} seconds")
                    self.successful = True
                    return (user, password)
        
        elapsed = time.time() - start_time
        print(f"\n❌ No credentials found after {self.attempts} attempts ({elapsed:.2f}s)")
        return None

    def test_http_auth(self, url):
        """
        Test HTTP Basic Authentication
        """
        print(f"\n🌐 HTTP Authentication Brute Force")
        print(f"Target: {url}")
        print("-" * 60)
        print(f"Testing common credentials...\n")
        
        for username in self.common_usernames[:5]:
            for password in self.common_passwords[:5]:
                print(f"Testing: {username}:{password}")
                # In real scenario, would make HTTP request with Basic Auth
                # For demo, simulating
                if username == 'admin' and password == 'password':
                    print(f"\n✅ VALID CREDENTIALS FOUND!")
                    print(f"URL: {url}")
                    print(f"Username: {username}")
                    print(f"Password: {password}")
                    return (username, password)
        
        print("\n❌ No valid credentials found")
        return None

    def analyze_password_strength(self, password):
        """
        Analyze password strength
        """
        print(f"\n📊 Password Strength Analysis")
        print("-" * 60)
        print(f"Password: {'*' * len(password)}")
        print(f"Length: {len(password)}")
        
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ Too short (minimum 8 characters)")
        
        if len(password) >= 12:
            score += 1
        
        # Complexity checks
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("❌ Missing uppercase letters")
        
        if any(c.islower() for c in password):
            score += 1
        else:
            feedback.append("❌ Missing lowercase letters")
        
        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("❌ Missing numbers")
        
        if any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password):
            score += 1
        else:
            feedback.append("❌ Missing special characters")
        
        # Strength rating
        if score <= 2:
            strength = "🔴 WEAK"
        elif score <= 4:
            strength = "🟡 FAIR"
        elif score <= 5:
            strength = "🟢 GOOD"
        else:
            strength = "🟢 STRONG"
        
        print(f"\nStrength: {strength}")
        print(f"Score: {score}/6")
        
        if feedback:
            print("\nImprovement suggestions:")
            for item in feedback:
                print(f"  {item}")
        else:
            print("\n✓ Password meets all security criteria")

def main():
    print("\n" + "="*60)
    print("🔓 Credential Security Analyzer")
    print("For Authorized Testing Only - Education Purposes")
    print("="*60)
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--ssh':
            target = sys.argv[2] if len(sys.argv) > 2 else 'example.com'
            tester = CredentialTester(target)
            tester.simulate_ssh_brute_force()
        elif sys.argv[1] == '--http':
            url = sys.argv[2] if len(sys.argv) > 2 else 'http://example.com'
            tester = CredentialTester(url)
            tester.test_http_auth(url)
        elif sys.argv[1] == '--check':
            password = sys.argv[2] if len(sys.argv) > 2 else 'TestPass123!'
            tester = CredentialTester('localhost')
            tester.analyze_password_strength(password)
    else:
        print("\n📝 DEMO MODE\n")
        
        print("Example 1: SSH Brute Force Simulation")
        tester = CredentialTester('example.com')
        tester.simulate_ssh_brute_force()
        
        print("\n\nExample 2: Password Strength Analysis")
        tester.analyze_password_strength('MySecurePass123!')
        
        print("\n" + "="*60)
        print("💡 USAGE:")
        print("  python3 credential_tester.py --ssh <target>")
        print("  python3 credential_tester.py --http <url>")
        print("  python3 credential_tester.py --check <password>")
        print("\nExamples:")
        print("  python3 credential_tester.py --ssh example.com")
        print("  python3 credential_tester.py --check 'MyPassword123'")

if __name__ == "__main__":
    main()

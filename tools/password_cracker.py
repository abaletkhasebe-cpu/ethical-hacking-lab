#!/usr/bin/env python3
"""
Password Cracker & Hash Analysis Tool
For authorized testing and educational purposes only
"""

import hashlib
import time
import sys
from datetime import datetime

class PasswordCracker:
    def __init__(self):
        # Common password wordlist for demo
        self.wordlist = [
            'password', '123456', 'admin', 'letmein', 'welcome',
            'monkey', 'dragon', 'master', 'sunshine', 'princess',
            'qwerty', 'hello', 'password123', 'admin123', '12345678',
            'test', 'user', 'guest', 'root', 'toor',
            'hello123', 'password1', 'admin1', 'test123', 'demo'
        ]

    def crack_md5(self, hash_value):
        """
        Attempt to crack MD5 hash using dictionary attack
        """
        print(f"\n🔓 MD5 Hash Cracking")
        print("-" * 50)
        print(f"Target Hash: {hash_value}")
        print(f"Wordlist size: {len(self.wordlist)} words")
        print("Attempting crack...\n")
        
        start_time = time.time()
        
        for i, word in enumerate(self.wordlist, 1):
            # Hash the word
            md5_hash = hashlib.md5(word.encode()).hexdigest()
            
            # Show progress
            if i % 5 == 0 or i == 1:
                print(f"[{i}/{len(self.wordlist)}] Testing: {word} -> {md5_hash[:16]}...")
            
            # Check if match
            if md5_hash == hash_value.lower():
                elapsed = time.time() - start_time
                print(f"\n✅ MATCH FOUND!")
                print(f"Password: {word}")
                print(f"Time taken: {elapsed:.2f} seconds")
                return word
        
        elapsed = time.time() - start_time
        print(f"\n❌ No match found in {elapsed:.2f} seconds")
        return None

    def crack_sha1(self, hash_value):
        """
        Attempt to crack SHA1 hash
        """
        print(f"\n🔓 SHA1 Hash Cracking")
        print("-" * 50)
        print(f"Target Hash: {hash_value}")
        print(f"Wordlist size: {len(self.wordlist)} words")
        print("Attempting crack...\n")
        
        start_time = time.time()
        
        for i, word in enumerate(self.wordlist, 1):
            sha1_hash = hashlib.sha1(word.encode()).hexdigest()
            
            if i % 5 == 0:
                print(f"[{i}/{len(self.wordlist)}] Testing: {word} -> {sha1_hash[:16]}...")
            
            if sha1_hash == hash_value.lower():
                elapsed = time.time() - start_time
                print(f"\n✅ MATCH FOUND!")
                print(f"Password: {word}")
                print(f"Time taken: {elapsed:.2f} seconds")
                return word
        
        elapsed = time.time() - start_time
        print(f"\n❌ No match found in {elapsed:.2f} seconds")
        return None

    def analyze_hash(self, hash_value):
        """
        Analyze hash to determine type
        """
        hash_len = len(hash_value)
        
        if hash_len == 32:
            return "MD5"
        elif hash_len == 40:
            return "SHA1"
        elif hash_len == 64:
            return "SHA256"
        elif hash_len == 128:
            return "SHA512"
        else:
            return "UNKNOWN"

    def generate_hashes(self, password):
        """
        Generate different hash types for a password
        """
        print(f"\n🔐 Hash Generation")
        print("-" * 50)
        print(f"Password: {password}")
        print(f"Generated at: {datetime.now()}\n")
        
        print(f"MD5:     {hashlib.md5(password.encode()).hexdigest()}")
        print(f"SHA1:    {hashlib.sha1(password.encode()).hexdigest()}")
        print(f"SHA256:  {hashlib.sha256(password.encode()).hexdigest()}")
        print(f"SHA512:  {hashlib.sha512(password.encode()).hexdigest()}")

def main():
    print("\n" + "="*50)
    print("🔐 Password Cracker & Hash Analysis Tool")
    print("For Educational & Authorized Testing Only")
    print("="*50)
    
    cracker = PasswordCracker()
    
    if len(sys.argv) > 1:
        hash_value = sys.argv[1]
        hash_type = cracker.analyze_hash(hash_value)
        
        print(f"\nDetected hash type: {hash_type}")
        
        if hash_type == "MD5":
            cracker.crack_md5(hash_value)
        elif hash_type == "SHA1":
            cracker.crack_sha1(hash_value)
        else:
            print(f"Hash type '{hash_type}' not yet supported")
    else:
        # Demo mode
        print("\n📌 DEMO MODE\n")
        
        print("Example 1: Generate hashes for password 'hello'")
        cracker.generate_hashes('hello')
        
        print("\n\nExample 2: Crack MD5 hash")
        md5_hash = hashlib.md5('password'.encode()).hexdigest()
        print(f"MD5 Hash: {md5_hash}")
        cracker.crack_md5(md5_hash)
        
        print("\n💡 USAGE: python3 password_cracker.py <hash>")
        print(f"Example: python3 password_cracker.py '{md5_hash}'")

if __name__ == "__main__":
    main()

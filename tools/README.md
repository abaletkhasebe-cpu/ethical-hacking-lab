# Ethical Hacking Tools

This directory contains Python-based security and penetration testing tools for **authorized testing and educational purposes only**.

## Tools Included

### 1. SQL Injection Tool (`sql_injection_tool.py`)

**Purpose:** Test web applications for SQL injection vulnerabilities

```bash
python3 sql_injection_tool.py
python3 sql_injection_tool.py 'http://example.com/search' 'query'
```

**Features:**
- Multiple SQL injection payloads
- URL parameter testing
- Login form testing
- Vulnerability pattern detection

### 2. Password Cracker (`password_cracker.py`)

**Purpose:** Crack password hashes using dictionary attacks

```bash
python3 password_cracker.py
python3 password_cracker.py '5d41402abc4b2a76b9719d911017c592'
```

**Features:**
- MD5, SHA1, SHA256, SHA512 support
- Automatic hash type detection
- Dictionary attack
- Hash generation for testing

### 3. Port Scanner (`port_scanner.py`)

**Purpose:** Scan target systems for open ports and services

```bash
python3 port_scanner.py localhost
python3 port_scanner.py example.com 1 1000
```

**Features:**
- Common ports scanning
- Custom port range scanning
- Service identification
- Multi-threaded scanning

### 4. Network Sniffer (`network_sniffer.py`)

**Purpose:** Analyze network packets and protocols

```bash
python3 network_sniffer.py
python3 network_sniffer.py eth0
```

**Features:**
- Packet capture and analysis
- IPv4, TCP, UDP parsing
- Protocol identification
- Packet formatting

## Requirements

```bash
pip install -r requirements.txt
```

## ⚠️ Legal & Ethical Guidelines

**These tools are for AUTHORIZED testing ONLY:**

1. ✅ **DO:** Test systems you own or have written permission to test
2. ✅ **DO:** Use in isolated lab environments
3. ✅ **DO:** Document findings responsibly
4. ✅ **DO:** Report vulnerabilities through proper channels

5. ❌ **DON'T:** Test without explicit written authorization
6. ❌ **DON'T:** Use against systems you don't own/permission
7. ❌ **DON'T:** Engage in illegal hacking activities
8. ❌ **DON'T:** Access unauthorized data

**Unauthorized access to computer systems is ILLEGAL and punishable by law.**

## Learning Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [HackerOne](https://www.hackerone.com/)
- [TryHackMe](https://tryhackme.com/)

## Contributing

To add new tools or improve existing ones:
1. Follow the code structure
2. Include proper documentation
3. Add legal disclaimers
4. Test thoroughly
5. Submit a pull request

---

**Remember: With great power comes great responsibility. Use these tools ethically and legally!** 🛡️

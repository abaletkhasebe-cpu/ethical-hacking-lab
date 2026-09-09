# Ethical Hacking Tools - Setup Instructions

## Quick Start

### 1. Install Python Requirements
```bash
pip install -r requirements.txt
```

### 2. Run Individual Tools

#### Web Vulnerability Scanner
```bash
python3 web_scanner.py
python3 web_scanner.py 'https://example.com/page?id=1'
```

#### JWT Security Analyzer
```bash
python3 jwt_analyzer.py
python3 jwt_analyzer.py 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
```

#### Credential Tester
```bash
python3 credential_tester.py --ssh example.com
python3 credential_tester.py --http http://example.com
python3 credential_tester.py --check 'MyPassword123'
```

#### SQL Injection Tool
```bash
python3 sql_injection_tool.py
python3 sql_injection_tool.py 'http://example.com/search' 'query'
```

#### Password Cracker
```bash
python3 password_cracker.py
python3 password_cracker.py '5d41402abc4b2a76b9719d911017c592'
```

#### Port Scanner
```bash
python3 port_scanner.py localhost
python3 port_scanner.py example.com 1 1000
```

#### Network Sniffer
```bash
python3 network_sniffer.py
python3 network_sniffer.py eth0
```

## Tool Descriptions

| Tool | Purpose | Severity |
|------|---------|----------|
| web_scanner.py | Comprehensive web vulnerability scanning | HIGH |
| jwt_analyzer.py | JWT token security analysis | HIGH |
| credential_tester.py | Credential strength & brute force simulation | CRITICAL |
| sql_injection_tool.py | SQL injection detection | CRITICAL |
| password_cracker.py | Hash cracking utilities | HIGH |
| port_scanner.py | Network reconnaissance | MEDIUM |
| network_sniffer.py | Packet analysis | MEDIUM |

## ⚠️ Legal Requirements

**You MUST have:**
1. ✅ Written authorization from system owner
2. ✅ Permission to test specific targets
3. ✅ Documented scope of testing
4. ✅ Insurance/liability coverage

**You MUST NOT:**
1. ❌ Test without explicit written permission
2. ❌ Target systems you don't own
3. ❌ Access unauthorized systems
4. ❌ Share tools or findings publicly without permission

## Professional Standards

Follow these standards for ethical hacking:
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [PTES (Penetration Testing Execution Standard)](http://www.pentest-standard.org/)
- [EC-Council Code of Ethics](https://www.eccouncil.org/)

## Common Testing Scenarios

### Bug Bounty Programs
- Use tools on authorized platforms (HackerOne, Bugcrowd)
- Follow program rules and scope
- Report responsibly

### Security Research
- Use isolated lab environments
- Document findings
- Publish responsibly

### Penetration Testing
- Get signed contract
- Define clear scope
- Regular communication
- Professional reporting

## Disclaimer

**These tools are provided for educational and authorized security testing ONLY.** Unauthorized access to computer systems is illegal under the Computer Fraud and Abuse Act (CFAA) and similar laws worldwide. Users are responsible for compliance with all applicable laws and regulations.

---

**Use responsibly. Hack ethically. Stay legal.** 🔐

# Ethical Hacking Lab - Security Testing Framework

## Overview

This comprehensive security testing framework provides multiple tools for ethical hacking education and authorized penetration testing.

## Quick Start

### Interactive Mode (Recommended)
```bash
cd tools
python3 run_tests.py
```

### Run Specific Tool
```bash
python3 run_tests.py <tool_number> [arguments]
```

## Available Tools

### 🔴 CRITICAL - High Risk Vulnerabilities

**1. SQL Injection Tool** (`sql_injection_tool.py`)
- Tests for SQL injection vulnerabilities
- Multiple payload types
- Login form testing
- Usage: `python3 sql_injection_tool.py 'URL' 'parameter'`

**2. Credential Tester** (`credential_tester.py`)
- SSH brute force simulation
- HTTP authentication testing
- Password strength analysis
- Usage: `python3 credential_tester.py --ssh example.com`

### 🟠 HIGH PRIORITY

**3. Web Vulnerability Scanner** (`web_scanner.py`)
- XSS detection
- CSRF protection analysis
- Security header scanning
- Cookie security testing
- Usage: `python3 web_scanner.py 'https://example.com'`

**4. JWT Analyzer** (`jwt_analyzer.py`)
- JWT token validation
- Algorithm analysis
- Secret key testing
- Claim validation
- Usage: `python3 jwt_analyzer.py 'token'`

**5. Password Cracker** (`password_cracker.py`)
- MD5/SHA1 hash cracking
- Dictionary attacks
- Hash generation
- Usage: `python3 password_cracker.py 'hash'`

### 🟡 MEDIUM PRIORITY

**6. Port Scanner** (`port_scanner.py`)
- Network reconnaissance
- Service identification
- Common port scanning
- Usage: `python3 port_scanner.py example.com`

**7. Network Sniffer** (`network_sniffer.py`)
- Packet capture simulation
- Protocol analysis
- Traffic monitoring
- Usage: `python3 network_sniffer.py eth0`

## Comprehensive Testing Workflow

### Phase 1: Reconnaissance
```bash
# Gather information about target
python3 port_scanner.py target.com
python3 web_scanner.py https://target.com
```

### Phase 2: Vulnerability Assessment
```bash
# Test for common vulnerabilities
python3 sql_injection_tool.py 'https://target.com/search' 'query'
python3 jwt_analyzer.py 'your_token_here'
python3 web_scanner.py 'https://target.com'
```

### Phase 3: Exploitation (Authorized Only)
```bash
# Test credential security
python3 credential_tester.py --ssh target.com
python3 password_cracker.py 'hash_value'
```

### Phase 4: Analysis & Reporting
```bash
# View all test results
python3 run_tests.py 9
```

## Security Testing Checklist

### Before Testing
- [ ] Written authorization obtained
- [ ] Scope documented in writing
- [ ] Legal agreement signed
- [ ] Insurance/liability coverage confirmed
- [ ] Testing dates/times agreed upon
- [ ] Key contacts identified
- [ ] Communication plan established

### During Testing
- [ ] Stay within defined scope
- [ ] Document all findings
- [ ] Don't modify systems
- [ ] Avoid DoS/resource exhaustion
- [ ] Maintain confidentiality
- [ ] Use non-destructive testing methods

### After Testing
- [ ] Compile comprehensive report
- [ ] Grade vulnerabilities by severity
- [ ] Provide remediation guidance
- [ ] Maintain confidentiality
- [ ] Delete test artifacts
- [ ] Follow responsible disclosure

## Example Test Scenarios

### Scenario 1: Web Application Testing
```bash
# Step 1: Initial reconnaissance
python3 port_scanner.py app.example.com 80 443

# Step 2: Vulnerability scanning
python3 web_scanner.py 'https://app.example.com'

# Step 3: Specific vulnerability testing
python3 sql_injection_tool.py 'https://app.example.com/api' 'id'

# Step 4: Authentication testing
python3 credential_tester.py --check 'TestPassword123!'
```

### Scenario 2: API Security Testing
```bash
# Analyze JWT tokens
python3 jwt_analyzer.py 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'

# Test API endpoints
python3 sql_injection_tool.py 'https://api.example.com/users' 'search'

# Check security
python3 web_scanner.py 'https://api.example.com'
```

## Common Findings & Remediation

### SQL Injection
**Finding**: Application accepts unsanitized user input in SQL queries
**Risk**: Data breach, data loss, unauthorized access
**Remediation**: 
- Use parameterized queries/prepared statements
- Input validation and escaping
- Principle of least privilege

### Missing Security Headers
**Finding**: Application doesn't implement security headers
**Risk**: XSS, clickjacking, MIME type sniffing
**Remediation**:
- Add X-Frame-Options
- Add Content-Security-Policy
- Add X-Content-Type-Options
- Add Strict-Transport-Security

### Weak Credentials
**Finding**: Default or weak credentials in use
**Risk**: Unauthorized access, system compromise
**Remediation**:
- Change default credentials
- Enforce strong password policies
- Implement MFA
- Regular access reviews

### Insecure JWT
**Finding**: JWT uses 'none' algorithm or weak secrets
**Risk**: Token forgery, authentication bypass
**Remediation**:
- Never use 'none' algorithm
- Use RS256 (asymmetric) for better security
- Strong secret keys (minimum 256-bit for HS256)
- Implement expiration and validation

## Professional Standards

### Follow These Guidelines
- **OWASP Testing Guide**: https://owasp.org/www-project-web-security-testing-guide/
- **PTES**: http://www.pentest-standard.org/
- **NIST SP 800-115**: Technical Security Testing
- **EC-Council Code of Ethics**: Professional responsibility

### Report Template

```
EXECUTIVE SUMMARY
- Scope and objectives
- Key findings and impact
- Overall risk assessment

DETAILED FINDINGS
- Vulnerability description
- Risk severity (Critical/High/Medium/Low)
- Step-by-step reproduction
- Proof of concept
- Impact analysis

REMEDIATION
- Recommended fixes
- Implementation timeline
- Verification methods

TESTING METHODOLOGY
- Tools and techniques used
- Testing phases
- Coverage areas
```

## Legal & Ethical Requirements

### ⚖️ LEGAL REQUIREMENTS

✅ **MUST HAVE:**
1. Written authorization from system owner
2. Defined scope in writing
3. Signed contract/agreement
4. Insurance/liability coverage
5. Clear testing timeline
6. Emergency contact information

❌ **STRICTLY PROHIBITED:**
1. Testing without written permission
2. Accessing systems outside scope
3. Modifying or destroying data
4. Sharing findings publicly
5. Using tools for malicious purposes
6. Accessing other people's data

### ⚠️ CONSEQUENCES OF UNAUTHORIZED TESTING
- Criminal charges under CFAA (up to 10 years prison)
- Civil liability (damages up to $300,000+)
- Loss of professional certifications
- Permanent criminal record
- Employment termination

## Responsible Disclosure

### Steps for Responsible Disclosure:
1. Document vulnerability details
2. Report to vendor privately first
3. Allow reasonable time to fix (30-90 days)
4. Don't share details publicly
5. Credit vendor for fixing
6. Only disclose after fix is available

## Disclaimer

**IMPORTANT**: These tools are provided SOLELY for educational purposes and authorized security testing. Unauthorized access to computer systems is ILLEGAL. Users are responsible for:
- Obtaining written authorization
- Complying with all applicable laws
- Understanding legal consequences
- Maintaining ethical standards
- Protecting confidentiality

**The creators and maintainers of this framework are NOT responsible for any illegal use or damages caused by these tools.**

---

**Remember**: Great power requires great responsibility. Test ethically, legally, and responsibly! 🔐

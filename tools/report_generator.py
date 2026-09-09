#!/usr/bin/env python3
"""
Security Lab Report Generator
Create professional penetration testing reports
"""

from datetime import datetime
import sys

class ReportGenerator:
    def __init__(self, target, tester_name="Security Analyst"):
        self.target = target
        self.tester_name = tester_name
        self.date = datetime.now().strftime('%Y-%m-%d')
        self.findings = []

    def add_finding(self, title, severity, description, remediation):
        """
        Add a finding to the report
        """
        self.findings.append({
            'title': title,
            'severity': severity,
            'description': description,
            'remediation': remediation
        })

    def generate_html_report(self, filename='report.html'):
        """
        Generate HTML report
        """
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Security Audit Report - {self.target}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                    background: #f5f5f5;
                }}
                .header {{
                    background: #2c3e50;
                    color: white;
                    padding: 20px;
                    border-radius: 5px;
                    margin-bottom: 20px;
                }}
                .finding {{
                    background: white;
                    padding: 15px;
                    margin: 10px 0;
                    border-left: 5px solid #e74c3c;
                    border-radius: 3px;
                }}
                .critical {{
                    border-left-color: #c0392b;
                }}
                .high {{
                    border-left-color: #e67e22;
                }}
                .medium {{
                    border-left-color: #f39c12;
                }}
                .severity {{
                    display: inline-block;
                    padding: 5px 10px;
                    border-radius: 3px;
                    color: white;
                    font-weight: bold;
                }}
                .severity-critical {{
                    background: #c0392b;
                }}
                .severity-high {{
                    background: #e67e22;
                }}
                .severity-medium {{
                    background: #f39c12;
                }}
                .remediation {{
                    background: #ecf0f1;
                    padding: 10px;
                    margin-top: 10px;
                    border-radius: 3px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>📄 Security Audit Report</h1>
                <p><strong>Target:</strong> {self.target}</p>
                <p><strong>Date:</strong> {self.date}</p>
                <p><strong>Tester:</strong> {self.tester_name}</p>
            </div>
            
            <h2>Executive Summary</h2>
            <p>This report documents the security assessment of {self.target}.</p>
            <p><strong>Total Findings:</strong> {len(self.findings)}</p>
        """
        
        # Add findings
        for finding in self.findings:
            severity_class = finding['severity'].lower()
            html_content += f"""
            <div class="finding {severity_class}">
                <h3>{finding['title']}</h3>
                <p><span class="severity severity-{severity_class}">{finding['severity']}</span></p>
                <p><strong>Description:</strong></p>
                <p>{finding['description']}</p>
                <div class="remediation">
                    <strong>🔧 Remediation:</strong>
                    <p>{finding['remediation']}</p>
                </div>
            </div>
            """
        
        html_content += """
            <footer>
                <hr>
                <p style="color: #7f8c8d; font-size: 12px;">
                    This report is confidential and for authorized use only.
                </p>
            </footer>
        </body>
        </html>
        """
        
        with open(filename, 'w') as f:
            f.write(html_content)
        
        print(f"\n✅ Report generated: {filename}")

    def generate_text_report(self, filename='report.txt'):
        """
        Generate text report
        """
        report = f"""
{'='*70}
                    SECURITY AUDIT REPORT
{'='*70}

Target: {self.target}
Date: {self.date}
Tester: {self.tester_name}

{'-'*70}
EXECUTIVE SUMMARY
{'-'*70}

This report documents the comprehensive security assessment of {self.target}.

Key Findings:
- Total Vulnerabilities: {len(self.findings)}

{'-'*70}
DETAILED FINDINGS
{'-'*70}

"""
        
        for i, finding in enumerate(self.findings, 1):
            report += f"""
[{i}] {finding['title']}
    Severity: {finding['severity']}
    
    Description:
    {finding['description']}
    
    Remediation:
    {finding['remediation']}
    
{'-'*70}
"""
        
        report += f"""
CONCLUSION

This assessment identified {len(self.findings)} security issues.
Immediate action is recommended to address critical and high severity findings.

DISCLAIMER:
This report is confidential and for authorized use only.
Unauthorized access or distribution is strictly prohibited.

{'='*70}
"""
        
        with open(filename, 'w') as f:
            f.write(report)
        
        print(f"\n✅ Report generated: {filename}")

def main():
    print("\n" + "="*70)
    print("📄 Security Report Generator")
    print("="*70)
    
    # Example usage
    generator = ReportGenerator('example.com', 'Security Analyst')
    
    # Add sample findings
    generator.add_finding(
        'SQL Injection Vulnerability',
        'CRITICAL',
        'The application is vulnerable to SQL injection in the search parameter.',
        'Use parameterized queries and input validation.'
    )
    
    generator.add_finding(
        'Missing Security Headers',
        'HIGH',
        'The application does not implement important security headers.',
        'Add X-Frame-Options, Content-Security-Policy, and X-Content-Type-Options headers.'
    )
    
    generator.add_finding(
        'Weak Password Policy',
        'MEDIUM',
        'Password requirements are not enforced.',
        'Implement strong password policy (minimum 12 characters, complexity).'
    )
    
    # Generate reports
    generator.generate_text_report('security_report.txt')
    generator.generate_html_report('security_report.html')
    
    print("\n📄 Sample reports generated!")
    print("   - security_report.txt")
    print("   - security_report.html")

if __name__ == "__main__":
    main()

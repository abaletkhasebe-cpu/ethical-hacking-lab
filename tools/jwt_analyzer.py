#!/usr/bin/env python3
"""
JSON Web Token (JWT) Security Analyzer
Detects JWT vulnerabilities and misconfigurations
"""

import base64
import json
import sys
import hmac
import hashlib

class JWTAnalyzer:
    def __init__(self, token=None):
        self.token = token
        self.vulnerabilities = []

    def decode_jwt(self, token):
        """
        Decode JWT token (without verification)
        """
        try:
            parts = token.split('.')
            if len(parts) != 3:
                return None
            
            header = json.loads(base64.urlsafe_b64decode(parts[0] + '=='))
            payload = json.loads(base64.urlsafe_b64decode(parts[1] + '=='))
            signature = parts[2]
            
            return {
                'header': header,
                'payload': payload,
                'signature': signature
            }
        except Exception as e:
            print(f"Error decoding JWT: {e}")
            return None

    def analyze_algorithm(self, header):
        """
        Analyze JWT algorithm for vulnerabilities
        """
        print("\n🔍 Algorithm Analysis")
        print("-" * 50)
        
        alg = header.get('alg')
        print(f"Algorithm: {alg}")
        
        if alg == 'none':
            print("⚠️  CRITICAL: 'none' algorithm - Token can be forged!")
            self.vulnerabilities.append({
                'type': 'No Signature Algorithm',
                'severity': 'CRITICAL',
                'description': 'JWT uses "none" algorithm'
            })
        elif alg in ['HS256', 'HS384', 'HS512']:
            print(f"✓ Using {alg} (HMAC - symmetric)")
            print("⚠️  WARNING: Symmetric key algorithm - ensure secret is strong")
        elif alg in ['RS256', 'RS384', 'RS512']:
            print(f"✓ Using {alg} (RSA - asymmetric)")
            print("✓ More secure than HMAC")
        else:
            print(f"⚠️  Uncommon algorithm: {alg}")

    def analyze_payload(self, payload):
        """
        Analyze JWT payload for issues
        """
        print("\n🔍 Payload Analysis")
        print("-" * 50)
        
        print("\nClaims found:")
        for key, value in payload.items():
            print(f"  {key}: {value}")
        
        # Check for standard claims
        print("\nStandard Claims Check:")
        if 'exp' not in payload:
            print("⚠️  WARNING: No expiration time (exp) set")
            self.vulnerabilities.append({
                'type': 'Missing Expiration',
                'severity': 'HIGH',
                'description': 'No exp claim in token'
            })
        else:
            print(f"✓ Expiration set: {payload['exp']}")
        
        if 'iat' not in payload:
            print("⚠️  WARNING: No issued-at time (iat)")
        else:
            print(f"✓ Issued at: {payload['iat']}")
        
        if 'nbf' not in payload:
            print("⚠️  WARNING: No not-before time (nbf)")
        else:
            print(f"✓ Not before: {payload['nbf']}")

    def check_common_secrets(self, token):
        """
        Test for common JWT secrets
        """
        print("\n🔍 Testing Common Secrets")
        print("-" * 50)
        
        common_secrets = [
            'secret', 'password', '123456', 'admin', 'jwt-secret',
            'your-secret-key', 'your-256-bit-secret', 'supersecret'
        ]
        
        parts = token.split('.')
        message = f"{parts[0]}.{parts[1]}"
        target_sig = parts[2]
        
        print("Testing against common weak secrets...\n")
        for secret in common_secrets[:5]:  # Test first 5
            signature = base64.urlsafe_b64encode(
                hmac.new(secret.encode(), message.encode(), hashlib.sha256).digest()
            ).decode().rstrip('=')
            
            if signature == target_sig:
                print(f"✓ MATCH FOUND! Secret is: '{secret}'")
                self.vulnerabilities.append({
                    'type': 'Weak Secret Key',
                    'severity': 'CRITICAL',
                    'secret': secret
                })
                return True
            else:
                print(f"✗ Secret '{secret}' - no match")
        
        print("\nNo common secrets matched.")
        return False

    def generate_report(self):
        """
        Generate security report
        """
        print("\n" + "="*60)
        print("📊 JWT SECURITY REPORT")
        print("="*60)
        print(f"Total Issues Found: {len(self.vulnerabilities)}")
        
        critical = [v for v in self.vulnerabilities if v.get('severity') == 'CRITICAL']
        high = [v for v in self.vulnerabilities if v.get('severity') == 'HIGH']
        
        if critical:
            print(f"\n🔴 CRITICAL ISSUES: {len(critical)}")
            for issue in critical:
                print(f"  - {issue['type']}: {issue.get('description', '')}")
        
        if high:
            print(f"\n🟠 HIGH ISSUES: {len(high)}")
            for issue in high:
                print(f"  - {issue['type']}: {issue.get('description', '')}")
        
        if not critical and not high:
            print("\n✓ No critical or high severity issues found")

    def demo_analysis(self):
        """
        Run demo JWT analysis
        """
        # Sample JWT tokens for demo
        demo_tokens = {
            'Valid': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c',
            'No Exp': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFkbWluIiwidXNlcl9pZCI6ImFkbWluIn0.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ',
        }
        
        print("\n📝 DEMO TOKENS:")
        for name, token in demo_tokens.items():
            print(f"\n{'='*60}")
            print(f"Token: {name}")
            print(f"JWT: {token[:50]}...")
            print(f"{'='*60}")
            
            decoded = self.decode_jwt(token)
            if decoded:
                self.analyze_algorithm(decoded['header'])
                self.analyze_payload(decoded['payload'])
                # self.check_common_secrets(token)
                self.generate_report()

def main():
    print("\n" + "="*60)
    print("🔐 JWT Security Analyzer")
    print("For Authorized Security Testing Only")
    print("="*60)
    
    if len(sys.argv) > 1:
        token = sys.argv[1]
        analyzer = JWTAnalyzer(token)
        decoded = analyzer.decode_jwt(token)
        
        if decoded:
            print("\n✓ Valid JWT structure detected")
            analyzer.analyze_algorithm(decoded['header'])
            analyzer.analyze_payload(decoded['payload'])
            analyzer.check_common_secrets(token)
            analyzer.generate_report()
        else:
            print("\n✗ Invalid JWT token")
    else:
        analyzer = JWTAnalyzer()
        analyzer.demo_analysis()
        print("\n💡 USAGE: python3 jwt_analyzer.py <JWT_TOKEN>")
        print("Example: python3 jwt_analyzer.py 'eyJhbGc...'")

if __name__ == "__main__":
    main()

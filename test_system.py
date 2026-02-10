#!/usr/bin/env python3
"""
Anh3d0nic System Test
Verifies that all components are working correctly
"""

import sys
import subprocess
import os

class Colors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    OKCYAN = '\033[96m'

def print_header():
    print(f"\n{Colors.OKCYAN}{Colors.BOLD}Anh3d0nic System Test{Colors.ENDC}")
    print("=" * 50)
    print()

def test_python_version():
    """Test Python version"""
    print(f"{Colors.BOLD}[1/6] Testing Python version...{Colors.ENDC}")
    version = sys.version_info
    
    if version.major >= 3 and version.minor >= 8:
        print(f"  {Colors.OKGREEN}✓ Python {version.major}.{version.minor}.{version.micro} - OK{Colors.ENDC}")
        return True
    else:
        print(f"  {Colors.FAIL}✗ Python version too old. Need 3.8+, got {version.major}.{version.minor}{Colors.ENDC}")
        return False

def test_gpt4all():
    """Test GPT4All installation"""
    print(f"\n{Colors.BOLD}[2/6] Testing GPT4All installation...{Colors.ENDC}")
    try:
        import gpt4all
        print(f"  {Colors.OKGREEN}✓ GPT4All module found{Colors.ENDC}")
        return True
    except ImportError:
        print(f"  {Colors.FAIL}✗ GPT4All not installed{Colors.ENDC}")
        print(f"  {Colors.WARNING}Run: pip3 install gpt4all{Colors.ENDC}")
        return False

def test_file_permissions():
    """Test file permissions"""
    print(f"\n{Colors.BOLD}[3/6] Testing file permissions...{Colors.ENDC}")
    
    if os.path.exists('anh3d0nic.py'):
        if os.access('anh3d0nic.py', os.X_OK):
            print(f"  {Colors.OKGREEN}✓ anh3d0nic.py is executable{Colors.ENDC}")
            return True
        else:
            print(f"  {Colors.WARNING}! anh3d0nic.py is not executable{Colors.ENDC}")
            print(f"  {Colors.WARNING}Run: chmod +x anh3d0nic.py{Colors.ENDC}")
            return False
    else:
        print(f"  {Colors.FAIL}✗ anh3d0nic.py not found in current directory{Colors.ENDC}")
        return False

def test_code_execution():
    """Test code execution capability"""
    print(f"\n{Colors.BOLD}[4/6] Testing code execution...{Colors.ENDC}")
    try:
        result = subprocess.run(
            [sys.executable, '-c', 'print("test")'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0 and result.stdout.strip() == "test":
            print(f"  {Colors.OKGREEN}✓ Code execution working{Colors.ENDC}")
            return True
        else:
            print(f"  {Colors.FAIL}✗ Code execution failed{Colors.ENDC}")
            return False
    except Exception as e:
        print(f"  {Colors.FAIL}✗ Code execution error: {str(e)}{Colors.ENDC}")
        return False

def test_bash_execution():
    """Test bash execution capability"""
    print(f"\n{Colors.BOLD}[5/6] Testing bash execution...{Colors.ENDC}")
    try:
        result = subprocess.run(
            ['echo', 'test'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0 and result.stdout.strip() == "test":
            print(f"  {Colors.OKGREEN}✓ Bash execution working{Colors.ENDC}")
            return True
        else:
            print(f"  {Colors.WARNING}! Bash execution may have issues{Colors.ENDC}")
            return False
    except Exception as e:
        print(f"  {Colors.FAIL}✗ Bash execution error: {str(e)}{Colors.ENDC}")
        return False

def test_curl():
    """Test curl for web features"""
    print(f"\n{Colors.BOLD}[6/6] Testing curl (for web features)...{Colors.ENDC}")
    try:
        result = subprocess.run(
            ['curl', '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print(f"  {Colors.OKGREEN}✓ curl available (web search enabled){Colors.ENDC}")
            return True
        else:
            print(f"  {Colors.WARNING}! curl not working properly{Colors.ENDC}")
            return False
    except FileNotFoundError:
        print(f"  {Colors.WARNING}! curl not installed (web search disabled){Colors.ENDC}")
        print(f"  {Colors.WARNING}Optional: Install curl for web search features{Colors.ENDC}")
        return False
    except Exception as e:
        print(f"  {Colors.WARNING}! curl test failed: {str(e)}{Colors.ENDC}")
        return False

def main():
    print_header()
    
    results = []
    
    results.append(("Python Version", test_python_version()))
    results.append(("GPT4All", test_gpt4all()))
    results.append(("File Permissions", test_file_permissions()))
    results.append(("Code Execution", test_code_execution()))
    results.append(("Bash Execution", test_bash_execution()))
    results.append(("Web Features", test_curl()))
    
    print(f"\n{Colors.BOLD}{'=' * 50}{Colors.ENDC}")
    print(f"{Colors.BOLD}Test Results Summary{Colors.ENDC}")
    print("=" * 50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = f"{Colors.OKGREEN}PASS{Colors.ENDC}" if result else f"{Colors.FAIL}FAIL{Colors.ENDC}"
        print(f"  {test_name:.
<30} {status}")
    
    print("=" * 50)
    print(f"{Colors.BOLD}Score: {passed}/{total} tests passed{Colors.ENDC}")
    
    if passed == total:
        print(f"\n{Colors.OKGREEN}{Colors.BOLD}✓ All tests passed! Anh3d0nic is ready to use!{Colors.ENDC}")
        print(f"{Colors.OKCYAN}Run: python3 anh3d0nic.py{Colors.ENDC}\n")
        return 0
    elif passed >= 4:
        print(f"\n{Colors.WARNING}{Colors.BOLD}! Most tests passed. Anh3d0nic should work with limited features.{Colors.ENDC}")
        print(f"{Colors.WARNING}Fix the failed tests for full functionality.{Colors.ENDC}\n")
        return 1
    else:
        print(f"\n{Colors.FAIL}{Colors.BOLD}✗ Critical tests failed. Please fix errors before using Anh3d0nic.{Colors.ENDC}")
        print(f"{Colors.WARNING}See TROUBLESHOOTING.md for help.{Colors.ENDC}\n")
        return 2

if __name__ == "__main__":
    sys.exit(main())

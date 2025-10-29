#!/usr/bin/env python3
"""
System Check - Verify all dependencies are installed
"""

import sys
import subprocess

def check_python():
    """Check Python version."""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 6:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"✗ Python version too old: {version.major}.{version.minor}.{version.micro}")
        print("  Need Python 3.6 or higher")
        return False

def check_module(module_name, import_name=None):
    """Check if a Python module is installed."""
    if import_name is None:
        import_name = module_name
    
    try:
        __import__(import_name)
        print(f"✓ {module_name} is installed")
        return True
    except ImportError:
        print(f"✗ {module_name} is NOT installed")
        print(f"  Install with: pip3 install {module_name}")
        return False

def check_libreoffice():
    """Check if LibreOffice is installed."""
    try:
        result = subprocess.run(['soffice', '--version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"✓ LibreOffice is installed ({version})")
            return True
    except:
        pass
    
    # Check macOS application folder
    import os
    if os.path.exists('/Applications/LibreOffice.app'):
        print("✓ LibreOffice is installed (in Applications)")
        print("  Note: You may need to add it to PATH")
        return True
    
    print("✗ LibreOffice is NOT installed")
    print("  Install with: brew install --cask libreoffice")
    print("  Or download from: https://www.libreoffice.org/")
    return False

def main():
    print("=" * 60)
    print("Resume Sync - System Check")
    print("=" * 60)
    print()
    
    all_good = True
    
    # Check Python
    print("Checking Python...")
    if not check_python():
        all_good = False
    print()
    
    # Check required modules
    print("Checking Python packages...")
    if not check_module('python-docx', 'docx'):
        all_good = False
    if not check_module('watchdog'):
        all_good = False
    print()
    
    # Check LibreOffice
    print("Checking LibreOffice...")
    if not check_libreoffice():
        all_good = False
    print()
    
    print("=" * 60)
    if all_good:
        print("✓ ALL CHECKS PASSED!")
        print("=" * 60)
        print()
        print("You're ready to use the resume sync scripts!")
        print()
        print("Try running:")
        print("  python3 sync_resumes.py [your-resume-folder]")
        print("  python3 watch_resumes.py [your-resume-folder]")
    else:
        print("✗ SOME CHECKS FAILED")
        print("=" * 60)
        print()
        print("Please install the missing dependencies listed above.")
        print()
        print("Quick fix:")
        print("  ./setup_macos.sh")
        print()
        print("Or manually:")
        print("  pip3 install python-docx watchdog")
        print("  brew install --cask libreoffice")
    print()

if __name__ == "__main__":
    main()

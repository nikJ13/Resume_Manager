#!/bin/bash
# Setup script for macOS

echo "=========================================="
echo "Resume Sync - Setup Script (macOS)"
echo "=========================================="
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install it first:"
    echo "   brew install python3"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Install Python dependencies
echo "📦 Installing Python dependencies..."
echo ""

echo "Installing python-docx..."
pip3 install python-docx --user || pip3 install python-docx

echo ""
echo "Installing watchdog (for auto-sync mode)..."
pip3 install watchdog --user || pip3 install watchdog

echo ""
echo "=========================================="
echo "Checking LibreOffice for PDF conversion..."
echo "=========================================="
echo ""

if command -v soffice &> /dev/null; then
    echo "✓ LibreOffice found"
elif [ -d "/Applications/LibreOffice.app" ]; then
    echo "✓ LibreOffice found in Applications"
    echo "Adding LibreOffice to PATH..."
    # Create a symbolic link if it doesn't exist
    if [ ! -f "/usr/local/bin/soffice" ]; then
        sudo ln -s /Applications/LibreOffice.app/Contents/MacOS/soffice /usr/local/bin/soffice 2>/dev/null
    fi
else
    echo "⚠️  LibreOffice not found"
    echo ""
    echo "LibreOffice is needed for PDF conversion."
    echo "You have two options:"
    echo ""
    echo "Option 1 - Install with Homebrew (recommended):"
    echo "  brew install --cask libreoffice"
    echo ""
    echo "Option 2 - Download manually:"
    echo "  Visit https://www.libreoffice.org/download/download/"
    echo ""
fi

echo ""
echo "=========================================="
echo "✓ Setup Complete!"
echo "=========================================="
echo ""
echo "You can now use the scripts:"
echo "  python3 sync_resumes.py [directory]"
echo "  python3 watch_resumes.py [directory]"
echo ""

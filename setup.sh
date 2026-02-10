#!/bin/bash

# Anh3d0nic Setup Script
# Automated installation for the Anh3d0nic AI Agent

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║     █████╗ ███╗   ██╗██╗  ██╗██████╗ ██████╗  ██████╗       ║
║    ██╔══██╗████╗  ██║██║  ██║╚════██╗██╔══██╗██╔═████╗      ║
║    ███████║██╔██╗ ██║███████║ █████╔╝██║  ██║██║██╔██║      ║
║    ██╔══██║██║╚██╗██║██╔══██║ ╚═══██╗██║  ██║████╔╝██║      ║
║    ██║  ██║██║ ╚████║██║  ██║██████╔╝██████╔╝╚██████╔╝      ║
║    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝       ║
║                                                               ║
║                    SETUP & INSTALLATION                       ║
╚═══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo -e "${GREEN}Starting Anh3d0nic installation...${NC}\n"

# Check if Python is installed
echo -e "${YELLOW}[1/5] Checking Python installation...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed!${NC}"
    echo -e "${YELLOW}Please install Python 3.8+ from https://www.python.org${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo -e "${GREEN}✓ Python ${PYTHON_VERSION} found${NC}\n"

# Check if pip is installed
echo -e "${YELLOW}[2/5] Checking pip installation...${NC}"
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}Error: pip3 is not installed!${NC}"
    echo -e "${YELLOW}Installing pip...${NC}"
    python3 -m ensurepip --upgrade
fi
echo -e "${GREEN}✓ pip is ready${NC}\n"

# Install dependencies
echo -e "${YELLOW}[3/5] Installing Python dependencies...${NC}"
echo -e "${BLUE}This may take a few minutes...${NC}"

pip3 install --user --upgrade pip
pip3 install --user gpt4all

echo -e "${GREEN}✓ Dependencies installed${NC}\n"

# Make the script executable
echo -e "${YELLOW}[4/5] Making Anh3d0nic executable...${NC}"
chmod +x anh3d0nic.py
echo -e "${GREEN}✓ Script is now executable${NC}\n"

# Optional: Create a system-wide alias
echo -e "${YELLOW}[5/5] Setting up quick launch...${NC}"
INSTALL_DIR=$(pwd)

# Detect shell
if [ -f "$HOME/.bashrc" ]; then
    SHELL_RC="$HOME/.bashrc"
elif [ -f "$HOME/.zshrc" ]; then
    SHELL_RC="$HOME/.zshrc"
else
    SHELL_RC=""
fi

if [ -n "$SHELL_RC" ]; then
    # Check if alias already exists
    if grep -q "alias anh3d0nic=" "$SHELL_RC" 2>/dev/null; then
        echo -e "${YELLOW}Alias already exists in $SHELL_RC${NC}"
    else
        echo "" >> "$SHELL_RC"
        echo "# Anh3d0nic AI Agent alias" >> "$SHELL_RC"
        echo "alias anh3d0nic='python3 $INSTALL_DIR/anh3d0nic.py'" >> "$SHELL_RC"
        echo -e "${GREEN}✓ Added 'anh3d0nic' command to $SHELL_RC${NC}"
        echo -e "${YELLOW}Run 'source $SHELL_RC' or restart your terminal to use the 'anh3d0nic' command${NC}"
    fi
fi

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════${NC}"
echo -e "${GREEN}${NC}"
echo -e "${GREEN}  ✓ Installation Complete!${NC}"
echo -e "${GREEN}${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════${NC}"
echo ""
echo -e "${BLUE}To start Anh3d0nic, run:${NC}"
echo -e "${YELLOW}  python3 anh3d0nic.py${NC}"
echo ""
if [ -n "$SHELL_RC" ]; then
    echo -e "${BLUE}Or after restarting your terminal:${NC}"
    echo -e "${YELLOW}  anh3d0nic${NC}"
    echo ""
fi
echo -e "${BLUE}First run will download the AI model (~4GB) - be patient!${NC}"
echo ""
echo -e "${GREEN}Happy chatting! 🤖${NC}"
echo ""

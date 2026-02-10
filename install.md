# 📦 Complete Installation Guide - Anh3d0nic

This guide will walk you through installing and setting up Anh3d0nic on any system.

## 📋 What You'll Get

After installation, you'll have:
- A fully functional AI CLI agent
- Code execution capabilities
- Web search features
- File management tools
- No API keys required
- Unlimited usage
- Complete privacy (runs locally)

## 🖥️ System Requirements

### Minimum Requirements
- **OS**: Linux, macOS, or Windows 10+
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Disk Space**: 6GB (5GB for model + 1GB for installation)
- **Internet**: Required for initial setup only

### Recommended Requirements
- **OS**: Linux/macOS (better terminal support)
- **Python**: 3.10+
- **RAM**: 8GB+
- **CPU**: Multi-core processor
- **Disk Space**: 10GB free

## 🚀 Installation Methods

Choose the method that best suits your system:

### Method 1: Automated Installation (Recommended for Linux/macOS)

```bash
# Step 1: Download all files to a directory
cd ~/Downloads/anh3d0nic/

# Step 2: Run the setup script
chmod +x setup.sh
./setup.sh

# Step 3: Start Anh3d0nic
python3 anh3d0nic.py
```

**What the setup script does:**
- ✓ Checks Python version
- ✓ Installs pip if needed
- ✓ Installs gpt4all package
- ✓ Makes scripts executable
- ✓ Creates shell aliases (optional)
- ✓ Tests the installation

### Method 2: Manual Installation (All Platforms)

```bash
# Step 1: Ensure Python 3.8+ is installed
python3 --version
# Should show: Python 3.8.x or higher

# Step 2: Install GPT4All
pip3 install gpt4all

# Step 3: Make the script executable (Linux/macOS)
chmod +x anh3d0nic.py

# Step 4: Run Anh3d0nic
python3 anh3d0nic.py
```

### Method 3: Windows Installation

```powershell
# Step 1: Install Python from python.org
# Make sure to check "Add Python to PATH" during installation

# Step 2: Open PowerShell or Command Prompt

# Step 3: Install GPT4All
pip install gpt4all

# Step 4: Navigate to anh3d0nic directory
cd C:\path\to\anh3d0nic\

# Step 5: Run using the batch file
launch.bat

# Or run directly
python anh3d0nic.py
```

## 📥 First-Time Setup

When you run Anh3d0nic for the first time:

1. **Model Download Starts Automatically**
   ```
   Initializing Anh3d0nic AI Brain...
   Loading AI model (this may take a moment on first run)...
   Downloading mistral-7b-openorca.gguf2.Q4_0.gguf...
   [████████████████████████████████] 100% 3.8GB
   ```

2. **Download Time**: 5-30 minutes depending on your internet speed
   - Fast connection (100Mbps+): ~5-10 minutes
   - Medium connection (25-100Mbps): ~10-20 minutes
   - Slow connection (<25Mbps): ~20-30 minutes

3. **One-Time Process**: This download only happens once
   - Model is cached at: `~/.cache/gpt4all/`
   - Subsequent starts are instant

4. **Ready to Use**: Once loaded, you'll see:
   ```
   ✓ Anh3d0nic AI Brain loaded successfully!
   
   Anh3d0nic is ready! Type your message or 'help' for commands.
   ```

## ✅ Verify Installation

Run the system test to verify everything works:

```bash
python3 test_system.py
```

Expected output:
```
[1/6] Testing Python version...
  ✓ Python 3.10.2 - OK

[2/6] Testing GPT4All installation...
  ✓ GPT4All module found

[3/6] Testing file permissions...
  ✓ anh3d0nic.py is executable

[4/6] Testing code execution...
  ✓ Code execution working

[5/6] Testing bash execution...
  ✓ Bash execution working

[6/6] Testing curl (for web features)...
  ✓ curl available (web search enabled)

Score: 6/6 tests passed
✓ All tests passed! Anh3d0nic is ready to use!
```

## 🎯 Post-Installation Setup

### Optional: Create System-Wide Command

**Linux/macOS (Bash):**
```bash
echo 'alias anh3d0nic="python3 ~/path/to/anh3d0nic.py"' >> ~/.bashrc
source ~/.bashrc
```

**macOS (Zsh):**
```bash
echo 'alias anh3d0nic="python3 ~/path/to/anh3d0nic.py"' >> ~/.zshrc
source ~/.zshrc
```

**Windows (PowerShell Profile):**
```powershell
notepad $PROFILE
# Add this line:
# function anh3d0nic { python C:\path\to\anh3d0nic.py }
```

Now you can start Anh3d0nic from anywhere by typing: `anh3d0nic`

### Optional: Install Additional Tools

For full functionality, install these optional tools:

**curl** (for web search):
```bash
# Ubuntu/Debian
sudo apt-get install curl

# macOS
brew install curl

# Windows: Download from https://curl.se/
```

## 📚 File Structure

After installation, your directory should look like:

```
anh3d0nic/
├── anh3d0nic.py          # Main application
├── setup.sh              # Automated setup (Linux/macOS)
├── launch.bat            # Windows launcher
├── test_system.py        # System verification
├── requirements.txt      # Python dependencies
├── README.md             # Main documentation
├── QUICKSTART.md         # Quick start guide
├── TROUBLESHOOTING.md    # Problem solving
├── EXAMPLES.md           # Usage examples
├── CHANGELOG.md          # Version history
└── LICENSE               # MIT License
```

## 🔧 Configuration

### Changing AI Model

Edit `anh3d0nic.py` around line 120:

```python
self.model = GPT4All(
    model_name="mistral-7b-openorca.gguf2.Q4_0.gguf",  # Default
    # Alternatives:
    # model_name="orca-mini-3b.ggmlv3.q4_0.bin"  # Faster, less RAM
    # model_name="wizardlm-13b-v1.2.Q4_0.gguf"   # Smarter, more RAM
    model_path=str(model_path),
    allow_download=True,
    device='cpu'
)
```

### Adjusting Response Length

Edit line 250:
```python
response = self.model.generate(
    context,
    max_tokens=500,  # Increase for longer responses (e.g., 1000)
    temp=0.7,        # 0.1-1.0: lower=focused, higher=creative
    top_p=0.9        # 0.1-1.0: nucleus sampling parameter
)
```

### Changing Execution Timeout

Edit lines 45 and 55:
```python
timeout=30  # Increase to 60 or 90 for longer-running code
```

## 🐛 Common Issues

### Issue: GPT4All won't install

**Solution:**
```bash
# Update pip first
pip3 install --upgrade pip

# Then install gpt4all
pip3 install gpt4all

# If that fails, try with --user
pip3 install --user gpt4all
```

### Issue: Model download fails

**Solution:**
1. Check internet connection
2. Try again - downloads can resume
3. Manual download from: https://gpt4all.io/models/
4. Place in: `~/.cache/gpt4all/`

### Issue: "Python not found"

**Solution:**
- Install Python 3.8+ from: https://www.python.org/downloads/
- During install, check "Add Python to PATH"
- Restart terminal after installation

For more issues, see **TROUBLESHOOTING.md**

## 🎓 Next Steps

1. **Read the Quick Start**: `QUICKSTART.md`
2. **Try Examples**: `EXAMPLES.md`
3. **Run Test**: `python3 test_system.py`
4. **Start Using**: `python3 anh3d0nic.py`

## 📖 Learning Resources

### Recommended Reading Order:
1. This file (INSTALL.md) ← You are here
2. QUICKSTART.md - Get started fast
3. README.md - Full documentation
4. EXAMPLES.md - See what's possible
5. TROUBLESHOOTING.md - When things go wrong

### Key Commands to Remember:
```
python3 anh3d0nic.py     # Start the agent
python3 test_system.py   # Test your installation
help                     # Inside Anh3d0nic: show commands
exit                     # Inside Anh3d0nic: quit
```

## 💡 Tips for Success

1. **First run patience**: Model download takes time but only happens once
2. **System resources**: Close other apps during first run
3. **Internet speed**: Fast connection = faster initial setup
4. **Disk space**: Ensure 6GB free before starting
5. **Test first**: Run `test_system.py` before first use

## 🌟 You're Ready!

Installation complete! You now have:

✅ A fully functional local AI assistant
✅ No API keys required
✅ Unlimited free usage
✅ Complete privacy
✅ Code execution capabilities
✅ Web search features

**Start now:**
```bash
python3 anh3d0nic.py
```

Enjoy your new AI assistant! 🤖

---

**Need Help?**
- Quick answers: QUICKSTART.md
- Problems: TROUBLESHOOTING.md
- Ideas: EXAMPLES.md
- Details: README.md

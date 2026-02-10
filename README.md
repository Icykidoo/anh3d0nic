# 🤖 Anh3d0nic - Free Local AI CLI Agent

A fully-featured, completely free AI assistant that runs entirely on your local machine. No API keys, no usage limits, no internet required (after initial setup).

```
╔═══════════════════════════════════════════════════════════════╗
║     █████╗ ███╗   ██╗██╗  ██╗██████╗ ██████╗  ██████╗       ║
║    ██╔══██╗████╗  ██║██║  ██║╚════██╗██╔══██╗██╔═████╗      ║
║    ███████║██╔██╗ ██║███████║ █████╔╝██║  ██║██║██╔██║      ║
║    ██╔══██║██║╚██╗██║██╔══██║ ╚═══██╗██║  ██║████╔╝██║      ║
║    ██║  ██║██║ ╚████║██║  ██║██████╔╝██████╔╝╚██████╔╝      ║
║    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝       ║
║                                                               ║
║              N  I  C     -     Local AI Agent                ║
║              🤖 Free • No API Keys • Unlimited 🤖            ║
╚═══════════════════════════════════════════════════════════════╝
```

## ✨ Features

- 🧠 **Local AI Brain** - Runs entirely on your machine using GPT4All
- 💰 **Completely Free** - No API keys, no subscriptions, no hidden costs
- ♾️ **Unlimited Usage** - No rate limits or usage restrictions
- 💻 **Code Execution** - Execute Python and Bash commands safely
- 🌐 **Web Browsing** - Search the web and fetch URLs
- 📁 **File Management** - Read, write, and manage files
- 🔧 **Code Assistant** - Write, fix, and update code
- 💬 **Natural Conversations** - Context-aware chat with memory
- 🎨 **Beautiful CLI** - Colored output with intuitive interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- 4GB+ RAM recommended
- ~5GB disk space for the AI model
- Internet connection (first-time setup only)

### Installation

#### Option 1: Automated Setup (Recommended)

```bash
# Clone or download the files
cd anh3d0nic/

# Run the setup script
chmod +x setup.sh
./setup.sh

# Start using Anh3d0nic
python3 anh3d0nic.py
```

#### Option 2: Manual Setup

```bash
# Install dependencies
pip3 install gpt4all

# Make executable
chmod +x anh3d0nic.py

# Run
python3 anh3d0nic.py
```

### First Run

On first run, Anh3d0nic will download the AI model (~4GB). This is a one-time download:

```
Initializing Anh3d0nic AI Brain...
Loading AI model (this may take a moment on first run)...
Downloading mistral-7b-openorca.gguf2.Q4_0.gguf...
```

**Be patient!** After the initial download, subsequent runs are instant.

## 📖 Usage Guide

### Basic Chat

Just type naturally:

```
You: Hello! How are you?
Anh3d0nic: Hello! I'm doing great, thank you for asking...
```

### Code Assistance

Ask for code help:

```
You: Write a Python function to calculate fibonacci numbers

Anh3d0nic: Here's a Python function that calculates Fibonacci numbers...
```

### Execute Python Code

```
You: execute this code:
```python
for i in range(5):
    print(f"Number: {i}")
```

Anh3d0nic: Executing Python code...
Code executed successfully!

Output:
Number: 0
Number: 1
Number: 2
Number: 3
Number: 4
```

### Run Bash Commands

```
You: $ ls -la

Anh3d0nic: Executing bash command...
Command executed successfully!

Output:
drwxr-xr-x  5 user user  4096 Feb 11 10:30 .
drwxr-xr-x 23 user user  4096 Feb 11 09:15 ..
-rw-r--r--  1 user user   256 Feb 11 10:30 anh3d0nic.py
```

Or using the bash prefix:

```
You: bash: pwd
```

### Web Search

```
You: search for Python 3.12 new features

Anh3d0nic: Searching the web...
[Search results appear here]
```

### File Operations

```
You: read file example.txt

Anh3d0nic: [Contents of example.txt]
```

## 🎮 Commands

| Command | Description |
|---------|-------------|
| `help` | Show available commands and capabilities |
| `clear` | Clear the terminal screen |
| `reset` | Clear conversation history |
| `exit` or `quit` | Exit Anh3d0nic |

## 🛠️ Advanced Features

### Code Execution Safety

- Commands timeout after 30 seconds
- Executed in isolated environment
- Python code runs in temporary files
- All executions are logged

### Context Memory

Anh3d0nic remembers your conversation:

```
You: My name is Alex
Anh3d0nic: Nice to meet you, Alex!

You: What's my name?
Anh3d0nic: Your name is Alex.
```

### Multi-turn Tasks

```
You: Write a Python script to parse CSV files
Anh3d0nic: [Provides code]

You: Add error handling to that
Anh3d0nic: [Updates the code with error handling]

You: Now execute it with test.csv
Anh3d0nic: [Executes the improved code]
```

## 🔧 Configuration

### Changing the AI Model

Edit `anh3d0nic.py` and change the model name:

```python
self.model = GPT4All(
    model_name="orca-mini-3b.ggmlv3.q4_0.bin",  # Smaller, faster
    # or
    model_name="wizardlm-13b-v1.2.Q4_0.gguf",   # Larger, smarter
    ...
)
```

Available models: https://gpt4all.io/index.html

### Performance Tuning

In `anh3d0nic.py`, adjust generation parameters:

```python
response = self.model.generate(
    context,
    max_tokens=500,    # Increase for longer responses
    temp=0.7,          # Higher = more creative (0.1-1.0)
    top_p=0.9          # Nucleus sampling (0.1-1.0)
)
```

## 💡 Examples

### Example 1: Code Review

```
You: Review this code for bugs:

def divide(a, b):
    return a / b

Anh3d0nic: This code has a potential bug - it doesn't handle division by zero.
Here's an improved version:

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### Example 2: Learning Assistant

```
You: Explain recursion with a simple example

Anh3d0nic: Recursion is when a function calls itself. Here's a simple example
calculating factorial:

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

When you call factorial(5), it calculates: 5 * 4 * 3 * 2 * 1 = 120
```

### Example 3: System Administration

```
You: $ df -h

Anh3d0nic: Executing bash command...
[Shows disk usage]

You: Which partition has the most free space?

Anh3d0nic: Based on the output, /dev/sda1 has the most free space with 250GB available.
```

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│         Anh3d0nic CLI Interface         │
├─────────────────────────────────────────┤
│                                         │
│  ┌──────────┐  ┌──────────────────┐   │
│  │  Intent  │  │  GPT4All Model   │   │
│  │ Detector │  │  (Local Brain)   │   │
│  └──────────┘  └──────────────────┘   │
│                                         │
│  ┌──────────┐  ┌──────────────────┐   │
│  │   Code   │  │   Web Browser    │   │
│  │ Executor │  │    (curl)        │   │
│  └──────────┘  └──────────────────┘   │
│                                         │
│  ┌──────────┐  ┌──────────────────┐   │
│  │   File   │  │  Conversation    │   │
│  │ Manager  │  │    History       │   │
│  └──────────┘  └──────────────────┘   │
│                                         │
└─────────────────────────────────────────┘
```

## 🔍 Troubleshooting

### Model Download Issues

If the model download fails:

```bash
# Manually download from: https://gpt4all.io/models/
# Place in: ~/.cache/gpt4all/
```

### Memory Issues

If you get out-of-memory errors:

1. Close other applications
2. Use a smaller model (see Configuration)
3. Reduce `max_tokens` in the code

### Import Errors

```bash
# Ensure gpt4all is installed
pip3 install --upgrade gpt4all

# Check Python version
python3 --version  # Should be 3.8+
```

### Permission Errors

```bash
# Make sure the script is executable
chmod +x anh3d0nic.py

# Install packages with --user flag
pip3 install --user gpt4all
```

## 🤝 Contributing

This is a personal project, but suggestions are welcome! Feel free to:

- Report bugs
- Suggest features
- Improve documentation
- Share your use cases

## 📜 License

This project is released under the MIT License. Free to use, modify, and distribute.

## 🙏 Credits

- **GPT4All** - For the amazing local LLM framework
- **Mistral AI** - For the base model
- **You** - For using Anh3d0nic!

## ⚠️ Disclaimer

- Code execution features can be dangerous - review code before running
- Web scraping may be subject to website terms of service
- AI responses may not always be accurate - verify important information
- This tool is for educational and personal use

## 🌟 Star Features

### Why Anh3d0nic?

✅ **Privacy First** - All processing happens locally, your data never leaves your machine
✅ **No Vendor Lock-in** - Not dependent on any commercial API
✅ **Educational** - Learn AI, Python, and system administration
✅ **Customizable** - Full source code, modify as needed
✅ **Offline Capable** - Works without internet after setup
✅ **Cost Effective** - Zero ongoing costs

## 🚀 Future Enhancements

Planned features:

- [ ] Multiple model support
- [ ] Plugin system
- [ ] Voice input/output
- [ ] GUI version
- [ ] Docker container
- [ ] Advanced web scraping
- [ ] Database integration
- [ ] Task automation
- [ ] Multi-language support

## 📞 Support

Having issues? Try these resources:

1. Check this README
2. Review the troubleshooting section
3. Check GPT4All documentation: https://docs.gpt4all.io/
4. Python documentation: https://docs.python.org/3/

---

**Made with ❤️ for the AI community**

*Anh3d0nic - Your Personal Free AI Assistant*

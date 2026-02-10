# 🚀 Quick Start Guide - Anh3d0nic

Get up and running with Anh3d0nic in 5 minutes!

## Step 1: Install (First Time Only)

### Linux / macOS

```bash
# Navigate to the anh3d0nic directory
cd anh3d0nic/

# Run the automated setup
chmod +x setup.sh
./setup.sh
```

### Windows

```powershell
# Install Python from python.org if not already installed

# Install dependencies
pip install gpt4all

# Ready to use!
```

## Step 2: Launch

```bash
python3 anh3d0nic.py
```

**First Run Note:** The AI model (~4GB) will download automatically. This happens only once and may take 5-20 minutes depending on your internet speed. Grab a coffee! ☕

## Step 3: Start Chatting!

### Try These First Commands:

```
# Simple chat
You: Hello! What can you do?

# Get help
You: help

# Write code
You: Write a Python function to reverse a string

# Execute code
You: execute this code:
```python
print("Hello from Anh3d0nic!")
```

# Run bash command
You: $ date

# Search web (requires curl)
You: search for Python tutorials

# Exit
You: exit
```

## Common First-Time Issues

### "gpt4all not found"
```bash
pip3 install gpt4all
# or
pip install gpt4all
```

### "Python not found"
Download from: https://www.python.org/downloads/
(Use Python 3.8 or newer)

### "Permission denied"
```bash
chmod +x anh3d0nic.py
chmod +x setup.sh
```

### Model download is slow
Be patient! First download is large but only happens once.
You can:
- Use a different network
- Download manually from https://gpt4all.io/models/
- Try a smaller model by editing the code

## Tips for Best Experience

1. **Be Specific** - "Write a Python function to sort a list" is better than "help with Python"

2. **Use Code Blocks** - When executing code, format it properly:
   ```
   execute this code:
   ```python
   your code here
   ```
   ```

3. **Ask Follow-ups** - Anh3d0nic remembers context:
   ```
   You: Write a function to add two numbers
   [Anh3d0nic provides code]
   You: Add error handling to that
   [Anh3d0nic updates the code]
   ```

4. **Use Commands** - Type `help` anytime for a reminder of capabilities

5. **Reset When Needed** - If conversation gets confused, type `reset`

## What's Next?

- Read the full README.md for advanced features
- Try different code execution examples
- Experiment with web search
- Customize the model settings
- Share your experience!

## Quick Reference Card

| What You Want | Command Example |
|---------------|-----------------|
| Chat | Just type naturally |
| Help | `help` |
| Execute Python | `execute this code: ...` |
| Run Bash | `$ command` or `bash: command` |
| Search Web | `search for topic` |
| Read File | `read file path.txt` |
| Clear Screen | `clear` |
| Reset Chat | `reset` |
| Exit | `exit` or `quit` |

## Keyboard Shortcuts

- **Ctrl+C** - Exit/Cancel current input
- **Up Arrow** - Previous command (history)
- **Down Arrow** - Next command (history)
- **Tab** - (In some terminals) Auto-complete

---

**You're all set! Enjoy using Anh3d0nic! 🎉**

Need help? Check README.md for detailed documentation.

# 🔧 Troubleshooting Guide - Anh3d0nic

Common issues and their solutions.

## Installation Issues

### Issue: "gpt4all not found" or "No module named 'gpt4all'"

**Solution:**
```bash
# Try these in order:
pip3 install gpt4all
# or
pip install gpt4all
# or
python3 -m pip install gpt4all
# or with --user flag
pip3 install --user gpt4all
```

### Issue: "Python not found" or "python3 not found"

**Solution:**
1. Install Python 3.8+ from https://www.python.org/downloads/
2. During installation, check "Add Python to PATH"
3. Restart your terminal
4. Verify: `python3 --version` or `python --version`

### Issue: Permission denied when running setup.sh

**Solution:**
```bash
chmod +x setup.sh
chmod +x anh3d0nic.py
```

### Issue: pip not found

**Solution:**
```bash
# Install pip
python3 -m ensurepip --upgrade
# or
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

## Model Download Issues

### Issue: Model download is very slow or stuck

**Solutions:**
1. **Be patient** - First download is ~4GB and can take 10-30 minutes
2. **Check internet connection**
3. **Try a different network** (sometimes helps with slow connections)
4. **Manual download**:
   ```bash
   # Download from https://gpt4all.io/models/
   # Save to: ~/.cache/gpt4all/
   # File: mistral-7b-openorca.gguf2.Q4_0.gguf
   ```

### Issue: Model download fails with error

**Solution:**
```bash
# Clear cache and retry
rm -rf ~/.cache/gpt4all/
python3 anh3d0nic.py
```

### Issue: "Model file corrupted" or checksum errors

**Solution:**
```bash
# Delete and re-download
rm ~/.cache/gpt4all/mistral-7b-openorca.gguf2.Q4_0.gguf
python3 anh3d0nic.py
```

## Runtime Issues

### Issue: Out of memory / RAM errors

**Solutions:**
1. **Close other applications** to free up RAM
2. **Use a smaller model**:
   ```python
   # Edit anh3d0nic.py, line ~120
   self.model = GPT4All(
       model_name="orca-mini-3b.ggmlv3.q4_0.bin",  # Smaller, less RAM
       ...
   )
   ```
3. **Reduce max_tokens**:
   ```python
   # Edit line ~250 in anh3d0nic.py
   response = self.model.generate(
       context,
       max_tokens=200,  # Reduced from 500
       ...
   )
   ```

### Issue: Very slow responses

**Solutions:**
1. **Normal on first use** - subsequent responses are faster
2. **CPU-bound** - This is expected, running AI locally is compute-intensive
3. **Use a smaller/faster model**:
   - orca-mini-3b (fastest, less accurate)
   - gpt4all-j (medium speed/accuracy)
   - mistral-7b (slower, more accurate - default)

### Issue: "Execution timeout" when running code

**Solutions:**
1. **Code runs longer than 30 seconds** - this is a safety limit
2. **Increase timeout** in anh3d0nic.py:
   ```python
   # Line ~45 and ~55
   timeout=60  # Changed from 30
   ```

### Issue: Code execution fails

**Possible causes and solutions:**

**Python code errors:**
```
✓ Check code syntax
✓ Ensure required packages are installed
✓ Check file paths are correct
```

**Bash commands fail:**
```
✓ Verify command exists: `which <command>`
✓ Check permissions
✓ Try running command manually first
```

### Issue: Web search returns "curl not installed"

**Solution:**
```bash
# Install curl
# Ubuntu/Debian:
sudo apt-get install curl

# macOS (using Homebrew):
brew install curl

# Windows:
# Download from: https://curl.se/download.html
```

### Issue: Cannot read files / "File not found"

**Solutions:**
1. **Use absolute paths**: `/home/user/file.txt` instead of `file.txt`
2. **Check file permissions**: `ls -l filename`
3. **Verify file exists**: `$ ls -la`

## Import and Dependency Issues

### Issue: "ModuleNotFoundError" for various modules

**Solution:**
```bash
# The only required dependency is gpt4all
pip3 install gpt4all

# If using additional features, install as needed:
pip3 install requests  # For advanced web features
```

### Issue: Readline errors on Windows

**Solution:**
Readline isn't required on Windows. The error can be ignored, or:
```powershell
# Windows alternative - pyreadline
pip install pyreadline3
```

## Response Quality Issues

### Issue: AI gives irrelevant or poor answers

**Solutions:**
1. **Be more specific** in your questions
2. **Provide context**: Include relevant details
3. **Try rephrasing**: Ask the question differently
4. **Reset conversation**: Type `reset` if context is confusing
5. **Use a better model**: Switch to a larger model for better quality

### Issue: AI repeats itself

**Solution:**
```
# Type: reset
# This clears conversation history
```

### Issue: AI doesn't remember previous context

**Solution:**
Context is working if you see relevant responses. If not:
1. Check conversation_history in code
2. Ensure you're not resetting too often
3. History limit is 20 messages - older messages are forgotten

## Platform-Specific Issues

### Linux Issues

**Issue: Permission denied**
```bash
chmod +x anh3d0nic.py
chmod +x setup.sh
```

**Issue: Command not found after alias setup**
```bash
source ~/.bashrc
# or
source ~/.zshrc
```

### macOS Issues

**Issue: "Developer cannot be verified"**
```bash
# Right-click the file → Open
# or
xattr -d com.apple.quarantine anh3d0nic.py
```

**Issue: Python version conflicts**
```bash
# Use python3 explicitly
python3 anh3d0nic.py
```

### Windows Issues

**Issue: "python not recognized"**
```
1. Reinstall Python
2. Check "Add Python to PATH" during install
3. Or use: python instead of python3
```

**Issue: Script won't run**
```powershell
# Use the batch file
launch.bat

# Or run directly
python anh3d0nic.py
```

**Issue: Colors don't display properly**
```
Use Windows Terminal or PowerShell 7+ for better color support
```

## Advanced Troubleshooting

### Enable Debug Mode

Add to anh3d0nic.py at the top:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check System Requirements

```bash
# Python version (need 3.8+)
python3 --version

# Available RAM
free -h  # Linux
# or
vm_stat  # macOS

# Disk space
df -h
```

### Test Components Individually

**Test GPT4All:**
```python
from gpt4all import GPT4All
model = GPT4All("mistral-7b-openorca.gguf2.Q4_0.gguf")
print(model.generate("Hello"))
```

**Test Code Execution:**
```python
import subprocess
result = subprocess.run(['python3', '-c', 'print("test")'], capture_output=True)
print(result.stdout)
```

### Common Error Messages and Fixes

| Error | Likely Cause | Solution |
|-------|--------------|----------|
| `ModuleNotFoundError: gpt4all` | Package not installed | `pip3 install gpt4all` |
| `FileNotFoundError: model` | Model not downloaded | Wait for download or manual install |
| `MemoryError` | Insufficient RAM | Use smaller model or close apps |
| `TimeoutExpired` | Code/command too slow | Increase timeout or optimize code |
| `Permission denied` | Insufficient permissions | `chmod +x` or run as admin |
| `Connection refused` | Network/firewall issue | Check internet/firewall |

## Getting Help

If you're still stuck:

1. **Check logs**: Look at error messages carefully
2. **Search issues**: Common errors often have documented solutions
3. **Minimal test**: Try the simplest possible use case
4. **System info**: Note your OS, Python version, and error message
5. **GPT4All docs**: Check https://docs.gpt4all.io/

## Performance Optimization

### Make Anh3d0nic Faster

1. **Use a smaller model**:
   ```python
   model_name="orca-mini-3b.ggmlv3.q4_0.bin"
   ```

2. **Reduce max_tokens**:
   ```python
   max_tokens=200  # Instead of 500
   ```

3. **Limit conversation history**:
   ```python
   # Line ~200
   if len(self.conversation_history) > 10:  # Instead of 20
   ```

4. **Use CPU with multiple cores**:
   Ensure you're not running other CPU-intensive tasks

### Make Responses Better

1. **Use a larger model**:
   ```python
   model_name="wizardlm-13b-v1.2.Q4_0.gguf"
   ```

2. **Increase max_tokens**:
   ```python
   max_tokens=800  # More detailed responses
   ```

3. **Adjust temperature**:
   ```python
   temp=0.9  # More creative (0.1 = focused, 1.0 = creative)
   ```

## Still Having Issues?

Create a detailed report including:
- Operating System and version
- Python version (`python3 --version`)
- Error message (full text)
- What you were trying to do
- Steps you've already tried

---

**Most issues are resolved by ensuring Python 3.8+ is installed and gpt4all package is properly installed!**

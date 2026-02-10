# Anh3d0nic - Example Use Cases

This file contains example conversations and use cases to help you get started with Anh3d0nic.

## 1. Code Writing Examples

### Example: Simple Python Function
```
You: Write a Python function that checks if a number is prime

Anh3d0nic: Here's a function to check if a number is prime:

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

### Example: Data Processing
```
You: Create a Python script to read a CSV and calculate averages

Anh3d0nic: Here's a script to read CSV and calculate column averages:

import csv

def calculate_averages(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        # ... (full code provided)
```

## 2. Code Execution Examples

### Example: Quick Calculation
```
You: execute this code:
```python
result = sum(range(1, 101))
print(f"Sum of 1 to 100: {result}")
```

Anh3d0nic: Executing Python code...
Code executed successfully!

Output:
Sum of 1 to 100: 5050
```

### Example: Testing Code
```
You: execute this code:
```python
import random

# Simulate 100 coin flips
heads = sum(1 for _ in range(100) if random.choice(['H', 'T']) == 'H')
print(f"Heads: {heads}, Tails: {100-heads}")
```

Anh3d0nic: Executing Python code...
Code executed successfully!

Output:
Heads: 52, Tails: 48
```

## 3. System Administration Examples

### Example: Disk Usage
```
You: $ df -h

Anh3d0nic: Executing bash command...
Command executed successfully!

Output:
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       100G   45G   55G  45% /
...
```

### Example: Process Monitoring
```
You: bash: ps aux | grep python

Anh3d0nic: [Shows running Python processes]
```

### Example: File Management
```
You: $ ls -lah | head -10

Anh3d0nic: [Shows first 10 files with details]
```

## 4. Learning & Education Examples

### Example: Explain Concepts
```
You: Explain what a decorator is in Python with an example

Anh3d0nic: A decorator in Python is a function that modifies the behavior 
of another function. Here's a simple example:

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello world"

print(greet())  # Outputs: HELLO WORLD
```

### Example: Debug Help
```
You: Why does this code give an error?

for i in range(5)
    print(i)

Anh3d0nic: The code has a syntax error - you're missing a colon (:) after 
the for statement. It should be:

for i in range(5):
    print(i)
```

## 5. Web Search Examples

### Example: Latest News
```
You: search for Python 3.12 new features

Anh3d0nic: Searching the web...
[Returns search results about Python 3.12 features]
```

### Example: Documentation Lookup
```
You: search for pandas dataframe tutorial

Anh3d0nic: [Returns relevant tutorial links and information]
```

## 6. Multi-Turn Conversation Examples

### Example: Iterative Development
```
You: Write a function to calculate factorial

Anh3d0nic: [Provides basic factorial function]

You: Add input validation to handle negative numbers

Anh3d0nic: [Updates code with validation]

You: Now add memoization for performance

Anh3d0nic: [Adds memoization to the function]

You: Execute it with factorial(10)

Anh3d0nic: [Executes and shows result: 3628800]
```

### Example: Learning Path
```
You: I'm new to Python, what should I learn first?

Anh3d0nic: [Provides learning roadmap]

You: Show me an example of variables

Anh3d0nic: [Provides variable examples]

You: Now explain data types

Anh3d0nic: [Explains data types with examples]
```

## 7. Practical Project Examples

### Example: Building a Tool
```
You: Help me create a command-line todo list manager

Anh3d0nic: I'll help you create a simple todo list manager. Here's the basic structure:

import json
import sys

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
    
    # ... (continues with full implementation)

You: Add the ability to save to a file

Anh3d0nic: [Adds file saving functionality]

You: Execute it to test

Anh3d0nic: [Runs the code and shows results]
```

## 8. Code Review Examples

### Example: Security Review
```
You: Review this code for security issues:

password = input("Password: ")
if password == "admin123":
    print("Access granted")

Anh3d0nic: This code has several security issues:
1. Hardcoded password is visible in source code
2. Password is compared in plain text
3. No rate limiting for brute force attempts

Here's a better approach:
[Provides improved version with hashing]
```

## 9. Data Analysis Examples

### Example: Quick Stats
```
You: execute this code:
```python
data = [23, 45, 12, 67, 89, 34, 56, 78, 90, 23]
print(f"Mean: {sum(data)/len(data):.2f}")
print(f"Max: {max(data)}")
print(f"Min: {min(data)}")
```

Anh3d0nic: [Shows calculated statistics]
```

## 10. File Operations Examples

### Example: Read Configuration
```
You: read file config.txt

Anh3d0nic: [Displays file contents]
```

### Example: Create Script
```
You: Create a Python script that backs up files

Anh3d0nic: [Provides backup script code]

You: Save that to backup.py

Anh3d0nic: [Saves the script]
```

## Tips for Effective Use

1. **Be Specific**: Instead of "help with code", say "write a function to sort a list of dictionaries by a key"

2. **Iterate**: Start simple and add features step by step

3. **Test Immediately**: Use the execute feature to test code right away

4. **Combine Features**: Use web search for research, then code based on findings

5. **Save Work**: Important code can be saved to files for later use

6. **Learn by Doing**: Ask for examples, then execute them to see how they work

## Common Workflows

### Workflow 1: Research → Code → Test
```
1. search for algorithm for sorting
2. Write a sorting function based on research
3. execute this code: [test the function]
4. Fix any issues
5. Save to file
```

### Workflow 2: Debug Existing Code
```
1. read file buggy_script.py
2. Explain what might be wrong
3. Here's the fixed version
4. execute this code: [test the fix]
```

### Workflow 3: Learn New Concept
```
1. Explain [concept]
2. Show me an example
3. Let me try - execute this code: [your attempt]
4. What did I do wrong?
5. Correct version
```

## Advanced Examples

### Example: API Integration
```
You: Write code to fetch data from a REST API

Anh3d0nic: [Provides requests-based code]

You: Add error handling and retry logic

Anh3d0nic: [Enhances code with error handling]
```

### Example: Automation Script
```
You: Create a script that monitors a directory and logs changes

Anh3d0nic: [Provides watchdog-based solution]
```

### Example: Data Pipeline
```
You: Build a script that reads CSV, processes data, and outputs JSON

Anh3d0nic: [Provides complete pipeline code]
```

---

**Try these examples and discover your own use cases!**

Remember: Anh3d0nic learns from context, so you can build on previous conversations!

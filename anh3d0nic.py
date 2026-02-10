#!/usr/bin/env python3
"""
Anh3d0nic - Free Local AI CLI Agent
A powerful AI assistant that runs completely locally without API keys or usage limits.
"""

import sys
import os
import json
import subprocess
import re
from pathlib import Path
from typing import Optional, Dict, List, Any
import readline  # For better input handling

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class CodeExecutor:
    """Handles safe code execution"""
    
    @staticmethod
    def execute_python(code: str) -> Dict[str, Any]:
        """Execute Python code safely"""
        try:
            # Create a temporary file
            temp_file = "/tmp/anh3d0nic_temp.py"
            with open(temp_file, 'w') as f:
                f.write(code)
            
            # Execute with timeout
            result = subprocess.run(
                [sys.executable, temp_file],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout,
                'error': result.stderr
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': '', 'error': 'Execution timeout (30s limit)'}
        except Exception as e:
            return {'success': False, 'output': '', 'error': str(e)}
    
    @staticmethod
    def execute_bash(command: str) -> Dict[str, Any]:
        """Execute bash command safely"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout,
                'error': result.stderr
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': '', 'error': 'Execution timeout (30s limit)'}
        except Exception as e:
            return {'success': False, 'output': '', 'error': str(e)}


class WebBrowser:
    """Handles web browsing capabilities"""
    
    @staticmethod
    def search_web(query: str) -> str:
        """Search the web using curl and a search engine"""
        try:
            # Using DuckDuckGo Lite for simple searches
            url = f"https://lite.duckduckgo.com/lite/?q={query.replace(' ', '+')}"
            result = subprocess.run(
                ['curl', '-s', '-A', 'Mozilla/5.0', url],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                return result.stdout[:1000]  # Limit output
            return "Search failed"
        except:
            return "Web search unavailable (curl not installed)"
    
    @staticmethod
    def fetch_url(url: str) -> str:
        """Fetch content from a URL"""
        try:
            result = subprocess.run(
                ['curl', '-s', '-L', url],
                capture_output=True,
                text=True,
                timeout=15
            )
            if result.returncode == 0:
                return result.stdout[:2000]  # Limit output
            return "Failed to fetch URL"
        except:
            return "URL fetch unavailable (curl not installed)"


class FileManager:
    """Handles file operations"""
    
    @staticmethod
    def read_file(filepath: str) -> str:
        """Read file contents"""
        try:
            with open(filepath, 'r') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"
    
    @staticmethod
    def write_file(filepath: str, content: str) -> str:
        """Write content to file"""
        try:
            with open(filepath, 'w') as f:
                f.write(content)
            return f"Successfully wrote to {filepath}"
        except Exception as e:
            return f"Error writing file: {str(e)}"
    
    @staticmethod
    def list_directory(path: str = ".") -> str:
        """List directory contents"""
        try:
            items = os.listdir(path)
            return "\n".join(items)
        except Exception as e:
            return f"Error listing directory: {str(e)}"


class Anh3d0nicAgent:
    """Main AI Agent class"""
    
    def __init__(self):
        self.conversation_history = []
        self.model = None
        self.model_loaded = False
        self.executor = CodeExecutor()
        self.browser = WebBrowser()
        self.file_manager = FileManager()
        self.tools_enabled = True
        
    def load_model(self):
        """Load the GPT4All model"""
        print(f"{Colors.OKCYAN}Initializing Anh3d0nic AI Brain...{Colors.ENDC}")
        
        try:
            from gpt4all import GPT4All
            
            # Check if model exists, if not download it
            model_path = Path.home() / ".cache" / "gpt4all"
            model_path.mkdir(parents=True, exist_ok=True)
            
            print(f"{Colors.WARNING}Loading AI model (this may take a moment on first run)...{Colors.ENDC}")
            
            # Use a lightweight model - mistral is good balance of speed and quality
            self.model = GPT4All(
                model_name="mistral-7b-openorca.gguf2.Q4_0.gguf",
                model_path=str(model_path),
                allow_download=True,
                device='cpu'  # Use CPU for compatibility
            )
            
            self.model_loaded = True
            print(f"{Colors.OKGREEN}✓ Anh3d0nic AI Brain loaded successfully!{Colors.ENDC}\n")
            
        except ImportError:
            print(f"{Colors.FAIL}Error: GPT4All not installed!{Colors.ENDC}")
            print(f"{Colors.WARNING}Please install it with: pip install gpt4all{Colors.ENDC}")
            self.model_loaded = False
        except Exception as e:
            print(f"{Colors.FAIL}Error loading model: {str(e)}{Colors.ENDC}")
            self.model_loaded = False
    
    def detect_intent(self, message: str) -> Dict[str, Any]:
        """Detect what the user wants to do"""
        message_lower = message.lower()
        
        # Code execution patterns
        if any(kw in message_lower for kw in ['execute', 'run code', 'run this', 'execute code']):
            # Extract code blocks
            code_match = re.search(r'```(?:python|py)?\n(.*?)```', message, re.DOTALL)
            if code_match:
                return {'type': 'execute_python', 'code': code_match.group(1)}
        
        # Web search patterns
        if any(kw in message_lower for kw in ['search for', 'search web', 'find information about', 'look up']):
            query = re.sub(r'(search for|search web|find information about|look up)\s*', '', message_lower, count=1)
            return {'type': 'web_search', 'query': query}
        
        # File operations
        if 'read file' in message_lower:
            filepath = message_lower.replace('read file', '').strip()
            return {'type': 'read_file', 'filepath': filepath}
        
        if 'write file' in message_lower or 'create file' in message_lower:
            return {'type': 'write_file', 'message': message}
        
        # Bash commands
        if message_lower.startswith('bash:') or message_lower.startswith('$'):
            command = message[5:].strip() if message_lower.startswith('bash:') else message[1:].strip()
            return {'type': 'bash', 'command': command}
        
        return {'type': 'chat', 'message': message}
    
    def execute_tool(self, intent: Dict[str, Any]) -> str:
        """Execute the appropriate tool based on intent"""
        
        if intent['type'] == 'execute_python':
            print(f"{Colors.OKCYAN}Executing Python code...{Colors.ENDC}")
            result = self.executor.execute_python(intent['code'])
            if result['success']:
                return f"Code executed successfully!\n\nOutput:\n{result['output']}"
            else:
                return f"Code execution failed!\n\nError:\n{result['error']}"
        
        elif intent['type'] == 'bash':
            print(f"{Colors.OKCYAN}Executing bash command...{Colors.ENDC}")
            result = self.executor.execute_bash(intent['command'])
            if result['success']:
                return f"Command executed successfully!\n\nOutput:\n{result['output']}"
            else:
                return f"Command failed!\n\nError:\n{result['error']}"
        
        elif intent['type'] == 'web_search':
            print(f"{Colors.OKCYAN}Searching the web...{Colors.ENDC}")
            return self.browser.search_web(intent['query'])
        
        elif intent['type'] == 'read_file':
            return self.file_manager.read_file(intent['filepath'])
        
        elif intent['type'] == 'write_file':
            # This would need more parsing in a real implementation
            return "File writing requires: write file <path> with content: <content>"
        
        return None
    
    def generate_response(self, message: str) -> str:
        """Generate AI response"""
        
        if not self.model_loaded:
            return "AI model not loaded. Please restart the application."
        
        # Check for tool usage first
        intent = self.detect_intent(message)
        
        if intent['type'] != 'chat' and self.tools_enabled:
            tool_result = self.execute_tool(intent)
            if tool_result:
                # Also get AI commentary on the result
                context = f"The user asked: {message}\n\nTool execution result:\n{tool_result}\n\nProvide a brief helpful response about this result."
                try:
                    ai_response = self.model.generate(context, max_tokens=200)
                    return f"{tool_result}\n\n{Colors.OKGREEN}Anh3d0nic:{Colors.ENDC} {ai_response}"
                except:
                    return tool_result
        
        # Regular chat
        try:
            # Build context from conversation history
            context = self._build_context(message)
            
            # Generate response
            response = self.model.generate(
                context,
                max_tokens=500,
                temp=0.7,
                top_p=0.9
            )
            
            # Store in history
            self.conversation_history.append({
                'role': 'user',
                'content': message
            })
            self.conversation_history.append({
                'role': 'assistant',
                'content': response
            })
            
            # Keep history manageable
            if len(self.conversation_history) > 20:
                self.conversation_history = self.conversation_history[-20:]
            
            return response
            
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def _build_context(self, message: str) -> str:
        """Build context for the model"""
        system_prompt = """You are Anh3d0nic, a helpful AI assistant with code execution, web browsing, and file management capabilities. 
You are knowledgeable, concise, and practical. You can help with programming, answer questions, and perform tasks.
Be direct and helpful. Keep responses focused and under 3 paragraphs unless more detail is specifically requested."""
        
        context = f"{system_prompt}\n\n"
        
        # Add recent history
        for msg in self.conversation_history[-6:]:  # Last 3 exchanges
            role = "User" if msg['role'] == 'user' else "Anh3d0nic"
            context += f"{role}: {msg['content']}\n\n"
        
        context += f"User: {message}\n\nAnh3d0nic:"
        
        return context
    
    def run(self):
        """Main chat loop"""
        self.print_banner()
        self.load_model()
        
        if not self.model_loaded:
            print(f"{Colors.FAIL}Failed to load AI model. Exiting.{Colors.ENDC}")
            return
        
        self.print_help()
        
        print(f"{Colors.OKGREEN}Anh3d0nic is ready! Type your message or 'help' for commands.{Colors.ENDC}\n")
        
        while True:
            try:
                # Get user input
                user_input = input(f"{Colors.BOLD}{Colors.OKBLUE}You: {Colors.ENDC}").strip()
                
                if not user_input:
                    continue
                
                # Handle special commands
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print(f"{Colors.OKCYAN}Goodbye! Anh3d0nic shutting down...{Colors.ENDC}")
                    break
                
                if user_input.lower() == 'help':
                    self.print_help()
                    continue
                
                if user_input.lower() == 'clear':
                    os.system('clear' if os.name != 'nt' else 'cls')
                    self.print_banner()
                    continue
                
                if user_input.lower() == 'reset':
                    self.conversation_history = []
                    print(f"{Colors.OKGREEN}Conversation history cleared!{Colors.ENDC}\n")
                    continue
                
                # Generate and print response
                print(f"\n{Colors.OKGREEN}{Colors.BOLD}Anh3d0nic:{Colors.ENDC} ", end='', flush=True)
                response = self.generate_response(user_input)
                print(response)
                print()  # Empty line for readability
                
            except KeyboardInterrupt:
                print(f"\n{Colors.OKCYAN}Goodbye! Anh3d0nic shutting down...{Colors.ENDC}")
                break
            except Exception as e:
                print(f"{Colors.FAIL}Error: {str(e)}{Colors.ENDC}\n")
    
    def print_banner(self):
        """Print welcome banner"""
        banner = f"""
{Colors.HEADER}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║     █████╗ ███╗   ██╗██╗  ██╗██████╗ ██████╗  ██████╗       ║
║    ██╔══██╗████╗  ██║██║  ██║╚════██╗██╔══██╗██╔═████╗      ║
║    ███████║██╔██╗ ██║███████║ █████╔╝██║  ██║██║██╔██║      ║
║    ██╔══██║██║╚██╗██║██╔══██║ ╚═══██╗██║  ██║████╔╝██║      ║
║    ██║  ██║██║ ╚████║██║  ██║██████╔╝██████╔╝╚██████╔╝      ║
║    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═════╝  ╚═════╝       ║
║                                                               ║
║              N  I  C     -     Local AI Agent                ║
║                                                               ║
║              🤖 Free • No API Keys • Unlimited 🤖            ║
╚═══════════════════════════════════════════════════════════════╝
{Colors.ENDC}
        """
        print(banner)
    
    def print_help(self):
        """Print help information"""
        help_text = f"""
{Colors.OKCYAN}{Colors.BOLD}Available Commands:{Colors.ENDC}
  {Colors.OKGREEN}help{Colors.ENDC}          - Show this help message
  {Colors.OKGREEN}clear{Colors.ENDC}         - Clear the screen
  {Colors.OKGREEN}reset{Colors.ENDC}         - Reset conversation history
  {Colors.OKGREEN}exit/quit{Colors.ENDC}     - Exit Anh3d0nic

{Colors.OKCYAN}{Colors.BOLD}Capabilities:{Colors.ENDC}
  {Colors.OKGREEN}💬 Chat{Colors.ENDC}        - Just type naturally to chat
  {Colors.OKGREEN}💻 Code{Colors.ENDC}        - Ask me to write, fix, or explain code
  {Colors.OKGREEN}▶️  Execute{Colors.ENDC}     - Run Python: "execute this code: ```python\\nprint('hi')\\n```"
  {Colors.OKGREEN}🐚 Bash{Colors.ENDC}        - Run commands: "bash: ls -la" or "$ pwd"
  {Colors.OKGREEN}🌐 Web{Colors.ENDC}         - Search: "search for python tutorials"
  {Colors.OKGREEN}📁 Files{Colors.ENDC}       - Read: "read file example.txt"

{Colors.OKCYAN}{Colors.BOLD}Examples:{Colors.ENDC}
  • "Write a Python script to sort a list"
  • "Execute this code: ```python\\nfor i in range(5): print(i)\\n```"
  • "Search for latest Python news"
  • "$ ls -lah"
  • "Explain recursion with examples"
        """
        print(help_text)


def main():
    """Entry point"""
    agent = Anh3d0nicAgent()
    agent.run()


if __name__ == "__main__":
    main()

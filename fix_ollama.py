# fix_ollama.py
import subprocess
import time
import requests

print("🔧 Fixing Ollama setup...")

# 1. Kill existing Ollama processes
subprocess.run(['taskkill', '/f', '/im', 'ollama.exe'], 
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 2. Start Ollama server
print("Starting Ollama server...")
subprocess.Popen(['ollama', 'serve'], 
                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 3. Wait and check
time.sleep(3)
try:
    resp = requests.get('http://localhost:11434/api/tags', timeout=5)
    print(f"✅ Ollama server responding: {resp.status_code}")
    
    # 4. Pull phi model if needed
    if 'phi' not in resp.text:
        print("Downloading phi model...")
        subprocess.run(['ollama', 'pull', 'phi'])
        print("✅ Model downloaded")
    else:
        print("✅ phi model already available")
        
except:
    print("❌ Ollama not starting. Please install Ollama from: https://ollama.com")
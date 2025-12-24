"""
LUXION VOICE ASSISTANT - COMPLETE WORKING VERSION
Opens in STANDALONE APP WINDOW (not Chrome browser)
"""

import os
import sys
import socket
import sqlite3
import tempfile
import eel
from engine.features import *
from engine.command import *

def find_available_port(start_port=8000, max_port=8010):
    """Find an available port"""
    for port in range(start_port, max_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('localhost', port))
            s.close()
            return port
        except:
            continue
    return start_port

def main():
    print("🚀 Starting Luxion Voice Assistant...")
    
    # Find available port
    port = find_available_port(8000, 8010)
    print(f"📡 Using port: {port}")
    
    # Initialize database
    try:
        conn = sqlite3.connect("sophia.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS sys_command
                         (id INTEGER PRIMARY KEY, 
                          name VARCHAR(100), 
                          path VARCHAR(1000))''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS web_command
                         (id INTEGER PRIMARY KEY, 
                          name VARCHAR(100), 
                          url VARCHAR(1000))''')
        conn.commit()
        conn.close()
        print("✅ Database initialized")
    except Exception as e:
        print(f"⚠️ Database error: {e}")
    
    # Initialize Eel
    eel.init('www')
    
    # Play startup sound
    try:
        playAssistantSound()
    except:
        print("⚠️ Could not play startup sound")
    
    print(f"\n🎯 Opening Luxion in STANDALONE APP WINDOW...")
    print(f"   URL: http://localhost:{port}")
    
    # CRITICAL: This opens in REAL app window (not Chrome tab)
    eel.start(
        'index.html',
        mode='chrome',  # Use 'chrome' mode but with app flags
        host='localhost',
        port=port,
        size=(1200, 800),
        position=(100, 100),
        block=True,
        cmdline_args=[
            '--app=http://localhost:{}'.format(port),  # MOST IMPORTANT - opens as app
            '--window-size=1200,800',
            '--window-position=100,100',
            '--disable-infobars',  # Hides "Chrome is controlled" message
            '--disable-extensions',
            '--disable-plugins',
            '--disable-translate',
            '--no-first-run',
            '--no-default-browser-check',
            '--disable-features=TranslateUI',
            '--disable-sync',
            '--disable-background-networking',
            '--disable-component-extensions-with-background-pages',
            '--disable-component-update',
            '--disable-default-apps',
            '--disable-domain-reliability',
            '--disable-breakpad',
            '--disable-backgrounding-occluded-windows',
            '--disable-renderer-backgrounding',
            '--disable-background-timer-throttling',
            '--disable-ipc-flooding-protection',
            '--disable-background-networking',
            '--metrics-recording-only',
            '--disable-prompt-on-repost',
            '--disable-hang-monitor',
            '--disable-prompt-on-repost',
            '--disable-client-side-phishing-detection',
            '--password-store=basic',
            '--use-mock-keychain',
            '--disable-component-update',
            '--disable-default-apps',
            '--disable-breakpad',
            '--disable-dev-shm-usage',
            '--disable-background-timer-throttling',
            '--disable-renderer-backgrounding',
            '--disable-backgrounding-occluded-windows',
            '--disable-ipc-flooding-protection',
            '--disable-background-networking',
            '--no-pings',
            '--no-experiments',
            '--no-crash-upload',
            '--disable-sync',
            '--disable-web-resources',
            '--safebrowsing-disable-auto-update',
            '--safebrowsing-disable-download-protection',
            '--disable-logging',
            '--disable-in-process-stack-traces',
            '--silent-debugger-extension-api',
            '--disable-search-engine-choice-screen',
            '--no-service-autorun',
            '--disable-component-update',
            '--disable-features=HardwareMediaKeyHandling,MediaRouter',
            '--disable-reading-from-canvas',
            '--no-default-browser-check',
            '--disable-component-update',
            '--disable-default-apps',
            '--disable-domain-reliability',
            '--disable-breakpad',
            '--disable-backgrounding-occluded-windows',
            '--disable-renderer-backgrounding',
            '--disable-background-timer-throttling',
            '--disable-ipc-flooding-protection',
            '--disable-background-networking',
            '--metrics-recording-only',
            '--disable-prompt-on-repost',
            '--disable-hang-monitor',
            '--disable-prompt-on-repost',
            '--disable-client-side-phishing-detection',
            '--password-store=basic',
            '--use-mock-keychain'
        ]
    )

if __name__ == "__main__":
    main()
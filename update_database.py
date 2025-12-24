import sqlite3
import os

def add_apps_to_database():
    conn = sqlite3.connect("sophia.db")
    cursor = conn.cursor()

    common_apps = [
        ('chrome', 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'),
        ('firefox', 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'),
        ('spotify', 'C:\\Users\\{}\\AppData\\Roaming\\Spotify\\Spotify.exe'.format(os.getlogin())),
        ('whatsapp', 'C:\\Users\\{}\\AppData\\Local\\WhatsApp\\WhatsApp.exe'.format(os.getlogin())),
        ('telegram', 'C:\\Users\\{}\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe'.format(os.getlogin())),
        ('steam', 'C:\\Program Files (x86)\\Steam\\Steam.exe'),
        ('vscode', 'C:\\Users\\{}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'.format(os.getlogin())),
        ('notepad', 'notepad.exe'),
        ('calculator', 'calc.exe'),
        ('cmd', 'cmd.exe'),
        ('paint', 'mspaint.exe'),
        ('discord', 'C:\\Users\\{}\\AppData\\Local\\Discord\\Update.exe'.format(os.getlogin())),
    ]
    
    for app_name, app_path in common_apps:
        # Check if already exists
        cursor.execute('SELECT * FROM sys_command WHERE LOWER(name) = ?', (app_name,))
        if not cursor.fetchall():
            cursor.execute('INSERT INTO sys_command (name, path) VALUES (?, ?)', (app_name, app_path))
            print(f"Added {app_name}: {app_path}")
    
    conn.commit()
    conn.close()
    print("Database updated successfully!")

if __name__ == "__main__":
    add_apps_to_database()
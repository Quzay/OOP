import pyautogui
import os

def open_terminal():
    try:
        os.system("ghostty &")
        print("🚀 Ghostty запуск...")
    except Exception as e:
        print(f"🚨 Помилка: {e}")

def show_alert(text):
   
    pyautogui.alert(text)

def take_screenshot():
    pyautogui.screenshot('src/myproject/last_snap.png')

def type_text(text="Hello from Poetry!"):
    pyautogui.write(text, interval=0.1)

import os
from flask import Flask, render_template
from .actions import open_terminal, take_screenshot, type_text, show_alert


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

app = Flask(__name__, template_folder=TEMPLATE_DIR)

@app.route('/')
def index():
    if not os.path.exists(os.path.join(TEMPLATE_DIR, 'index.html')):
        return f"🚨 Файла нема! Шукав тут: {TEMPLATE_DIR}"
    return render_template('index.html')

@app.route('/run/<command>')
def run_command(command):
    status_msg = ""
    if command == 'terminal':
        open_terminal()
        status_msg = "Термінал відкрито"
    elif command == 'screenshot':
        take_screenshot()
        status_msg = "Скріншот збережено"
    elif command == 'type':
        type_text()
        status_msg = "Текст надруковано"
    elif command == 'alert':
        show_alert("Лаба 6: Poetry працює!")
        status_msg = "Сповіщення виведено"
    
    return render_template('index.html', status=status_msg)

if __name__ == '__main__':
    app.run(debug=True)
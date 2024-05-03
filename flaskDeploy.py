from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Проверяем, что запрос пришел от GitHub и событие - push
    if request.headers.get('X-GitHub-Event') == 'push':
        payload = request.json
        ref = payload['ref']
        headCommit = payload['head_commit']
        modified = headCommit['modified']


        # Проверяем, что событие - push в ветку master
        if ref == 'refs/heads/master' and "testdrone/main.py" in modified:
        
            # Запускаем скрипт для обработки события
            cwd = '/testdrone'  # Укажите путь к вашей папке
            pwd = os.getcwd()
            path=pwd+cwd
            print(path)
            
            #NOTE
            #chmod +x deploy.sh #для прав на исполнение
            subprocess.Popen([f'{path}/deploy.sh'], cwd=pwd+cwd)

    return jsonify({'message': 'Webhook received'}), 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

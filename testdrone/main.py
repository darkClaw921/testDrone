from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def webhook():
    # Проверяем, что запрос пришел от GitHub и событие - push
    
       

    return jsonify({'message': 'Webhook received222'}), 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=3005)
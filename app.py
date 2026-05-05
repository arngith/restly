import os
import requests
from flask import Flask, render_template, request, jsonify, send_from_directory
from dotenv import load_dotenv

load_dotenv()
#test #test
app = Flask(__name__)  

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def home():
    return render_template('index.html', 
                           hf_token=os.getenv("HF_TOKEN"), 
                           api_lokal=os.getenv("API_LOKAL"), 
                           api_public=os.getenv("API_PUBLIC"),
                           agent=os.getenv("AGENT"),
                           module=os.getenv("MODULE"))

@app.route('/pcm-processor.js')
def serve_pcm_processor():
    return send_from_directory('templates', 'pcm-processor.js', mimetype='application/javascript')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/<agent>/<module>', methods=['POST', 'OPTIONS'])
def chat(agent, module):
    if request.method == 'OPTIONS':
        return jsonify({}), 200
        
    data = request.get_json()
    user_message = data.get('message')
    
    payload = {
        "message": user_message,
        "history": [],
        "conversation_id": ""
    }

    if request.host.startswith('localhost') or request.host.startswith('127.0.0.1'):
        api_base = os.getenv("API_LOKAL")
    else:
        api_base = os.getenv("API_PUBLIC")

    api_url = f"{api_base}/{agent}/{module}"

    try:
        hf_token = os.getenv("HF_TOKEN")
        print(f"Debug: Mengirim request ke {api_url} dengan token: {hf_token[:5]}***")
        headers = {"Authorization": f"Bearer {hf_token}"}
        api_response = requests.post(api_url, json=payload, headers=headers, timeout=60)
        print(f"Debug: Respons dari API: {api_response.status_code}")
        response_data = api_response.json()
        if response_data.get('status_code') == 200:
            bot_reply = response_data.get('response')
        else:
            bot_reply = "Maaf, terjadi kesalahan dari server AI."

    except requests.exceptions.RequestException as e:
        print(f"Error API: {e}")
        bot_reply = "Maaf, server AI sedang tidak dapat dihubungi saat ini. Silakan coba beberapa saat lagi."
    
    return jsonify({'response': bot_reply})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 7860))
    app.run(host='0.0.0.0', port=port, debug=True)
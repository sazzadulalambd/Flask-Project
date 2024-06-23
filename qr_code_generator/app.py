from flask import Flask, request, jsonify, send_file
import qrcode
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    img = qrcode.make(data)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    return jsonify({'qr_code': img_str})

@app.route('/download_qr', methods=['POST'])
def download_qr():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    img = qrcode.make(data)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    buffered.seek(0)
    
    return send_file(buffered, mimetype='image/png', as_attachment=True, download_name='qrcode.png')

if __name__ == '__main__':
    app.run(debug=True)

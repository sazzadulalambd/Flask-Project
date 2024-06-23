from flask import Flask, render_template, request, jsonify
import qrcode
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Function to generate a QR code image with a logo
def generate_qr_code(data, color="#000000", logo_file=None):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=color, back_color="white").convert('RGB')

    if logo_file:
        logo = Image.open(logo_file)
        # Calculate logo size and position
        logo_size = int(qr_img.size[0] * 0.25)  # 25% of the QR code size
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        logo_position = (
            (qr_img.size[0] - logo_size) // 2,
            (qr_img.size[1] - logo_size) // 2,
        )
        qr_img.paste(logo, logo_position, mask=logo if logo.mode == 'RGBA' else None)

    buffered = BytesIO()
    qr_img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

# Route to render index.html for QR code generation
@app.route('/')
def index():
    return render_template('index.html')

# Route to render contact_form.html for submitting contacts
@app.route('/contact_form')
def contact_form():
    return render_template('contact_form.html')

# Endpoint to handle submission of contact form data
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    additional_info = request.form.get('additional_info')
    qr_color = request.form.get('qr_color', '#000000')
    logo = request.files.get('logo')

    if not name or not phone or not email:
        return jsonify({'error': 'Please fill in all required fields.'}), 400

    vcard = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEMAIL:{email}\nNOTE:{additional_info}\nEND:VCARD"

    img_str = generate_qr_code(vcard, qr_color, logo)

    return jsonify({'qr_code': img_str})

# Endpoint to generate QR code from input data
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form.get('data')
    qr_color = request.form.get('qrColor', '#000000')
    logo = request.files.get('logo')

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    img_str = generate_qr_code(data, qr_color, logo)

    return jsonify({'qr_code': img_str})

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify, send_file
import qrcode
import base64
from io import BytesIO

app = Flask(__name__)


# Mock storage for contacts (replace with database or file storage in production)
contacts = []

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
    qr_color = request.form.get('qr_color', '#000000')  # Default color if not provided

    if not name or not phone or not email:
        return jsonify({'error': 'Please fill in all required fields.'}), 400

    # Create vCard (virtual contact file) content
    vcard = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEMAIL:{email}\nNOTE:{additional_info}\nEND:VCARD"

    # Generate QR code for vCard
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=qr_color, back_color="white")

    buffered = BytesIO()
    qr_img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return jsonify({'qr_code': img_str})


# Endpoint to generate QR code from input data
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json.get('data')
    qr_color = request.json.get('qrColor', '#000000')  # Default color is black (#000000)

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=qr_color, back_color="white")

    buffered = BytesIO()
    qr_img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return jsonify({'qr_code': img_str})


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)

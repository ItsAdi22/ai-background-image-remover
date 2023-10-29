from flask import Flask, render_template, request, redirect, url_for
import os
from PIL import Image
from rembg import remove  # Make sure to install the rembg library

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/output', methods=['POST'])
def output():
    img = request.files['img']
    
    if img:
        # Save the uploaded image
        img_path = os.path.join('static/input', img.filename)
        img.save(img_path)

        # Process the uploaded image using rembg
        input_image = Image.open(img_path)  # Assuming you have PIL installed
        output_image = remove(input_image)
        output_path = os.path.join('static/output', img.filename)
        output_image.save(output_path)
        
        return render_template('output.html', input_image=img_path, output_image=output_path)

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import os
from PIL import Image
from rembg import remove  # Make sure to install the rembg library

app = Flask(__name__)

@app.route('/')
def home():
    try:
    #we delete all the existing input and output images (to save space :D)
    input_dir_path = './static/input/'
    output_dir_path = './static/output/'
    
    for x in os.listdir(input_dir_path):
        filename = os.path.join(input_dir_path,x)
        os.remove(filename)

    for x in os.listdir(output_dir_path):
        filename = os.path.join(output_dir_path,x)
        os.remove(filename)

    
except Exception as e:
    print(f'Could not delete: {e}')
    
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

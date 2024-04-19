
# main.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def press_release():
    return render_template('press_release.html')

@app.route('/about')
def about_product():
    return render_template('about_product.html')

@app.route('/download-press-kit')
def download_press_kit():
    return 'Download Link'

if __name__ == '__main__':
    app.run(debug=True)

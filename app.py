from flask import Flask, render_template_string
import os
import sys

app = Flask(__name__)

VALID_COLORS = {'white', 'black', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta'}

@app.route('/')
def home():
    color = os.getenv('PAGE_COLOUR', 'white')
    
    if color not in VALID_COLORS:
        sys.exit(f"Invalid color: {color}. Must be one of: {', '.join(VALID_COLORS)}")

    html = f"""
    <html>
        <head><title>Web Page Colour</title></head>
        <body style="background-color: {color};">
            <h1>The background colour of this page is {color}!</h1>
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
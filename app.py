from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Get the colour from the environment variable, default to "white" if not set
    colour = os.getenv('PAGE_COLOUR', 'white')
    html = f"""
    <html>
        <head><title>Web Page Colour</title></head>
        <body style="background-color: {colour};">
            <h1>The background colour of this page is {colour}!</h1>
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

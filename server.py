from flask import Flask, render_template

app = Flask(__name__)

with open('client_id', 'r') as f:
    client_id = f.read().strip()
with open('callback_url', 'r') as f:
    callback_url = f.read().strip()

@app.route('/')
def page_index():
    return render_template('index.html', client_id=client_id, callback_url=callback_url)

@app.route('/callback')
def page_callback():
    return render_template('callback.html', client_id=client_id, callback_url=callback_url)

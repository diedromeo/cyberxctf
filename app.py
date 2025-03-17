from flask import Flask, request, send_file, render_template
import os

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template("index.html", theme="Loki and the Multiverse")

@app.route('/read')
def read_file():
    file = request.args.get('file', '')
    if not file:
        return "No timeline specified.", 400
    
    file_path = os.path.join("files/textfiles/uploads/", file)
    
    try:
        return send_file(file_path)
    except Exception:
        return "The TVA has restricted access to this timeline!", 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template, send_from_directory
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/resume")
def resume():
    return send_from_directory(BASE_DIR / "resume", "Talal_Siddiqui_Resume_Upd.pdf", as_attachment=False)

@app.route("/certificate")
def certificate():
    return send_from_directory(
        BASE_DIR / "certificates",
        "Microsoft_Certified_Professional_Certificate.pdf",
        as_attachment=False
    )

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)

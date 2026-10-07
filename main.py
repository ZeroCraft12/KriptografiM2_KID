import os
import sys
import importlib.util
import webbrowser
from threading import Timer
from flask import Flask, request, jsonify, render_template, Response

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

app = Flask(__name__)

from Beaufort import beaufort_transform
from Vigenere import encrypt_vigenere, decrypt_vigenere


def _load_spaced(name, filename):
    """Load a module whose filename contains spaces."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(BASE_DIR, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_caesar = _load_spaced("caesar_cipher", "Caesar Cipher.py")
caesar_transform = _caesar.caesar_transform

_foursquare = _load_spaced("four_square", "Four Square.py")
four_square_encipher = _foursquare.four_square_encipher
four_square_decipher = _foursquare.four_square_decipher


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    try:
        method = request.form.get("method", "")
        action = request.form.get("action", "")

        input_file = request.files.get("input_file")
        if input_file and input_file.filename:
            input_text = input_file.read().decode("utf-8-sig", errors="replace")
        else:
            input_text = request.form.get("input_text", "")

        if not input_text.strip():
            return jsonify({"error": "Teks input tidak boleh kosong."})

        if method == "beaufort":
            key = _read_key(request)
            if not key:
                return jsonify({"error": "Key tidak boleh kosong."})
            result = beaufort_transform(input_text, key)

        elif method == "caesar":
            try:
                shift = int(request.form.get("key_shift", 0))
            except (ValueError, TypeError):
                return jsonify({"error": "Key Caesar harus berupa angka (0-25)."})
            mode = "encrypt" if action == "encrypt" else "decrypt"
            result = caesar_transform(input_text, shift, mode)

        elif method == "foursquare":
            key1 = request.form.get("key1", "").strip()
            key2 = request.form.get("key2", "").strip()
            if not key1 or not key2:
                return jsonify({"error": "Key 1 dan Key 2 harus diisi."})
            if action == "encrypt":
                result = four_square_encipher(input_text, key1, key2)
            else:
                result = four_square_decipher(input_text, key1, key2)

        elif method == "vigenere":
            key = _read_key(request)
            if not key:
                return jsonify({"error": "Key tidak boleh kosong."})
            if action == "encrypt":
                result = encrypt_vigenere(input_text, key)
            else:
                result = decrypt_vigenere(input_text, key)

        else:
            return jsonify({"error": "Metode tidak valid."})

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)})


def _read_key(req):
    """Read key from uploaded file or text field."""
    key_file = req.files.get("key_file")
    if key_file and key_file.filename:
        return key_file.read().decode("utf-8-sig", errors="replace").strip()
    return req.form.get("key_text", "").strip()


@app.route("/download", methods=["GET", "POST"])
def download():
    if request.method == "POST":
        text = request.form.get("text", "")
    else:
        text = request.args.get("text", "")
    return Response(
        text,
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment; filename=output.txt"},
    )


if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true" or not app.debug:
        Timer(1.0, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    app.run(debug=True, port=5000)

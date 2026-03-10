from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
import shutil
import uuid

from image_processor import process_exam_image

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
PROCESSED_DIR = os.path.join(BASE_DIR, "static", "processed_images")

# Allowed file extensions (case-insensitive)
ALLOWED_EXTENSIONS = {"jpg", "jpeg"}

# Ensure folders exist
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    exam = request.form.get("exam", "").strip()
    img_type = request.form.get("img_type", "").strip()
    uploaded_file = request.files.get("file")

    error_msg = None
    success_msg = None
    download_filename = None
    suggest_signature = False

    if not uploaded_file or uploaded_file.filename == "":
        error_msg = "Please choose a JPG/JPEG image to upload."
        return render_template(
            "index.html",
            error_msg=error_msg,
            exam=exam,
            img_type=img_type,
        )

    if not allowed_file(uploaded_file.filename):
        error_msg = "Only JPG and JPEG images are allowed."
        return render_template(
            "index.html",
            error_msg=error_msg,
            exam=exam,
            img_type=img_type,
        )

    safe_name = secure_filename(uploaded_file.filename)
    input_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4().hex}_{safe_name}")

    try:
        # Save uploaded file
        uploaded_file.save(input_path)

        # Process image using existing logic
        result = process_exam_image(exam, img_type, input_path)

        if result.startswith("SUCCESS:"):
            # Extract output filename created by practice.py
            output_name = result.split("SUCCESS:", 1)[1].split("(", 1)[0].strip()
            output_path = os.path.join(BASE_DIR, output_name)

            if os.path.exists(output_path):
                final_name = f"{uuid.uuid4().hex}_{output_name}"
                final_path = os.path.join(PROCESSED_DIR, final_name)
                shutil.move(output_path, final_path)
                download_filename = final_name
                success_msg = result

                # Suggest signature if photo was processed
                if img_type.lower() == "photo":
                    suggest_signature = True
            else:
                error_msg = "Processed file was not found. Please try again."
        else:
            error_msg = result

    except Exception as e:
        error_msg = f"Upload failed: {str(e)}"

    finally:
        # Clean up uploaded file
        if os.path.exists(input_path):
            try:
                os.remove(input_path)
            except Exception:
                pass

    return render_template(
        "index.html",
        success_msg=success_msg,
        error_msg=error_msg,
        download_filename=download_filename,
        exam=exam,
        img_type=img_type,
        suggest_signature=suggest_signature,
    )


@app.route("/download/<filename>", methods=["GET"])
def download(filename):
    return send_from_directory(PROCESSED_DIR, filename, as_attachment=True)


if __name__ == "__main__":
    # Run the Flask development server
    app.run(debug=True)

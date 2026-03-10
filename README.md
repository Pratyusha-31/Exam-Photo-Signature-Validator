# Exam Photo & Signature Validator

## Project Specifications

The application processes user-uploaded images for competitive examination applications by performing **automatic resizing and compression** based on the selected exam requirements.

* The user selects a specific competitive examination (such as UPSC, RRB Group D, SBI PO/Clerk, JEE, GATE, etc.).
* The user uploads a photograph or signature image in any common image format.
* The application does **not reject images based on background, format, or dimensions at input time**.
* The system automatically resizes and compresses the uploaded image according to the predefined specifications of the selected examination.
* The processed output is returned as an **exam-ready image** that meets file size and dimension requirements.
* The entire image processing workflow is handled locally without using any database.

## Scope of the Project

* The project focuses only on **image resizing and compression** for photographs and signatures used in online examination applications.
* It supports multiple competitive examinations, each with different image size and dimension constraints.
* The application works independently of image source quality by converting user-provided images into compliant outputs.
* No database is used for storing user data or images.
* The project does not include user authentication, backend storage, or online application submission.
* The scope can be extended in the future to include additional exams, advanced image quality checks, or deployment as a web/mobile application.

## How to Run Locally

### 1. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 2. Run the Flask app

```bash
python app.py
```

### 3. Open in browser

Open your browser and go to:

```
http://127.0.0.1:5000
```

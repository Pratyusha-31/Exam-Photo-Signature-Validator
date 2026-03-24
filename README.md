# Exam Photo & Signature Validator

<p align="center">
  <img src="static/favicon.svg" alt="Logo" width="80" height="80">
</p>

<p align="center">
  A modern web application that automatically resizes and compresses exam photos and signatures to meet official government portal requirements.
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/Pratyusha-31/Exam-Photo-Signature-Validator?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/stars/Pratyusha-31/Exam-Photo-Signature-Validator?style=flat-square" alt="Stars">
  <img src="https://img.shields.io/github/issues/Pratyusha-31/Exam-Photo-Signature-Validator?style=flat-square" alt="Issues">
</p>

---

## Features

- **Smart Resize** - Automatically adjusts image dimensions to exact specifications
- **File Optimization** - Compresses or pads images to meet file size requirements
- **Multiple Exams** - Supports UPSC, GATE, and GROUP-D requirements
- **Drag & Drop** - Easy file upload with preview
- **Instant Processing** - Get your processed image in seconds
- **100% Private** - No data stored or transmitted anywhere
- **Responsive Design** - Works on mobile, tablet, and desktop

---

## Supported Exams

| Exam | Photo Size | Signature Size | File Size Range |
|------|------------|----------------|-----------------|
| **UPSC** | 200 x 230 px | 140 x 60 px | 20 - 300 KB |
| **GATE** | 200 x 230 px | 150 x 80 px | 10 - 200 KB |
| **GROUP-D** | 200 x 230 px | 140 x 60 px | 20 - 100 KB |

---

## Screenshots

> Add screenshots to the `static/images/screenshots/` folder and update the paths below.

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│    📷 Exam Photo & Signature Validator                      │
│                                                             │
│    ┌─────────────────────────────────────────────────┐     │
│    │                                                 │     │
│    │         [Drag & Drop Upload Area]               │     │
│    │                                                 │     │
│    └─────────────────────────────────────────────────┘     │
│                                                             │
│    [UPSC ▼]  [Photo ▼]  [Process Image Button]             │
│                                                             │
│    ✓ Image Processed Successfully!                          │
│    [Download Image]                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/Pratyusha-31/Exam-Photo-Signature-Validator.git
cd Exam-Photo-Signature-Validator

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Open in Browser

Navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Usage

1. **Select your exam** from the dropdown (UPSC, GATE, or GROUP-D)
2. **Choose image type** (Photo or Signature)
3. **Upload your image** by dragging and dropping or clicking to browse
4. **Click "Process Image"** to resize and compress
5. **Download** your processed image ready for upload

---

## Project Structure

```
Exam-Photo-Signature-Validator/
├── app.py                      # Flask application
├── image_processor.py           # Image processing logic
├── templates/
│   └── index.html               # HTML template
├── static/
│   ├── css/
│   │   └── style.css           # Styles
│   ├── js/
│   │   └── main.js             # JavaScript
│   ├── favicon.svg              # Favicon
│   └── images/                  # Images directory
├── uploads/                     # Temporary uploads
├── requirements.txt             # Dependencies
├── README.md                   # Documentation
├── LICENSE                     # MIT License
└── .gitignore                  # Git ignore
```

---

## Tech Stack

- **Backend**: Flask (Python)
- **Image Processing**: Pillow (PIL)
- **Frontend**: Vanilla HTML, CSS, JavaScript
- **Design**: Custom responsive CSS

---

## Development

### Run in Debug Mode

```bash
python app.py
```

### Production Deployment

For production, use Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ for exam aspirants
</p>

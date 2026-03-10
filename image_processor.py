import os
from PIL import Image, ImageOps

# Exact rules for government portals
RULES = {
    "UPSC": {
        "Photo": {"width": 200, "height": 230, "min_kb": 20, "max_kb": 300, "target_kb": 100},
        "Signature": {"width": 140, "height": 60, "min_kb": 10, "max_kb": 100, "target_kb": 50}
    },
    "GATE": {
        "Photo": {"width": 200, "height": 230, "min_kb": 20, "max_kb": 200, "target_kb": 80},
        "Signature": {"width": 150, "height": 80, "min_kb": 10, "max_kb": 100, "target_kb": 50}
    },
    "GROUP-D": {
        "Photo": {"width": 200, "height": 230, "min_kb": 20, "max_kb": 100, "target_kb": 50},
        "Signature": {"width": 140, "height": 60, "min_kb": 30, "max_kb": 40, "target_kb": 35}
    }
}

def process_exam_image(exam_name, img_type, input_path):
    exam_name = exam_name.upper().strip()
    img_type = img_type.capitalize().strip()

    try:
        # 1. Rules Check
        if exam_name not in RULES or img_type not in RULES[exam_name]:
            return "Invalid photo: Exam or Type not found."

        rule = RULES[exam_name][img_type]
        output_filename = f"processed_{exam_name}_{img_type}.jpg"

        # 2. Smart Resize (Cropping to fit dimensions without stretching)
        img = Image.open(input_path).convert("RGB")
        img = ImageOps.fit(img, (rule["width"], rule["height"]), Image.LANCZOS)

        # 3. High Clarity Save (Subsampling=0 keeps colors sharp)
        img.save(output_filename, "JPEG", quality=100, subsampling=0, optimize=False)

        current_kb = os.path.getsize(output_filename) / 1024

        # 4. Handle Max Size (If file is naturally too big)
        if current_kb > rule["max_kb"]:
            quality = 95
            while current_kb > rule["max_kb"] and quality > 20:
                img.save(output_filename, "JPEG", quality=quality, optimize=True)
                current_kb = os.path.getsize(output_filename) / 1024
                quality -= 5

        # 5. Handle Target Size (Padding to hit your 100KB or 35KB goal)
        if current_kb < rule["target_kb"]:
            target_bytes = int(rule["target_kb"] * 1024)
            padding_needed = target_bytes - os.path.getsize(output_filename)
            with open(output_filename, "ab") as f:
                f.write(b'\0' * padding_needed)
            current_kb = os.path.getsize(output_filename) / 1024

        return f"SUCCESS: {output_filename} ({round(current_kb, 2)} KB)"

    except Exception as e:
        return f"Invalid photo: {str(e)}"

if __name__ == "__main__":
    print("--- Government Exam Image Validator ---")
    e = input("Exam (UPSC/GATE/GROUP-D): ")
    t = input("Type (Photo/Signature): ")
    p = input("Path to image: ")

    result = process_exam_image(e, t, p)
    print(f"\nResult: {result}")

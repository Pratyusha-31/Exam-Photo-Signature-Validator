#!/bin/bash
cd /home/pratyusha/Exam-Photo-Signature-Validator

pkill -f "python.*app.py" 2>/dev/null
sleep 1

echo "Starting app..."
python3 app.py &
sleep 5

xdg-open http://localhost:5000

echo "App running at: http://localhost:5000"

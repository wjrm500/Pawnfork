#!/bin/bash
rm Pawnfork.zip
./venv/Scripts/activate # Activate virtual environment
pip freeze | xargs pip uninstall -y # Clear packages
pip install -r requirements.txt # Load necessary packages
python update_stockfish.py ./venv/Lib/site-packages/stockfish/models.py # Update stockfish models.py to prevent terminal window opening in application
pip install pyinstaller # Load pyinstaller
pyinstaller main.py --onefile --noconsole # Create executable
rm main.spec
rm -r build
mv dist app
cp -r stockfish_15_win_x64_avx2/ app/ # Copy Stockfish engine into app directory
cp -r static/ app/ # Copy static files into app directory
"C:\Program Files\7-Zip\7z.exe" a -tzip Pawnfork.zip ./app # Zip up directory
rm -r app
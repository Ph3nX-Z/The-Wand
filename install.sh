apt install python3
apt install python3-pip
pip install pyinstaller
pyinstaller --onefile ./wand.py
cp ./dist/wand /bin/wand
echo "[*] Installed The Wand"
echo "[+] Installation Complete !"
echo "[+] Run : wand -i [file] -m [mode] -o [Output file]"
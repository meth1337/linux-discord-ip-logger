#!/bin/bash
pyinstaller -F --onefile --icon=NONE main.py
cd dist
cp main ..
cd ..
rm -rf main.spec dist build
mv main build
clear
echo "Done!"


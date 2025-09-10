simpleScreenGrab is a lightweight Windows tool that lets you quickly capture a region of your screen and copy it straight to the clipboard as an image.

🖱️ Drag to select any area of the screen

📋 Paste instantly into Word, Paint, Slack, Discord, etc.

⎋ Press Esc to cancel mid-snipping

🚀 Works across multiple monitors


How to Install

- Download the latest release from the Releases page
.
(You’ll get a .zip file containing simpleScreenGrab.exe.)

- Extract the zip.

- Run simpleScreenGrab.exe.

 Drag a rectangle to select an area.

Release mouse → the screenshot is copied to clipboard.

Press Esc to cancel without capturing.

⚠️ Windows may show a SmartScreen warning since this app isn’t code-signed.
Click More info → Run anyway to continue.

I recommend building from source, this will prevent the SmartScreen warnings from occuring.

- <a href="https://www.python.org/downloads/" target="_blank">Download Python</a>

Open a terminal and run:

- git clone https://github.com/YOUR_USERNAME/simpleScreenGrab.git
- cd simpleScreenGrab
- pip install -r requirements.txt
- python main.py

To make a standalone Windows executable:

- pip install pyinstaller

- pyinstaller --onefile --noconsole main.py

The compiled .exe will be in the dist/ folder.
Double-click it to run without needing Python installed.  You can bind this to a key or mouse button to use as a macro.


License

This project is licensed under the MIT License.

Third-Party Dependencies

Pillow
 – Historical PIL License

MSS
 – MIT License

pywin32
 – PSF License

Copies of their licenses are included in THIRD_PARTY_LICENSES.md
.
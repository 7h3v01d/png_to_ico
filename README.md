# PNG to ICO Converter

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![PyQt6](https://img.shields.io/badge/PyQt6-6.4+-green)](https://www.riverbankcomputing.com/software/pyqt/)
[![Pillow](https://img.shields.io/badge/Pillow-9.0+-yellow)](https://python-pillow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](#installation)

**Simple, modern desktop GUI application** to convert **PNG images** to **ICO icon files** with multiple standard sizes — perfect for creating application icons, favicons, Windows shortcuts, and more.

![Screenshot of the application](https://via.placeholder.com/800x500/2c3e50/ecf0f1?text=PNG+to+ICO+Converter+Screenshot)  
*(Replace this placeholder with an actual screenshot of your running app)*

## Features

- Clean and intuitive graphical user interface built with **PyQt6**
- Preview selected PNG image before conversion
- Automatic output path suggestion with `.ico` extension
- Supports common ICO sizes: 16×16, 32×32, 48×48, 64×64, 128×128, 256×256, 512×512
- Converts PNG → ICO while preserving transparency (RGBA)
- Error handling with user-friendly messages
- Cross-platform (Windows, macOS, Linux)
- No external dependencies beyond Python packages

## Screenshots

### Main Window

![Main window](https://via.placeholder.com/800x500/34495e/ffffff?text=Main+Window+with+Preview)

### Successful Conversion

![Success message](https://via.placeholder.com/400x200/27ae60/ffffff?text=Conversion+Successful)

*(Add real screenshots here — recommended sizes: 800×500 or 1200×750)*

## Requirements

- Python **3.8** or newer
- PyQt6
- Pillow (PIL fork)

## Installation

### Option 1: Run from source (recommended for development)

1. Clone the repository

   ```bash
   git clone https://github.com/YOUR-USERNAME/png-to-ico-converter.git
   cd png-to-ico-converter

(Optional but recommended) Create a virtual environmentBashpython -m venv venv

Windows
```bash
venv\Scripts\activate
```
macOS / Linux
```bash
source venv/bin/activate
```
Install dependencies
```bash
pip install PyQt6 Pillow
```
Run the application
```bash
python png_to_ico_gui_v1.0.py
```
### Option 2: One-file executable (using PyInstaller)
After installing dependencies:
```bash
pip install pyinstaller
```
Create single-file executable
```bash
pyinstaller --onefile --windowed --name "PNGtoICO" \
  --icon=your_app_icon.ico \
  png_to_ico_gui_v1.0.py
```
The executable will appear in the dist/ folder.

## Usage
1. Click Browse PNG → select your .png file
2. (Optional) Click Browse ICO → choose where to save the .ico file
(if not selected, you'll be prompted during conversion)
3. Click Convert
4. Wait a moment — you'll see a success message with the output path

The generated ICO contains multiple sizes for best quality across different uses (taskbar, desktop, file explorer, etc.).

## Supported Input
- PNG files with transparency (recommended)
- Any size (will be resized automatically to ICO standard sizes)

## Planned Improvements / Roadmap
- Add custom size selection
- Batch conversion (multiple PNGs → ICOs)
- Drag & drop support
- Remember last used folder
- Dark mode toggle
- Progress bar for larger images
- Command-line interface (CLI) mode

Contributions welcome!

## Contributing
Pull requests are welcome!</br>
For major changes, please open an issue first to discuss what you would like to change.
1. Fork the repository
2. Create your feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

## License
Distributed under the MIT License.</br>
See LICENSE for more information.

## Acknowledgments

- Pillow — powerful image processing library
- PyQt6 — excellent Qt bindings for Python
- Icons & inspiration from many open-source icon utilities


Happy icon making! 🖼️ → 🪟
Created by Leon • Last updated January 2026

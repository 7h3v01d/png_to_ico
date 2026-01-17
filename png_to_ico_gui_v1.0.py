from PIL import Image
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QPushButton, QLineEdit, QFileDialog, QMessageBox)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
import sys

class PNGtoICOConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PNG to ICO Converter")
        self.setGeometry(100, 100, 600, 400)
        
        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout()
        self.central_widget.setLayout(self.main_layout)
        
        # Input section
        self.input_frame = QWidget()
        self.input_layout = QVBoxLayout()
        self.input_frame.setLayout(self.input_layout)
        
        self.title_label = QLabel("PNG to ICO Converter")
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
        self.input_layout.addWidget(self.title_label)
        
        self.png_path = QLineEdit()
        self.png_path.setPlaceholderText("Select PNG file...")
        self.input_layout.addWidget(self.png_path)
        
        self.browse_png_btn = QPushButton("Browse PNG")
        self.browse_png_btn.clicked.connect(self.browse_png)
        self.input_layout.addWidget(self.browse_png_btn)
        
        self.ico_path = QLineEdit()
        self.ico_path.setPlaceholderText("Select ICO output path...")
        self.input_layout.addWidget(self.ico_path)
        
        self.browse_ico_btn = QPushButton("Browse ICO")
        self.browse_ico_btn.clicked.connect(self.browse_ico)
        self.input_layout.addWidget(self.browse_ico_btn)
        
        self.convert_btn = QPushButton("Convert")
        self.convert_btn.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; font-weight: bold;")
        self.convert_btn.clicked.connect(self.convert)
        self.input_layout.addWidget(self.convert_btn)
        
        self.input_layout.addStretch()
        self.main_layout.addWidget(self.input_frame)
        
        # Preview section
        self.preview_frame = QWidget()
        self.preview_layout = QVBoxLayout()
        self.preview_frame.setLayout(self.preview_layout)
        
        self.preview_label = QLabel("Preview")
        self.preview_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.preview_layout.addWidget(self.preview_label)
        
        self.image_label = QLabel("No image selected")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc; min-width: 200px; min-height: 200px;")
        self.preview_layout.addWidget(self.image_label)
        
        self.preview_layout.addStretch()
        self.main_layout.addWidget(self.preview_frame)
        
        # Apply stylesheet
        self.setStyleSheet("""
            QMainWindow { background-color: #ffffff; }
            QLineEdit { padding: 5px; border: 1px solid #ccc; border-radius: 4px; }
            QPushButton { padding: 8px; border-radius: 4px; border: none; }
            QPushButton:hover { background-color: #45a049; }
        """)
        
    def browse_png(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select PNG File", "", "PNG Files (*.png)")
        if file_path:
            self.png_path.setText(file_path)
            self.update_preview(file_path)
    
    def browse_ico(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save ICO File", "", "ICO Files (*.ico)")
        if file_path:
            if not file_path.lower().endswith('.ico'):
                file_path += '.ico'
            self.ico_path.setText(file_path)
    
    def update_preview(self, file_path):
        try:
            img = Image.open(file_path)
            # Resize image for preview (max 200x200)
            img = img.resize((200, 200), Image.Resampling.LANCZOS)
            img.save("temp_preview.png")
            pixmap = QPixmap("temp_preview.png")
            self.image_label.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))
            self.image_label.setText("")
            os.remove("temp_preview.png")
        except Exception as e:
            self.image_label.setPixmap(QPixmap())
            self.image_label.setText("Error loading image")
    
    def convert_png_to_ico(self, png_path, ico_path, sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256), (512, 512)]):
        try:
            img = Image.open(png_path)
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            img.save(ico_path, format='ICO', sizes=sizes)
            return True, f"Successfully converted {png_path} to {ico_path}"
        except FileNotFoundError:
            return False, f"Error: Input file {png_path} not found"
        except Exception as e:
            return False, f"Error during conversion: {str(e)}"
    
    def convert(self):
        png_path = self.png_path.text()
        ico_path = self.ico_path.text()
        
        if not png_path or not os.path.exists(png_path):
            QMessageBox.critical(self, "Error", "Please select a valid PNG file")
            return
        if not ico_path:
            QMessageBox.critical(self, "Error", "Please specify an output ICO file path")
            return
        
        success, message = self.convert_png_to_ico(png_path, ico_path)
        if success:
            QMessageBox.information(self, "Success", message)
        else:
            QMessageBox.critical(self, "Error", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PNGtoICOConverter()
    window.show()
    sys.exit(app.exec())
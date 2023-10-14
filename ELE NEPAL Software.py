import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QPainter, QBrush, QColor

class CustomDesignWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor(255, 0, 0)))  # Set a red brush (customize color)
        painter.drawRect(0, 0, self.width(), self.height())  # Draw a red rectangle

class MainLauncher(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Application Launcher")
        self.setGeometry(0, 0, 400, 200)  # Center the window on the screen
        self.setWindowIcon(QIcon(r"D:\ELE Nepal Materials\ELE NEPAL Complete Software\Resource For Software\Launcher Logo.png"))  # Set a custom launcher icon (customize the path)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create layout for central widget
        layout = QVBoxLayout()

        # Add title label
        title_label = QLabel("Choose an Application to Launch")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Add custom design widget
        design_widget = CustomDesignWidget(self)
        layout.addWidget(design_widget)

        # Create a horizontal layout for buttons and icons
        app_layout = QHBoxLayout()

        # Add buttons for launching applications with tooltips
        app1_button = QPushButton("Korean Classes Software", self)
        app1_button.setToolTip("Launch Korean Classes Software")
        app2_button = QPushButton("Japanese Classes Software", self)
        app2_button.setToolTip("Launch Japanese Classes Software")

        app1_button.clicked.connect(self.launch_app1)
        app2_button.clicked.connect(self.launch_app2)

        app_layout.addWidget(app1_button)
        app_layout.addWidget(app2_button)

        # Create a horizontal layout for icons
        icon_layout = QHBoxLayout()

        # Add icons for each application (customize paths)
        app1_icon = QLabel(self)
        pixmap1 = QPixmap(r"D:\ELE Nepal Materials\ELE NEPAL Complete Software\Resource For Software\Korean Logo.png")  # Customize path to Korean Classes Software icon image
        app1_icon.setPixmap(pixmap1)
        app1_icon.setAlignment(Qt.AlignCenter)

        app2_icon = QLabel(self)
        pixmap2 = QPixmap(r"D:\ELE Nepal Materials\ELE NEPAL Complete Software\Resource For Software\Japan Logo.png")  # Customize path to Japanese Classes Software icon image
        app2_icon.setPixmap(pixmap2)
        app2_icon.setAlignment(Qt.AlignCenter)

        icon_layout.addWidget(app1_icon)
        icon_layout.addWidget(app2_icon)

        # Add the button and icon layouts to the main layout
        layout.addLayout(app_layout)
        layout.addLayout(icon_layout)

        # Add an exit button
        exit_button = QPushButton("Exit", self)
        exit_button.clicked.connect(self.close_app)
        layout.addWidget(exit_button)

        central_widget.setLayout(layout)

    def launch_app1(self):
        # Check if the Korean Classes Software file exists before launching
        if os.path.exists(r"D:\ELE Nepal Materials\ELE NEPAL Complete Software\Resource For Software\softwareforELEKorean.py"):
            import subprocess
            subprocess.Popen(["python", r"D:\ELE Nepal Materials\ELE NEPAL Complete Software\Resource For Software\softwareforELEKorean.py"])
        else:
            QMessageBox.critical(self, "Error", "Korean Classes Software not found!")

    def launch_app2(self):
        # Check if the Japanese Classes Software file exists before launching
        if os.path.exists(r"D:\ELE Nepal Materials\ELE NEPAL Complete Software\Resource For Software\SoftwareForELEJapan.py"):
            import subprocess
            subprocess.Popen(["python", r"D:\ELE Nepal Materials\ELE NEPAL Complete Software\Resource For Software\SoftwareForELEJapan.py"])
        else:
            QMessageBox.critical(self, "Error", "Japanese Classes Software not found!")

    def close_app(self):
        self.close()

def main():
    app = QApplication(sys.argv)
    launcher = MainLauncher()
    launcher.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

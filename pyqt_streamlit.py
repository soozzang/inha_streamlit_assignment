# pyqt_streamlit.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import threading
import os

def run_streamlit():
    os.system("streamlit run streamlit_calculator.py")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Streamlit Engineering Calculator in PyQt5")

        self.browser = QWebEngineView()
        self.browser.setUrl("http://localhost:8501")

        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    streamlit_thread = threading.Thread(target=run_streamlit, args=(), daemon=True)
    streamlit_thread.start()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


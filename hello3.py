import sys
import PySide
from PySide.QtGui import QApplication
from PySide.QtGui import QMessageBox

app = QApplication(sys.argv)

msgBox = QMessageBox()
msgBox.setText("Hello baby- using Pyside" + PySide.__version__)
msgBox.exec_() 

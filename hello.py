import sys
from PySide.QtCore import *
from PySide.QtGui import *
app = QApplication(sys.argv)
label = QLabel("<font color=blue size=30>Hello World</font>")
label.show()
app.exec_()
sys.exit()
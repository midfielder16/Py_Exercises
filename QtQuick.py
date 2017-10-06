import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import QtDeclarativeView

app = QApplication(sys.argv)
view = QtDeclarativeView()

url = QUrl('view.qml')

view.setSource(url)
view.show()
sys.exit(app.exec_())
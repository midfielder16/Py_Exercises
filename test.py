import sys
from PySide.QtCore import *
from PySide.QtGui import *

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.setWindowTitle("First Gui")
		self.show()

def main():
	app = QApplication(sys.argv)
	main = MyWindow()
	sys.exit(app.exec_())

if __name__== "__main__":

	main()



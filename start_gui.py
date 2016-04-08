from PyQt4 import QtGui, QtCore

import sys

from gui import Ui_Mosaic
from os.path import expanduser
from generator import generate

class StartGUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Mosaic()
        self.ui.setupUi(self)
        self.dir_name = ""

        self.ui.heightSpinBox.setMinimum(0)
        self.ui.heightSpinBox.setMaximum(10000)

        self.ui.widthSpinBox.setMinimum(0)
        self.ui.widthSpinBox.setMaximum(10000)

        QtCore.QObject.connect(self.ui.openButton, QtCore.SIGNAL("clicked()"), self.file_dialog)
        QtCore.QObject.connect(self.ui.startButton, QtCore.SIGNAL("clicked()"), self.start)

    def file_dialog(self):
        fd = QtGui.QFileDialog(self)
        self.dir_name = str(fd.getExistingDirectory(self, "Open a folder", expanduser("~"), QtGui.QFileDialog.ShowDirsOnly))
        self.ui.editDirPath.setText(self.dir_name)

    def start(self):
        print "starting with arguments: \ndir={} \nwidth={} \nheight={}\n".format(self.dir_name, self.ui.widthSpinBox.value(), self.ui.heightSpinBox.value())
        generate(self.dir_name, self.ui.widthSpinBox.value(), self.ui.heightSpinBox.value())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartGUI()
    myapp.show()
    sys.exit(app.exec_())
from PyQt4 import QtGui, QtCore

import sys

from PyQt4.QtGui import QLabel, QPixmap, QImage

from gui import Ui_Mosaic
from os.path import expanduser
from generator import generate
import ImageQt


class StartGUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Mosaic()
        self.ui.setupUi(self)
        self.dir_name = ""

        self.result_label = QLabel()

        QtCore.QObject.connect(self.ui.openButton, QtCore.SIGNAL("clicked()"), self.file_dialog)
        QtCore.QObject.connect(self.ui.startButton, QtCore.SIGNAL("clicked()"), self.start)

    def file_dialog(self):
        fd = QtGui.QFileDialog(self)
        self.dir_name = str(fd.getExistingDirectory(self, "Open a folder", expanduser("~"), QtGui.QFileDialog.ShowDirsOnly))
        self.ui.editDirPath.setText(self.dir_name)

    def start(self):
        print "starting with arguments: \ndir={} \nwidth={} \nheight={}\n".format(self.dir_name, self.ui.widthSpinBox.value(), self.ui.heightSpinBox.value())
        width = self.ui.widthSpinBox.value()
        height = self.ui.heightSpinBox.value()
        max_gens = self.ui.maxGenNumberSpinBox.value()
        num_bees = self.ui.beeNumberSpinBox.value()
        num_sites = self.ui.selectBestedSidesNumberSpinBox.value()
        patch_size = self.ui.patchSizeSpinBox.value()
        elite_bees = self.ui.eliteBeesNumberSpinbox.value()
        other_bees = self.ui.otherBeesNumberSpinBox.value()
        patch_decrease_factor = self.ui.patchDecreaseFactorSpinBox.value()

        image = generate(self.dir_name, width, height, max_gens, num_bees, num_sites, patch_size, elite_bees, other_bees, patch_decrease_factor)
        self.show_result(image, width, height)

    def show_result(self, image, width, height):
        self.qimage = ImageQt.ImageQt(image)
        self.pixmap = QPixmap.fromImage(self.qimage)
        self.result_label.setPixmap(self.pixmap)
        self.result_label.setFixedHeight(height)
        self.result_label.setFixedWidth(width)
        self.result_label.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartGUI()
    myapp.show()
    sys.exit(app.exec_())
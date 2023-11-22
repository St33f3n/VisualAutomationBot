from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
from app.hello import Ui_MainWindow  # Import Ui_MainWindow from the generated module
import sys, os
from lib.jsonHandler import JsonHandler 

class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)


    def fileopen(self):
        options = QFileDialog.Options()
        current_dir = QFileDialog.getExistingDirectory(self,"QFileDialog.getExistingDirectory()", "", options=options)
        if os.path.exists(current_dir + "/config.json") == True:
            folder_name = os.path.basename(current_dir)
            jHandler = JsonHandler(folder_name)
            print(jHandler.getData("playset"))

            self.openFileButton.setText(folder_name)

    def save(self):
        print("Saved clicked")

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, QMimeData, QObject
from PyQt5.QtGui import QDrag, QDragEnterEvent, QDropEvent
from app.hello import Ui_MainWindow  # Import Ui_MainWindow from the generated module
import sys, os
from lib.commander import Commander
from lib.jsonHandler import JsonHandler 


class DragHandler(QObject):
    def __init__(self, widget):
        super().__init__(widget)
        self.widget = widget

    def setupDraggableButton(self, button):
        button.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.widget.ddButton:
            if event.type() == event.MouseButtonPress:
                self.drag_start_position = event.pos()
            elif event.type() == event.MouseMove:
                if hasattr(self, 'drag_start_position') and (event.buttons() & Qt.LeftButton):
                    drag = QDrag(self.widget.ddButton)
                    mime_data = QMimeData()
                    drag.setMimeData(mime_data)

                    drag.setHotSpot(event.pos() - self.drag_start_position)

                    drag.exec_(Qt.MoveAction)

        return super().eventFilter(obj, event)
class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.jHandler = None
        self.com = Commander()

        # self.setAcceptDrops(True)

        # self.ddButton = QPushButton('Drag me', self)
        # self.ddButton.setGeometry(50, 50, 100, 50)

        # # Initialize DragHandler and set up drag for ddButton
        # self.dragHandler = DragHandler(self)
        # self.dragHandler.setupDraggableButton(self.ddButton)
    
    def openConfig(self):
        if self.jHandler:
            item = sum(self.jHandler.getData('playset'), [])
            print(item)
            current_text = ""
            for i in item:
                current_text += i + "\n"
            self.textlist.setText(current_text)
            self.openConfigButton.setText("Config Loaded")
        else:
            self.openConfigButton.setText("No Config Found")


    def openDir(self):
        options = QFileDialog.Options()
        current_dir = QFileDialog.getExistingDirectory(self,"QFileDialog.getExistingDirectory()", "", options=options)
        if os.path.exists(current_dir + "/config.json") == True:
            folder_name = os.path.basename(current_dir)
            self.jHandler = JsonHandler(folder_name)

            self.openDirButton.setText(folder_name)

            item = self.jHandler.getData('pictures', 0).keys()
            self.pictureWidget.addItems(item)


    def save(self):
        current_text = self.textlist.text().splitlines()
        print(current_text)
        arr = []
        temp = []

        temp_counter = 0

        for i in current_text:            
            if i[0] == "\"":
                temp.append(i)

            else:
                if temp_counter == 1 :
                    arr.append(temp)
                    temp = []
                    temp_counter = 0
            
                if i[0] != "\"":
                    temp.append(i)
                    temp_counter = 1
        
        arr.append(temp)

        self.jHandler.update('playset', arr)


    def dragEnterEvent(self, event):
        event.accept()
    
    def dropEvent(self, event):
        position = event.pos()
        self.ddButton.move(position)
        event.accept()
    
    def add(self):
        selected_item = self.pictureWidget.currentItem()
        if selected_item is not None:
            current_text = self.textlist.text()
            self.textlist.setText(current_text + f"\"{selected_item.text()}\"\n")
        self.pictureWidget.clearSelection()
        self.pictureWidget.setCurrentItem(None)

    def deleteLast(self):
        current_text = self.textlist.text()
        lines = current_text.splitlines()
        resultText = '\n'.join(lines[:-1])
        self.textlist.setText(resultText + "\n")


    # All Gamer Button Functions 

    def simpleClick(self):
        current_text = self.textlist.text()
        if self.xLabel.text() != "" and self.yLabel.text() != "":
            self.textlist.setText(current_text + f"simpleClickButton\n {self.xLabel.text()}\n {self.yLabel.text()}\n")
            self.xLabel.setText("")
            self.yLabel.setText("")

    def clickOnPicture(self):
        current_text = self.textlist.text()
        self.textlist.setText(current_text + "clickOnPicture\n")

    def keyPress(self):
        current_text = self.textlist.text()
        if self.keyLabel.text() != "":
            self.textlist.setText(current_text + f"keyPress\n {self.keyLabel.text()}\n")
            self.keyLabel.setText("")

    def clickIfPicture(self):
        current_text = self.textlist.text()
        self.textlist.setText(current_text + "clickIfPicture\n")

    def locateRessource(self):
        current_text = self.textlist.text()
        self.textlist.setText(current_text + "locateRessource\n")
  
    def loadGame(self):
        options = QFileDialog.Options()
        current_dir = QFileDialog.getExistingDirectory(self,"QFileDialog.getExistingDirectory()", "", options=options)
        if os.path.exists(current_dir + "/config.json") == True:
            folder_name = os.path.basename(current_dir)


            self.com.addGame(folder_name)
            self.com.queueGamer(folder_name)
            print(self.com)

    def selectTopLeft(self):
        pass

    def selectBottomRight(self):
        pass

    def start_stop(self):
        self.com.playGame()


def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

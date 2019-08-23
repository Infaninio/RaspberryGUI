from src.mainWindow import MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import sys




if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    mainWin = MainWindow()
    mainWin.show()


    sys.exit(app.exec_())


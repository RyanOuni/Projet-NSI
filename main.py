import random
import sys
import os
from PySide6 import QtCore, QtWidgets, QtGui


class Bouton(QtWidgets.QWidget):
    def __init__(self, projet):
        super().__init__()
        self.nom = projet["nom"]
        self.chemin = projet["chemin"]
        self.terminal = projet["terminal"]
        self.button = QtWidgets.QPushButton(self.nom)
        self.button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.button.clicked.connect(self.magic)
    
    @QtCore.Slot()
    def magic(self):
        parent = QtCore.QObject()
        if os.name == "nt":
            terminalprogram = "powershell"
            pythonname = "python"
            args = ["Start-Process", '-FilePath', 'python ' + os.path.dirname(os.path.abspath(__file__)) + "\\" + "\\".join(self.chemin.split("/"))]
        else:
            terminalprogram = "gnome-terminal"
            pythonname = "python3"
            args = ["--", pythonname , os.path.dirname(__file__) + "/" + self.chemin ]
        if self.terminal:
            program = terminalprogram
            arg = args
        else:
            program = pythonname
            arg = [os.path.dirname(__file__) + "/" + self.chemin]
        myProcess = QtCore.QProcess(parent)
        myProcess.start(program, arg)
        myProcess.waitForStarted()
        myProcess.waitForFinished()
        myProcess.readAll()
        myProcess.close()

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.projets = [
            {"chemin" : "Pong/pong.py",
             "nom" : "Pong",
             "terminal" : False
             }, 
            {"chemin" : "Race/Race.py",
             "nom" : "Race",
             "terminal" : False
             },
            {"chemin" : "Jeu_des_5000/Jeu-Anissa-Aline.py",
             "nom" : "Jeu des 5000",
             "terminal" : True
             }, 
            {"chemin" : "labyrinthe/labyrinthe_v1.py",
             "nom" : "Générateur de labyrinthes",
             "terminal" : False
             }
            ]
        self.buttonlist = []
        self.layout = QtWidgets.QGridLayout(self)
        cpt = 0
        for projet in self.projets:
            bouton = Bouton(projet)
            self.buttonlist.append(bouton)
            self.layout.addWidget(bouton.button, cpt // 2, cpt % 2)
            cpt += 1

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

import sys
from PyQt4.QtGui import *

# Bon mon application
a = QApplication(sys.argv)

# Ma fenetre $ moi a 4h du mat
w = QWidget()

# Mon texte
nameLabel = QLabel("Bonne nuit les amis vampires", w)
nameLabel.move(100, 80)

# la taille de ma fenetre
w.resize(320, 240)

# Un bon hello world
w.setWindowTitle("Hello World!")

# Bon le nom du fichier en utilisant QFileDialog
filename = QFileDialog.getOpenFileName(w, 'Open File', '/')
print(filename)

# Bon j'affiche le contenu
with open(filename, 'r') as f:
    print(f.read())

# Et voila
w.show()

sys.exit(a.exec_())

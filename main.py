import sys

from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtCore import QPoint
from PyQt6 import uic
from random import randint


class YellowCircles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap()
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def draw_circle(self, qp):
        circle_radius = randint(1, 120)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(QPoint(200, 130), circle_radius, circle_radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    yc = YellowCircles()
    yc.show()
    sys.exit(app.exec())
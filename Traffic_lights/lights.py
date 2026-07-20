from PyQt5.QtWidgets import (
    QGraphicsScene, QGraphicsRectItem, QGraphicsItemGroup, QGraphicsEllipseItem
)
from PyQt5.QtGui import QBrush, QColor, QPen
from PyQt5.QtCore import Qt, QTimer

class light(QGraphicsItemGroup):

    def __init__(self, x = 0, y = 0, width=20, height=50, parent = None):
        super().__init__(parent)

        #body of the traffic light
        body = QGraphicsRectItem(0, 0, width, height)
        body.setBrush(QBrush(QColor("#222222")))
        body.setPen(QPen(Qt.NoPen))
        self.addToGroup(body)

        #dimension of the colored lights
        light_diam = width - 6
        margin = 3
        spacing = (height - margin) / 3

        self.red = QGraphicsEllipseItem(margin/2, margin, light_diam, light_diam)
        self.yellow = QGraphicsEllipseItem(margin/2, margin + spacing, light_diam, light_diam)
        self.green = QGraphicsEllipseItem(margin/2, margin + 2 * spacing, light_diam, light_diam)

        for circle in (self.red, self.yellow, self.green):
            circle.setPen(QPen(Qt.NoPen))
            self.addToGroup(circle)

        self.lights_list = {
            "red": self.red,
            "yellow": self.yellow,
            "green": self.green
        }

        self.lights_on = {
            "red": QColor("red"),
            "yellow": QColor("yellow"),
            "green": QColor("#2ee82e")
        }

        self.lights_off = {
            "red": QColor("#550000"),
            "yellow": QColor("#555500"),
            "green": QColor("#005500"),
        }

        self.set_state("red") #first state
        self.setPos(x, y)

    def set_state(self, state):
        """state = 'red' | 'yellow' | 'green'"""
        for name, light in self.lights_list.items():
            if name == state:
                color = self.lights_on[name]
            else:
                color = self.lights_off[name]
            light.setBrush(QBrush(QColor(color)))
        self.current_state = state    

    def get_state(self):
        return self.current_state

from PyQt5.QtWidgets import (
    QGraphicsScene, QGraphicsRectItem, QGraphicsItemGroup, QGraphicsEllipseItem
)
from PyQt5.QtGui import QBrush, QColor, QPen
from PyQt5.QtCore import Qt, QTimer

class car(QGraphicsRectItem):

    def __init__(self, x=0, y=0, width=15, height=25, color="#3399ff", speed=2.5, direction="down", tag = "abc"):
        super().__init__(0, 0, width, height)
        self.setBrush(QBrush(QColor(color)))
        self.setPen(QPen(Qt.NoPen))
        self.setPos(x, y)
        self.speed = speed        #pixel add to move
        self.direction = direction
        self.current_x = x
        self.current_y = y
        self.counted = False
        self.tag = tag
        self.speed = speed
        self.checked = False


        self.stopped = False
        self.too_close = False 

    def move(self):
        if self.stopped == True:
            return

        if self.direction == "down":
            self.moveBy(0, self.speed) #x() and y() return the values of x and y
            if self.y() >= 800:
                self.reset()

        elif self.direction == "up":
            self.moveBy(0, -self.speed)
            if self.y() <= -150:
                self.reset()

        elif self.direction == "right":
            self.moveBy(self.speed, 0)
            if self.x() >= 1000:
                self.reset()

        elif self.direction == "left":
            self.moveBy(-self.speed, 0)
            if self.x() <= -100:
                self.reset()

    def stop(self):
        self.stopped = True

    def go(self):
        self.stopped = False

    def reset(self):
        self.setX(self.current_x)
        self.setY(self.current_y)
        self.counted = False

    def get_tag(self):
        return self.tag
    
    def get_speed(self):
        return self.speed
    
    

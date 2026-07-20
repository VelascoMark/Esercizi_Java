from PyQt5.QtWidgets import QGraphicsScene, QGraphicsRectItem
from PyQt5.QtGui import QBrush, QColor, QPen
from PyQt5.QtCore import Qt, QTimer

from lights import light
from cars import car
from exceed_speed import save_data
import random
import math
import string

class main_roads(QGraphicsScene):

    def __init__(self):
        super().__init__()
        self.setSceneRect(0,0,800,600)

        self.lights = []
        self.coche = []
        self.coche_down = []
        self.coche_up = []
        self.coche_left = []
        self.coche_right= []
        self.tag_speed = []
        self.autovelox_exceed = []

        self.tag = "None"
        self.speed = 0
        self.ts_north = ""
        self.ts_south = ""
        self.ts_east = ""
        self.ts_west = ""

        self.sorted_cars = []
        self.sorted_cars_north = []
        self.sorted_cars_south = []
        self.sorted_cars_east = []
        self.sorted_cars_west = []

        self.removed = False
        self.recreate = False
        self.first_car = True #flag to spawn the first car

        self.counted_cars_north = 0
        self.counted_cars_south = 0
        self.counted_cars_east = 0
        self.counted_cars_west = 0

        self.createRoads()
        self.createTraffic_light()
        self.create_cars()

        self.timer = QTimer()
        self.timer.timeout.connect(self.autovelox_tag)
        self.timer.timeout.connect(self.autovelox_speed)
        self.timer.timeout.connect(self.create_cars)
        self.timer.timeout.connect(self.move_cars)
        self.timer.timeout.connect(self.count_cars)
        self.timer.start(30)

    def createRoads(self):
        road1 = QGraphicsRectItem(
            300,
            -600,
            200,
            2000
        )
        road2 = QGraphicsRectItem(
            -100,
            200,
            1000,
            200
        )
        road1.setBrush(QBrush(QColor("#333333")))
        road2.setBrush(QBrush(QColor("#333333")))
        road1.setPen(QPen(Qt.NoPen))#removes the external border 
        road2.setPen(QPen(Qt.NoPen))
        self.addItem(road1)
        self.addItem(road2)


        #Adding the white stripes
        hStripe1 = QGraphicsRectItem(0, 300, 60, 3.5)
        hStripe2 = QGraphicsRectItem(80, 300, 60, 3.5)
        hStripe3 = QGraphicsRectItem(160, 300, 60, 3.5)
        hStripe4 = QGraphicsRectItem(240, 300, 30, 3.5)     #EAST ROAD
        hStripe1.setBrush(QBrush(QColor("#ffffff")))
        hStripe2.setBrush(QBrush(QColor("#ffffff")))
        hStripe3.setBrush(QBrush(QColor("#ffffff")))
        hStripe4.setBrush(QBrush(QColor("#ffffff")))
        self.addItem(hStripe1)
        self.addItem(hStripe2)
        self.addItem(hStripe3)
        self.addItem(hStripe4)

        hStripe5 = QGraphicsRectItem(745, 300, 60, 3.5)
        hStripe6 = QGraphicsRectItem(665, 300, 60, 3.5)
        hStripe7 = QGraphicsRectItem(585, 300, 60, 3.5)
        hStripe8 = QGraphicsRectItem(535, 300, 30, 3.5)     #WEST ROAD
        hStripe5.setBrush(QBrush(QColor("#ffffff")))
        hStripe6.setBrush(QBrush(QColor("#ffffff")))
        hStripe7.setBrush(QBrush(QColor("#ffffff")))
        hStripe8.setBrush(QBrush(QColor("#ffffff")))
        self.addItem(hStripe5)
        self.addItem(hStripe6)
        self.addItem(hStripe7)
        self.addItem(hStripe8)

        vStripe1 = QGraphicsRectItem(400, -60, 3.5, 60)
        vStripe2 = QGraphicsRectItem(400, 20, 3.5, 60)
        vStripe3 = QGraphicsRectItem(400, 100, 3.5, 40)     #NORTH ROAD
        vStripe1.setBrush(QBrush(QColor("#ffffff")))
        vStripe2.setBrush(QBrush(QColor("#ffffff")))
        vStripe3.setBrush(QBrush(QColor("#ffffff")))
        self.addItem(vStripe1)
        self.addItem(vStripe2)
        self.addItem(vStripe3)

        vStripe4 = QGraphicsRectItem(400, 600, 3.5, 60)
        vStripe5 = QGraphicsRectItem(400, 520, 3.5, 60)
        vStripe6 = QGraphicsRectItem(400, 460, 3.5, 40)     #SOUTH ROAD
        vStripe4.setBrush(QBrush(QColor("#ffffff")))
        vStripe5.setBrush(QBrush(QColor("#ffffff")))
        vStripe6.setBrush(QBrush(QColor("#ffffff")))
        self.addItem(vStripe4)
        self.addItem(vStripe5)
        self.addItem(vStripe6)


        #stop lines
        stopStripe1 = QGraphicsRectItem(253, 300, 17, 100) #WEST ROAD
        stopStripe1.setBrush(QBrush(QColor("#ffffff")))
        self.addItem(stopStripe1)

        stopStripe2 = QGraphicsRectItem(535, 200, 17, 103.5) #EAST ROAD
        stopStripe2.setBrush(QBrush(QColor("#ffffff")))
        self.addItem(stopStripe2)

        stopStripe3 = QGraphicsRectItem(300, 127, 103.5, 17) #NORTH ROAD
        stopStripe3.setBrush(QBrush(QColor("#ffffff")))
        self.addItem(stopStripe3)

        stopStripe4 = QGraphicsRectItem(400, 460, 101.75, 17) #SOUTH ROAD
        stopStripe4.setBrush(QBrush(QColor("#ffffff")))
        self.addItem(stopStripe4)


    def createTraffic_light(self):
        positions = [
            (300, 150), #north west
            (500, 200), #north east
            (480, 400), #south east
            (280, 350), #south west

        ]

        for x, y in positions:
            
            traffic_light = light(x, y) #the constructor of light has 5 inputs but since they're all defined, Im changing x and y only
            self.addItem(traffic_light)
            self.lights.append(traffic_light)


        for z in range(0,3):
            current_state = self.lights[z].current_state
            next_state = self.lights[z + 1].current_state
            if current_state == next_state and current_state == "red":
                self.lights[z].set_state("red")
                self.lights[z + 1].set_state("green")
            elif current_state == next_state and current_state == "green":
                self.lights[z + 1].set_state("green")
            else:
                self.lights[z + 1].set_state("red")

    def create_cars(self):
        if self.recreate == False:
            return

        directions_list = {
            "down": (350, -100),
            "right": (-100, 320),
            "up": (410, 900),
            "left": (950, 220)
        }

        direction_rand = random.choice(list(directions_list.keys()))
        create_pass = random.randint(0, 200)
        random_speed = random.uniform(1, 3)
        colore_hex = "#{:02x}{:02x}{:02x}".format( #generates a random HEX code color 
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )   
        random_tag = "{:03d}{}{}".format(
            random.randint(0, 999),
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_uppercase)
        )
        if create_pass >= 1:
            return
        
        dx, dy = directions_list[direction_rand]

        car1 = car(x = dx, y = dy, width=15, height=15, color = colore_hex, speed = random_speed, direction = direction_rand, tag = random_tag)
        self.addItem(car1)
        self.coche.append(car1)
        
        if car1.direction == "down":
            self.coche_down.append(car1)
        elif car1.direction == "up":
            self.coche_up.append(car1)
        elif car1.direction == "left":
            self.coche_left.append(car1)
        elif car1.direction == "right":
            self.coche_right.append(car1)


    def move_cars(self):

        self.sorted_cars = sorted(self.coche, key=lambda car: car.speed, reverse=True)
        self.sorted_cars_north = sorted(self.coche_down, key=lambda car: car.speed, reverse=True)
        self.sorted_cars_south = sorted(self.coche_up, key=lambda car: car.speed, reverse=True)
        self.sorted_cars_east = sorted(self.coche_left, key=lambda car: car.speed, reverse=True)
        self.sorted_cars_west = sorted(self.coche_right, key=lambda car: car.speed, reverse=True)

        self.check_cars(self.sorted_cars_east)
        self.check_cars(self.sorted_cars_north)
        self.check_cars(self.sorted_cars_south)
        self.check_cars(self.sorted_cars_west)

        for car in self.coche:
            traffic_light_stop = False
            if self.lights[0].get_state() == "red" and car.y() >= 115 and car.y() <= 125 and car.x() >= 300 and car.x() <= 403: #NORTH ROAD
                traffic_light_stop = True
            elif self.lights[3].get_state() == "red" and car.x() >= 240 and car.x() <= 255 and car.y() >= 300 and car.y() <= 400: #WEST ROAD
                traffic_light_stop = True
            elif self.lights[2].get_state() == "red" and car.y() >= 440 and car.y() <= 460 and car.x() >= 400 and car.x() <= 501: #SOUTH ROAD
                traffic_light_stop = True
            elif self.lights[1].get_state() == "red" and car.x() >= 510 and car.x() <= 530 and car.y() >= 200 and car.y() <= 300: #EAST ROAD
                traffic_light_stop = True
            
            if traffic_light_stop == True or car.too_close == True:
                car.stop()
            else:
                car.go()
            car.move()

    def check_cars(self, ordered_cars, min_distance = 25):
        for c in ordered_cars:
            c.too_close = False
        
        for i in range(0, len(ordered_cars) - 1):
            if i == 0:
                after_car = ordered_cars[len(ordered_cars) - 1]
                current_car = ordered_cars[i]
                before_car = ordered_cars[i + 1]
            elif i == len(ordered_cars) - 1:
                after_car =  ordered_cars[i - 1]
                current_car = ordered_cars[i]
                before_car = ordered_cars[0]
            else:
                after_car = ordered_cars[i - 1]
                current_car = ordered_cars[i]
                before_car = ordered_cars[i + 1]
            
            distance_before_y = abs(current_car.y() - before_car.y())
            distance_before_x = abs(current_car.x() - before_car.x())
            distance_after_y = abs(current_car.y() - after_car.y())
            distance_after_x = abs(current_car.x() - after_car.x())

            if distance_before_y <= min_distance and distance_before_x <= min_distance and distance_after_y <= min_distance and distance_after_x <= min_distance:
                before_car.too_close = True


    def remove_cars(self):
        if self.removed == True:
            return
        
        for car in self.sorted_cars:
            self.removeItem(car)

        for car in self.sorted_cars_east:
            self.removeItem(car)
        
        for car in self.sorted_cars_west:
            self.removeItem(car)

        for car in self.sorted_cars_south:
            self.removeItem(car)

        for car in self.sorted_cars_north:
            self.removeItem(car)
        
        self.coche.clear()
        self.coche_down.clear()
        self.coche_up.clear()
        self.coche_left.clear()
        self.coche_right.clear()
        
        


        self.removed = True

    def recreate_cars(self):
        self.recreate = True
        self.removed = False

    def count_cars(self):
        for car in self.coche:
            if car.counted:
                continue
            if self.lights[0].get_state() == "green" and car.y() >= 121 and car.y() <= 125 and car.x() >= 340 and car.x() <= 360: #NORTH ROAD
                self.counted_cars_north += 1
                car.counted = True
            elif self.lights[3].get_state() == "green" and car.x() >= 235 and car.x() <= 260 and car.y() >= 300 and car.y() <= 340 : #WEST ROAD
                self.counted_cars_west += 1
                car.counted = True
            elif self.lights[2].get_state() == "green" and car.y() >= 445 and car.y() <= 470 and car.x() >= 390 and car.x() <= 415 : #SOUTH ROAD
                self.counted_cars_south += 1
                car.counted = True
            elif self.lights[1].get_state() == "green" and car.x() >= 525 and car.x() <= 545 and car.y() >= 205 and car.y() <= 235 : #EAST ROAD
                self.counted_cars_east += 1
                car.counted = True

    def autovelox_tag(self):
        if len(self.coche) >= 1:
            for car in self.coche:
                if car.y() >= 121 and car.y() <= 125 and car.x() >= 340 and car.x() <= 360:#NORTH ROAD
                    self.ts_north = car.get_tag() + " " + f"{car.get_speed():.2f}"
                elif car.x() >= 235 and car.x() <= 260 and car.y() >= 300 and car.y() <= 340 : #WEST ROAD
                    self.ts_west = car.get_tag() + " " + f"{car.get_speed():.2f}"
                elif car.y() >= 445 and car.y() <= 470 and car.x() >= 390 and car.x() <= 415 : #SOUTH ROAD
                    self.ts_south = car.get_tag() + " " + f"{car.get_speed():.2f}"
                elif car.x() >= 525 and car.x() <= 545 and car.y() >= 205 and car.y() <= 235 :#EAST ROAD
                    self.ts_east = car.get_tag() + " " + f"{car.get_speed():.2f}"

    def autovelox_speed(self):
        max_speed = 2.5
        if len(self.coche) >= 1:
            for car in self.coche:
                if car.y() >= 121 and car.y() <= 125 and car.x() >= 340 and car.x() <= 360 and car.get_speed() >= max_speed: #NORTH ROAD
                    self.autovelox_exceed.append({"tag": car.get_tag(), "speed": car.get_speed()})
                    if car.checked == True:
                        return
                    save_data(car.get_tag(), car.get_speed())
                    car.checked = True

                elif car.x() >= 260 and car.x() <= 270 and car.y() >= 310 and car.y() <= 340 and car.get_speed() >= max_speed: #WEST ROAD
                    self.autovelox_exceed.append({"tag": car.get_tag(), "speed": car.get_speed()})
                    car.checked = True
                    if car.checked == False:
                        save_data(car.get_tag(), car.get_speed())
                elif car.y() >= 445 and car.y() <= 470 and car.x() >= 390 and car.x() <= 415 and car.get_speed() >= max_speed: #SOUTH ROAD
                    self.autovelox_exceed.append({"tag": car.get_tag(), "speed": car.get_speed()})
                    car.checked = True
                    if car.checked == False:
                        save_data(car.get_tag(), car.get_speed())
                elif car.x() >= 525 and car.x() <= 545 and car.y() >= 205 and car.y() <= 235 and car.get_speed() >= max_speed: #EAST ROAD
                    self.autovelox_exceed.append({"tag": car.get_tag(), "speed": car.get_speed()})
                    car.checked = True
                    if car.checked == False:
                        save_data(car.get_tag(), car.get_speed())
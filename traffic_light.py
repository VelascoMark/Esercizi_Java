from PyQt5.QtWidgets import QApplication, QSplitter, QMainWindow, QGraphicsView, QDesktopWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QCompleter, QComboBox   
import sys
from PyQt5.QtCore import Qt, QTimer, QElapsedTimer

from main_road import main_roads


class TrafficView(QGraphicsView):

    def resizeEvent(self, event): #method that will active whenever the window changes like fullscreen,etc to resize the graphic scene

        super().resizeEvent(event)

        self.fitInView(
            self.scene().sceneRect(),
            Qt.KeepAspectRatio
        )


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.makeUI()
        self.makeCentered()

    def makeUI(self):

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_count_cars)
        self.timer.start(30)

        self.scene = main_roads() #Object of main roads
        view = TrafficView() #Object of traffic viws 
        view.setScene(self.scene) #make the scene appear

        self.setWindowTitle("Velasco Converter")
        self.resize(800, 600)

        #Central widget the bottle which will contain the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)   
        layout = QHBoxLayout()
        central_widget.setLayout(layout)

        #Making the window divided
        traffic_side = QWidget()
        cmd_side = QWidget()

        traffic_layout = QVBoxLayout()
        cmd_layout = QVBoxLayout()

        traffic_side.setLayout(traffic_layout)
        cmd_side.setLayout(cmd_layout)
        
        traffic_layout.addWidget(view)

        traffic_side.setStyleSheet("""
            border-radius: 8px;
            background-color: #2b2b2b;
            padding: 10px;     
            
        """)
        cmd_side.setStyleSheet("""
            border-radius: 8px;
            background-color: #2b2b2b;
            padding: 10px;     
            
        """)

        
        #Define a divider so I can change the dimension
        splitter = QSplitter(Qt.Horizontal)#horizontal so we can drag the division in horinzotal
        splitter.addWidget(traffic_side)
        splitter.addWidget(cmd_side)

        splitter.setSizes([700, 300])#start size 700 for traffic side and 300 for the cmd side

        #Add the splitter to the main layout
        layout.addWidget(splitter)

        #Define the parts that will be added on CMD part
        self.cmd_title = QLabel("Commands:", self)
        self.cmd_title.adjustSize()
        cmd_layout.addWidget(self.cmd_title)
        self.cmd_title.setStyleSheet("""
            background-color: #1b1c1c;                  
            border: 1px solid black;     
            
        """)
        self.cmd_title.setFixedWidth(100)

        self.cmd_change_state = QPushButton("change", self)
        self.cmd_change_state.setStyleSheet("""
            background-color: #1b1c1c;                  
            border: 1px solid black;     
            
        """)
        cmd_layout.addWidget(self.cmd_change_state)

        


        #Define the display counter for each road
        count_layout_north = QHBoxLayout()
        cmd_layout.addLayout(count_layout_north)
        self.cmd_count_north = QLabel("North Road:", self)
        count_layout_north.addWidget(self.cmd_count_north)
        self.cmd_count_north.setFixedWidth(100)

        self.cmd_count_output_north = QLabel("", self)
        self.cmd_count_output_north.adjustSize()
        count_layout_north.addWidget(self.cmd_count_output_north)
        self.cmd_count_output_north.setStyleSheet("""
            background-color: #1b1c1c;                  
            border: 1px solid black;
        """)

        count_layout_south = QHBoxLayout()
        cmd_layout.addLayout(count_layout_south)
        self.cmd_count_south = QLabel("South Road:", self)
        count_layout_south.addWidget(self.cmd_count_south)
        self.cmd_count_south.setFixedWidth(100)

        self.cmd_count_output_south = QLabel("", self)
        self.cmd_count_output_south.adjustSize()
        count_layout_south.addWidget(self.cmd_count_output_south)
        self.cmd_count_output_south.setStyleSheet("""
            background-color: #1b1c1c;                  
            border: 1px solid black;
        """)

        count_layout_east = QHBoxLayout()
        cmd_layout.addLayout(count_layout_east)
        self.cmd_count_east = QLabel("West Road:", self)
        count_layout_east.addWidget(self.cmd_count_east)
        self.cmd_count_east.setFixedWidth(100)

        self.cmd_count_output_east = QLabel("", self)
        self.cmd_count_output_east.adjustSize()
        count_layout_east.addWidget(self.cmd_count_output_east)
        self.cmd_count_output_east.setStyleSheet("""
            background-color: #1b1c1c;                  
            border: 1px solid black;
        """)

        count_layout_west = QHBoxLayout()
        cmd_layout.addLayout(count_layout_west)
        self.cmd_count_west = QLabel("East Road:", self)
        count_layout_west.addWidget(self.cmd_count_west)
        self.cmd_count_west.setFixedWidth(100)

        self.cmd_count_output_west = QLabel("", self)
        self.cmd_count_output_west.adjustSize()
        count_layout_west.addWidget(self.cmd_count_output_west)
        self.cmd_count_output_west.setStyleSheet("""
            background-color: #1b1c1c;                  
            border: 1px solid black;
        """)

        autovelox_layout = QHBoxLayout()
        cmd_layout.addLayout(autovelox_layout)

        cmd_tag_layout1 = QHBoxLayout()
        autovelox_layout.addLayout(cmd_tag_layout1)
        self.cmd_tag1 = QLabel("(N) T/S:", self)
        cmd_tag_layout1.addWidget(self.cmd_tag1)
        self.cmd_tag1.setFixedWidth(70)

        self.cmd_tag_output1 = QLabel("", self)
        self.cmd_tag_output1.adjustSize()
        autovelox_layout.addWidget(self.cmd_tag_output1)
        self.cmd_tag_output1.setStyleSheet("""
            background-color: #1b1c1c;                  
            border: 1px solid black;
        """)

        cmd_tag_layout2 = QHBoxLayout()
        autovelox_layout.addLayout(cmd_tag_layout2)
        self.cmd_tag2 = QLabel("(S) T/S:", self)
        cmd_tag_layout2.addWidget(self.cmd_tag2)
        self.cmd_tag2.setFixedWidth(70)

        self.cmd_tag_output2 = QLabel("", self)
        self.cmd_tag_output2.adjustSize()
        autovelox_layout.addWidget(self.cmd_tag_output2)
        self.cmd_tag_output2.setStyleSheet("""
            background-color: #1b1c1c;                  
            border: 1px solid black;
        """)

        autovelox_layout2 = QHBoxLayout()
        cmd_layout.addLayout(autovelox_layout2) 

        cmd_tag_layout3 = QHBoxLayout()
        autovelox_layout2.addLayout(cmd_tag_layout3)
        self.cmd_tag3 = QLabel("(E) T/S:", self)
        cmd_tag_layout3.addWidget(self.cmd_tag3)
        self.cmd_tag3.setFixedWidth(70)

        self.cmd_tag_output3 = QLabel("", self)
        self.cmd_tag_output3.adjustSize()
        autovelox_layout2.addWidget(self.cmd_tag_output3)
        self.cmd_tag_output3.setStyleSheet("""
            background-color: #1b1c1c;                  
            border: 1px solid black;
        """)

        cmd_tag_layout4 = QHBoxLayout()
        autovelox_layout2.addLayout(cmd_tag_layout4)
        self.cmd_tag4 = QLabel("(W) T/S:", self)
        cmd_tag_layout4.addWidget(self.cmd_tag4)
        self.cmd_tag4.setFixedWidth(70)

        self.cmd_tag_output4 = QLabel("", self)
        self.cmd_tag_output4.adjustSize()
        autovelox_layout2.addWidget(self.cmd_tag_output4)
        self.cmd_tag_output4.setStyleSheet("""
            background-color: #1b1c1c;                  
            border: 1px solid black;
        """)
        cmd_layout.addStretch()

        self.cmd_change_state.clicked.connect(self.on_click)

        self.cmd_visual_output = QLabel("", self)
        self.cmd_visual_output.adjustSize()
        cmd_layout.addWidget(self.cmd_visual_output)
        self.cmd_visual_output.setStyleSheet("""
            background-color: #1b1c1c;                  
            border: 1px solid black;     
            """)

        self.cmd_remove_car = QPushButton("Remove cars!!", self)
        self.cmd_remove_car.setStyleSheet("""
            background-color: #1b1c1c;                  
            border: 1px solid black;     
            
        """)
        cmd_layout.addWidget(self.cmd_remove_car)

        self.cmd_remove_car.clicked.connect(self.on_click_removeCar)

        self.cmd_add_car = QPushButton("Add cars!!", self)
        self.cmd_add_car.setStyleSheet("""
            background-color: #1b1c1c;                  
            border: 1px solid black;     
            
        """)
        cmd_layout.addWidget(self.cmd_add_car)

        self.cmd_add_car.clicked.connect(self.on_click_addCar)


    def on_click(self):
        for x in range(0, 4):
            if self.scene.lights[x].get_state() == "green":
                self.scene.lights[x].set_state("red")
            else:
                self.scene.lights[x].set_state("green")

    def on_click_removeCar(self):
        self.scene.remove_cars()
        self.cmd_visual_output.setText("Removed cars, BOMBOCLAT")

    def on_click_addCar(self):
        if self.scene.recreate == False:
            self.scene.recreate_cars()
            self.cmd_visual_output.setText("ADDING CARS, BOMBOCLAT")
        else:
            self.scene.recreate = not (self.scene.recreate)
            self.cmd_visual_output.setText("STOPPED ADDING CARS, BOMBOCLAT")
        
    def makeCentered(self):
        frameDim = self.frameGeometry()#this mtethod takes the dimension in pixel of the screen
        center = QDesktopWidget().availableGeometry().center()
        frameDim.moveCenter(center)       
        self.move(frameDim.topLeft())

    def update_count_cars(self):
        self.cmd_count_output_north.setText(f"{self.scene.counted_cars_north}")
        self.cmd_count_output_south.setText(f"{self.scene.counted_cars_south}")
        self.cmd_count_output_east.setText(f"{self.scene.counted_cars_east}")
        self.cmd_count_output_west.setText(f"{self.scene.counted_cars_west}")
        self.cmd_tag_output1.setText(self.scene.ts_north)
        self.cmd_tag_output2.setText(self.scene.ts_south)
        self.cmd_tag_output3.setText(self.scene.ts_east)
        self.cmd_tag_output4.setText(self.scene.ts_west)


def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.showFullScreen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
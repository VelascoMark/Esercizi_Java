from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QCompleter, QComboBox
import sys
import math

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Velasco Converter")
        self.mainUI()
        

    def mainUI(self):
        #make the window in the center
        self.resize(800, 600)
        self.makeCentered()

        #Create a widget which will contain a vertival layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        #Define title of the label for the type
        self.type_title = QLabel("Pick type:", self)
        layout.addWidget(self.type_title)

        self.type_list = ["lenght", "time"]
        self.type_input = QComboBox()
        self.type_input.addItems(self.type_list)
        layout.addWidget(self.type_input)

        #Define a Hbox which will have labels and completers in horrizontal
        title_box = QHBoxLayout()
        layout.addLayout(title_box)

        #Define label titles
        self.input_title = QLabel("Input:", self)
        title_box.addWidget(self.input_title)
        self.output_title = QLabel("Output:", self)
        title_box.addWidget(self.output_title)

        #Define a QComboBox to make it a completer
        self.input_box = QComboBox()
        self.output_box = QComboBox()

        self.type_input.currentTextChanged.connect(self.change_type)

        self.input_box.currentTextChanged.connect(self.update_box)

        title_box2 = QHBoxLayout()
        layout.addLayout(title_box2)

        title_box2.addWidget(self.input_box)
        title_box2.addWidget(self.output_box)

        #Define label
        self.main_Text = QLabel("Insert a number to convert:", self)
        self.main_Text.setGeometry(5, 5, 1, 1)
        self.main_Text.setStyleSheet("""
            QLabel{
                font-size: 13px;        
            }
        """)
        self.main_Text.setFixedWidth(200)
        layout.addWidget(self.main_Text)

        #Define input con lineEdit
        self.input_Main = QLineEdit(self)
        layout.addWidget(self.input_Main)

        #When the return is pressed it doea the operation
        self.input_Main.returnPressed.connect(self.insert_clicked)

        #Define button to confirm the input
        self.confirm_Input = QPushButton("Insert", self)
        layout.addWidget(self.confirm_Input)

        #Connect a function when the button is clicked
        self.confirm_Input.clicked.connect(self.insert_clicked)

        #Define result text
        self.result_text = QLabel("Result:", self)  
        self.result_text.setStyleSheet("""
            QLabel{
                font-size: 10px;        
            }
        """)
        layout.addWidget(self.result_text)


        #Define output (result)
        self.output_main = QLabel("", self)
        self.output_main.setFixedWidth(200)
        self.output_main.setStyleSheet("""
            QLabel{
                font-size: 10px;
                border: 1px solid white;
                border-radius: 10px;
                padding: 5px;        
            }
        """)
        layout.addWidget(self.output_main)
        layout.addStretch()#move everything upwards

    def change_type(self, text):
        self.input_box.clear()
        self.output_box.clear()

        if text == "lenght":
            self.lenght_method()
        elif text == "time":
            self.time_method()

    def lenght_method(self):
        self.lenght_values = ["m", "km"]
        self.input_box.addItems(self.lenght_values)
        self.output_box.addItems(self.lenght_values)

    def time_method(self):
        self.time_values = ["minutes", "hour"]
        self.input_box.addItems(self.time_values)
        self.output_box.addItems(self.time_values)

    def update_box(self, choice):
        for i in range(self.output_box.count()):
            text = self.output_box.itemText(i)
            element = self.output_box.model().item(i)
            element.setEnabled(text != choice)


    def makeCentered(self):
        frameDim = self.frameGeometry()#this mtethod takes the dimension in pixel of the screen
        center = QDesktopWidget().availableGeometry().center()
        frameDim.moveCenter(center)
        self.move(frameDim.topLeft())

    def insert_clicked(self):
        try:
            output_text = f"{self.result():g}"
            self.output_main.setText(output_text)
        except ValueError as e:
            self.output_main.setText(str(e))

    def result(self):
        value = float(self.input_Main.text())

        if value < 0:
            raise ValueError("Negative numbers are not allowed")
        
        return self.conversion()
    
    def conversion(self):
        if self.type_input.currentText() == "lenght":
            value = float(self.input_Main.text())
            unit_input = self.input_box.currentText()
            unit_output = self.output_box.currentText()
            factors = {
                "m": 1,
                "km": 1000
            }
            meters = value * factors[unit_input]
            result = meters / factors[unit_output]
        elif self.type_input.currentText() == "time":
            value = float(self.input_Main.text())
            unit_input = self.input_box.currentText()
            unit_output = self.output_box.currentText()
            factors = {
                "minutes": 1,
                "hour": 60
            }
            minutes = value * factors[unit_input]
            result = minutes / factors[unit_output]
        
        return result

 


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
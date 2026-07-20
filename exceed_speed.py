import csv
import os

def save_data(tag, speed, file_name = "output.txt"):
    file_exist = os.path.isfile(file_name)
    with open(file= file_name, mode="a", newline="") as f:
        writer = csv.writer(f)
        if not file_exist:
            writer.writerow(["tag", "speed"])
        writer.writerow([tag, speed])

        
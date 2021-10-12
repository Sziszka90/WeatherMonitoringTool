
from datetime import datetime
import matplotlib.pyplot as plt
import os
import json

def create_plot(data_to_plot: dict) -> None:
    plt.title("City temperatures")

    temps = [temp for temp in data_to_plot.values()]

    plt.bar(list(data_to_plot), temps, width=0.25, edgecolor='k', linewidth=0.5)

    plt.xlabel("city")
    plt.ylabel("temperature")

    plt.yticks(ticks=[x for x in range(int(max(data_to_plot.values()))+5)])
     
    for index, value in enumerate(temps):
        plt.text(index, value, str(value),ha='center', va='bottom')
        

    my_path = os.getcwd()
    is_exist = my_path + "/plots/" + datetime.now().strftime("%Y-%m-%d") + "/"

    if not os.path.exists(is_exist):
        os.makedirs(is_exist)

    plt.savefig(my_path + "/plots/" + datetime.now().strftime("%Y-%m-%d") + "/" + datetime.now().strftime('%H-%M-%S') + ".pdf")


def create_file(data: dict) -> None:
    my_path = os.getcwd()
    is_exist = my_path + "/data/" + data['City'] + "/" + datetime.now().strftime("%Y-%m-%d") + "/"

    if not os.path.exists(is_exist):
        os.makedirs(is_exist)

    with open(is_exist + datetime.now().strftime('%H-%M-%S') + ".json", 'w') as convert_file:
     convert_file.write(json.dumps(data))

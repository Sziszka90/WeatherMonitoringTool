
from datetime import datetime
import matplotlib.pyplot as plt
import os
import json

def create_plot(data_to_plot: dict) -> None:

    min_value = int(min(data_to_plot.values()))
    max_value = int(max(data_to_plot.values()))
   
    plt.clf()

    plt.title("City temperatures")

    temps = [temp for temp in data_to_plot.values()]

    plt.bar(list(data_to_plot), temps, width=0.25, edgecolor='k', linewidth=0.5,color=['red', 'green', 'blue', 'yellow'])

    plt.grid(color='grey', linestyle='dotted', linewidth=0.5)

    plt.xlabel("city")
    plt.ylabel("temperature")

    if(max_value-min_value>30):
        step = 2
    else:
        step = 1

    plt.yticks(fontsize=6, ticks=[x for x in range(min_value-5, max_value+5, step)])

    plt.axhline(y=0)

    for index, value in enumerate(temps):
        plt.text(index, max_value+0.75, str(value),ha='center', va='bottom')

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

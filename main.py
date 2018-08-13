import os
import json
from measure_and_save import measure_and_save


def main():
    file = open("config.json","r")
    config = json.load(file)
    color_list = config["list"]
    SAVEFILENAME = config["savefile"]
    while(True):
        function = measure_and_save(SAVEFILENAME,"champ_and_lower.json", "session.json",color_list)
        end_flag = function.save_to_json()
        if end_flag ==1 :
            break
    print("Finish!")
    file.close()



if __name__ == "__main__":
    main()
import os
import json
from measure_and_save import measure_and_save


def main():
    color_list = ["red","blue","green","lgreen","brown","black","orange","yellow","violet","pink","gray","lred"]
    savefile_flag = 0
    SAVEFILENAME = "thicknessdata.json"
    while(True):
        function = measure_and_save(SAVEFILENAME,"champ_and_lower.json", "session.json",color_list)
        end_flag = function.save_to_json()
        if end_flag ==1 :
            break
    print("Finish!")



if __name__ == "__main__":
    main()
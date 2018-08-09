import os
import json

class measure_and_save:
    def __init__(self, savefile, champ_and_lower,session, option_list):
        self.savefile = savefile
        self.session = session
        self.champ_and_lower = champ_and_lower
        self.option_list = option_list

    def save_to_json(self):
        index = 0
        end_flag = 0
        if os.path.exists(self.session):
            file2 = open(self.session, "r")
            now_session = json.load(file2)
            index = now_session["session"]
            file2.close()
        else:
            now_session = {}
        if os.path.exists(self.savefile):
            file = open(self.savefile,"r")
            savejson = json.load(file)
            file.close()
        else:
            savejson = []
        if not os.path.exists(self.champ_and_lower):
            file = open(self.champ_and_lower,"w")
            savejson = {"champ_index":0,"lowest_index":0}
            json.dump(savejson, file, indent=2, sort_keys =True)
            file.close()
        OK_flag = "n"
        while(True):
            print("")
            print("index",index)
            print("Input Now thickness or q to finish programm")
            now_thickness = input()
            if now_thickness == "q":
                break
            while(True):
                print("Input Now color")
                print("Please choose from list below")
                print(self.option_list)
                now_color = input()
                if now_color in self.option_list:
                    break
                print("This is not in the option_list")
            print("OK? y/n")
            while(True):
                OK_flag = input()
                if OK_flag == "y":
                    break
                elif OK_flag == "n":
                    print("please enter correct thickness and color")
                    break
                else:
                    print("please enter y/n")
            if OK_flag == "y":
                try:
                    test = float(now_thickness)
                    break
                except ValueError:
                    print("please enter correct type number")
        if not now_thickness == "q":
            file = open(self.savefile,"w")
            savejson.append({"index":index,
                             "thickness":float(now_thickness),
                             "color":now_color})
            json.dump(savejson, file)
            file.close()
            file = open(self.champ_and_lower,"r")
            c_l_index = json.load(file)
            file.close()
            nowchamp, nowlowest = self.champion_or_lowest(float(now_thickness),
                                                          index,
                                                          c_l_index["champ_index"],
                                                          c_l_index["lowest_index"])
            file = open(self.champ_and_lower,"w")
            savejson = {"champ_index":nowchamp,"lowest_index":nowlowest}
            json.dump(savejson, file, indent=2, sort_keys =True)
            file.close()
            now_session["session"] = index + 1
            file2 = open(self.session, "w")
            json.dump(now_session, file2)
            file2.close()
        if now_thickness == "q":
            end_flag = 1
        return end_flag
    
    def champion_or_lowest(self, now_thickness:int, index, now_champion_index, now_lowest_index):
        if index == 0:
            champion_index = None
            lowest_index = None
        file = open(self.savefile, "r")
        nowjson = json.load(file)
        if max([x["thickness"] for x in nowjson]) == now_thickness:
            print()
            print("#################")
            print("You are Champion!")
            print("#################")
            print()
            champion_index = index
            lowest_index = now_lowest_index
        elif min([x["thickness"] for x in nowjson]) == now_thickness:
            print()
            print("#################")
            print("You are Lowest!")
            print("#################")
            print()
            champion_index = now_champion_index
            lowest_index = index
        else :
            print("Normal...")
            champion_index = now_champion_index
            lowest_index = now_lowest_index
        file.close()
        return champion_index, lowest_index
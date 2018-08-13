import os
import json

savefile = open("thickness_ave.json","w")
file = open("config.json","r")
config = json.load(file)
color_list = config["list"]
data = json.load(open(config["savefile"],"r"))
savedata_json = {}
for color in color_list:
  print(color)
  counter = 0
  sum_data = 0
  max_data = 0
  min_data = 100
  for now_data in data:
    print(now_data)
    if now_data["color"] == color:
      counter += 1
      sum_data += now_data["thickness"]
      if now_data["thickness"] > max_data:
        max_data = now_data["thickness"]
      if now_data["thickness"] < min_data:
        min_data = now_data["thickness"]
  if not counter == 0:
    thickness_average = round(sum_data/counter,2)
    savedata_json[color] = {}
    savedata_json[color]["average"] = thickness_average
    savedata_json[color]["max"] = max_data
    savedata_json[color]["min"] = min_data
    savedata_json[color]["counter"] = counter
json.dump(savedata_json,savefile,sort_keys=True)
savefile.close()
file.close()
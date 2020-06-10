import pandas as pd
import json
import os



#forMoreJsonFiles
data= []
#pathOfJsonFiles
path_to_json = 'C:/Users/Αναστασία/Desktop/collaborative filtering/json/'
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
  with open(path_to_json + file_name) as json_file:
      data.append(json.load(json_file))

df=pd.DataFrame()
for i, ind in enumerate(data):
   # read list inside dict
   _list = data[data.index(ind)]['Reviews']
   hotelInfo = data[data.index(ind)]['HotelInfo']['Name']
   ratings = {}
   #read listvalue and load dict
   for v in _list:
      ratings[v['Author']]= float(v['Ratings']['Overall'])

   df2 = pd.DataFrame(ratings,index=[hotelInfo])
   df = df.append(df2)

print(df)

#forOneJsonFile
#with open('C:/Users/Αναστασία/Desktop/json/72572.json','r') as f:
#  data = json.load(f)
# read list inside dict
#_list = data['Reviews']
#hotelInfo = data['HotelInfo']['Name']

# read listvalue and load dict
#for v in _list:
# ratings[v['Author']]= float(v['Ratings']['Overall'])

#df = pd.DataFrame(ratings,index=[hotelInfo])
#print(df)
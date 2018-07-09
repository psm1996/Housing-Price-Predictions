import csv
data_csv=open("total_dataset.csv","w")

#Columns name
value="House ID,Built_Date,Priced_date,Garden,dock_dist,capital_dist,royalMarket_dist,guardingTower_dist,river_dist,renovation,dining,bedroom,bathroom,kingVisit,curse,blessing,farm_land,location,holy_tree,knight_house_dist,builder\n"
data_csv.write(value)

dict={"ID":"NaN","Date Built":"NaN","Date Priced":"NaN","garden":"NaN","Dock":"NaN","Capital":"NaN","Royal Market":"NaN","Guarding":"NaN","River":"NaN","renovation":"NaN","dining":"NaN",
"bedrooms":"NaN","bathrooms":"NaN","Visited":"NaN","curse":"NaN","blessed":"NaN","farm":"NaN","Location":"NaN","Holy":"NaN","Knight":"NaN","builder":"NaN"}

build={"Bob":"0","Bright_Brothers":"1","The_Greens":"2","The_Lannisters":"3","The_Kings":"4","The_Ollivers":"5","The_Overlords":"6","The_Starks":"7","Wood_Priests":"8","Masters_of_Stones":"9","Not_Known":"NaN"}
locate={"King's Landing":"0","The Mountains":"1","Servant's Premises":"2","Cursed Land":"3"}

def makedataset(file):
	dict['builder']=file.split(".")[0]
	flag=1
	with open(file,"rt") as f:
		for line in f:
			if line=='\n':
				if flag==1:
					value=[]
					dict['builder']=build[file.split(".")[0]]
					for keys in dict:
						value.append(dict[keys])
						dict[keys]="NaN"
					flag=0
					row=csv.writer(data_csv)
					row.writerow(value)
					#data_csv.write(value)
				else:
					flag=1
				continue
			if 'ID' in line:
				dict['ID']=line.split(" ")[4]
			elif 'Date' in line:
				dict['Date Built']=line.split(" ")[3].split("/")[2]
				dict['Date Priced']=line.split(" ")[11].split("/")[2]
			elif 'garden' in line:
				if 'no' in line:
					dict['garden']='0'
				else:
					dict['garden']='1'
			elif 'Dock' in line:
				dict['Dock']=line.split(" ")[5]
			elif 'Capital' in line:
				dict['Capital']=line.split(" ")[4]
			elif 'Royal' in line:
				dict['Royal Market']=line.split(" ")[5]
			elif 'Guarding' in line:
				dict['Guarding']=line.split(" ")[5]
			elif 'River' in line:
				dict['River']=line.split(" ")[5]
			elif 'renovation' in line:
				if 'not' in line:
					dict['renovation']='0'
				else:
					dict['renovation']='1'
			elif 'dining' in line:
				dict['dining']=line.split(" ")[2]
			elif 'bedrooms' in line:
				dict['bedrooms']=line.split(" ")[2]
			elif 'bathrooms' in line:
				dict['bathrooms']=line.split(" ")[2]
			elif 'visit' in line:
				dict['Visited']='0'	
			elif 'Visited' in line:
				dict['Visited']='1'
			elif 'cursed' in line:
				dict['curse']='1'
			elif 'curse' in line:
				dict['curse']='0'
			elif 'blessed' in line:
				dict['blessed']=line.split(" ")[5]
			elif 'farm' in line:
				if 'small' in line:
					dict['farm']='1'
				elif 'huge' in line:
					dict['farm']='2'
				else:
					dict['farm']='0'
			elif 'Location' in line:
				dict['Location']=locate[line[27:].rstrip('\n')]
			elif 'Holy' in line:
				if 'stands' in line:
					dict['Holy']='1'
				else:
					dict['Holy']='0'
			elif 'Knight\'s' in line:
				dict['Knight']=line.split(" ")[5]


text_list=["Bob.txt","Bright_Brothers.txt","Masters_of_Stones.txt","Not_Known.txt",
"The_Greens.txt","The_Kings.txt","The_Lannisters.txt","The_Ollivers.txt","The_Overlords.txt","The_Starks.txt","Wood_Priests.txt"]
for builders in text_list:
	makedataset(builders)
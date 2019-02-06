fin=open("Street_Centrelines.csv","r")
x=fin.readlines()
def street_classes():
	street_class={}
	for data in x:
		if data[10] not in street_class:
			street_class[data[10]]=data[2]
		else:
			street_class[data[10]].join(x[2])
	return street_class

street_classes()


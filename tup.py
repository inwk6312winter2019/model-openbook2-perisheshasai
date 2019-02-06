file=open("Street_Centrelines.csv")
l=[]
def easy(file):
	file.readline()
	for line in file:
		line=line.split(",")
		a=tuple((line[2],line[4],line[6],line[7]))
		print(a)
easy(file)

def maintenance():
    hist = dict()
    for fun in file:
        fun = fun.split(",")
        if fun[12] not in hist:
            hist[fun[12]] = 1
        else :
            hist[fun[12]] += 1
    print(hist)


def unique():
    own_list = file[11]
    new_list = []
    for u in file:
        u = u.split(",")
        if u[11] not in new_list:
            new_list.append(u[11])
print(new_list)

easy()
maintenance()
unique()

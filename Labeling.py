# combining all *.fits data 
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import os
import glob

def loaddata():
	path1='/home/zhou/keras/kepler/kepler_0021_orig_nokoi'

	step = 100
	index = 0

	name1=[]
	transits=[]

#loading data into matrix
	for filename in glob.glob(os.path.join(path1, '*.fits')):
		name1.append(filename)
	#print(len(name1))
	#char = input("please stop")

    #length estimation
	#summ = 0
	#for i in range(len(name1)):
		#data = fits.getdata(name1[i])
		#time = data[0]
		#length = len(time)
		#summ = summ + int(length/step)
	#print (summ)
	#char = input('1234')

	#main function
	s=(100,274189)
	trainx=np.zeros(s)
	trainy=np.zeros(274189)
	for i in range(len(name1)):
		data = fits.getdata(name1[i])
		print (name1[i], i, i/len(name1))
		time=data[0]
		flux=data[1]
		initialtime = time[0]
		length=len(time)
		k = 0
		t = 1
		print (time[length-1])
		while(k<time[length-1]): #locating transits in time
			k=initialtime+t*3.166666
			transits.append(k)
			t=t+1
		initial = 0
		for j in range(0, int(length/step)):
			fluxtemp=flux[initial:initial+step]
			#timetemp=time[initial:initial+step]
			#trainy[j+index] = 0
			#plt.plot(timetemp,fluxtemp)
			#for m in range(len(transits)):
			#	if(time[initial]<transits[m] and transits[m]<time[initial+step]):
			#		trainy[j+index] = 1
			#print(trainy[j+index])
			#plt.show()
			#char = input("please stop")
			trainx[:,j+index]=fluxtemp
			initial = initial+step
		index = index + int(length/step)
		print (index)
	p = 'x-nokoi.csv'
	q = 'y-nokoi.csv'
	np.savetxt(p,trainx,delimiter=",")
	np.savetxt(q,trainy,delimiter=",")


loaddata()



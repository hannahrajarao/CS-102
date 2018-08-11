#input: destination, departure time
print("""List of Stations:
            Penn
            Jamaica
            Baldwin
            Bellmore
            Massapequa
            Babylon
            """)
origin = input("Please enter origin: ")
destination = input("Please enter destination: ")
departTime = input("Please enter departure time (24 hours) ex. '0739', '1428': ")
eastbound = -1   #0: false  1: true
reverseTrick = 0 #0: false  1: true
smallestTime = 0 #I wish!
arrivalTime = ''

#station lists
#stores data of train times by station
#matching indices indicate same train
pennE =       [ None ,  None , '1105', '1122', '1135', '1205', '1214']
jamaicaE =    [ None ,  None , '1128', '1142', '1158', '1228', '1243']
baldwinE =    [ None ,  None ,  None , '1148',  None , '1219', '1247']
bellmoreE =   [ None , '1128', '1157',  None , '1228', '1256',  None ]
massapequaE = ['1105', '1137', '1205',  None , '1237', '1305',  None ]
babylonE =    ['1124', '1153', '1221', '1224', '1253', '1321', '1325']

babylonW =    [ None ,  None ,  None ,  None , '1100', '1115', '1148']
massapequaW = [ None ,  None ,  None , '1104',  None , '1131', '1204']
bellmoreW =   [ None ,  None ,  None , '1112',  None , '1139', '1212']
baldwinW =    ['1022',  None , '1048', '1122',  None , '1148', '1222']
jamaicaW =    [ None ,  None , '1109', '1147', '1149', '1209', '1247']
pennW =       ['1105', '1108', '1129', '1205', '1208', '1229', '1305']

#use list to number stations
stations = ["Penn","Jamaica", "Baldwin", "Bellmore", "Massapequa", "Babylon"]
originIndex = -1
destIndex = -1
#determine whether train is travelling eastbound or westbound
for i in range(len(stations)):
    if(stations[i] == origin):
        originIndex = i
    if(stations[i] == destination):
        destIndex = i

if(originIndex > destIndex):
    eastbound = 0 #false - westbound
if(destIndex > originIndex):
    eastbound = 1 #true - eastbound
else:
    print("You're already at your station!")
    #origin station is the same as destination

#list of lists (similar to 2D array in other languages
#to determine which station list is needed
#(using same index system as before)
east = [pennE, jamaicaE, baldwinE, bellmoreE, massapequaE, babylonE]
west = [pennW, jamaicaW, baldwinW, bellmoreW, massapequaW, babylonW]
direction = [west, east]

departTimeList = direction[eastbound][originIndex] #returns station list
arriveTimeList = direction[eastbound][destIndex]

print(departTimeList)
print(arriveTimeList)

for i in range(len(departTimeList)):
    if(departTimeList[i] > departTime):
        departTime = departTimeList[i]
        arrivalTime = arriveTimeList[i]
        break
if(i == len(departTimeList)):
    departTime = departTimeList[i-1]
    arrivalTime = arriveTimeList[i-1]
    print('No trains past desired separture time, here is the latest one')

#TODO make a method to take two strings and return time interval
smallestTime = int(arrivalTime[2:]) - int(departTime[2:]) #calculate minutes
smallestTime += (int(arrivalTime[:2]) - int(departTime[:2])) * 60 #calculate hours

#check reverse trick

print('Departure time: {0}'.format(departTime))
print('Arrival time: {0}'.format(arrivalTime))
print('Travel time: {0}'.format(smallestTime))

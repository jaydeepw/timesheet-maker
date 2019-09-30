from datetime import datetime

def getTimeWithCheckInOut(line):
    strings = line.rpartition(":")
    print strings
    #('[11:36 AM, 9/28/2019] J W', ':', ' Out 1136\n')
    amPmItem = strings[-3]
    #[3:18 PM, 9/27/2019] J W
    amPm = None
    if "AM" in amPmItem:
        amPm = "AM"
    elif "PM" in amPmItem:
        amPm = "PM"
    else:
        print("Error! No AM/PM found")
    #print amPm
    #get last item in the list
    timeWithCheckInOut = strings[-1].replace('\n', '').replace('\r', '')
    timeListWithCheckInOut = timeWithCheckInOut.rsplit(" ")
    #print "timeListWithCheckInOut" , timeListWithCheckInOut
    #['', 'Out', '834']
    timeMagnitue = timeListWithCheckInOut[-1]
    #print timeMagnitue
    #1136
    formattedTime = insertChar(timeMagnitue, -2, ":")
    #print formattedTime
    #11:36
    clockTime = formattedTime + " " + amPm
    #11:36 AM
    return clockTime

def insertChar(mystring, position, chartoinsert):
    longi = len(mystring)
    mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
    return mystring  

def getTime(line):
    strings = line.rsplit(":", 2)
    #print strings
    #print len(strings)
    #get last item in the list
    return strings[-1]


whatsapp_names = ["J W", "Jay", "JZ"]
lineExclusion = ["@J W", "Hey JW", "Hey J W"]

f= open("data-sep2019.txt","r")
lines =f.readlines()
linesWithName = 0
print "Parsing ",len(lines)," lines"
for line in lines:
    for name in whatsapp_names:
        if name in line:
            if name not in lineExclusion:
                #print(line)
                timeWithCheckInOut = getTimeWithCheckInOut(line)
                print(timeWithCheckInOut)
                time = getTime(timeWithCheckInOut)
                linesWithName = linesWithName + 1

if linesWithName != 0:
    print "Found ", linesWithName, " relevant lines"
else:
    print "Error! Found no check in/out"
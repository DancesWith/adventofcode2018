from datetime import datetime, timedelta
from statistics import mode
from operator import attrgetter
import collections

class Shift:
    guardID = ""
    minsAsleep = 0
    instructions = []
    iMinsAsleep = []
    commonMin = 0
    frequentMin = 0

    def __init__(self, data):
        self.instructions = data

    def parseInstructions(self):
        fallAsleepMin = 0
        self.iMinsAsleep = []

        for i in self.instructions:
            if "#" in i:
                #print(i.split("#")[1])
                #print(i.split("#")[1].split(" "))
                self.guardID = int(i.split("#")[1].split(" ")[0])
                continue

            if "falls asleep" in i:
                fallAsleepMin = int(i.split("]")[0][15:])
                continue

            if "wakes up" in i:
                wakeUpMin = int(i.split("]")[0][15:])
                self.minsAsleep = self.minsAsleep + (wakeUpMin - fallAsleepMin)

                while wakeUpMin > fallAsleepMin:
                    self.iMinsAsleep.append(fallAsleepMin)

                    fallAsleepMin = fallAsleepMin + 1

                continue

        if len(self.iMinsAsleep) > 0:
            self.commonMin = max(self.iMinsAsleep, key = self.iMinsAsleep.count)
            icount = {}
            for i in self.iMinsAsleep:
                icount[i] = icount.get(i, 0) + 1

            self.frequentMin = max(icount.values())

    def appendInstructions(self, data):
        for d in data:
            self.instructions.append(d)

        self.parseInstructions()

file = open("C:\\Users\\Alexander\Documents\\adventofcode2018\\Day4\\input.txt", "r").readlines()

datetime_object = datetime.strptime('1518-05-28 00:59', '%Y-%m-%d %H:%M')

#for f in file:w
#datetime.strptime('1518-05-28 00:59', '%Y-%m-%d %H:%M')
#    g = f.split("]")[0][6:]

file.sort(key = lambda x: datetime.strptime(x.split("]")[0][1:], '%Y-%m-%d %H:%M'))

shifts = []
singleShift = []
first = True

counter = 0

for f in file:

    if "#" in f:
        if first != True:
            shifts.append(singleShift)
            singleShift = []
    
    if first == True:
        first = False

    singleShift.append(f)

    counter = counter + 1

    if counter == len(file):
        shifts.append(singleShift)

parsedShifts = []

for s in shifts:
    shift = Shift(s)
    shift.parseInstructions()
    existingShifts = [s for s in parsedShifts if shift.guardID == s.guardID]

    existingShift = next(iter(existingShifts), None)

    if existingShift is None: 
        parsedShifts.append(shift)
    else: 
        existingShift.appendInstructions(s)

    
    

mostAsleepGuard = [s for s in parsedShifts if s.minsAsleep == max(s.minsAsleep for s in parsedShifts)][0]

mostFrequentMin = [s.commonMin for s in parsedShifts if s.commonMin == max([s.commonMin for s in parsedShifts])][0]
mostFrequentMinGuardID = [s.guardID for s in parsedShifts if s.commonMin == max([s.commonMin for s in parsedShifts])][0]

theminsasleep = []

#for p in parsedShifts:


print(mostAsleepGuard.guardID * mostAsleepGuard.commonMin)

print(mostFrequentMinGuardID * mostFrequentMin)

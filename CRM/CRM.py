#OVERVIEW:
#The goal of this CRM is to make a more 'firm' centric pros system.  Instead of people being the primary object, Firms themselves are objects that have both people and initiative within them.  Innitiatives are their own objects, and have their own people, revenue and notes that are distinct to the innitiative itself. Innitiatives roll up into Firms. 

from tkinter import *
import pandas as pd
from firm import Firm
from desk import Desk
from initiative import Initiative
from person import Person

#create firm
wfa = Firm('Wells Fargo Advisors')
desks = {}
people = {}
initiatives = {}

#add people to firm
people_data = pd.read_csv('people.csv')
for person_data in people_data.values:
  name = person_data[0]
  role = person_data[1]
  desk = person_data[2]
  notes = person_data[3]
  initiative = person_data[4]
  
  #add innititive to firm
  if initiative not in initiatives:
    initiatives[initiative] = Initiative(initiative)

  #add desks to firm
  if desk not in desks:
    desks[desk] = Desk(desk, wfa)
  
  if name not in people:
    people[name] = Person(name, role, desks[desk], notes, initiatives[initiative])

  #add person to firm
  wfa.addPpl(people[name])

  #add people to desks
  desks[desk].addPpl(people[name])
  
#ADD note to muni desk
desks['Muni'].addNote("All users on this desk share the same TW view")
desks['Corporate'].addNote("Heavy users of SSOX and TW")
desks['Strategy'].addNote("Primary decision makers for all technology decisions")



#UI STUFF___________________________________________________________________
def getMuniDesk():
    return deskClick('Muni')
def getCorpDesk():
    return deskClick('Corporate')
def getTechDesk():
    return deskClick('Tech')
def getStrategyDesk():
    return deskClick('Strategy')
def getMtgeDesk():
    return deskClick('Mortgage')
def getRatesDesk():
    return deskClick('Rates')

def getFunction(desk):
    if desk == 'Muni':
        return getMuniDesk
    if desk == 'Corporate':
        return getCorpDesk
    if desk == 'Tech':
        return getTechDesk
    if desk == 'Strategy':
        return getStrategyDesk
    if desk == 'Mortgage':
        return getMtgeDesk
    if desk == 'Rates':
        return getRatesDesk

def getBrianMartin():
    return personClick("Brian Martin")
def getBrianBishop():
    return personClick("Brian Bishop")
def getRobAston():
    return personClick("Rob Aston")
def getBenManga():
    return personClick("Ben Manga")
def getJohnReilly():
    return personClick("John Reilly")
def getKevinDevlin():
    return personClick("Kevin Devlin")

def getPersonFunction(person):
    if person == "Brian Martin":
        return getBrianMartin
    if person == "Brian Bishop":
        return getBrianBishop
    if person == "Rob Aston":
        return getRobAston
    if person == "Ben Manga":
        return getBenManga
    if person == "John Reilly":
        return getJohnReilly
    if person == "Kevin Devlin":
        return getKevinDevlin
    
def personClick(name):
    person = people[name]
    personWindow = Tk()
    
    text = name + ", " + person.role + " on the " + person.desk.name + " desk."
    personLabel = Label(personWindow, text = text)
    personLabel.pack(fill = X)
    
    notesLabel = Label(personWindow, text = person.notes)
    notesLabel.pack()
    
    personWindow.mainloop()
    
def deskClick(desk):
    #create a new window focusing on the desk entity
    text = "Overview of the " + desk + " desk"
    deskWindow = Tk()
    
    deskLabel = Label(deskWindow, text = text, bg = "blue", fg = "white")
    deskLabel.pack(fill = X)
    
    #notes about the desk
    noteFrame = Frame(deskWindow)
    noteFrame.pack()
    noteLabel = Label(noteFrame, text = desks[desk].notes)
    noteLabel.pack()
    
    #people in the desk
    peopleFrame = Frame(deskWindow)
    peopleFrame.pack()
    peopleLabel = Label(peopleFrame, text = "Users", bg = "red", fg = "white")
    peopleLabel.pack(fill = X)
    
    #make button for each person
    for person in desks[desk].people:
        function = getPersonFunction(person.name) #TODO return a function to the correct person
        button = Button(peopleFrame, text = person.name, command = function)
        button.pack(side = LEFT)
    
    deskWindow.mainloop()
    
#BUILD UI with Pack
window = Tk()

topLabel = Label(window, text = "Desks at Wells Fargo Advisors", fg = "white", bg = "blue")
topLabel.pack(fill = X)

#bottomFrame = Frame(window)
#bottomFrame.pack(side = BOTTOM, fill = X)
#bottomLabel = Label(bottomFrame, text = "People", fg = "white", bg = "red")
#bottomLabel.pack(fill = X)

#make a button for each desk
for desk in desks.keys():
    function = getFunction(desk)
    button = Button(window, text = desk, fg = "blue", command = function)
    button.pack(side = LEFT)
    
#for person in people.keys():
    #button = Button(bottomFrame, text = person)
    #button.pack(side = LEFT)

window.mainloop()


  



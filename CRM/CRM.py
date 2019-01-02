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
people = {'unknown' : None} #{names : people objects}
initiatives = {}

#add people to firm
people_data = pd.read_csv('WFA_people.csv')
for person_data in people_data.values:
  name = person_data[0]
  role = person_data[1]
  desk = person_data[2]
  notes = person_data[3]
  initiative = person_data[4]
  boss = person_data[5]
  
  #add innititive to firm
  if initiative not in initiatives:
    initiatives[initiative] = Initiative(initiative)

  #add desks to firm
  if desk not in desks:
    desks[desk] = Desk(desk, wfa)
  
  #create person
  if name not in people:
    people[name] = Person(name, role, desks[desk], notes, initiatives[initiative], boss)

  #add person to firm
  wfa.addPpl(people[name])

  #add people to desks
  desks[desk].addPpl(people[name])
  
#second iteration to add all bosses to people objects:
for person in people.values():
    if person:
        person.boss = people[person.boss]
    
  
#ADD notes to desks #TODO to add an 'add note' field/button to do this from UI
desks['Muni'].addNote("All users on this desk share the same TW view")
desks['Corporate'].addNote("Heavy users of SSOX and TW")
desks['Strategy'].addNote("Primary decision makers for all technology decisions")
desks['Tech'].addNote("Buncha nerds")

#UI STUFF___________________________________________________________________

#Create desk click function dictionary___________________________
desk_to_deskFunc = {}
for desk in desks:
    def f(desk = desk):
        return deskClick(desk)
    desk_to_deskFunc[desk] = f
    
#Create person click function dictionary___________________________
name_to_personFunc = {}
for name in people:
    def f(name = name):
        return personClick(name)
    name_to_personFunc[name] = f
    
    
#Person Button___________________________________________________________

def personClick(name):
    person = people[name]
    personWindow = Tk()
    
    text = name + ", " + person.role + " on the " + person.desk.name + " desk."
    personLabel = Label(personWindow, text = text)
    personLabel.pack(fill = X)
    
    notes = Label(personWindow, text = "Notes", bg = "blue", fg = "white")
    notes.pack(fill = X)

    notesLabel = Label(personWindow, text = person.notes)
    notesLabel.pack()
    
    bossLabel = Label(personWindow, text = "Reports up to", bg = "red")
    bossLabel.pack(fill = X)
    
    if person.boss:
        function = name_to_personFunc[person.boss.name]
        button = Button(personWindow, text = person.boss.name, command = function)
        button.pack()
    
    personWindow.mainloop()

#Person Button End_____________________________________________________________


#Desk Button___________________________________________________________________

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
        function = name_to_personFunc[person.name] #TODO return a function to the correct person
        button = Button(peopleFrame, text = person.name, command = function)
        button.pack(side = LEFT)
    
    deskWindow.mainloop()

#Desk button end_______________________________________________________________

    
    
#BUILD UI of main window______________________________________________________
window = Tk()

topLabel = Label(window, text = "Desks at Wells Fargo Advisors", fg = "white", bg = "blue")
topLabel.pack(fill = X)

#bottomFrame = Frame(window)
#bottomFrame.pack(side = BOTTOM, fill = X)
#bottomLabel = Label(bottomFrame, text = "People", fg = "white", bg = "red")
#bottomLabel.pack(fill = X)

#make a button for each desk
for desk in desks:
    function = desk_to_deskFunc[desk]
    button = Button(window, text = desk, fg = "blue", command = function)
    button.pack(fill = X)
    
#for person in people.keys():
    #button = Button(bottomFrame, text = person)
    #button.pack(side = LEFT)

window.mainloop()

#END OF UI Main Window_________________________________________________________


    
  




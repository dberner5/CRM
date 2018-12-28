# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:40:38 2018

@author: traveler
"""

class Firm():
  def __init__(self, name):
    self.name = name
    self.people = []
    self.initiative = []
    self.notes = []
    self.desks = []

  def addInn(self, i):
    self.initiative.append(i)
  
  def addPpl(self, person):
    self.people.append(person)

  def addDesk(self, desk):
    self.desks.append(desk)
  
  def addNote(self, note):
    '''
    note is a string
    '''
    self.notes.append(note)
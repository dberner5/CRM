# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:39:35 2018

@author: traveler
"""

class Desk():
  def __init__(self, name, firm):
    self.name = name
    self.firm = firm
    self.people = []
    self.initiative = []
    self.notes = ''
    
  def addFirm(self, firm):
    self.firms.append(firm)
  
  def addPpl(self, person):
    self.people.append(person)

  def addNote(self, note):
    '''
    note is a string
    '''
    self.notes = note
    
  def addInn(self, i):
    self.initiative.append(i)
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:40:58 2018

@author: traveler
"""

class Initiative():
  def __init__(self, name):
    self.name = name
    self.firms = []
    self.revenue = None
    self.people = [] #list of people objects
    self.notes = [] #list of notes that are strings

  def addFirm(self, firm):
    self.firms.append(firm)

  def setRev(self, rev):
    self.revenue = rev
  
  def addPpl(self, person):
    self.people.append(person)

  def addNotes(self, note):
    '''
    note is a string
    '''
    self.notes.append(note)

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:41:18 2018

@author: traveler
"""

class Person():
  def __init__(self, name, role, desk, notes, initiative, boss):
    self.name = name
    self.role = role
    self.desk = desk
    self.notes = notes #list of strings
    self.initiative = initiative
    self.boss = boss

  def addInn(self, i):
    self.initiative.append(i)

  def addDesk(self, desk):
    self.desk = desk

  def addNote(self, note):
    '''
    note is a string
    '''
    self.notes.append(note)
  
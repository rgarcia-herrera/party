# coding: utf-8
"""a directed graph example."""

from sqlalchemy import MetaData, Table, Column, Integer, ForeignKey, String, Float, Boolean
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.ext.declarative import declarative_base
import random

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    guests = relationship("Guest", back_populates="group")

    def boring(self):
        return True

    
class Guest(Base):
    __tablename__ = 'guests'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group", back_populates="guests")

    happy   = Column(Boolean)
    sex = Column(Boolean)

    def __init__(self, id):
        self.id = id
        self.happy = random.choice([True, False])
        self.sex = random.choice([True, False])
        self.group = random.choice(Group.query.all())

    def update_happiness(self):
#         let total count turtles-here
#   let same count turtles-here with [color = [color] of myself]
#   let opposite (total - same)
#   ;; you are happy if the proportion of people of the opposite sex
#   ;; does not exceed your tolerance
#   set happy? (opposite / total) <= (tolerance / 100)
# end

# to leave-if-unhappy  ;; turtle procedure
#   if not happy? [
#     set heading one-of [90 270]  ;; randomly face right or left
#     fd 1                         ;; leave old group
#   ]
# end

    def __repr__(self):        
        return "g'%s %s@%s'" % (self.happy, self.sex, self.group)


# coding: utf-8

from sqlalchemy import Column, Integer, ForeignKey, Float, Boolean
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

    def __repr__(self):
        return "group%s" % self.id
    
    
class Guest(Base):
    
    __tablename__ = 'guests'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group", back_populates="guests")

    happy   = Column(Boolean)
    sex = Column(Boolean)
    tolerance = Column(Float)
    
    def __init__(self, tolerance):
        self.happy = random.choice([True, False])
        self.sex = random.choice([True, False])
        self.group = random.choice(session.query(Group).all())
        self.tolerance = tolerance
        
    def update_happiness(self):
        total = len(self.group.guests)
        same = session.query(Guest).filter(
            Guest.sex == self.sex,
            Guest.group == self.group).count()

        opposite = total - same
        # you are happy if the proportion of people of the opposite sex
        # does not exceed your tolerance
        self.happy = (float(opposite) / float(total)) <= (self.tolerance)

# to leave-if-unhappy  ;; turtle procedure
#   if not happy? [
#     set heading one-of [90 270]  ;; randomly face right or left
#     fd 1                         ;; leave old group
#   ]
# end

    def __repr__(self):
        happy = "happy" if self.happy else "unhappy"
        sex = "male" if self.sex else "female"
        
        return "'guest=%s %s %s@%s'" % (self.id, happy, sex, self.group)


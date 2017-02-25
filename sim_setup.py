import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import random
import model

################################
# parse command line arguments #
################################
parser = argparse.ArgumentParser(description='Setup party simulation by creating and populating groups and guests.')
parser.add_argument('--db_url', default='sqlite:///party_sim.sqlite', help='DB URL, default: sqlite:///party_sim.sqlite')
parser.add_argument('--guests', type=int, default=100)
parser.add_argument('--min_tolerance', type=float, default=0.25)
parser.add_argument('--max_tolerance', type=float, default=0.30)
parser.add_argument('--groups', type=int, default=10)
args = parser.parse_args()

####################
# database connect #
####################
engine  = create_engine(args.db_url)
Session = sessionmaker(bind=engine)

session = Session()

model.Base.metadata.create_all(engine)
model.session=session

# create a bunch of groups
for n in range(args.groups):
    group=model.Group()
    session.add(group)

session.commit()

# create a bunch of guests    
for n in range(args.guests):
    guest=model.Guest(tolerance=random.uniform(args.min_tolerance, args.max_tolerance))
    session.add(guest)

session.commit()

for g in session.query(model.Guest).all():
    g.update_happiness()

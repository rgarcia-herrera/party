import argparse
from time import sleep

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import model

################################
# parse command line arguments #
################################
parser = argparse.ArgumentParser(description='Print command to run guest process for each guest in database.')
parser.add_argument('--db_url', default='sqlite:///party_sim.sqlite', help='DB URL, default: sqlite:///party_sym.sqlite')
args = parser.parse_args()

####################
# database connect #
####################
engine  = create_engine(args.db_url)
Session = sessionmaker(bind=engine)

session = Session()

model.Base.metadata.create_all(engine)
model.session=session

for g in session.query(model.Guest).all():
    print g

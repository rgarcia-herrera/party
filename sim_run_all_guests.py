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
parser.add_argument('--sleep', type=float, default=0.1)
parser.add_argument('--seconds', type=int, default=10)
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
    print "python guest_agent.py --db_url %s --sleep %s --seconds %s --guest %s &" % (args.db_url,
                                                                                         args.sleep,
                                                                                         args.seconds,
                                                                                         g.id)

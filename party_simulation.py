import argparse
from time import sleep

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import *

################################
# parse command line arguments #
################################
parser = argparse.ArgumentParser(description='edge interaction script')
parser.add_argument('--db_url', default='sqlite:///party_sim.sqlite', help='DB URL, default: sqlite:///db.sqlite')
parser.add_argument('--guest', type=int, required=True)
parser.add_argument('--sleep', type=float, default=0.1)
args = parser.parse_args()


####################
# database connect #
####################
engine  = create_engine(args.db_url)
Session = sessionmaker(bind=engine)

session = Session()

g = Guest.query.get(args.guest)
while True:
    g.update_happiness()
    session.commit()
    sleep(args.sleep)

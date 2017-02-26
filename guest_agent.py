import argparse
from time import sleep
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import model

################################
# parse command line arguments #
################################
parser = argparse.ArgumentParser(description='edge interaction script')
parser.add_argument('--db_url', default='sqlite:///party_sim.sqlite', help='DB URL, default: sqlite:///db.sqlite')
parser.add_argument('--guest', type=int, required=True)
parser.add_argument('--sleep', type=float, default=0.1)
parser.add_argument('--seconds', type=int, default=200)
args = parser.parse_args()


####################
# database connect #
####################
engine  = create_engine(args.db_url)
Session = sessionmaker(bind=engine)

session = Session()
model.session=session

g = session.query(model.Guest).get(args.guest)

now = datetime.datetime.now()
current_sec = (now.minute*60000000)+(now.second*1000000)
end_sec = current_sec + (args.seconds * 1000000)
while current_sec < end_sec:
    g.update_happiness()
    g.leave_if_unhappy()
    sleep(args.sleep)
    now = datetime.datetime.now()
    current_sec = (now.minute*60000000)+(now.second*1000000)
    

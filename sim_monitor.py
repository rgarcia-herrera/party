import argparse
import csv
from time import sleep
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import model
import sys

################################
# parse command line arguments #
################################
parser = argparse.ArgumentParser(description='Realtime monitor of simulation state.')
parser.add_argument('--db_url', default='sqlite:///party_sim.sqlite', help='DB URL, default: sqlite:///party_sym.sqlite')
parser.add_argument('--sleep', type=float, default=0.1)
parser.add_argument('--log', type=argparse.FileType('w'), default=sys.stdout, help='log to file')
args = parser.parse_args()

####################
# database connect #
####################
engine  = create_engine(args.db_url)
Session = sessionmaker(bind=engine)

session = Session()

model.Base.metadata.create_all(engine)
model.session=session

log = csv.writer(args.log)

while True:
    happy_guests = session.query(model.Guest).filter(model.Guest.happy == True).count()
    boring_groups = [g.boring() for g in session.query(model.Group).all()].count(True)
    now = datetime.datetime.now()
    second = str((now.minute*60000000)+(now.second*1000000)+now.microsecond)
    log.writerow([second, happy_guests, boring_groups])
    sleep(args.sleep)
    session.commit()

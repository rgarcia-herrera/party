#!/bin/bash

########################
# Simulation arguments #
########################
GUESTS=50
PARTY_GROUPS=10
MIN_TOLERANCE=0.22
MAX_TOLERANCE=0.25
DURATION=10 # in seconds

#####################
# environment setup #
#####################
MONITOR_SLEEP=0.05 # delay between sampling 
AGENT_SLEEP=0.1 # delay betwen agent iterations
DB_URL=mysql://party:hola@localhost/party


# setup simulation
python sim_setup.py --guests $GUESTS \
       --groups $PARTY_GROUPS \
       --min_tolerance $MIN_TOLERANCE \
       --max_tolerance $MAX_TOLERANCE \
       --db_url $DB_URL

# start logging monitor
python sim_monitor.py --sleep $MONITOR_SLEEP \
       --db_url $DB_URL \
       --log run.log \
       --seconds $(($DURATION+2)) &

sleep 0.02

# start all agents!
python sim_run_all_guests.py --sleep $AGENT_SLEEP \
       --seconds $DURATION \
       --db_url $DB_URL | sh


# let it cook for a short while
sleep $(($DURATION+4))

# plot the log!
python sim_plot.py --log run.log --fig run.png
geeqie run.png


#!/bin/bash

# setup simulation
python sim_setup.py --guests 50 \
       --groups 10 \
       --min_tolerance 0.2 \
       --max_tolerance 0.2 \
       --db_url mysql://party:hola@localhost/party

# start logging monitor
python sim_monitor.py --sleep 0.05 \
       --db_url mysql://party:hola@localhost/party \
       --log run.log \
       --seconds 12 &

sleep 0.02

# start all agents!
python sim_run_all_guests.py --sleep 0.1 \
       --seconds 10 \
       --db_url mysql://party:hola@localhost/party | sh


# let it cook for a short while
sleep 15

# plot the log!
python sim_plot.py --log run.log --fig run.png
geeqie run.png



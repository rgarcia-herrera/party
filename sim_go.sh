#!/bin/bash

python sim_setup.py --guests 50 \
       --groups 10 \
       --min_tolerance 0.2 \
       --max_tolerance 0.25 \
       --db_url mysql://party:hola@localhost/party

python sim_monitor.py --sleep 0.05 \
       --db_url mysql://party:hola@localhost/party \
       --log run.log &

sleep 0.1

python sim_run_all_guests.py --sleep 0.1 \
       --iterations 50 \
       --db_url mysql://party:hola@localhost/party | sh


#watch ps 


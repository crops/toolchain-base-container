#!/bin/bash

/etc/init.d/rethinkdb start
sleep 5
python3 -m launchers.codi-launcher

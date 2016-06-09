#!/bin/bash

/etc/init.d/rethinkdb start
python3 -m launchers.codi-launcher

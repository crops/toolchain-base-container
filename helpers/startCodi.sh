#!/bin/bash

/etc/init.d/rethinkdb start
sleep 5
python3 -m launchers.codi-launcher
# in case things went poorly, this tail
# will give us info rather than having a stopped
# container
tail -f /var/lib/rethinkdb/default/data/log_file

#!/bin/bash

/etc/init.d/rethinkdb start
sleep 5
/usr/local/bin/gunicorn -w 4 -b 0.0.0.0:10000 codi-launcher:app

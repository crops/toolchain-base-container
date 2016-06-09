#!/usr/bin/env python

import unittest
import os
import subprocess
import shutil
import tempfile
import sys
import stat
import imp
import inspect
from utils.testutils import *
import time

class TestCodiUp(unittest.TestCase):
    def setUp(self):
        self.codiAddr = os.environ['CODI_ADDR']
        self.codiPort=os.environ['CODI_PORT']
        self.dockerhubRepo=os.environ['DOCKERHUB_REPO']
        cmd = "docker  run -d -v /var/run/docker.sock:/var/run/docker.sock -p %s:%s  --name=codiTest %s/codi" % \
              (self.codiPort,self.codiPort,self.dockerhubRepo)
        p=subprocess.Popen(cmd.split(), shell=False)
        # getting rethinkdb and codi up can take a bit
        time.sleep(15)
    def tearDown(self):
        cmd = "docker rm -f codiTest"
        p=subprocess.Popen(cmd.split(), shell=False)
        pass


    def test_codi_up(self):
        cmd = "curl --silent -o- http://%s:%s/codi/ "%(self.codiAddr,self.codiPort)
        p=subprocess.Popen(cmd.split(), stderr=sys.stderr, stdout=subprocess.PIPE,
                        shell=False)

        upString="Show CODI API"
        found=checkString(upString,p.stdout)
        if not found:
            # error information is more useful than true is not false
            printStringSad(inspect.stack()[0][3],upString)

        self.assertTrue(found)



if __name__ == '__main__':
    unittest.main()

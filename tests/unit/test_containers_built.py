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

class TestContainersBuilt(unittest.TestCase):
    def setUp(self):
        self.sdkCropsRelease = os.environ['CROPS_RELEASE']
        self.containers=[]

        c={}
        c['name']="toolchain-base:%s"%(self.sdkCropsRelease)
        c['found']=False
        self.containers.append(c)
        c={}
        c['name']="codi:%s"%(self.sdkCropsRelease)
        c['found']=False
        self.containers.append(c)

    def tearDown(self):
        pass


    def test_containers_built(self):
        cmd = """docker  images """
        p=subprocess.Popen(cmd.split(), stderr=sys.stderr, stdout=subprocess.PIPE,
                        shell=False)

        allBuilt=checkPresentA(self.containers,p.stdout)
        if not allBuilt:
            # error information is more useful than true is not false
            printDockerImagesSadA(inspect.stack()[0][3],self.containers)

        self.assertTrue(allBuilt)



if __name__ == '__main__':
    unittest.main()

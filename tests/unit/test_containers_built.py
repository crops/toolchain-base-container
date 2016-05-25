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
        self.sdkTargets = os.environ['TARGETS'].split()
        self.sdkYPRelease = os.environ['YP_RELEASE']
        self.zephyrRelease = os.environ['ZEPHYR_RELEASE']
        self.ostroRelease =  os.environ['OSTRO_RELEASE']
        self.sdkCropsRelease = os.environ['CROPS_RELEASE']
        self.travisSlug = os.environ['TRAVIS_REPO_SLUG']
        self.dockerhubRepo = os.environ['DOCKERHUB_REPO']
        #print("travisSlug=%s"%(self.travisSlug))
        #print("dockerhubRepo=%s"%(self.dockerhubRepo))
        self.cList=[]
        self.baseD={}
        self.baseD['x86-64']={}
        self.baseD['x86-64']['name']="%s/toolchain-base:%s"%(self.dockerhubRepo,"latest")
        self.baseD['x86-64']['found']=False
        self.cList.append(self.baseD)
    def tearDown(self):
        pass


    def test_containers_built(self):
        cmd = """docker  images """
        p=subprocess.Popen(cmd.split(), stderr=sys.stderr, stdout=subprocess.PIPE,
                        shell=False)
        for c in self.cList:
            check=c
            allBuilt=checkPresent(check,p.stdout)
            if not allBuilt:
                # error information is more useful than true is not false
                printDockerImagesSad(inspect.stack()[0][3],check)

        self.assertTrue(allBuilt)



if __name__ == '__main__':
    unittest.main()

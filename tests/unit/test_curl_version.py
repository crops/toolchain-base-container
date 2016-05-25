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


def checkCurlVersion(majorVersion,minorVersion,myStream):
    v = getField(1,2,myStream)
    major=int(v.split('.')[0])
    minor=int(v.split('.')[1])
    if major < majorVersion:
        return False
    elif major > majorVersion:
        return True

    return minor>=minorVersion

class TestCurlVersion(unittest.TestCase):
    def setUp(self):
        self.dockerhubRepo = os.environ['DOCKERHUB_REPO']
        self.Container="%s/toolchain-base"%(self.dockerhubRepo)
        self.Program="curl"
        self.majorVersion=7
        self.minorVersion=45
    def tearDown(self):
        pass


    def test_program(self):
        cmd = "docker  run -it %s %s --version " %(self.Container,self.Program)
        p=subprocess.Popen(cmd.split(), stderr=sys.stderr, stdout=subprocess.PIPE,
                        shell=False)
        sThere=checkString(self.Program,p.stdout)
        if not sThere:
            # error information is more useful than true is not false
            printStringSad(inspect.stack()[0][3],self.Program)


        self.assertTrue(sThere)

    def test_version(self):
        cmd = "docker  run -it %s %s --version " %(self.Container,self.Program)
        p=subprocess.Popen(cmd.split(), stderr=sys.stderr, stdout=subprocess.PIPE,
                        shell=False)
        vOk=checkCurlVersion(self.majorVersion,self.minorVersion,p.stdout)
        if not vOk:
            # error information is more useful than true is not false
            printStringSad(inspect.stack()[0][3],"curl %s.%s"%(self.majorVersion,self.minorVersion))


        self.assertTrue(vOk)



if __name__ == '__main__':
    unittest.main()

import shlex
# general utility functions for checking things

def getField(line,field,myStream):
    ''' line counts from 1, field counts from 1 '''
    lCount=1
    for l in myStream:
        if lCount == line:
            fieldList=shlex.split(l)
            if len(fieldList) >= field:
                return fieldList[field-1]
            else:
                return None
        lCount+=1

def checkString(s,myStream):
    for l in myStream:
        if s in l:
            return True
    return False


def printStringSad(who,s):
    print("%s did not appear in check %s\n"%(s,who))

def checkPresent(myDict,myStream):
    for l in myStream:
        for k,v in  myDict.iteritems():
            repo=v['name'].split(':')[0]
            tag=v['name'].split(':')[1]
            if repo in l and tag in l :
                v['found']=True
    present=True
    for v in  myDict.itervalues():
        present &= v['found']
    return present

def printDockerImagesSad(hdr,myDict):
    cmd="docker images"
    p=subprocess.Popen(cmd.split(), stderr=sys.stderr, stdout=subprocess.PIPE,
                       shell=False)
    print("\n\nFAILURE--%s-- Images ->"%(hdr))
    for l in p.stdout:
        print ("%s",l)
    print ("Looking for:")
    for k,v in myDict.iteritems():
        print("%s found = %s"%(v['name'],v['found']))

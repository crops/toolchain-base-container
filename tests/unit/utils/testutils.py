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

def checkPresentA(myA,myStream):
    for l in myStream:
        for d in  myA:
            name=d['name'].split(':')[0]
            tag=d['name'].split(':')[1]
            if name in l and tag in l :
                d['found']=True
    present=True
    for d in  myA:
        present &= d['found']
    return present

def printDockerImagesSadA(hdr,myA):
    cmd="docker images"
    p=subprocess.Popen(cmd.split(), stderr=sys.stderr, stdout=subprocess.PIPE,
                       shell=False)
    print("\n\nFAILURE--%s-- Images ->"%(hdr))
    for l in p.stdout:
        print ("%s",l)
    print ("Looking for:")
    for d in myA:
        if not d['found']:
            print("%s found = %s"%(d['name'],d['found']))

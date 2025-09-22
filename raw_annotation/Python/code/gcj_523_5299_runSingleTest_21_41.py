from __future__ import print_function
import sys
import time
sys.setrecursionlimit(10 ** 6)
inputFileName = None
outputFileName = None
if inputFileName is not None:
    outputFileName = inputFileName[:-3] + ".out"
import platform
global MY_DEBUG
MY_DEBUG = platform.node().lower() in map(lambda s: s.lower(), ['HOMEPC3', 'lenovo'])
logF = None
if MY_DEBUG:
    logF = open("run.log", 'w')
def dbg_print(s):
    if MY_DEBUG:
        logF.write('{0}\n'.format(s))
        logF.flush()
startTime = time.time()
dbg_print(startTime)
def runSingleTest(inpF, outF):
    line = inpF.readline()
    tokens = line.split()
    a_exc = int(tokens[0])
    b_inc = int(tokens[1])
    line = inpF.readline()
    n = int(line)
    for i in xrange(n):
        guess = (a_exc + b_inc + 1) / 2
        print(guess, file=outF)
        line = inpF.readline_safe()
        if 'CORRECT' == line:
            return
        elif 'TOO_SMALL' == line:
            a_exc = guess + 1
        elif 'TOO_BIG' == line:
            b_inc = guess - 1
        else:
            dbg_print("Unexpected line '{0}'".format(line))
            raise RuntimeError("Unexpected line '{0}'".format(line))
    raise RuntimeError("AAAAA")
class InpFWrapper:
    def __init__(self, inpF):
        self.inpF = inpF
    def readline(self):
        line = self.inpF.readline()
        dbg_print("Read line is '{0}'".format(line.replace("\n", "\\n")))
        return line
    def readline_safe(self):
        line = self.inpF.readline()
        dbg_print("Read line safe is '{0}'".format(line.replace("\n", "\\n")))
        return line[0:-1] if (line[-1] == '\n') else line
class OutFWrapper:
    def __init__(self, outF):
        self.outF = outF
    def __getattr__(self, name):
        return getattr(self.outF, name)
    def write(self, str):
        dbg_print("Writing '{0}'".format(str.replace("\n", "\\n")))
        self.outF.write(str)
        self.outF.flush()
def myMain(inpF, outF):
    if (MY_DEBUG):
        dbg_print('input = {0}, out = {1}'.format(inputFileName, outputFileName))
    inpF = InpFWrapper(inpF)
    outF = OutFWrapper(outF)
    line = inpF.readline()
    testsCount = int(line)
    for i in xrange(1, testsCount + 1):
        dbg_print('--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime)))
        runSingleTest(inpF, outF)
        dbg_print('--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime)))
if inputFileName is not None:
    with open(inputFileName) as inpF:
        with open(outputFileName, 'w') as outF:
            myMain(inpF, outF)
else:
    myMain(sys.stdin, sys.stdout)
dbg_print("Finished!!!! Total time = {0}".format((time.time() - startTime)))
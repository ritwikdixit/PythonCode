#!usr/bin/python

#Ritwik Dixit 2015
#USACO style C++ auto compiler and grader
#
#Usage - In order to work properly:
#1. All inputs must be in the directory labled 1.in, 2.in ... n.in (n = # of test cases)
#2. likewise, outputs must be labeled 1.out, 2.out ... n.out
#3. the name of the .cpp file must be the same as the name of the directory with i/o files
#
#EXAMPLE dir:
#cmdrun.py <-- this script
#task.cpp <-- your C++ solution
#	task/
#		1.in
#		1.out
#		2.in
#		2.out
#		...
#		n.in
#		n.out

import os, os.path, time, sys, signal
import subprocess as sp

#C++ time out after 2 seconds
TIMEOUT = 2

def cleanCpp(filename):
	removefiles = ['rm', filename + '_exec', filename + '.in', filename + '.out']
	sp.call(removefiles)

#handle timeouts, interrupt with an exception
def signal_handler(signum, frame):
	raise Exception('T - Case Timed Out\n')

#Run the executable, timeout by raising an exception if takes too long
def execute(runcmd):
	global TIMEOUT
	signal.signal(signal.SIGALRM, signal_handler)
	signal.alarm(TIMEOUT)
	try:
		sp.call(runcmd)
	except Exception, msg:
		print msg


def runCpp(filename, numfiles):
	global TIMEOUT
	correct = 0
	#build the executable with g++ with same file name
	buildcmds = ['g++', filename + '.cpp', '-o', filename + '_exec']
	runcmd = ['./' + filename + '_exec']
	try:
		sp.call(buildcmds)
	except:
		print 'Compilation Error.'
		return
	#for each test case execute and check
	for i in range(1, numfiles+1):		
		print 'Running Test Case ' + str(i) + '...'
		caseStr = filename + '/' + str(i)
		#copies test case input contents into filename.in in working directory
		f = open(filename + '.in', 'w')
		f.writelines([line for line in open(caseStr + '.in', 'r')])
		f.close()

		#start a timer, execute
		start = time.time()
		execute(runcmd)
		end = time.time()

		elapsed = (end - start)*1000
		#format milliseconds nicely
		ms =  '%.2f' % elapsed

		#check outputs of the program and expected output
		fout = open(filename + '.out', 'r')
		f2 = open(caseStr + '.out', 'r')
		program_out = fout.readlines()
		expected_out = f2.readlines()
		fout.close()
		f2.close()

		#display the results
		if elapsed >= TIMEOUT*1000:
			continue
		elif program_out == expected_out:
			print '***--Correct--***'
			correct += 1
			print  'elapsed: ' + ms + 'ms\n'
		else:
			print 'XXXX--WRONG--XXXX\n'

	print 'Correct: ' + str(correct) + '/' + str(numfiles)
	#results, clean up current directory
	cleanCpp(filename)

args = sys.argv
filename = args[1]
usage = 'usage: python cmdrun.py <name>'

try:
	# of input and output files / 2
	testcases = len(os.listdir(os.getcwd() + '/' + filename))/2
	#go!
	runCpp(filename, testcases)
except:
	print usage
	print 'Attempting to clean files...'
	cleanCpp(filename)



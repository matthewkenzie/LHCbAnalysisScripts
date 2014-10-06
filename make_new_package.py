#!/usr/bin/env python

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-p","--packageName",help="The name of the package")
parser.add_option("-l","--location",default="../",help="Location to put package")
(opts,args) = parser.parse_args()

import sys
import os

os.system('mkdir -p %s/%s/interface'%(opts.location,opts.packageName))
os.system('mkdir -p %s/%s/src'%(opts.location,opts.packageName))
os.system('mkdir -p %s/%s/dat'%(opts.location,opts.packageName))
os.system('mkdir -p %s/%s/python'%(opts.location,opts.packageName))

def mkdir(subloc):

	os.system('mkdir -p %s/%s/%s'%(opts.location,opts.packageName,subloc))
	print '  -- ', 'Made directory', subloc

def linkFile(name, subloc):

	target_loc = os.path.abspath(os.path.join(opts.location,opts.packageName,subloc,name))
	source_loc = os.path.abspath(os.path.join('required_files',name))
	os.system('ln -s %s %s'%(source_loc,target_loc))
	print '  -- ', 'Linked file', name, 'to', subloc

print 'Building package', opts.packageName, 'in location', opts.location
os.system('mkdir -p %s/%s'%(opts.location,opts.packageName))

mkdir('interface')
mkdir('src')
mkdir('dat')
mkdir('python')
mkdir('scripts')

os.system('touch %s/%s/python/__init__.py'%(opts.location,opts.packageName))

linkFile('BranchDef.h','interface')
linkFile('BranchDef.cc','src')
linkFile('BaseAnalyser.h','interface')
linkFile('BaseAnalyser.cc','src')
linkFile('configProducer.py','python')
linkFile('dumpTreeBranches.py','scripts')
linkFile('makeBranchDef.py','scripts')
linkFile('makeLooper.py','scripts')
linkFile('makefile','')
linkFile('runAnalysis.py','')
linkFile('runFitter.py','')
linkFile('README.txt','')

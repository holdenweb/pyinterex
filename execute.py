#!/usr/bin/env python
#
# Hacked utility to allow the production of playerpiano script files
#
# If "interactive" input is required for target x.py then the system
# will look for a file called x.in (but only when input is actually
# called for, so you need not provide input files except when input
# is required).
#
import code
import sys
import os.path

class Raw_Input:
    def __init__(self, name):
        self.name = name
        self.new = True
    def __call__(self, prompt):
        if self.new:
            self.new = False
            self.file = open(self.name+".in")
        r = self.file.next()[:-1]
        print "%s%s" % (prompt, r)
        return r

def fixed_input(prompt):
    s = fixed_raw_input(prompt)
    r = eval(s, namespace)
    return r

def tagged(p, l, o, c): # returns prompted command
    if l:
        return "%s %s%s%s" % (p, o, l, c)
    else:
        return p

#
# This bit is so I can use the same utility to generate
# XML transcripts of interactive Python sessions for my
# Python classes at O'Reilly School of Technology. This
# will hopefully make the editor's life a little easier.
#
if sys.argv[1] == "-o": # O'Reilly output
    o, c = "<INS>", "</INS>"
    del sys.argv[1]
else:
    o = c = ""

filename = sys.argv[1]
fileroot = os.path.splitext(filename)[0]
fixed_raw_input = Raw_Input(fileroot)
namespace = {
    "raw_input": fixed_raw_input,
    "input": fixed_input}
SIloop = None # Used in pathological EOF
exprs = (line[:-1] for line in open(filename))
for e in exprs:
    print tagged('>>>', e, o, c)
    cmd = code.compile_command(e)
    while cmd is None:
        try:
            n = exprs.next()
        except StopIteration:
            if SIloop:
                sys.exit("Last statement appears to be incomplete")
            SIloop = True
            print >> sys.stderr, "[Attempting terminal newline insertion]"
            n = ""
        e += "\n" + n
        print tagged('...', n, o, c)
        print "+++ namespace +++\n", namespace
        cmd = code.compile_command(e)
    r = eval(cmd, namespace)
    if r:
        print repr(r)

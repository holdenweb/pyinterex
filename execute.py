#!/usr/bin/env python
#
# Hacked utility to allow the production of playerpiano script files
#
# Do not try to make this script execute itself!
#
import code
import sys

if sys.argv[1] == "-o": # O'Reilly output
    o, c = "<INS>", "</INS>"
    del sys.argv[1]
else:
    o = c = ""

def tagged(p, l, o, c): # returns prompted command
    if l:
        return "%s %s%s%s" % (p, o, l, c)
    else:
        return p

SIloop = None # Used in pathological EOF
exprs = (line[:-1] for line in open(sys.argv[1]))
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
        cmd = code.compile_command(e)
    r = eval(cmd)
    if r:
        print repr(r)

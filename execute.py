#!/usr/bin/env python
#
# Hacked utility to allow the production of playerpiano script files
#
# Do not try to make this script execute itself!
#
import code
import sys

SIloop = None # Used in pathological EOF
exprs = (line[:-1] for line in open(sys.argv[1]))
for e in exprs:
    print '>>> %s' % e
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
        print '... %s' % n
        cmd = code.compile_command(e)
    r = eval(cmd)
    if r:
        print repr(r)

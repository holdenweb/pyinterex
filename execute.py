#!/usr/bin/env python
#
# Hacked utility to allow the production of playerpiano script files
#
# Do not try to make this script execute itself!
#
import code
import sys

exprs = (line[:-1] for line in open(sys.argv[1]))
for e in exprs:
    print '>>> %s' % e
    cmd = code.compile_command(e)
    while cmd is None:
        n = exprs.next()
        e += "\n" + n
        print '... %s' % n
        cmd = code.compile_command(e)
    r = eval(cmd)
    if r:
        print repr(r)

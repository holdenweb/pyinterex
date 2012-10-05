This directory supports the first Pluralsight "Introduction to Python" class
with Python scripts that, when pasted into an interactive session, will
produce outputs suitable for running in playerpiano (the .pp files).

These latter are used to present the interactive sessions. Since a facility
with the keyboard is now no longer required, you should really have a copy
of the .pp file in printed form to ensure that only appropriate amounts of
"typing" are done. It sounds odd if the keyboard clatters after the end
of a line.

Also, ideally there will be a way to hide the fact that playerpiano is in use,
which I my be able to do with some fancy menu or script trickery. Alternatively
just be barefaced about the fact that playerpiano is in use, and make a feature
of it.

The makefile is an attempt to automate the production of the playerpiano
scripts and retain some sanity. The scripts end up in the ppfiles directory.
They are named LNN-NNN.pp, where NN is the lesson number and NNN is an
arbitrary number to induce an ordering in the files.

There are also a number of test*.py files, all of which should ultimately
verify the features of the program are still functional.

Steve Holden                                              October 4, 2012

Occasionally it would be nice if a script could read standard input
using raw_input() or input(). Even nicer would be if the substituted functions
could be 'lazy,' so there was no need to provide input files for those tests
where input was not required.

First approach: raw_input() is an object created with the knowledge of the
module name it is testing. It only opens the data file (whose name relates
directly to that of the module) when its __call__ method is activated.

The approach initially implemented brought out the interesting fact that
the namespace needs to be maintained across all statements in the file.
Considering that I hadn't considered the role of the global namespace at
all in the early versions I am impressed how much of my code actually
ran at all

Steve Holden                                (still, just) October 4, 2012
Shit, I don't have any unit tests. What should I do about that?


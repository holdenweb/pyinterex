This directory supports the first Pluralsight "Intrduction to Python" class
with Python scripts that, when pasted into an interactive session, will
produce outputs suitable for running in playerpiano (the .pp files).

These latter are used to present the interactive sessions. Since a facility
with the keyboard is now no longer required, you should really have a copy
of the .pp file in printed form to ensure that only appropriate amounts of
"typing" are done. It sounds silly if the keyboard clatters after the end
of a line.

Also, ideally there will be a way to hide the fact that playerpiano is in use,
which I my be able to do with some fancy menu or script trickery. Alternatively
just be barefaced about the fact that playerpiano is in use, and make a feature
of it.

The makefile is an attempt to automate the production of the playerpiano
scripts and retain some sanity. The scripts end up in the ppfiles directory.
They are named LNN-NNN.pp, where NN is the lesson number and NNN is an
arbitrary number to induce an ordering in the files.

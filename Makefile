# Makefile for the Data Structures repository.
#
# Author: Alexander Roth
# Date:   2014-11-27

PYTHON = Python/*.*~ Python/*.pyc

.PHONY: clean
clean:
	rm -rf *~ $(PYTHON)

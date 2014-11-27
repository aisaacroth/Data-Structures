# Makefile for the Data Structures repository.
#
# Author: Alexander Roth
# Date:   2014-11-27

.PHONY: clean
clean:
	rm -rf *~ 
	(cd Python/; make clean)

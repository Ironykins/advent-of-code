#
# makefile
# konrad, 2015-12-09 13:01
#
# Shouldn't need to use this much.

all:
	gcc -lbsd -o day4b day4b.c

clean:
	rm -f day4b

# vim:ft=make
#

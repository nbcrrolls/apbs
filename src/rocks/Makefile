# @Copyright@
# @Copyright@
#
# $Log: Makefile,v $
# Revision 1.1  2012/07/11 02:12:53  nadya
# initial revision. Based on roll from Robert Konecny
#
#

REDHAT.ROOT = $(CURDIR)/../../

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

build:

install::
	mkdir -p $(ROOT)/etc/profile.d
	install -m755  apbs.* $(ROOT)/etc/profile.d

clean::
	rm -f $(NAME).spec.in


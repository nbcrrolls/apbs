#
# $Id: Makefile,v 1.1 2012/07/11 02:12:48 nadya Exp $
#
# @Copyright@
# @Copyright@
#
# $Log: Makefile,v $
# Revision 1.1  2012/07/11 02:12:48  nadya
# initial revision. Based on roll from Robert Konecny
#
#

REDHAT.ROOT	= $(PWD)/../../
MAKE.iscontrib	= 1
-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

rpm:: build
	-cp *.$(ARCH).rpm $(REDHAT.RPMS)/$(ARCH)/

build:
	mkdir -p $(REDHAT.RPMS)/$(ARCH)/


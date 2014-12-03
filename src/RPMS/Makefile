# --------------------------------------------------- -*- Makefile -*- --
#
# @Copyright@
# @Copyright@
#
#

PKGROOT 	= 
REDHAT.ROOT	= $(PWD)/../../
#ROCKSROOT	= ../../../../..
ROLLSROOT	= /opt/rocks/share/devel/src/roll
MAKE.iscontrib	= 1
-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

rpm::
	cp *.$(ARCH).rpm ../../RPMS/$(ARCH)/
#	cp *.$(ARCH).rpm $(REDHAT.RPMS)/$(ARCH)/

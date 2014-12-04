# --------------------------------------------------- -*- Makefile -*- --
#
# @Copyright@
# @Copyright@
#
#

PKGROOT 	= 
REDHAT.ROOT	= $(PWD)/../../
MAKE.iscontrib	= 1
-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk
VERSION		= 1.3
BROOT = $(PWD)/rpmbuild

rpm::
	mkdir -p $(BROOT)
	mkdir -p $(BROOT)/BUILD
	mkdir -p $(BROOT)/RPMS
	mkdir -p $(BROOT)/SOURCES
	mkdir -p $(BROOT)/SPECS
	mkdir -p $(BROOT)/SRPMS
	sed -e 's/ZZZVERSIONZZZ/$(VERSION)/' -e 's:ZZZBUILDROOTZZZ:$(BROOT):'\
		 apbs-rocks.spec > $(BROOT)/SPECS/apbs-rocks.spec
	cp apbs-$(VERSION)-source.tar.gz $(BROOT)/SOURCES/
	rpmbuild -ba $(BROOT)/SPECS/apbs-rocks.spec
	cp $(BROOT)/RPMS/x86_64/apbs-rocks-*.rpm ../../RPMS/$(ARCH)/

clean::
	rm -rf $(BROOT)


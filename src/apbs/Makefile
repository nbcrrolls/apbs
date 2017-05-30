#
# $Id: Makefile,v 1.3 2012/07/14 01:42:53 nadya Exp $
#
# @Copyright@
# @Copyright@
#
# $Log: Makefile,v $
# Revision 1.3  2012/07/14 01:42:53  nadya
# add wrapper script
#
# Revision 1.2  2012/07/13 19:35:56  nadya
# use common place for version
#
# Revision 1.1  2012/01/28 00:57:52  nadya
# initial
#
#

REDHAT.ROOT     = $(CURDIR)/../../
-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk


APBSBUILDOPT=-DCMAKE_BUILD_TYPE=RelWithDebInfo -DBUILD_DOC=OFF -DBUILD_SHARED_LIBS=ON -DENABLE_PYTHON=ON -DENABLE_MPI=ON
BUILDDIR=build


version.mk:
	cat ../../apbs.mk version.mk.in > version.mk

build:
	tar xzf $(NAME)-$(VERSION).$(TARBALL_POSTFIX)  --strip-components=1
	mkdir -p $(BUILDDIR)
	(									\
		module load opt-python; 					\
		cd $(BUILDDIR); 						\
		cmake -DCMAKE_INSTALL_PREFIX=$(PKGROOT) $(APBSBUILDOPT) ../apbs ;\
		echo make -j2;							\
	)

oldbuild:
	mkdir -p build
	gunzip -c $(NAME)-$(VERSION).tar.gz | $(TAR) -xf -
	(									\
		cd build;							\
		cmake -DCMAKE_INSTALL_PREFIX=$(PKGROOT) ../$(NAME)-$(VERSION);	\
		make -j2;							\
	)
	
install::
	mkdir -p $(ROOT)/$(PKGROOT)
	(					\
		cd $(BUILDDIR); 		\
		make DESTDIR=$(ROOT) install;	\
	)
	(cd $(ROOT)/opt; ln -s apbs-$(VERSION) apbs)

clean::
	rm -rf $(NAME)
	rm -rf $(BUILDDIR)
	rm -rf version.mk

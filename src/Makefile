# $Id: Makefile,v 1.1 2012/07/11 02:12:47 nadya Exp $
#
# @Copyright@
# @Copyright@
#
# $Log: Makefile,v $
# Revision 1.1  2012/07/11 02:12:47  nadya
# initial revision. Based on roll from Robert Konecny
#
#

-include $(shell $(ROCKSROOT)/bin/arch).mk
-include $(shell $(ROCKSROOT)/bin/os).mk

default:        pkg

copyright pkg rpm clean::
	for i in $(SRCDIRS) ; do \
		cd $$i; \
		$(MAKE) $@ || exit 2 ; \
		cd ..; \
	done


# 
# $Id: Makefile,v 1.1 2012/07/11 02:12:53 nadya Exp $
#
# @Copyright@
# @Copyright@
#
# $Log: Makefile,v $
# Revision 1.1  2012/07/11 02:12:53  nadya
# initial revision. Based on roll from Robert Konecny
#
#

PKGROOT		= /var/www/html/roll-documentation/apbs/$(VERSION)

REDHAT.ROOT	= $(PWD)/../../
-include $(ROCKSROOT)/etc/Rules.mk
-include Rules.mk

SEDSPEC += \
	-e 's%@VERSION_NAME@%$(VERSION_NAME)%g' \
	-e 's%@VERSION@%$(VERSION)%g' \
	-e 's%@PUBDATE@%$(PUBDATE)%g' \
	-e 's%@APBS.VERSION@%$(APBS.VERSION)%g' \
	-e 's%@PDB2PQR.VERSION@%$(PDB2PQR.VERSION)%g'

default: $(NAME).spec 


html: index.sgml requirements.sgml predoc
	jw --backend html --dsl $(PWD)/rocks.dsl#html index.sgml

pdf: index.sgml requirements.sgml predoc
	jw --backend pdf --dsl $(PWD)/rocks.dsl#print index.sgml

index.sgml: index.sgml.in
	$(SED) $(SEDSPEC) $^ > $@

requirements.sgml: requirements.sgml.in
	$(SED) $(SEDSPEC) $^ > $@

build: html pdf

install:: build
	mkdir -p $(ROOT)/$(PKGROOT)/images
	mkdir -p $(ROOT)/$(PKGROOT)/stylesheet-images
	install -ma+r index.pdf 	$(ROOT)/$(PKGROOT)/$(NAME).pdf
	install -ma+r *.html    	$(ROOT)/$(PKGROOT)/
	install -ma+r images/*.png	$(ROOT)/$(PKGROOT)/images/
	install -ma+r stylesheet-images/{*.gif,*.png} \
		$(ROOT)/$(PKGROOT)/stylesheet-images/
	install -ma+r rocks.css $(ROOT)/$(PKGROOT)/

clean::
	rm -f *.html
	rm -f index.pdf
	rm -f index.sgml requirements.sgml 

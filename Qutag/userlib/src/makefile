############################################################
#
#  Project:        quTAG User Library
#
#  Filename:       Makefile
#
#  Purpose:        GCC makefile for examples
#
#  Author:         N-Hands GmbH & Co KG
#
############################################################
# $Id: makefile.lx,v 1.1 2017/12/14 12:50:37 trurl Exp $

LIBDIR=../lib
INCDIR=../inc

TARGET=example0 example5

all : $(TARGET)

define outputrule
$(1): $(1:%=%.c)
	gcc -o $$@ -g -Wall -O0 -I$(INCDIR) -L$(LIBDIR) $$< -ltdcbase
endef
$(foreach src,$(TARGET),$(eval $(call outputrule,$(src))))

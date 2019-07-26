############################################################
#
#  Project:        TDC User Library
#
#  Filename:       Makefile
#
#  Purpose:        GCC makefile for tdcbase CLI
#
#  Author:         N-Hands GmbH & Co KG
#
############################################################
# $Id: makefile.lx,v 1.2 2015/10/28 18:51:34 trurl Exp $

LIBDIR=../lib
INCDIR=../inc

tdccli : tdccli.c makefile
	cl -nologo -W3 -Zi -MD -wd4996 -I$(INCDIR) $(LIBDIR)\tdcbase.lib tdccli.c
	gcc -o tdccli -g -Wall -O0 -I$(INCDIR) -L$(LIBDIR) tdccli.c -ltdcbase

clean:
	rm tdccli *.o

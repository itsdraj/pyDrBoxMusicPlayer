#!/usr/bin/env python

# TODO: import selectively
from libdropboxaccess import *

dropbox_client = getDropboxClient( getDropboxSession() )

account_info = dropbox_client.account_info()
for keys in account_info:
	print '%s : %s' % ( keys, account_info[keys] )


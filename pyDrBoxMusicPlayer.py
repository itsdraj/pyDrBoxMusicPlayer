#!/usr/bin/env python

# TODO: import selectively
from libdropboxaccess import *

kwargs = {
    'APP_KEY': '',
    'APP_SECRET':  '',
    # change to 'dropbox' if you're not using limited access
    'ACCESS_TYPE': '',
}

dropbox_accessor = DropboxAccessor( **kwargs )
dropbox_client = dropbox_accessor.getDropboxClient()

account_info = dropbox_client.account_info()
for keys in account_info:
	print '%s : %s' % ( keys, account_info[keys] )


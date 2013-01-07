#!/usr/bin/env python

from dropbox import client, rest, session

APP_KEY = ''
APP_SECRET = ''
# change to 'dropbox' if you're not using limited access
ACCESS_TYPE = ''
TOKEN_FILE = ''

# Code taken from Dropbox website tutorial
def requestDropboxSessionToken():
	dropbox_session = session.DropboxSession( APP_KEY, APP_SECRET, ACCESS_TYPE )
	request_token = dropbox_session.obtain_request_token()
	dropbox_session_url = dropbox_session.build_authorize_url( request_token )

	print "url:", dropbox_session_url
	print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
	raw_input()

	access_token = dropbox_session.obtain_access_token()

	# TODO: Handle case where invalid data is read
	with open( TOKEN_FILE, 'w' ) as token_file:
		token_file.write( '%s\n%s' % ( access_token.key, access_token.secret ) )
		print "Token file '%s' written successfully" % TOKEN_FILE
	
	return ( access_token.key, access_token.secret, )

def getDropboxSessionToken():
	""" Check if token exists in a file. If not, request a new one """
	token = None
	try:
		with open( TOKEN_FILE, 'r' ) as token_file:
			token_key = token_file.readline().strip()
			token_secret = token_file.readline().strip()
			token = ( token_key, token_secret, )

	except IOError as e:
		token = requestDropboxSessionToken()
	
	return token

def getDropboxSession():
	token_key, token_secret = getDropboxSessionToken()
	dropbox_session = session.DropboxSession( APP_KEY, APP_SECRET, ACCESS_TYPE )
	dropbox_session.set_token( token_key, token_secret )

	return dropbox_session

def getDropboxClient( dropbox_session ):
	dropbox_client = client.DropboxClient( dropbox_session )

	return dropbox_client


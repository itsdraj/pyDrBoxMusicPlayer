#!/usr/bin/env python

from dropbox import client, rest, session

TOKEN_FILE = 'token.txt'

# Code taken from Dropbox website tutorial
class DropboxAccessor:
    """ Pass in APP_KEY, APP_SECRET, ACCESS_TYPE when instantiating """

    def __init__(self, **kwargs ):
		self._APP_KEY = kwargs['APP_KEY']
		self._APP_SECRET = kwargs['APP_SECRET']
		self._ACCESS_TYPE = kwargs['ACCESS_TYPE']
		
    def requestDropboxSessionToken(self):
    	dropbox_session = session.DropboxSession( self.APP_KEY, self.APP_SECRET, self.ACCESS_TYPE )
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
    
    def getDropboxSessionToken(self):
    	""" Check if token exists in a file. If not, request a new one """
    	token = None
    	try:
    		with open( TOKEN_FILE, 'r' ) as token_file:
    			token_key = token_file.readline().strip()
    			token_secret = token_file.readline().strip()
    			token = ( token_key, token_secret, )
    
    	except IOError as e:
    		token = self.requestDropboxSessionToken()
    	
    	return token

    def getDropboxSession(self):
    	token_key, token_secret = self.getDropboxSessionToken()
    	dropbox_session = session.DropboxSession( self._APP_KEY, self._APP_SECRET, self._ACCESS_TYPE )
    	dropbox_session.set_token( token_key, token_secret )
    
    	return dropbox_session

    def getDropboxClient(self):
        dropbox_session = self.getDropboxSession()
    	dropbox_client = client.DropboxClient( dropbox_session )
    
    	return dropbox_client


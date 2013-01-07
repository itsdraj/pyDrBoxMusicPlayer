from dropbox import client, rest, session

APP_KEY = ''
APP_SECRET = ''
# change to 'dropbox' if you're not using limited access
ACCESS_TYPE = 'app_folder'

# Code taken from Dropbox website tutorial
def getDropboxAccessToken():
	dropbox_session = session.DropboxSession( APP_KEY, APP_SECRET, ACCESS_TYPE )
	request_token = dropbox_session.obtain_request_token()

	dropbox_session_url = dropbox_session.build_authorize_url( request_token )

	print "url:", dropbox_session_url
	print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
	raw_input()

	try:
		access_token = dropbox_session.obtain_access_token( request_token )
	except Exception as e:
		print 'Error while obtaining token. Did you authenticate the app?. \nERROR: %\n' % e.strerror

def getDropboxClientFromAccessToken():
	dropbox_client = client.DropboxClient( dropbox_session )
	account_info = dropbox_client.account_info()
	for keys in account_info:
		print '%s : %s' % ( keys, account_info[keys] )

getDropboxClientFromAccessToken()

#!/usr/bin/env python
import webbrowser
import os
from Tkinter import *
import dropbox
import pygtk
pygtk.require('2.0')
import gtk



def generate_token(app_key, app_secret):
    '''Generate access token for Dropbox Core API.

    Get your app key and secret from the Dropbox developer website
    '''

    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(
        app_key,
        app_secret
    )

    # Have the user sign in and authorize this token
    authorize_url = flow.start()
    print '1. Go to: ' + authorize_url
    print '2. Click "Allow" (you might have to log in first)'
    print '3. Copy the authorization code.'

    webbrowser.open_new(authorize_url)


    clipboard = gtk.clipboard_get()
    code = clipboard.wait_for_text()
    print(code)
   
    access_token, user_id = flow.finish(code)

    print ''
    print 'Generated access token'
    print '----------------------'
    print access_token
    print '----------------------'

    return access_token


app_key = 'lcuez9lfnuddevz'
app_secret = 'i17rzjkms3cyinl'



access_token = generate_token(app_key, app_secret)
client = dropbox.client.DropboxClient(access_token)
print ''
print 'Linked account:', client.account_info().get('display_name')
print ''

text_file = open("/home/shishir/Output_copy.txt", "w")
dat=os.popen('xsel').read()
text_file.write(dat + '\n')
print(dat)
response=client.put_file('Input_paste.txt',dat)
text_file.close()
print 'Uploaded :',response

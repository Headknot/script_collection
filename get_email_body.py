# -*- coding: utf-8 -*-

'''
Created: 2018-05-13
@author: Alexander Jacobsson
'''

from imaplib import IMAP4_SSL
import email
import getpass

imap_url = 'outlook.office365.com'
username = 'foo.bar@xyz.com'
password = getpass.getpass()

def get_email_body(key, value):
	""" 
	Uses IMAP to search through your inbox for emails matching your specific criteria.
	After finding your matches it will return all matching emails body fields in a list.
	Possible IMAP search keys can be found here: https://tools.ietf.org/html/rfc3501#section-6.4.4
	"""
	with IMAP4_SSL(imap_url) as session:
		session.login(username,password)
		session.select('INBOX')
		_, messages = session.uid('search', key, value)
		messages = messages[0].split()
		body_container = []
		
		for message in messages:
			message = session.uid('fetch', message, "(RFC822)")
			msg = email.message_from_bytes(message[1][0][1])
			
			if msg.is_multipart():
				for part in msg.walk():
					if part.get_content_type() == "text/plain":
						body = part.get_payload(decode=True)
						body = body.decode('latin-1')	
			else:
				body = part.get_payload(decode=True)
				body = body.decode('latin-1')
				
			body_container.append(body)
		
		return body_container
			
if __name__ == '__main__':
	body = get_email_body('FROM', 'foo.bar@xyz.com')
	print(body)
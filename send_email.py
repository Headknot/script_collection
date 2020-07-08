# -*- coding: utf-8 -*-

'''
Created: 2018-04-15
@author: Alexander Jacobsson
'''

from smtplib import SMTP 
from email.message import EmailMessage

def send_email(Subject, From, To, Body):
    """Send an email using my own predefined settings.
    The arguments are:
      - Subject
      - From
      - To
      - Body
    """
    
    # Create the EmailMessage object and insert variables into the objects respective key-value pairs.
    msg = EmailMessage()
    msg['Content-Type'] = 'text/plain; charset="utf-8"'
    msg['Content-Transfer-Encoding'] = '7bit'
    msg['MIME-Version'] = '1.0'
    msg['Subject'] = Subject 
    msg['From'] = From 
    msg['To'] = To 
    msg.set_content(Body)

    # Using 'with' as a context manager, login and send email using TLS encryption.
    with SMTP('my.smtp.server', port=587) as s:
        s.starttls()
        s.login('username', 'password')
        s.send_message(msg)
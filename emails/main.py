# import smtplib
#
# smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
# smtp_obj.ehlo()
# smtp_obj.starttls()
#
# import getpass
# email = 'jainayushjain95@gmail.com'
# password = getpass.getpass('Password:')
#
# smtp_obj.login(email, password)
#
# from_address = email
# to_address = email
# subject = 'Mail Test - Ayush1 - qwertyuioplkjhgfdsazxcvbnm'
# message = 'Message of Mail - Ayush2'
#
# text = f"Subject: {subject}\n{message}"
#
# smtp_obj.sendmail(from_address, to_address, text)

import imaplib
instance = imaplib.IMAP4_SSL('imap.gmail.com')
email = 'jainayushjain95@gmail.com'
password = 'aejy hgzv stfv mesw'

print(instance.login(email, password))

print(instance.select('inbox'))

typ, data = instance.search(None, 'FROM jainayushjain95@gmail.com')

print(typ)
print(data)

print(instance.logout())
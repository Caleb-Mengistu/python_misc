import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Caleb Mengistu'
email['to'] = 'ammramengistu52@gmail.com' #email to be sent to
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name':'Amrra'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port= 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('calebm1114@gmail.com','kaavuczulhtbsymr')
	smtp.send_message(email)
	print('Email sent!')
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Sai Kasam'
email['to'] = 'spk20487@gmail.com'
email['subject'] = 'you just won a million dollars'
email.set_content(html.substitute({'name': 'tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    myEmail = #enter email here
    myPassword = #enter password here
    smtp.login(myEmail, myPassword)
    smtp.send_message(email)



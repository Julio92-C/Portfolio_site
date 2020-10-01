import smtplib

from email.mime.text import MIMEText


def send_email(username, email, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'a8cfa54676ad2b'
    password = 'c1accdb36d2f24'
    message = f"<h3>Comment from user:</h3><ul><li>Username: {username}</li><li>Email: {email}</li></li><li>Comments: {comments}</li></ul>"

    sender_email = '54b9dd2f7f-1e78bd@inbox.mailtrap.io'
    receiver_email = '54b9dd2f7f-1e78bd@inbox.mailtrap.io'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'New comment'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

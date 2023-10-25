import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

class notification:
    def __init__(self):
        self.smtp_server = 'smtp.gmail.com'
        self.port = 465
        self.email = 'sriramsridhar27@gmail.com'
        
    
    def emailnotif(self,receiver,subject,body):
        msg = MIMEText(body)
        msg['Subject']=subject
        msg['From']=self.email
        msg['To']=receiver

        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.port) as smtp_server:
                smtp_server.login(self.email, self.password)
                smtp_server.sendmail(self.email, receiver, msg.as_string())
            # print('Email sent successfully!')
            return True
        except:
            # Log error
            return False

    def mobilenotif(self, receiver, content):
        client = Client(self.account_sid, self.auth_token)
        
        message = client.messages.create(
          from_='+17088132890',
          body=content,
          to=receiver
        )
        # print(message.sid)
        return True

         
         
# nt = notification()
# nt.mobilenotif('+12269612724','Test SMS from backend')
# nt.emailnotif("sriramsridhar26@gmail.com","status","test")
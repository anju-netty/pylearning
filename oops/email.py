class Email:
#Change the state of the email
    def __init__(self):
        self.is_email_sent = False
        

    def email_sent(self):
        self.is_email_sent = True
        return(self.is_email_sent)

myemail = Email()
print(myemail.email_sent())
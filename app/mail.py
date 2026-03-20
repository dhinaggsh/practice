import yagmail

def send_mail(file):
    try:
        yag = yagmail.SMTP(
            user="dhinag96@gmail.com",
            password="uhva eeoi lpcg fdpq"
        )
        
        picture = "Testing.png"
        
        yag.send(
            to="dhinag3110@gmail.com",
            subject="code checking",
            attachments=[file, picture]
        )
        return ({"Message":"Mail sent Success"})
    
    except Exception as e:
        return ({"error":True, "Error Message":str(e)})

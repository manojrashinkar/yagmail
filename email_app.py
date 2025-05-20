import yagmail
subject = "email from python script"
content = "Hi , where are you ?" 
ya = yagmail.SMTP(user = "abc@gmail.com", password="x")
ya.send(to = "xyz@gmail.com",subject=subject,contents=content)

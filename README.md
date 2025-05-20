# 📧 Python Email Sender with yagmail

This simple Python script sends an email using the `yagmail` library.

## Requirements

- Python 3.x
- yagmail (`pip install yagmail`)

## Usage

Update the script with your credentials and run:

```python
import yagmail

subject = "email from python script"
content = "Hi , where are you ?" 

ya = yagmail.SMTP(user="your_email@gmail.com", password="your_app_password")
ya.send(to="recipient_email@gmail.com", subject=subject, contents=content)

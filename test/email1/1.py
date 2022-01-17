import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# 内容
body = MIMEText("正文")
with open('附件.png', 'rb') as fp:
    img = MIMEImage(fp.read())
# 邮件
msg = MIMEMultipart()
msg['Subject'] = '标题'
msg['From'] = "lvlm@fxqifu.com"
msg['To'] = "lvlm@fxqifu.com"
msg.attach(body)
msg.attach(img)
# 登录
s = smtplib.SMTP('smtp.mxhichina.com')
s.login("lvlm@fxqifu.com", "77e5f61a")
# 发送
s.send_message(msg)
s.quit()

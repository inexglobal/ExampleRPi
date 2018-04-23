import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
HostSMTP='smtp.gmail.com'
Port=587
you_email='you_email@gmail.com'
to_email=['example@inex.co.th','example@outlook.com']#ส่งมากว่า 1 อีเมล์
user=you_email
password='you_password_email'
server = smtplib.SMTP(HostSMTP,Port) 
server.starttls() 
server.login(user,password)

msg = MIMEMultipart()
msg['From'] = you_email
msg['To'] = '<'+'>,<'.join(to_email)+'>'
msg['Subject'] = 'การส่งอีเมล์ด้วย python'

# เนื้อหาของอีเมล
body = "ทดสอบส่ง email"
msg.attach(MIMEText(body,'plain')) # ส่งแบบ plain

# แนบไฟล์อื่น ๆส่งไปพร้อมกัน
filename = "BH1750.txt"
file = MIMEBase('application', "octet-stream")
file.set_payload(open(filename, 'rb').read())
encoders.encode_base64(file)
file.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(filename))
msg.attach(file)

server.sendmail(you_email,to_email, msg.as_string()) # ส่งอีเมล์พร้อมรายละเอียดที่กำหนด
server.quit() # ปิดการเชื่อมต่อ
print ("Successfully sent email")

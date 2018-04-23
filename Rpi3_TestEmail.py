import smtplib
HostSMTP='smtp.gmail.com'
Port=587
you_email='you_email@gmail.com'
to_email=['example@inex.co.th','example@outlook.com']#ส่งมากว่า 1 อีเมล์
user=you_email
password='you_password_email'
server = smtplib.SMTP(HostSMTP,Port) # คำสั่งสร้างวัตถุ SMTP จากการเชื่อมต่อ
server.starttls() #เป็นคำสั่งสำหรับเชื่อมต่อ SMTP เข้ารหัสโหมด TLS(Transport Layer Security)
server.login(user,password)#ล็อกอินเข้าสู่ระบบอีเมล์
text = 'Test by Python'
server.sendmail(you_email,to_email,text)#ส่งอีเมล
server.quit() #ปิดการเชื่อมต่อ
print("Successfully sent email") 

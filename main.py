
import smtplib

sender = "example123@gmai.com"
receiver = "example123@gmai.com"
msg = "Hello, have a nice day"


     #create connection
connection = smtplib.SMTP("smtp.gmail.com", 587)

     #start TLS
connection.starttls()
print("Connection made successfully")


     #login with app password
connection.login(user=sender,password="example123")
print("Logged in successfully") 

connection.sendmail(from_addr=sender,to_addrs=receiver,msg=msg)
print("sent email  successfully")

connection.close()
print("Closed connection in successfully")

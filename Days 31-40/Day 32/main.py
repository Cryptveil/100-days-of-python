import smtplib

my_email = "[email here]"
password = "[password here]"

connection = smtplib.SMTP("[SMTP server]", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email,
                    to_addrs="", msg="")
connection.close()

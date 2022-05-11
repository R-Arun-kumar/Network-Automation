#NAPALM (Network Automation and Programmability Abstraction Layer with Multivendor support) is a Python library that implements a set of functions to interact with different router vendor devices using a unified API.
from napalm import get_network_driver

# following libraries are used to send an email from automation container to gmail server.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#JSON allows data to be formatted to user readable string
import json

#gets network details
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'cisco', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_mac_address_table()
maildata = json.dumps(ios_output, sort_keys=True, indent=4)
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = iosvl2.get_arp_table()
print (json.dumps(ios_output, sort_keys=True, indent=4))

# create message object instance
msg = MIMEMultipart()

message = "This is your Switch's Mac address table. \n " + str(maildata)

# setup the parameters of the message
password = "password"
msg['From'] = "from@gmail.com"
msg['To'] = "to@gmail.com"
msg['Subject'] = "Mail Subject here"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

# create server
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

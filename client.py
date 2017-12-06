import radius
import json

outfile = "login.json"
hostname = ""
port = 1812
secret = ""
username = ""
password = ""
data = dict()

try:
    data = json.load(open('client.json'))
except FileNotFoundError:
    pass

if "hostname" in data: hostname = data["hostname"]
if "port" in data: port = data["port"]
if "username" in data: username = data["username"]

s = input("Enter hostname name ("+hostname+") : ")
if s != "":
    hostname = s.strip()
s = input("Enter port number ("+str(port)+") : ")
if s != "":
    port = int(s)
s = input("Enter username (" + username + ") : ")
if s != "":
    username = s.strip()
s = input("Enter radius secret (" + secret + ") : ")
if s != "":
    secret = s.strip()
s = input("Enter radius secret (" + password + ") : ")
if s != "":
    password = s.strip()

d = dict(hostname=hostname, port=port, username=username)
with open('client.json', 'w') as outfile:
    json.dump(d, outfile)

r = radius.Radius(secret, host=hostname, port=port)
print('success' if r.authenticate(username, password) else 'failure')
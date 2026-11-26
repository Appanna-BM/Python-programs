username=["John","Karen","Mister"]
password=["password","mypassword","guest"]
users=dict(zip(username, password))
for key,value in users.items():
    print({key,value}) 
# from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client['SalesNotification']
import smtplib
import os
import pymongo
arrayOfUser=[]
arrayOfSale =[]
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["SalesNotification"]

#user array
usercol = mydb["User"]
x = usercol.find({},{"_id":0, "user":1,"email":1})
for i in x:
    arrayOfUser.append(i['email'])
print(arrayOfUser)

# sales array

salescol = mydb["Sales"]
y = salescol.find({},{'_id':0,'title':1,'startDate':1}).sort('startDate',-1).limit(2)
for i in y:
    arrayOfSale.append(i)

print(arrayOfSale)
password = os.getenv('password')
for i in arrayOfUser:
    for sales in arrayOfSale:

        with smtplib.SMTP('smtp.sgp1013.siteground.asia/roundcube',465) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login("webhypeoffcial@webhype.site",password)
            subject = "Sales Again (Get off now)"
            body=sales['title'] + "Sale is starting from "+ sales['startDate']
            msg = f'Subject : {subject}\n\n{body}'
            smtp.sendmail('webhypeoffcial@webhype.site', i,msg)

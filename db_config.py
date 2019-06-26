from pymongo import MongoClient

# myclient=MongoClient('mongodb+srv://illmf:azsxdc12#@cluster0-oobsq.mongodb.net/test') 
myclient=MongoClient('mongodb://localhost:27017/')
print("Opened database successfully")
print("Opened database successfully")

mydb=myclient['HC']
# mycol=mydb['student']                                                                             
doctor=mydb['Doctor']
patient=mydb["Patient"]
# mycol1=mydb['Patient']
print("DB created successfully")
# conn.close()
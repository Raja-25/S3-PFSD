from pymongo import MongoClient

#create an instance (DB connectivity)
client=MongoClient('mongodb://127.0.0.1:27017')

#create database
db=client['s3']

#create collection
studentdata=db.students

#create Document
student1={"regd":"111","name":"raja"}
student2=[{"regd":"222","name":"abc"},
         {"regd":"333","name":"raja"},
         {"regd":"444","name":"def"}]

#inserting documents
studentdata.insert_one(student1)
studentdata.insert_many(student2)
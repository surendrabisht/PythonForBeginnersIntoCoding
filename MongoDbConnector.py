from pymongo import MongoClient,ReadPreference
import bson
import datetime


class MongoDbConnector:

    def __init__(self,ConnectionUrl:str,dbName:str):
        self.client=MongoClient(ConnectionUrl)
        self.db=self.client[dbName]
    
    def listTables(self):
        return self.db.list_collection_names()
    
    def GetDatabases(self):
        self.client.list_database_names()
    
    def DeleteItem(self,tableName:str,filterParameters:dict):
        table=self.db[tableName]
        table.delete_one(filterParameters)
    
    def insertIntoTable(self,tableName:str,collection:dict):
        table=self.db[tableName]
        table.insert_one(collection)
    
    def UpdateSingleRecordInTable(self,tableName:str,idInString:str,collection:dict):
        id=bson.ObjectId(idInString)
        table=self.db[tableName]
        table.update_one({"_id":id},collection)      
    
    def GetSingleRecord(self,tableName:str,idInString:str):
        id=bson.ObjectId(idInString)
        table=self.db[tableName]
        return table.find_one(id)
    
    def GetAllRecords(self,tableName:str,filterParameters:dict={}):
        table=self.db[tableName]
        return table.find(filterParameters)    

    #utility method
    @staticmethod
    def GetBsonObjectID(id:str):
        return bson.ObjectId(id)


if __name__ == '__main__':
    print("start")
    mongoDb=MongoDbConnector("mongodb+srv://sa:admin@cluster0.c2wxg.mongodb.net/vikalp?retryWrites=true&w=majority","sample_airbnb")
    mongoDb.DeleteItem("listingsAndReviews",{"_id":"10006546"}) #{"_id":"10006546"})
    
    #1. print all tables
    print(mongoDb.listTables())

    # # #2. insert statement
    # # post = {"author": "Surendra","text": "first connection to mongo","tags": ["vikalp", "python", "pymongo"],"date": datetime.datetime.utcnow()}
    # # mongoDb.insertIntoTable("posts",post)

    # # #3. update query
    # # updateQuery={"$set": { "text": "Canyon " ,"asd":"qwert" } }   
    # # mongoDb.UpdateSingleRecordInTable("posts","60155f2e1ac3e4539146e969",updateQuery)
    
    # # #4. using Id
    # # print(mongoDb.GetSingleRecord("posts","6015679cc989c35e8e0ffd96"))

    # #5. using filters
    # for post in mongoDb.GetAllRecords("posts",{'author': 'Mike'}):
    #     print(post)

    print("Done")




# client = pymongo.MongoClient("mongodb+srv://sa:<password>@cluster0.c2wxg.mongodb.net/<dbname>?retryWrites=true&w=majority")
# db = client.test








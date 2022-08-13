from pymongo import MongoClient
from bson.objectid import ObjectId
from json import dumps
from bson import json_util

class AnimalShelter(object):
    def __init__(self, username=None, password=None):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:48341/?authSource=AAC&authMechanism=SCRAM-SHA-256' % (username, password))
        self.database = self.client['AAC']
        
        
     #This is the CREATE method of CRUD
    def create(self, animal_data):
        if animal_data is not None:
            insert = self.database.animals.insert(animal_data)   #data should be a dictionary
            if insert != 0:
                print("Completed")
                return True
            else:
                print("Nothing to CREATE")
                return False
        else:
            raise Exception("Nothing to save, because parameter is empty")
            
    #This is the READ method of CRUD
    def read(self, look):
        #Below will seatch the database looking for data
        if look:
            data = self.database.animals.find(look, {"_id":False})
        else:
            #This will search all possible records if nothing is searched
            data = self.database.animals.find({}, {"_id":False})
        return data
    
    #This is the update function
    def update(self, record, newRecord):
        #First, we will verify the selection being updated exists
        if record is not None:
            update_result = self.database.animals.update(record, {"$set":newRecord})
            results = "Documents updated " + dumps(update_result)
            print(results)
            return results
        else:
            raise Exception("Records not found")
            
    def delete(self, excise):
        if excise is not None:
            delete_result = self.database.animals.delete_one(excise)
            result = "Documents Deleted: " + dumps(excise)
            return result
        else:
            raise Exception("No record provided.")
                           
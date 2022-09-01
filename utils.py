from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):

 client = pymongo.MongoClient('mongodb+srv://regiapriandi012:Sinheul24.@instance2.jrd6j.mongodb.net/?retryWrites=true&w=majority')
 db_handle = client['registrationdatabase']
 return db_handle, client
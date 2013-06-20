import sys
import pymongo
import MySQLdb 
import uuid

def main(args):
    
    #MongoDB Connection
    mongodb_uri = 'mongodb://localhost:27017'
    db_name = 'keyvalue'
    connection = pymongo.Connection(mongodb_uri)
    database = connection[db_name]
    
    
    #MySQL Connection
    con = MySQLdb.connect('localhost','root','','dbMongo');
    cursor = con.cursor()
    
    
    #create a mongo collection
    database.collection.insert({'Name':'Bart',
                                'Age':25,
                                'Salary': {'num1':100,
                                            'num2':200,
                                            'num3':300,}})
    
    #look for the collection
    content = database.collection.find({})
    
   
    #traverse through the collection and get values
    for info in content:
        Average = (info['Salary']['num1'] + info['Salary']['num2'] + info['Salary']['num3'])/3
        sql = """INSERT INTO userInfo(id,name,age,average) VALUES ("%s","%s","%s","%s")""" %(uuid.uuid1(),info['Name'],info['Age'],Average)
    try:
        cursor.execute(sql)
        con.commit()
        
    except:
        con.rollback()
    
    finally:
        con.close()
        database.drop_collection('collection')
        
if __name__ == '__main__': 
    main(sys.argv[1:])
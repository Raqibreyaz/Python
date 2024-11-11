from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost',27017)
# database = client.get_database("ytmanager")
# video_collection= database.get_collection("videos")
database  = client['ytmanager']
video_collection  = database['videos']

def show_options():
	print("\n#### Youtube Manager with MongoDb ####")
	print("1. List all Videos")
	print("2. Add a Video")
	print("3. Update a Video")
	print("4. Delete a Video")
	print("5. Exit")
    
def input_data():
    name = input("\nEnter Video Name: ")
    duration = input("Enter Video Duration: ")
    
    return name,duration

def catchDatabaseError(Controller):
  def wrapper(*args,**kwargs):
    try:
       Controller(*args,**kwargs)
    except Exception as e:
        print("Error: ",e)
  return wrapper

@catchDatabaseError
def list_all_videos():
   all_videos = video_collection.find() or []
   print("\n","*"*50)
   for video in all_videos:
       print(*video.values())
   print("\n","*"*50)

@catchDatabaseError
def add_a_video():
    name,duration = input_data()
    video_collection.insert_one({"name":name,'duration':duration})
    print("video added successfully")

@catchDatabaseError
def update_a_video():
    # first show all the videos so that user can pick one
    list_all_videos()
    # take the id of the video from user
    _id = ObjectId(input("\nEnter video id: "))
    name,duration = input_data()
    result = video_collection.update_one(
        {"_id":_id},
        {"$set":{"name":name,"duration":duration}}
         )
    print("video updated successfully ",result)

@catchDatabaseError
def delete_a_video():
    # first show all the videos so that user can pick one
    list_all_videos()
    # take the id of the video from user
    _id =ObjectId(input("\nEnter video id: "))
    result = video_collection.delete_one({"_id":_id})
    print("video deleted successfully ",result)

def main():
    while True:
        show_options()
        choice = input('Enter you Choice: ')
        match choice:
            case '1':
                list_all_videos();
            case '2':
                add_a_video();
            case '3':
                update_a_video();
            case '4':
                delete_a_video();
            case '5':
                print("Invalid Choice")
                break
        
if(__name__ == '__main__'):
    main()
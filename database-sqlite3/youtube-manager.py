# create a table of columns: name, duration
# 

# add a row
# update a row
# delete a row
# create a row

import sqlite3

conn = sqlite3.connect("youtube-videos.db")

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos (
				   id   INTEGER PRIMARY KEY,
       			   name TEXT NOT NULL,
			 	   duration TEXT NOT NULL
			   )
               ''')

def input_data():
    name = input("Enter Video Name: ")
    duration = input("Enter Video Duration: ")
    
    return name,duration
    
def show_options():
	print("\n#### Youtube Manager with DB ####")
	print("1. List all Videos")
	print("2. Add a Video")
	print("3. Update a Video")
	print("4. Delete a Video")
	print("5. Exit")
    

# (name:string)
def list_all_videos():
    # taking just the name of the videos
   cursor.execute(''' 
                   SELECT * FROM videos
                   ''') or []
   print("*"*50)
   print("\n")
   print("Id | \t Name | \t Duration")
   for id,name,duration in cursor.fetchall():
     print(f"{id} | \t {name} | \t {duration}")
           
  
   print("\n")
   print("*"*50)
    
def add_a_video():
  name,duration = input_data()
  print(name)
  print(duration)
  cursor.execute(''' 
				INSERT INTO videos (name,duration)
				VALUES (?,?)''',
    			(name,duration)
    			)
  conn.commit()

def update_a_video():
    videoId =int(input("Enter Video Id: "))
    name,duration = input_data()
    cursor.execute('''
                   UPDATE videos SET name = ? ,duration = ? WHERE id = ?
                   ''',
                   (name,duration,videoId)
                   )
    conn.commit()
    
    
def delete_a_video():
    videoId = int(input("Enter Video Id: "))
    cursor.execute(""" 
                    DELETE FROM videos WHERE id = ?
                    """,(videoId,)
                  )
    conn.commit()

def main():
    while True:
        show_options()
        choice = input("\nEnter your Choice: ")
        match choice:
            case '1':
                list_all_videos()
            case '2':
                add_a_video()
            case '3':
                update_a_video()
            case '4':
                delete_a_video()
            case _:
                print("Invalid Choice")
                break
    conn.close()         

if __name__ == '__main__': main()
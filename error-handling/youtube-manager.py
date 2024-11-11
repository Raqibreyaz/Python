import json
 
# load the data from the file if there is no file found then give empty array
def load_data():
    try:
        with open('youtube.txt','r') as file:
            test= json.load(file)
            return test
    except FileNotFoundError as e:
        return []

# write the data to the file
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
        print("\n****videos successfully saved!****\n")

def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video["name"]}")
    print("\n")
    print("*" * 50)
    
def add_video(videos):
    video_name = input("enter video name: ")
    video_time = input("enter video time: ")
    videos.append({'name':video_name,'time':video_time})
    save_data_helper(videos)
    
def update_video(videos):
    list_all_videos(videos)
    ithVideo =  int(input("Choose Which Video you Want to Update: "))
        
    if 1<= ithVideo <= len(videos):
        newVideoName =  input("Enter new Video name: ")
        newVideoTime =  input("Enter new Video Time: ")
        
        videos[ithVideo-1] = {"name":newVideoName,"time":newVideoTime}
        save_data_helper(videos)
    else: print("Inavalid Video Selected")
    
def delete_video(videos):
        list_all_videos(videos)
        ithVideo =  int(input("Choose Which Video you Want to Delete: "))
        
        if 1<= ithVideo <= len(videos):        
           del videos[ithVideo-1]
           print("video deleted successfully")
           save_data_helper(videos)
        else: print("Inavalid Video Selected")

def main():
    videos = load_data();
    while True:
        print("\n Youtube Manager | Choose an Option")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter Your Choice: ")
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break;
            case _:
                print("Invalid Choice")

# making the function callable only in current file not by importing in another file
if __name__ == "__main__":
    main();

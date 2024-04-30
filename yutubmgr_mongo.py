from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://prabhatthakur672:Pt672839@cluster0.zbcz6x5.mongodb.net/", tlsAllowInvalidCertificates=True)

db = client["youtubemanager"]

videos_collection = db["videos"]

print(videos_collection)


def list_all_videos():
    for video in videos_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time:{video['time']}")

def add_video(name,time):
    videos_collection.insert_one({"name":name, "time":time})

def update_video(video_id,new_name,new_time):
    videos_collection.update_one(
        {"_id":ObjectId(video_id)},
        {"$set":{"name":new_name,"time":new_time}}
        
    )

def delete_video(video_id):
    videos_collection.delete_one({'_id':ObjectId(video_id)})



def main():
    while True:
        print("\n Youtube Manager with SQLite3 DB")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        

        match choice:
            case '1':
                list_all_videos()

            case '2':
                name = input("Enter the video name: ")
                time = input("Entert the video duration: ")
                add_video(name, time)  

            case '3':
                video_id = input("Enter the video id to update: ")
                name = input("Enter the video name: ")
                time = input("Entert the video duration: ")
                update_video(video_id,name,time)

            case '4':
                video_id = input("Enter the video id to update: ")
                delete_video(video_id)

            case '5':
                break

            case _:
                print('Invalid choice') 
 
    



if __name__ == "__main__":
    main()
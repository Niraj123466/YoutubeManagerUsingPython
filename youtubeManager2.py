import sqlite3

# make a connection with database
conn = sqlite3.connect('youtube_manager.db')
cursor = conn.cursor()

# make queries using cursor
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_all_videos() :
    print("*" * 50)
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall() :
        print(f'{row[0]}. {row[1]}  {row[2]}')
    print("*" * 50)

def add_video(name, time) :
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)", (name, time))
    conn.commit()

def update_video(videoId, name, time) :
    cursor.execute("UPDATE videos SET name = ?,  time = ? WHERE id = ?", (name, time, videoId))
    conn.commit()

def delete_video(videoId) :
    cursor.execute("DELETE FROM videos WHERE id = ?",(videoId,))
    conn.commit()

def main() :
    while True :
        print('''Youtube Manager App with Database
                1. List all videos
                2. Add a video
                3. Update a video
                4. Delete a video
                5. Exit''')
        choice = input("Enter your choice : ")
        if choice == '1' :
            list_all_videos()

        elif choice == '2' :
            name = input("Enter name of video : ")
            time = input("Enter duration of video : ")
            add_video(name, time)

        elif choice == '3' :
            id = int(input("Enter the id of video you want to update : "))
            name = input("Enter newname of video : ")
            time = input("Enter the duration of video : ")
            update_video(id, name, time)
        
        elif choice == '4' : 
            id = input("Enter the id of video you want to delete : ")
            delete_video(id)
        
        elif choice == '5':
            break

        else :
            print("Enter a valid choice")

if __name__ == "__main__" :
    main()
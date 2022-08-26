import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

fromdir = "/Users/nealpatel/Downloads"
todir = "document_files"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']

}

class fileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        #print(event)
        name,ext = os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            fname = os.path.basename(event.src_path)
            print("Dowloaded" + fname)
            p1 = fromdir + "/" + fname
            p2 = todir + "/" + key
            p3 = todir + "/" + key + "/" + fname
            if os.path.exists(p2):
                shutil.move(p1,p3)
                time.sleep(1)
            else:
                os.makedirs(p2)
                shutil.move(p1,p3)
                time.sleep(1)


event_handler = fileMovementHandler()
observer = Observer()
observer.schedule(event_handler, fromdir, recursive = True)
observer.start()


try:
    while True:
        time.sleep(2)
        print("Running")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            logging.info(f"Directory created: {event.src_path}")
        else:
            logging.info(f"File created: {event.src_path}")

    def on_modified(self, event):
        if event.is_directory:
            logging.info(f"Directory modified: {event.src_path}")
        else:
            logging.info(f"File modified: {event.src_path}")

    def on_deleted(self, event):
        if event.is_directory:
            logging.info(f"Directory deleted: {event.src_path}")
        else:
            logging.info(f"File deleted: {event.src_path}")

if __name__ == "__main__":
    path_to_watch = "C:/"

    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=True)

    logging.info(f"Monitoring started for: {path_to_watch}")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

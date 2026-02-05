import time
from collections import deque
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyEventHandler(FileSystemEventHandler):
    def __init__(self, threshold_count=5, threshold_seconds=10):
        self.DETECTION_THRESHOLD_COUNT = threshold_count
        self.DETECTION_THRESHOLD_SECONDS = threshold_seconds
        self.recent_events = deque()

    def on_any_event(self, event):
        if event.is_directory:
            return
        if event.event_type in ['created', 'modified', 'moved']:
            self.recent_events.append(time.time())
            self.check_for_ransomware()

    def check_for_ransomware(self):
        current_time = time.time()
        while self.recent_events and self.recent_events[0] < current_time - self.DETECTION_THRESHOLD_SECONDS:
            self.recent_events.popleft()

        if len(self.recent_events) > self.DETECTION_THRESHOLD_COUNT:
            print("\n!!! WARNING: RANSOMWARE-LIKE ACTIVITY DETECTED! !!!")
            print(f"Detected multiple file changes in the last few seconds.")
            self.recent_events.clear()

path_to_watch = "Sandbox"
print(f"--- Starting Real-Time Detector on folder: '{path_to_watch}' ---")
print("--- Press Ctrl+C to stop. ---")

event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, path_to_watch, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    print("\n--- Detector stopped by user. ---")

observer.join()

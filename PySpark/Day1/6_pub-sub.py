import threading
import random
from queue import Queue

def set_interval(fn, interval=None):
    actual_interval = interval if interval is not None else random.randint(2,5)

    def fn_wrapper(): 
        set_interval(fn, interval)
        fn()

    t = threading.Timer(actual_interval, fn_wrapper)
    t.start()

def push_string(subscribers):
    nameList = ["Python", "JavaScript", "Java", "DotNet", "Scala"]
    s = random.choice(nameList)
    print(f"Pushed: {s}")

    for queue in subscribers:
        queue.put(s)

def handle_events(event_queue, consumer_id):
    while True:
        try:
            s = event_queue.get(timeout=1)
            print(f"Consumer {consumer_id} received: {s}")
            event_queue.task_done()
        except Exception:
            pass

def start(num_consumers=3):
    subscribers = [Queue() for _ in range(num_consumers)]

    for i, queue in enumerate(subscribers):
        consumer_thread = threading.Thread(target=handle_events, args=(queue, i+1))
        consumer_thread.daemon = True
        consumer_thread.start()
    
    set_interval(lambda: push_string(subscribers), 2)

start(num_consumers=3)
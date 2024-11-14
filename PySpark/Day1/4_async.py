import threading
import random

def set_interval(fn, interval=None):
    actual_interval = interval if interval is not None else random.randint(2,5)

    def fn_wrapper(): 
        set_interval(fn, interval)
        fn()

    t = threading.Timer(actual_interval, fn_wrapper)
    t.start()

# def get_string():
#     nameList = ["Python", "JavaScript", "Java", "DotNet", "Scala"]
#     return random.choice(nameList)

# # s = get_string()
# # print(s)

# def process_data():
#     s = get_string()
#     print(s)

# set_interval(process_data, interval=2)

# # Call 1 - 1000
# # Call 2 - 3000
# # Call 3 - 1000

# def push_string(cb):
#     def push():
#         s = random.choice(nameList)
#         cb(s)
    
#     nameList = ["Python", "JavaScript", "Java", "DotNet", "Scala"]
#     set_interval(push)

# push_string(lambda s: print("S1: ", s))
# push_string(lambda s: print("S2: ", s))


def push_string(cb):
    def push():
        s = random.choice(nameList)
        cb(s)
    
    nameList = ["Python", "JavaScript", "Java", "DotNet", "Scala"]
    set_interval(push, interval=2)

push_string(lambda s: print("S1: ", s))
push_string(lambda s: print("S2: ", s))

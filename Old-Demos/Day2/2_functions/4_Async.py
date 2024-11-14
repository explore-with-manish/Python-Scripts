# import threading
# import random


# def set_interval(fn, sec):
#     def fn_wrapper():
#         set_interval(fn, sec)
#         fn()
#     t = threading.Timer(sec, fn_wrapper)
#     t.start()
#     return t


# # def get_string():
# #     nameList = ["Python", "JavaScript", "Java", "DotNet", "Scala"]
# #     return random.choice(nameList)


# # s = get_string()
# # print(s)

# # for r in range(6):
# #     s = get_string()
# #     print(s)

# # def caller():
# #     s = get_string()
# #     print(s)


# # set_interval(caller, 2)

# # -------------------------------------------------

# # Dev1
# def push_string(cb):
#     def push():
#         s = random.choice(nameList)
#         cb(s)

#     nameList = ["Python", "JavaScript", "Java", "DotNet", "Scala"]
#     set_interval(push, 2)


# # Dev2
# push_string(lambda s: print(s))

# print("---------------------- Last Line ------------------")

import threading
import random

def set_interval(fn, interval=None):
    """Schedules a function to run at a specified interval or a random interval between 2 and 5 seconds."""
    # Use the provided interval or generate a random one between 2 and 5 seconds
    actual_interval = interval if interval is not None else random.randint(2, 5)

    def fn_wrapper():
        set_interval(fn, interval)  # Reschedule with the same logic
        fn()  # Execute the function

    t = threading.Timer(actual_interval, fn_wrapper)
    t.start()
    # return t  # Return the timer object for control

# ------------------------------------
# def get_string():
#     nameList = ["Python", "JavaScript", "Java", "DotNet", "Scala"]
#     return random.choice(nameList)

# s = get_string()
# print(s)

# for r in range(6):
#     s = get_string()
#     print(s)

# def caller():
#     s = get_string()
#     print(s)

# set_interval(caller, interval=2)
# ------------------------------------

def push_string(cb):
    def push():
        s = random.choice(nameList)
        cb(s)

    nameList = ["Python", "JavaScript", "Java", "DotNet", "Scala"]
    set_interval(push)

push_string(lambda s: print("S1: ", s))
push_string(lambda s: print("S2: ", s))
# import threading
# import random
# from queue import Queue

# def set_interval(fn, interval=None):
#     """Schedules a function to run at a specified interval or a random interval between 2 and 5 seconds."""
#     actual_interval = interval if interval is not None else random.randint(2, 5)

#     def fn_wrapper():
#         set_interval(fn, interval)  # Reschedule with the same logic
#         fn()  # Execute the function

#     t = threading.Timer(actual_interval, fn_wrapper)
#     t.start()

# def push_string(subscribers):
#     """Generate a random string and broadcast it to all subscribers."""
#     name_list = ["Python", "JavaScript", "Java", "DotNet", "Scala"]
#     s = random.choice(name_list)
#     print(f"Pushed: {s}")  # Log the broadcasted event

#     # Broadcast to all subscriber queues
#     for queue in subscribers:
#         queue.put(s)

# def handle_events(event_queue, consumer_id):
#     """Continuously consume events from the queue."""
#     while True:
#         try:
#             s = event_queue.get(timeout=1)  # Wait for an event from the queue
#             print(f"Consumer {consumer_id} received: {s}")
#             event_queue.task_done()  # Mark the task as done
#         except Exception:
#             pass  # Handle empty queue or timeout gracefully

# def start_event_loop(num_consumers=3):
#     """Start the event loop with producer and multiple consumers."""
#     # Create a separate queue for each consumer
#     subscribers = [Queue() for _ in range(num_consumers)]

#     # Start multiple consumer threads
#     for i, queue in enumerate(subscribers):
#         consumer_thread = threading.Thread(target=handle_events, args=(queue, i + 1))
#         consumer_thread.daemon = True  # Ensure threads exit with the main program
#         consumer_thread.start()

#     # Schedule the producer to broadcast events at random intervals
#     set_interval(lambda: push_string(subscribers), 2)

# # Start the event-driven program with multiple consumers
# start_event_loop(num_consumers=3)

# -------------------------------------- Weather SImulator
import threading
import random
import time

# List of cities for temperature updates
cities = ["New York", "London", "Mumbai", "Tokyo", "Sydney"]

stop_event = threading.Event()  # Event to stop the simulator gracefully

def set_interval(fn, interval=None):
    """Schedules a function to run at a specified interval or a random interval between 2 and 5 seconds."""
    def fn_wrapper():
        if not stop_event.is_set():  
            fn()  
            actual_interval = interval if interval is not None else random.randint(2, 5)
            threading.Timer(actual_interval, fn_wrapper).start()

    fn_wrapper()  

def generate_temperature(callbacks):
    """Generates a random temperature update for a random city."""
    city = random.choice(cities)
    temperature = random.randint(-10, 40)  # Random temperature between -10°C and 40°C
    update = f"\nTemperature Update: {city} - {temperature}°C"
    print(update)

    # Push the update to all registered callbacks
    for callback in callbacks:
        callback(city, temperature)

# Define callback functions to act as consumers
def log_temperature(city, temperature):
    print(f"Logger: {city} - {temperature}°C")

def ui_display(city, temperature):
    print(f"UI Display: {city} - {temperature}°C")

def alert_system(city, temperature):
    if temperature > 35 or temperature < 0:
        print(f"ALERT! {city} has extreme temperature: {temperature}°C")

def start_weather_simulator(interval=2):
    """Starts the real-time weather update simulator."""
    # Register all callback functions
    callbacks = [log_temperature, ui_display, alert_system]

    # Schedule the temperature generator at fixed intervals
    set_interval(lambda: generate_temperature(callbacks), interval)

    # Keep the program running until interrupted
    try:
        print("Weather simulator started. Press Ctrl+C to stop.")
        while not stop_event.is_set():  # Keep main thread active
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping the simulator...")
        stop_event.set()  # Signal the simulator to stop

# Start the weather update simulator
start_weather_simulator(interval=2)

# ------------------------------- using asyncio
# import asyncio
# import random

# # List of cities for temperature updates
# cities = ["New York", "London", "Mumbai", "Tokyo", "Sydney"]

# async def generate_temperature(callbacks):
#     """Generates random temperature updates at random intervals."""
#     while True:
#         city = random.choice(cities)
#         temperature = random.randint(-10, 40)
#         print(f"\nTemperature Update: {city} - {temperature}°C")

#         # Push the update to all registered callbacks
#         for callback in callbacks:
#             callback(city, temperature)

#         # Wait for a random interval between 2 to 5 seconds
#         await asyncio.sleep(random.randint(2, 5))

# # Define callback functions to act as consumers
# def log_temperature(city, temperature):
#     """Logs the temperature update."""
#     print(f"Logger: {city} - {temperature}°C")

# def ui_display(city, temperature):
#     """Displays the temperature update on a simulated UI."""
#     print(f"UI Display: {city} - {temperature}°C")

# def alert_system(city, temperature):
#     """Sends an alert if the temperature is critical."""
#     if temperature > 35 or temperature < 0:
#         print(f"ALERT! {city} has extreme temperature: {temperature}°C")

# async def main():
#     """Starts the weather update simulator."""
#     print("Weather simulator started. Press Ctrl+C to stop.")

#     # Register all callback functions
#     callbacks = [log_temperature, ui_display, alert_system]

#     # Schedule the temperature generator
#     await generate_temperature(callbacks)  # Runs indefinitely

# # Run the event loop
# try:
#     asyncio.run(main())
# except KeyboardInterrupt:
#     print("\nWeather simulator stopped by user.")

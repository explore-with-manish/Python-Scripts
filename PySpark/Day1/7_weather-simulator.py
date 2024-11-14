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
import asyncio
import random

# List of cities for temperature updates
cities = ["New York", "London", "Mumbai", "Tokyo", "Sydney"]

async def generate_temperature(callbacks):
    """Generates a random temperature update for a random city."""
    while True:
        city = random.choice(cities)
        temperature = random.randint(-10, 40)  # Random temperature between -10°C and 40°C
        update = f"\nTemperature Update: {city} - {temperature}°C"
        print(update)

        # Push the update to all registered callbacks
        for callback in callbacks:
            callback(city, temperature)

        await asyncio.sleep(random.randint(2,5))

# Define callback functions to act as consumers
def log_temperature(city, temperature):
    print(f"Logger: {city} - {temperature}°C")

def ui_display(city, temperature):
    print(f"UI Display: {city} - {temperature}°C")

def alert_system(city, temperature):
    if temperature > 35 or temperature < 0:
        print(f"ALERT! {city} has extreme temperature: {temperature}°C")

async def main():
    """Starts the real-time weather update simulator."""
    print("Weather simulator started. Press Ctrl+C to stop.")

    # Register all callback functions
    callbacks = [log_temperature, ui_display, alert_system]

    await generate_temperature(callbacks)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nWeather simulator stopped by user.")
import time
import random
import json
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "bikelock/device1/data"

class LockState:
    LOCKED = "locked"
    UNLOCKED = "unlocked"
    ALARM = "alarm"

class SmartBikeLock:
    def __init__(self):
        self.state = LockState.LOCKED
        self.battery = 100
        self.gps = {"lat": 59.3293, "lon": 18.0686}
        self.movement = False

    def update_sensors(self):
        # Simulate GPS drift
        self.gps["lat"] += random.uniform(-0.0005, 0.0005)
        self.gps["lon"] += random.uniform(-0.0005, 0.0005)
        # Simulate battery drain
        self.battery = max(0, self.battery - random.uniform(0.01, 0.1))
        # Simulate movement
        self.movement = random.choice([True, False])
        # State transition: alarm if locked and movement detected
        if self.state == LockState.LOCKED and self.movement:
            self.state = LockState.ALARM
        elif self.state == LockState.ALARM and not self.movement:
            self.state = LockState.LOCKED

    def lock(self):
        self.state = LockState.LOCKED

    def unlock(self):
        self.state = LockState.UNLOCKED

    def get_status(self):
        return {
            "lock_status": self.state,
            "gps": {
                "lat": round(self.gps["lat"], 6),
                "lon": round(self.gps["lon"], 6)
            },
            "battery": round(self.battery, 2),
            "movement": self.movement
        }

def on_message(client, userdata, msg):
    command = msg.payload.decode()
    print(f"Received command: {command}")
    if command == "lock":
        userdata.lock()
        print("Locking the bike.")
    elif command == "unlock":
        userdata.unlock()
        print("Unlocking the bike.")

def main():
    lock = SmartBikeLock()
    client = mqtt.Client(userdata=lock)
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.subscribe("bikelock/device1/command")
    print("Connected to MQTT broker. Publishing simulated data...")

    try:
        while True:
            lock.update_sensors()
            data = lock.get_status()
            payload = json.dumps(data)
            client.publish(TOPIC, payload)
            print(f"Published: {payload}")
            client.loop(timeout=0.1)  # Process incoming messages
            time.sleep(5)
    except KeyboardInterrupt:
        print("Simulation stopped.")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()
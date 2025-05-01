import paho.mqtt.client as mqtt

broker_1 = "192.168.1.2"  # Source broker IP (Edit this)
broker_2 = "192.168.1.1"  # Destination broker IP (Edit this)
port = 1883  # (Edit this) // add another port and change the rest if you have different ports

# Define the client for broker 1 (source)
def on_connect_broker1(client, userdata, flags, rc):
    print(f"Connected to Broker 1 with result code {rc}")
    # Subscribe to all topics
    client.subscribe("#")

def on_message_broker1(client, userdata, msg):
    try:
        print(f"Received message on {msg.topic}: {msg.payload.decode('utf-8')}")
        # Republish the message to broker 2
        client_broker2.publish(msg.topic, msg.payload)
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
    except Exception as e:
        print(f"Error publishing to Broker 2: {e}")

# Define the client for broker 2 (destination)
def on_connect_broker2(client, userdata, flags, rc):
    print(f"Connected to Broker 2 with result code {rc}")

# Set up the source broker client
client_broker1 = mqtt.Client()
client_broker1.username_pw_set("admin", "admin")
client_broker1.on_connect = on_connect_broker1
client_broker1.on_message = on_message_broker1

# Set up the destination broker client
client_broker2 = mqtt.Client()
client_broker2.username_pw_set("admin", "admin")
client_broker2.on_connect = on_connect_broker2
# Connect to both brokers
try:
    client_broker1.connect(broker_1, port, 60)
    client_broker2.connect(broker_2, port, 60)
except Exception as e:
    print(f"Error connecting to brokers: {e}")

# Start the loop for both clients
try:
    client_broker2.loop_start()  # Start destination broker first
    client_broker1.loop_forever()  # Source broker keeps listening for messages
except Exception as e:
    print(f"Error in loop: {e}")

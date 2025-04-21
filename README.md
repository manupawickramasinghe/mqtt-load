# MQTT Load Transfer

This repository provides a solution for transferring MQTT load from one broker to another. By modifying the source and destination IPs, users can redirect MQTT messages efficiently across brokers.

## Features
- Transfers MQTT messages between brokers
- Configurable source and destination broker IPs
- Supports various MQTT topics and payloads

## Requirements
- Python3 and the relevant Libraries 
- MQTT

## Installation & Usage

### Clone the Repository
```bash
git clone https://github.com/manupawickramasinghe/mqtt-load.git
cd mqtt-load
```

### Python `pip` Installation and Commands for MQTT

To use the `paho-mqtt` library in Python, you need to install it using `pip`. Here’s how you can do it:

1. **Install `paho-mqtt` using `pip`**:
   ```bash
   pip install paho-mqtt
   ```

2. **Verify Installation**:
   ```bash
   python -m pip show paho-mqtt
   ```

3. **Upgrade `paho-mqtt` (if needed)**:
   ```bash
   pip install --upgrade paho-mqtt
   ```

4. **Uninstall `paho-mqtt` (if needed)**:
   ```bash
   pip uninstall paho-mqtt
   ```

---

### Modifying the Brokers in Your Code

If you need to change the MQTT broker IPs or add another port, you can modify your code like this:

```python
import paho.mqtt.client as mqtt

# Update these IPs and ports as needed
broker_1 = "192.168.1.100"  # New Source Broker IP
broker_2 = "192.168.1.200"  # New Destination Broker IP
port_1 = 1883  # Source broker port
port_2 = 8883  # Destination broker port (example for TLS)

# Define the source broker client
client_broker1 = mqtt.Client()
client_broker1.username_pw_set("admin", "newpassword123")  # Update credentials
client_broker1.connect(broker_1, port_1, 60)

# Define the destination broker client
client_broker2 = mqtt.Client()
client_broker2.username_pw_set("admin", "newpassword123")  # Update credentials
client_broker2.connect(broker_2, port_2, 60)

# Start the connection loop
client_broker2.loop_start()
client_broker1.loop_forever()
```

This setup allows you to:
- Change the broker IPs (`broker_1`, `broker_2`).
- Modify the ports (`port_1`, `port_2`) if needed.
- Adjust credentials securely.


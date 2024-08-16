# IoT-based-Fire-Alarm-System
1. Design Overview   
Sensors: Use a smoke sensor (e.g., MQ-2) and/or a temperature sensor (e.g., DHT11 or DHT22) to detect fire-related events.
Microcontroller: An Arduino or Raspberry Pi will process sensor data and manage communication.
Wi-Fi Module: For Arduino, an ESP8266 or ESP32 can be used to connect to the internet.
For Raspberry Pi, Wi-Fi is built-in.
Alert System: When a fire is detected, the system sends alerts via SMS, email, or an app notification using a cloud service like Firebase, Blynk, or IFTTT.
3. Components Needed
Smoke Sensor (MQ-2 or MQ-135)
Temperature Sensor (DHT11 or DHT22)
Microcontroller (Arduino UNO, ESP32, or Raspberry Pi)
Wi-Fi Module (ESP8266 or ESP32)
Breadboard and Jumper Wires
Buzzer (for local alarm)
LEDs (for visual indicators)
Resistors
Power Supply (e.g., 5V for Arduino, USB for Raspberry Pi)
4. Circuit Design
Connect the Smoke Sensor:
VCC to 5V (3.3V for some sensors).
GND to Ground.
Analog or Digital output to a microcontroller analog or digital input pin.
Connect the Temperature Sensor:
VCC to 5V.
GND to Ground.
Data pin to a digital input pin on the microcontroller (with a pull-up resistor if necessary).
Connect the Buzzer and LED:Connect the buzzer's positive terminal to a digital output pin via a resistor.
Connect LEDs to digital output pins with current-limiting resistors.

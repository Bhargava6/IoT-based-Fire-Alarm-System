import RPi.GPIO as GPIO
import Adafruit_DHT
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
DHT_PIN = 4  # DHT11 data pin connected to GPIO 4
SMOKE_SENSOR_PIN = 17  # Smoke sensor connected to GPIO 17 (analog pin via ADC)
BUZZER_PIN = 18  # Buzzer connected to GPIO 18
LED_PIN = 27  # LED connected to GPIO 27

# Set up the GPIO pins
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)

# Use DHT11 sensor
DHT_SENSOR = Adafruit_DHT.DHT11

def read_smoke_sensor():
    # Simulating analog read, adapt to your ADC
    smoke_level = GPIO.input(SMOKE_SENSOR_PIN)
    return smoke_level

def main():
    try:
        while True:
            # Read temperature and humidity from DHT11
            humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
            smoke_level = read_smoke_sensor()
            
            print(f"Temperature: {temperature:.1f}C, Smoke Level: {smoke_level}")

            if smoke_level > 300 or (temperature is not None and temperature > 50):
                GPIO.output(BUZZER_PIN, GPIO.HIGH)
                GPIO.output(LED_PIN, GPIO.HIGH)
                print("Fire detected!")
            else:
                GPIO.output(BUZZER_PIN, GPIO.LOW)
                GPIO.output(LED_PIN, GPIO.LOW)

            time.sleep(2)

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()

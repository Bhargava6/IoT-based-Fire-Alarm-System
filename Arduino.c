#include <DHT.h>  // Include the DHT sensor library

#define DHTPIN 2      
#define DHTTYPE DHT11  

#define SMOKE_SENSOR_PIN A0 
#define BUZZER_PIN 8         
#define LED_PIN 7            

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();

  pinMode(SMOKE_SENSOR_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  int smokeLevel = analogRead(SMOKE_SENSOR_PIN);
  float temperature = dht.readTemperature();

  // Simple threshold for smoke and temperature
  if (smokeLevel > 300 || temperature > 50) {
    digitalWrite(BUZZER_PIN, HIGH); 
    digitalWrite(LED_PIN, HIGH);
    Serial.println("Fire detected!");  
    delay(1000);  // Pause before rechecking
  } else {
    digitalWrite(BUZZER_PIN, LOW);  
    digitalWrite(LED_PIN, LOW);     
  }

  delay(2000);
}

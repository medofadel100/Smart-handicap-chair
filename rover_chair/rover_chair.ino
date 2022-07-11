#include <Wire.h>

# define I2C_SLAVE_ADDRESS 11

#define PAYLOAD_SIZE 2

#define echoPin 5 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin A3 //attach pin D3 Arduino to pin Trig of HC-SR04

// defines variables
long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement

//motor
#define motor1a A1
#define motor1b 9

#define motor2a 11
#define motor2b A2

#define lamp 8
#define led 7


int n = 0;

void setup() {
   // Initialize I2C communications as Slave
  Wire.begin(I2C_SLAVE_ADDRESS);



  Wire.onRequest(requestEvents);
  Wire.onReceive(receiveEvents);

  
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
  pinMode(motor1a, OUTPUT);
  pinMode(motor1b, OUTPUT);
  pinMode(motor2a, OUTPUT);
  pinMode(motor2b, OUTPUT);


  pinMode(lamp, OUTPUT);
  digitalWrite(lamp, HIGH);
  pinMode(led, OUTPUT);

}
void loop() {

ultrasonic();
delay(100);
}

void ultrasonic(){
    // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  // Displays the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
}
void avoid(){
  ultrasonic();
  if (distance > 1 && distance< 40){
        stoop();
        delay (500);
        righ(); 
        delay(1000);
        stooop();
  }
}

void forward(){
  avoid();
  digitalWrite(motor1a, HIGH);
  digitalWrite(motor1b, LOW);
  
  digitalWrite(motor2a, HIGH);
  digitalWrite(motor2b, LOW);
  delay(2000);
  
}

void back(){
  digitalWrite(motor1a, LOW);
  digitalWrite(motor1b, HIGH);
  
  digitalWrite(motor2a, LOW);
  digitalWrite(motor2b, HIGH);
  delay(2000);
  
}

void righ(){
  digitalWrite(motor1a, LOW);
  digitalWrite(motor1b, HIGH);

  digitalWrite(motor2a, HIGH);
  digitalWrite(motor2b, LOW);
  avoid();
  delay(2000);
  
}

void left(){
  digitalWrite(motor1a, HIGH);
  digitalWrite(motor1b, LOW);
  
  digitalWrite(motor2a, LOW);
  digitalWrite(motor2b, HIGH);
  delay(2000);
  
}
void stoop(){
  digitalWrite(motor1a, LOW);
  digitalWrite(motor1b, LOW);
  
  digitalWrite(motor2a, LOW);
  digitalWrite(motor2b, LOW);
   pinMode(lamp, LOW);
   pinMode(led, HIGH);
  delay(4000);
  pinMode(lamp, HIGH);
  pinMode(led, LOW);
  
}

void stooop(){
  digitalWrite(motor1a, LOW);
  digitalWrite(motor1b, LOW);
  
  digitalWrite(motor2a, LOW);
  digitalWrite(motor2b, LOW);
  digitalWrite(lamp, HIGH);
  
  delay(2000);
  
}

void requestEvents()
{
  Serial.println(F("---> recieved request"));
  Serial.print(F("sending value : "));
  Serial.println(n);
  Wire.write(n);
}

void receiveEvents(int howMany)
{  pinMode(led, LOW);
  while (Wire.available()) {
    pinMode(led, HIGH);
  char n = Wire.read();
  
  Serial.println(n);

  if (n == 4){
    forward();
    Serial.println("forward");
  }

   else if (n == 5){
    back();
    Serial.println("back");
  }

   else if (n == 2){
    righ();
    Serial.println("righ");
  }

   else if (n == 3){
    left();
    Serial.println("left");
  }

   else if (n == 6){
    stoop();
    Serial.println("stoop");
  }

  else if (n == 1){
   
    
    stoop();
  }
  else if (n == 7){
    stooop();

  }
else {
  stooop();
}

 
}}

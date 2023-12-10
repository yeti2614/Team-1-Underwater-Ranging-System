bool ledState=1; //variable used to save the state of LED
int inByte = 0; // for incoming serial data



void setup() {
  Serial.begin(9600);// set baud rate to 9600
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    inByte = Serial.read();

    // say what you got:
    Serial.print("I received: ");
    Serial.println(inByte);
    delay(10);
  }
}


#include <SparkFunSerialGraphicLCD.h>
#include <string.h>

LCD LCD;

void distance(float num) {
  LCD.setX(0);
  LCD.setY(63);
  float dist[] = {};
  int i;
  char buff[64];
  int maxY = 63;
  LCD.printStr("Distance: ");
  LCD.printStr(dtostrf(num, 3, 2, buff));
  LCD.printStr("m");

  // for(i = 0; i < 4; i++){
  //   LCD.setX(0);
  //   LCD.setY(maxY);
  //   if(i == 0){
  //     LCD.printStr("Distance: ");
  //     LCD.printStr(dtostrf(num, 3, 2, buff));
  //     LCD.printStr("m");
  //     maxY = maxY - 12;
  //   }
  //   else if(i == 1) {
  //     LCD.printStr(dtostrf(i, 1, 0, buff));
  //     LCD.printStr("st Prev. Dist: ");
  //     LCD.printNum(dtostrf(num, 3, 2, buff));
  //     LCD.printStr("m");
  //     maxY = maxY - 12;
  //   }
  //   else if(i == 2) {
  //     LCD.printStr(dtostrf(i, 1, 0, buff));
  //     LCD.printStr("nd Prev. Dist: ");
  //     LCD.printNum(dtostrf(num, 3, 2, buff));
  //     LCD.printStr("m");
  //     maxY = maxY - 12;
  //   }
  //   else if(i == 3) {
  //     LCD.printStr(dtostrf(i, 1, 0, buff));
  //     LCD.printStr("rd Prev. Dist: ");
  //     LCD.printNum(dtostrf(num, 3, 2, buff));
  //     LCD.printStr("m");
  //     maxY = maxY - 12;
  //   }
  // }
}
void displayPrev(float num){
  LCD.setX(0);
  LCD.setY(51);
  float dist[] = {};
  int i;
  char buff[64];
  int maxY = 63;
  LCD.printStr("Prev Dist: ");
  LCD.printStr(dtostrf(num, 3, 2, buff));
  LCD.printStr("m");
}

void setup() {
  LCD.clearScreen();

  // put your setup code here, to run once:
}

void loop() {
  float num = rand();
  distance(num);
  delay(2000);
  int count = 1;
  float last_val = 0;
  float first = num;
  displayPrev(last_val);
  delay(2000);
  while(count == 1){
    if(first == num){
      displayPrev(first);
      first = 0;
    }
    num = rand();
    delay(1000);
    distance(num);
    delay(1000);
    last_val = num;
    displayPrev(last_val);

  }

  // put your main code here, to run repeatedly:

}


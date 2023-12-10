#include <SparkFunSerialGraphicLCD.h>
#include <string.h>

LCD LCD;

long freq;  //32-bit global frequency variable
#include <SPI.h>
// Define the FSYNC (used for SD funtion)
#define FSYNC 2
void WriteFrequencyAD9837(long frequency)
{
  //
  int MSB;
  int LSB;
  int phase = 0;
  //We can't just send the actual frequency, we have to calculate the "frequency word".
  //This amounts to ((desired frequency)/(reference frequency)) x 0x10000000.
  //calculated_freq_word will hold the calculated result.
  long calculated_freq_word;
  float AD9837Val = 0.00000000;
  AD9837Val = (((float)(frequency))/16000000);
  calculated_freq_word = AD9837Val*0x10000000;
  /*
  Serial.println("");
  Serial.print("Frequency word is ");
  Serial.print(calculated_freq_word);
  Serial.println("");
  */
  //Once we've got that, we split it up into separate bytes.
  MSB = (int)((calculated_freq_word & 0xFFFC000)>>14); //14 bits
  LSB = (int)(calculated_freq_word & 0x3FFF);
  //Set control bits DB15 ande DB14 to 0 and one, respectively, for frequency register 0
  LSB |= 0x4000;
  MSB |= 0x4000;
  phase &= 0xC000;
  WriteRegisterAD9837(0x2100);
  delay(500);
  //Set the frequency==========================
  WriteRegisterAD9837(LSB);  //lower 14 bits
  WriteRegisterAD9837(MSB);  //upper 14 bits
  WriteRegisterAD9837(phase);  //mid-low
  //Power it back up
  //AD9837Write(0x2020); //square
  WriteRegisterAD9837(0x2000); //sin
  //AD9837Write(0x2002); //triangle
}
//This is the guy that does the actual talking to the AD9837
void WriteRegisterAD9837(int dat)
{ 
  digitalWrite(FSYNC, LOW);  //Set FSYNC low
  delay(10);
  SPI.transfer(highByte(dat)); Serial.println(highByte(dat));
  SPI.transfer(lowByte(dat));  Serial.println(lowByte(dat));
  delay(10);
  digitalWrite(FSYNC, HIGH);  //Set FSYNC high
}
// function: distance
// This function is responsible for printing to the liquid crystal display (LCD) the character array that it takes as an argument. 
// This data is displayed at the top left corner of the LCD. First a portion of the top of the screen is erased.
void distance(char distance[])
{
  LCD.eraseBlock(0, 56, 127, 64);
  LCD.setX(0);
  LCD.setY(63);
  LCD.printStr("Distance: ");
  LCD.printStr(distance);
}

// function: displayPrev
// This function is responsible for printing to the liquid crystal display (LCD) the character array that it takes as an argument. 
// This data is displayed below the top left corner of the LCD. First a portion below the top of the screen is erased.
// This function acts to display the distance after the distance function has displayed it.

void displayPrev(char distance[])
{
  LCD.eraseBlock(0, 45, 127, 54); 
  LCD.setX(0);
  LCD.setY(51);
  LCD.printStr("Prev Dist: ");
  LCD.printStr(distance);
}

void setup() {
  LCD.clearScreen();
  LCD.setBaud(54);
  Serial.begin(9600, SERIAL_8N2);
  pinMode(LED_BUILTIN, OUTPUT);

  pinMode(FSYNC, OUTPUT);  //FSYNC
  digitalWrite(FSYNC, HIGH);
  SPI.setDataMode(SPI_MODE2); // requires SPI Mode for AD9837
  SPI.begin();
  delay(100);  //A little set up time, just to make sure everything's stable
  //Initial frequency
  freq = 63000;
  WriteFrequencyAD9837(freq);
  Serial.print("Frequency is ");
  Serial.print(freq);
  Serial.println("");



}

void loop() {

  if (Serial.available() > 0)
  {
    int count = 0; 
    String stri = "";
    stri = Serial.readStringUntil("m");
    Serial.print(stri); 
    Serial.flush();
    int str_l = stri.length()+1;
    char dist[str_l];
    stri.toCharArray(dist, str_l);
    distance(dist);
    String trash = Serial.readStringUntil("m");
    delay(4000);
    displayPrev(dist);
    
  }

}

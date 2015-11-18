/*
USB Pinout (Left to Right, USB symbol up)
4: GND
3: Clk
2: Data
1: Vcc
*/
#define CLOCK 5
#define DATA 6
#include "ps2.h"

PS2 mouse(6,5);


void setup(){
  
  pinMode(DATA,INPUT);
  pinMode(CLOCK,OUTPUT);
  
  int dataR = digitalRead(DATA);
  int clockR = digitalRead(CLOCK);
  //digitalWrite(CLOCK, LOW);
  
  Serial.begin(9600);
  while(!Serial); 
  Serial.println("Setup");
  Serial.println(clockR);
  Serial.println(dataR);
  mouse.mouse_init();
  Serial.println(clockR);
  Serial.println(dataR);
  Serial.println("Mouse Ready");
}

void loop(){
  char stat,x,y;
  mouse.mouse_pos(stat,x,y);
  
  Serial.print(stat, BIN);
  Serial.print("\tx=");
  Serial.print(x, DEC);
  Serial.print("\ty=");
  Serial.println(y, DEC);
  
  delay(1);
}

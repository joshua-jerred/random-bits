/**
 * @file bmp180_16x2.ino
 * @author Joshua Jerred (https://joshuajer.red)
 * @brief A simple example of using the BMP180 library with a 16x2 LCD
 * @date 2022-12-01
 * @copyright Copyright (c) 2022
 * @version 1.0
 */

#include <Wire.h>
#include <Adafruit_BMP085.h>
#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
Adafruit_BMP085 bmp;

void setup() {
  lcd.begin(16, 2);

  if (!bmp.begin()) { // Initialize the BMP180, if it fails enter endless loop after printing error to LCD
    lcd.print("Error Starting");
    while (1) {}
  }
}

void loop() {
  // Temperature
  lcd.setCursor(0, 0); 
  lcd.print("T: ");
  lcd.print((bmp.readTemperature() * 9/5) + 32);
  lcd.setCursor(7, 0); // A cheap way to 'round' the temperature to 1 decimal place (overwrites the last digit)
  lcd.print((char)223);
  lcd.print("F");

  lcd.setCursor(0, 1);
  lcd.print("P: ");
  lcd.print((float)bmp.readPressure()/100);
  lcd.setCursor(8, 1); // Another cheap rounding, but for the pressure.
  lcd.print("mb");
  delay(100); // Makes the display more readable
}

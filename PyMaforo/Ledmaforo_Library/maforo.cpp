/*
  Maforo.cpp - Library for flashing semaphore code.
  Created by Eddy Alfaro, November 8, 2019.
  Released into the public domain.
*/

#include "Arduino.h"
#include "Maforo.h"

Maforo::Maforo(int pinGreen, int pinYellow, int pinRed, int pinBtn, int pinSpk)
{
  pinMode(pinGreen, OUTPUT);
  pinMode(pinYellow, OUTPUT);
  pinMode(pinRed, OUTPUT);
  pinMode(pinBtn, INPUT);
  pinMode(pinSpk, OUTPUT);

  _pinGreen = pinGreen;
  _pinYellow = pinYellow;
  _pinRed = pinRed;
  _pinBtn = pinBtn;
  _pinSpk = pinSpk;
}

void Maforo::greenON()
{
  digitalWrite(_pinGreen, HIGH);
}

void Maforo::greenOFF()
{
  digitalWrite(_pinGreen, LOW);
}

void Maforo::yellowON()
{
  digitalWrite(_pinYellow, HIGH);
}

void Maforo::yellowOFF()
{
  digitalWrite(_pinYellow, LOW);
}

void Maforo::redON()
{
  digitalWrite(_pinRed, HIGH);
}

void Maforo::redOFF()
{
  digitalWrite(_pinRed, LOW);
}

bool Maforo::getBtnState()
{
  int BtnState = digitalRead(_pinBtn);
  if (BtnState == LOW) {
    return true;
  } else {
    return false;
  }
}

void Maforo::speakerON()
{
  digitalWrite(_pinSpk, HIGH);
}

void Maforo::speakerOFF()
{
  digitalWrite(_pinSpk, LOW);
}

void Maforo::giveWay()
{
  delay(3000);
  pLed(_pinGreen);
  pLed(_pinYellow);
  redON();
  
  for(int i=0; i<10; i++){
    pLedBeep(_pinYellow);
    delay(800);
  }
  
  for(int i=0; i<7; i++){
    pLedBeep(_pinYellow);
    delay(300);
  }

  for(int i=0; i<8; i++){
    pLedBeep(_pinYellow);
    delay(25);
  }
}

void Maforo::givePriority()
{
  delay(1000);
  greenOFF();
  pLed(_pinYellow);
  redON();
  
  for(int i=0; i<10; i++){
    pLedBeep(_pinYellow);
    delay(1000);
  }
  
  for(int i=0; i<7; i++){
    pLedBeep(_pinYellow);
    delay(300);
  }

  for(int i=0; i<8; i++){
    pLedBeep(_pinYellow);
    delay(25);
  }
}

void Maforo::giveWayVehicules()
{
  redOFF();
  yellowOFF();
  greenON();
}

void Maforo::pLed(int led)
{
  for(int i = 0; i<5; i++){
    digitalWrite(led,HIGH);
    delay(500);
    digitalWrite(led,LOW);
    delay(500);
  }
}

void Maforo::pLedBeep(int led)
{
  redON();
  for(int i = 0; i<500; i++){
    speakerON();
    digitalWrite(led,HIGH);
    delayMicroseconds(400);
    digitalWrite(led,LOW);
    speakerOFF();
    delayMicroseconds(400);
  }
  delay(250);

}


/*
  Maforo.h - Library for flashing semaphore code.
  Created by Eddy Alfaro, November 8, 2019.
  Released into the public domain.
*/

#ifndef Maforo_h
#define Maforo_h

#include "Arduino.h"

class Maforo
{
  public:
    Maforo(int pinGreen, int pinYellow, int pinRed, int pinBtn, int pinSpk);
    void giveWay();
    void givePriority();
    void giveWayVehicules();
    bool getBtnState();
    
  private:
    int _pinGreen;
    int _pinYellow;
    int _pinRed;
    int _pinBtn; 
    int _pinSpk;

    void greenON();
    void greenOFF();

    void yellowON();
    void yellowOFF();

	void redON();
    void redOFF();

    void speakerON();
    void speakerOFF();

 	void pLed(int led);
    void pLedBeep(int led);
};

#endif
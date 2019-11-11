#include <maforo.h>

int Option;
// Maforo(pinGreen, pinYellow, pinRed, pinBtn, pinSpk)
Maforo maforo(2,7,8,4,10);

void setup(){ 
  // Inicializamos el puerto serial
  Serial.begin(115200);
  // make a infinite bucle to the port
  while (!Serial) continue;
}

void loop(){
  if(Serial.available()>0){
    char Option = Serial.read();
    if(Option == 'A'){
      maforo.giveWay();
    }else if(Option == 'B'){
      maforo.givePriority();
    }
    while(Serial.available()>0){
      char Option = Serial.read();
    }
  }else{
    if(!maforo.getBtnState()){
      maforo.giveWayVehicules();
    }else{
      maforo.giveWay();
    }
  } 
}

#include "SerialTransfer.h"
SerialTransfer myTransfer;

#define LED1 3
#define LED2 5
#define LED3 6

double arr[4]; // array to store data from the master

void setup()
{
    Serial.begin(115200);
    //Serial1.begin(115200);
    myTransfer.begin(Serial);

    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
}

void loop()
{
    if(myTransfer.available()) {
        uint16_t recSize = 0;

        recSize = myTransfer.rxObj(arr, recSize);
        analogWrite(LED1, int(arr[0]));
        analogWrite(LED2, 1023 - int(arr[1]));
        analogWrite(LED3, 1023 - int(arr[2]));
    }
}
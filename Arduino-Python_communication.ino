
#include <Ethernet.h>//Comunicación red ethernet
#include <EthernetUdp.h>//Comunicación por UDP
#include <SPI.h>//Comunicación por SPI

byte mac[] = {0x90, 0xA2, 0xDA, 0x00, 0x4A, 0xE0}; //Se define la dirección MAC
IPAddress ip(192, 168, 2, 41);                     //Se define la dirección IP

char packetBuffer[UDP_TX_PACKET_MAX_SIZE];  //matriz tipo char para almacenar datos recibidos
String receivedData;                        //cadena string para almacenar los datos
int packetSize;                             //variable que almacena el tamaño del paquete que se recibio
EthernetUDP UDP;                            //objeto UDP

void setup()
{
  Ethernet.begin(mac, ip);                  //Se inicializa ethernet con los parametos de la MAC e IP
  UDP.begin(5000);                          //Se unicializa el UDP usando el puerto 5000(los puertos entre el arduino y python deben ser los mismos)
  delay(1500);                              //Delay de 1.5 segundos
}

void loop()
{  
  packetSize = UDP.parsePacket();                     //Se obtiene el tamaño del paquete recibido 
  if(packetSize > 0)                                  //Se pregunta si se ricibió un paquete si >0
  {
    UDP.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);   //Se leen los dato recibidos via UDP
    String receivedData(packetBuffer);                //Y se convierten a string

    receivedData.toUpperCase();                       //Se convierten a mayúsculas la cadena string
  
    UDP.beginPacket(UDP.remoteIP(), UDP.remotePort());//Se inicializa el paquete a enviar
    UDP.print(receivedData);                          //Se envia la cadena string de nuevo a Python
    UDP.endPacket();                                  //Se finaliza el envió
  }
  memset(packetBuffer, 0, UDP_TX_PACKET_MAX_SIZE);    //Se resetea el array o matriz a 0
}

int x=3;
int xd = 4;
int y = 5;
int yd = 6;
int oku=0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(x , OUTPUT);
pinMode(xd , OUTPUT);
pinMode(y , OUTPUT);
pinMode(yd , OUTPUT);
}

void loop() {
if(Serial.available()==1) //Serial Portta değer gelirse
{
oku = Serial.read();

if (oku == "0"){
//dur
digitalWrite(x ,LOW);
digitalWrite(xd ,LOW);
digitalWrite(y ,LOW);
digitalWrite(yd ,LOW);
}

if(oku=="1"){
//sag
digitalWrite(xd , HIGH);

digitalWrite(x , HIGH);
delayMicroseconds(500);
digitalWrite(x , LOW);
delayMicroseconds(500);
}

if(oku=="2"){
//sol
digitalWrite(xd , LOW);

digitalWrite(x , HIGH);
delayMicroseconds(500);
digitalWrite(x , LOW);
delayMicroseconds(500);
}

if(oku=="3"){
//yukarı
digitalWrite(yd , HIGH);

digitalWrite(y , HIGH);
delayMicroseconds(500);
digitalWrite(y , LOW);
delayMicroseconds(500);
}


if(oku=="4"){
//alt
digitalWrite(yd , LOW);

digitalWrite(y , HIGH);
delayMicroseconds(500);
digitalWrite(y , LOW);
delayMicroseconds(500);
}

if(oku=="5"){
//sag ust
digitalWrite(xd , HIGH);
digitalWrite(yd , HIGH);

digitalWrite(y , HIGH);
digitalWrite(x , HIGH);
delayMicroseconds(500);
digitalWrite(x , LOW);
digitalWrite(y , LOW);
delayMicroseconds(500);
}

if(oku=="6"){
//sag alt
digitalWrite(xd , HIGH);
digitalWrite(yd , LOW);

digitalWrite(x , HIGH);
digitalWrite(y , HIGH);
delayMicroseconds(500);
digitalWrite(x , LOW);
digitalWrite(y , LOW);
delayMicroseconds(500);
}


if(oku=="7"){
//sol ust
digitalWrite(xd , LOW);
digitalWrite(yd , HIGH);

digitalWrite(y , HIGH);
digitalWrite(x , HIGH);
delayMicroseconds(500);
digitalWrite(x , LOW);
digitalWrite(y , LOW);
delayMicroseconds(500);
}

if(oku=="8"){
//sol alt
digitalWrite(xd , LOW);
digitalWrite(yd , LOW);

digitalWrite(x , HIGH);
digitalWrite(y , HIGH);
delayMicroseconds(500);
digitalWrite(x , LOW);
digitalWrite(y , LOW);
delayMicroseconds(500);
}



}


if(Serial.available()==0) //Serial Portta değer gelirse
{
  
//dur
digitalWrite(x ,LOW);
digitalWrite(xd ,LOW);
digitalWrite(y ,LOW);
digitalWrite(yd ,LOW);

}

}

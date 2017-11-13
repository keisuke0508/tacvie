void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int val = 0;
  if(Serial.available() > 0) {
    val = Serial.read();
  }
  Serial.println(val);
}

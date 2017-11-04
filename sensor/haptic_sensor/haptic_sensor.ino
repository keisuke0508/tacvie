const int pin = 1;
const double r = 5.1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int pressure = analogRead(pin);
  double volt = pressure * 5.0 / 1024;
  double frs = r * volt / (5.0 - volt);
  double fg = 880.79 / frs + 47.96;
  Serial.println(fg);
  delay(16);
}

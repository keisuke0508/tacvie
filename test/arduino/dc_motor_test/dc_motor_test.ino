void setup() {
  // put your setup code here, to run once:
  pinMode(1, OUTPUT);
  pinMode(2, OUTPUT);
  delay(3000);
}

void loop() {
  // put your main code here, to run repeatedly:
//  test1();
//  test2();
  test3();
}

// motor test
void test1() {
  digitalWrite(1, HIGH);
  digitalWrite(2, LOW);
  delay(1000);
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  delay(500);
  digitalWrite(1, LOW);
  digitalWrite(2, HIGH);
  delay(1000);
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  delay(500);
}

// for rolling up
void test2() {
  digitalWrite(1, LOW);
  digitalWrite(2, HIGH);
  delay(100);
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  delay(1000);
}

// prototype
void test3() {
  digitalWrite(1, LOW);
  digitalWrite(2, HIGH);
  delay(100);
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  delay(1000);
  digitalWrite(1, HIGH);
  digitalWrite(2, LOW);
  delay(100);
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  delay(1000);
}


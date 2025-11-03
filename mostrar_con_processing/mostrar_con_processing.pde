void setup() {
  size(800, 600);
  //background(255);
  fill(255);
}

void draw() {
  background(0);
  int s = second();  // Values from 0 - 59
  int m = minute();  // Values from 0 - 59
  int h = hour();    // Values from 0 - 23
  textSize(32);
  text(h, 50*width/100, 30*height/100);
  text(m, 50*width/100, 40*height/100);
  text(s, 50*width/100, 50*height/100);
}

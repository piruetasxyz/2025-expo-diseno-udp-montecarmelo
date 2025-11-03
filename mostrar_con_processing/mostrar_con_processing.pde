String comando = "vlc --video-filter 'transform' --transform-type '270' '/085.mp4'";

void setup() {
  size(1600, 900);
  //background(255);
  fill(255);
  textSize(64);
  launch(comando);
}

void draw() {
  background(0);
  int s = second();  // Values from 0 - 59
  int m = minute();  // Values from 0 - 59
  int h = hour();    // Values from 0 - 23

  // Apply transformations
  pushMatrix();
  translate(width/2, height/2); // Move the origin to the center
  rotate(radians(270)); // Rotate by 90 degrees

  text(h, 0, -15* height/100);
  text(m, 0, 0*height/100);
  text(s, 0, 15*height/100);

  popMatrix();
}

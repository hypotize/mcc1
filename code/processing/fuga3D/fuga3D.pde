void setup() {
  size(500, 500, P3D);
  background(0);
  noFill();
  stroke(255);
  strokeWeight(2);
}

float x = 0, y = 0, z = 0;
float dx = random(-5, 5), dy = random(-5, 5), dz = random(-5, 5);

void draw() {
  background(0);

  translate(width/2, height/2);
  rotateY(frameCount / 200.0);
  stroke(255);
  noFill();
  box(300);

  translate(x, y, z);
  noStroke();
  fill(x+125, y+125, z+125);
  sphere(20);
  x += dx;
  if (x > 120 || x < -120) {
    dx = - dx;
  }
  y += dy;
  if (y > 120 || y < -120) {
    dy = - dy;
  }
  z += dz;
  if (z > 120 || z < -120) {
    dz = - dz;
  }
}

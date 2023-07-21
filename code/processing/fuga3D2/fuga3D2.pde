final int side = 300;

class Ball {
  private float x, y, z;
  private float dx, dy, dz;
  private int r;
  private int explosion;
  Ball(int r) {
    x = random(-side/2+r, side/2-r);
    y = random(-side/2+r, side/2-r);
    z = random(-side/2+r, side/2-r);
    dx = random(-5, 5);
    dy = random(-5, 5);
    dz = random(-5, 5);
    this.r = r;
    explosion = 0;
  }
  void draw() {
    pushMatrix();
    noStroke();
    if (explosion > 0) {
      if (explosion % 10 > 5) {
        fill(255, 255, 0);
      } else {
        fill(0, 0, 255);
      }
      explosion--;
    } else {
      fill(x+125, y+125, z+125);
    }
    x += dx;
    if ((x > side/2-r && dx > 0) || (x < -side/2+r && dx < 0)) {
      dx = - dx;
    }
    y += dy;
    if ((y > side/2-r && dy > 0) || (y < -side/2+r && dy < 0)) {
      dy = - dy;
    }
    z += dz;
    if ((z > side/2-r && dz > 0) || (z < -side/2+r && dz < 0)) {
      dz = - dz;
    }
    translate(x, y, z);
    sphere(r);
    popMatrix();
  }
  boolean checkCollision(Ball b) {
    float d = (r + b.r) * (r + b.r);
    return (x - b.x) * (x - b.x) < d &&
      (y - b.y) * (y - b.y) < d &&
      (z - b.z) * (z - b.z) < d;
  }
  void collision(Ball b) {
    float m1 = 4.0 / 3.0 * PI * r * r * r;
    float m2 = 4.0 / 3.0 * PI * b.r * b.r * b.r;
    float a = -2.0 * m1 * m2 / (m1 + m2);
    float d = dx - b.dx;
    dx += a * d / m1;
    b.dx -= a * d / m2;
    d = dy - b.dy;
    dy += a * d / m1;
    b.dy -= a * d / m2;
    d = dz - b.dz;
    dz += a * d / m1;
    b.dz -= a * d / m2;
    explosion = b.explosion = 100;
  }
}

int[] ballr = {20, 20, 20};
Ball[] balls = new Ball[ballr.length];

void setup() {
  size(500, 500, P3D);
  background(0);
  noFill();
  stroke(255);
  strokeWeight(2);
  for (int i = 0; i < balls.length; i++) {
    while (true) {
      boolean notCollision = true;
      balls[i] = new Ball(ballr[i]);
      for (int j = 0; j < i; j++) {
        if (balls[i].checkCollision(balls[j])) {
          notCollision = false;
          break;
        }
      }
      if (notCollision) {
        break;
      }
    } 
  }
}

void draw() {
  background(0);

  translate(width/2, height/2);
  rotateY(frameCount / 200.0);
  stroke(255);
  noFill();
  box(side);
  
  for (Ball b : balls) {
    b.draw();
  }
  for (int i = 0; i < balls.length; i++) {
    for (int j = i+1; j < balls.length; j++) {
      if (balls[i].checkCollision(balls[j])) {
          balls[i].collision(balls[j]);
      }
    }
  }
}

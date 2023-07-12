final int AMOUNT = 80 * 80;

class Spin {
  private int[] x, y, z;
  private color[] c;
  private String name;
  Spin(int l, int m, String s, int n) {
    name = s;
    x = new int[AMOUNT];
    y = new int[AMOUNT];
    z = new int[AMOUNT];
    c = new color[AMOUNT];
    float theta = 0.0;
    for (int i = 0; i < 80; i++) {
      float phi = 0.0;
      for (int j = 0; j < 80; j++) {
        float S = spherical(theta, phi, l, m);
        if (l == 0) {
          if (n == 1) {
             c[i*80+j] = color(255, 0, 0);
          } else {
             if (j % 2 == 0) {
               c[i*80+j] = color(255, 0, 0);
             } else {
               c[i*80+j] = color(0, 0, 255);
             }
          }
        } else {
          if (n == 1 || S >= 0.0) {
            c[i*80+j] = color(255, 0, 0);
          } else {
            c[i*80+j] = color(0, 0, 255);
          }
        }
        float R = pow(S, 2.0) * 500;
        x[i*80+j] = int(R * sin(theta) * cos(phi));
        y[i*80+j] = int(R * sin(theta) * sin(phi));
        z[i*80+j] = int(R * cos(theta));
        phi += PI * 2 / 80;
      }
      theta += PI / 80;
    }
  }
  private float spherical(float theta, float phi, int l, int m) {
    if (l == 0) {
      if (m == 0) {
        return sqrt(1.0 / (4 * PI));
      }
    }
    if (l == 1) {
      if (m == 0) {
        return sqrt(3.0 / (4.0 * PI)) * cos(theta);
      }
      if (m == 1) {
        return sqrt(3.0 / (4.0 * PI)) * sin(theta) * cos(phi);
      }
      if (m == -1) {
        return sqrt(3.0 / (4.0 * PI)) * sin(theta) * sin(phi);
      }
    }
    if (l == 2) {
      if (m == 0) {
        return sqrt(5.0 / (16.0 * PI)) * (3.0 * pow(cos(theta), 2.0) - 1.0);
      }
      if (m == 1) {
        return sqrt(15.0 / (4.0 * PI)) * cos(theta) * sin(theta) * cos(phi);
      }
      if (m == -1) {
        return sqrt(15.0 / (4.0 * PI)) * cos(theta) * sin(theta) * sin(phi);
      }
      if (m == 2) {
        return sqrt(15.0 / (16.0 * PI)) * pow(sin(theta), 2.0) * cos(2*phi);
      }
      if (m == -2) {
        return sqrt(15.0 / (16.0 * PI)) * pow(sin(theta), 2.0) * sin(2*phi);
      }
    }
    if (l == 3) {
      if (m == 0) {
        return sqrt(7.0 / (16.0 * PI)) * (5.0 * pow(cos(theta), 3) - 3.0 * cos(theta));
      }
      if (m == 1) {
        return sqrt(21.0 / (32.0 * PI)) * sin(theta) * (5.0 * pow(cos(theta), 2) - 1.0) * cos(phi);
      }
      if (m == -1) {
        return sqrt(21.0 / (32.0 * PI)) * sin(theta) * (5.0 * pow(cos(theta), 2) - 1.0) * sin(phi);
      }
      if (m == 2) {
        return sqrt(105.0 / (16.0 * PI)) * pow(sin(theta), 2.0) * cos(theta) * cos(2*phi);
      }
      if (m == -2) {
        return sqrt(105.0 / (16.0 * PI)) * pow(sin(theta), 2.0) * cos(theta) * sin(2*phi);
      }
      if (m == 3) {
        return sqrt(35.0 / (32.0 * PI)) * pow(sin(theta), 3.0) * cos(3*phi);
      }
      if (m == -3) {
        return sqrt(35.0 / (32.0 * PI)) * pow(sin(theta), 3.0) * sin(3*phi);
      }
    }
    return 0.0;
  }
  public void draw(int i){
    stroke(c[i]);
    point(y[i], z[i], x[i]);
  }
  public void title() {
    hint(DISABLE_DEPTH_TEST);
    rotateY(-frameCount / 200.0);
    textSize(20);
    fill(255);
    text(name, 0, 200);
    noFill();
    hint(ENABLE_DEPTH_TEST);
  }
}

Spin[] spin = new Spin[16];
int cnt;
String[] names = {"s", "p y", "p z", "p x", "d xy", "d yz", "d z^2", "d zx", "d x^2-y^2",
  "f x(x^2-3y^2)", "f z(x^2-y^2)", "f xz^2", "f z^3", "f yz^2", "f xyz", "f y(y^2-3x^2)" };

void setup() {
  size(500, 500, P3D);
  background(0);
  noFill();
  stroke(255);
  strokeWeight(2);
  int i = 0;
  for (int l = 0; l < 4; l++) {
    for (int m = -l; m <= l; m++) {
      spin[i] = new Spin(l, m, names[i], 0);
      i++;
    }
  }
  cnt = 0;
}

int pattern = 0;

void draw() {
  background(0);

  translate(width/2, height/2);
  rotateY(frameCount / 200.0);

  stroke(255);
  box(300);

  Spin s = spin[pattern];
  for (int i = 0; i < AMOUNT; i++) {
    s.draw(i);
  }
  if (cnt++ > 600) {
    pattern = (pattern + 1) % 16;
    cnt = 0;
  }
  s.title();
}

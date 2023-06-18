import processing.video.*;

Capture cam;

Boolean cameraOn = true;

void setup() {
  size(640, 480);
  
  String[] cameras = Capture.list();
  for (int i = 0; i < cameras.length; i++) {
    println("[" + i + "] " + cameras[i]);
  }
  
  cam = new Capture(this, cameras[0]);
  cam.start();
}

void draw() {
  if (cam.available() == true && cameraOn) {
    cam.read();
    image(cam, 0, 0);
  }
  
  filter(THRESHOLD);
//  filter(INVERT);
//  filter(GRAY);
  
    if(!cameraOn){
        fill(0);
        if(mousePressed){
          ellipse(mouseX, mouseY, 10, 10);
        }
    }
}

void keyPressed() {
 save("/home/mcc/sketchbook/test2.jpg");
}

void mousePressed() {
//  cam.save("/home/mcc/sketchbook/test.jpg");
  save("/home/mcc/sketchbook/test.jpg");
  cameraOn = false;
}

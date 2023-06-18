import gab.opencv.*;
import processing.video.*;
import java.awt.Rectangle;

Capture cam;
OpenCV opencv;
Rectangle[] eyes;

void setup(){
  size(640, 480);
  
  String[] cameras = Capture.list();
  
  for(int i=0; i<cameras.length; i++){
    println("[" + i + "] " + cameras[i]);
  }
  
  cam = new Capture(this, cameras[0]);
  cam.start();
}

void draw(){
  if(cam.available() == true){
    cam.read();
    
    image(cam, 0, 0);
 
    opencv = new OpenCV(this, cam);
    opencv.loadCascade(OpenCV.CASCADE_EYE);
    eyes = opencv.detect();
    
    for(int i=0; i<eyes.length; i++){
      noStroke();
      fill(#ffff00);
      float x = eyes[i].x;
      float y = eyes[i].y;
      float w = eyes[i].width;
      float h = eyes[i].height;
      ellipse(x + w / 2, y + h / 2, w, h);
    }
  }
}

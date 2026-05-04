Testing the mask with color yellow [0, 255, 255] on a bright yellow-stripped lanyard. The mask filter was set to have a target zone of +-30.

![alt text](image.png)

Testing the same color mask on an orange/gold colored bag. It still detects it but not the text on it which is in dark blue.

![alt text](image-1.png)

The target area was tuned down to +-5 and this only picked up the lanyard and just barely the outline of the bag when placed together.

![alt text](image-2.png)

After using pillow to generate a bounding box, it's pretty cool to see the lanyard being detected in real time. Despite the lanyard having sections of blue, it was suprising how its able to still detect the full lanyard. 

![alt text](image-3.png)
![alt text](image-4.png)
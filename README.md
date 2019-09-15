# Image Retargetting

Uses dynamic programming to calculate minimum edge energy path (seam) in the image from one edge to the opposite edge. This seam is then removed to obtain a resized image with minimal perceptual loss of information.

### Parameters

ROOT_DIR (String) = root folder which contains the folders for the source images.  
IMAGE_NAME (String) = name of the image. (eg. image_1.jpg)  
IMAGE_MASK (String) = name of the image mask. (mask_4.jpg)  
SEAM_TYPE (String) = type of seam to compute. V - vertical, H - horizontal. (V, H)  
USE_MASK (bool) - choice use mask image

### Usage

`python run_retarget.py ROOT_DIR IMAGE_NAME IMAGE_MASK SEAM_TYPE USE_MASK`

### Results

![ScreenShot](/images/image_06.jpg "Original Image")     ![alt text](/images/image_06_with_mask.jpg "Retargetted Image")  
<pre>
                  Fig.1 - Vertical Seam Removal (Left - Original Image, Right - Retargetted Image) </pre>

![ScreenShot](/images/image_05_ori.jpg "Original Image")     ![alt text](/images/image_05.jpg "Retargetted Image")  
<pre>
                  Fig.2 - Horizontal Seam Removal (Top - Original Image, Bottom - Retargetted Image) </pre>

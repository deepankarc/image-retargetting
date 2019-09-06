import cv2
import matplotlib.pyplot as mp_plt

def plot_retarget(rtg_img, rtg_imgcolor, seamtrace_img, SEAM_TYPE):
  # seam type
  if(SEAM_TYPE == 'H'):
    H,W = rtg_img.shape
    # rotate image anticlockwise
    rtg_img = cv2.rotate(rtg_img, rotateCode=cv2.ROTATE_90_COUNTERCLOCKWISE)
    rtg_imgcolor = cv2.rotate(rtg_imgcolor, rotateCode=cv2.ROTATE_90_COUNTERCLOCKWISE)
    seamtrace_img = cv2.rotate(seamtrace_img, rotateCode=cv2.ROTATE_90_COUNTERCLOCKWISE)

  mp_plt.figure(figsize=(16,16))
  ax1 = mp_plt.subplot(1,2,1)
  mp_plt.imshow(rtg_imgcolor[:,:,[2,1,0]])
  ax1.set_title('Retargeted Color Image')
  ax2 = mp_plt.subplot(1,2,2)
  mp_plt.imshow(rtg_img, cmap='gray')
  ax2.set_title('Retargeted Grascale Image')
  
  mp_plt.figure(figsize=(8,8))
  mp_plt.imshow(seamtrace_img[:,:,[2,1,0]])
  mp_plt.title('Seam Trace')
  return rtg_imgcolor
  
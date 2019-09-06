import cv2
from retarget_image import retarget_image
from plot_retarget import plot_retarget

def process_image(image_gray, image_color, mask, NUM_REMOVE_SEAMS, SEAM_TYPE, USE_MASK):
  # seam choice
  if(SEAM_TYPE == 'V'):
    rtg_img = image_gray
    rtg_imgcolor = image_color
    if(USE_MASK):
      rtg_mask = mask
    seamtrace_img = image_color
  elif(SEAM_TYPE == 'H'):
    # rotate image clockwise
    rtg_img = cv2.rotate(image_gray, rotateCode=cv2.ROTATE_90_CLOCKWISE)
    rtg_imgcolor = cv2.rotate(image_color, rotateCode=cv2.ROTATE_90_CLOCKWISE)
    if(USE_MASK):
      rtg_mask = cv2.rotate(mask, rotateCode=cv2.ROTATE_90_CLOCKWISE)
    seamtrace_img = cv2.rotate(image_color, rotateCode=cv2.ROTATE_90_CLOCKWISE)
  else:
    raise RuntimeError('Error! Only \'V\' and \'H\' allowed.')

  # perform image retargetting
  if(not USE_MASK):
    rtg_img, rtg_imgcolor, seamtrace_img = retarget_image(
      rtg_img, rtg_imgcolor, seamtrace_img, NUM_REMOVE_SEAMS, USE_MASK)
  else:
    rtg_img, rtg_imgcolor, seamtrace_img = retarget_image(
      rtg_img, rtg_imgcolor, seamtrace_img, NUM_REMOVE_SEAMS, USE_MASK, rtg_mask)

  save_img = plot_retarget(rtg_img, rtg_imgcolor, seamtrace_img, SEAM_TYPE)
  return save_img
  
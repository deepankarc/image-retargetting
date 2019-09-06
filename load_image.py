import cv2
import matplotlib.pyplot as mp_plt

def load_image(SOURCE_IMG, MASK_IMG, ROOT_DIR, kwargs):

  if(len(kwargs) == 2):
    SEAM_TYPE = kwargs['SEAM_TYPE']
    USE_MASK = kwargs['USE_MASK']
  else:
    raise RuntimeError('Error! kwargs accepts 2 parameters only {} given.'.format(len(kwargs)))

  # load image
  image_color = cv2.imread(ROOT_DIR+SOURCE_IMG)
  image_gray = cv2.cvtColor(image_color, code=cv2.COLOR_BGR2GRAY)
  img = cv2.normalize(image_gray.astype('float'), None, alpha=0.0, beta=1.0, norm_type=cv2.NORM_MINMAX)
  H,W = image_gray.shape
  
  if(SEAM_TYPE == 'V'):
    NUM_REMOVE_SEAMS = int(W/2)
  else:
    NUM_REMOVE_SEAMS = int(H/2)

  # get mask
  if(USE_MASK):
    mask = cv2.imread(ROOT_DIR+MASK_IMG, flags=cv2.IMREAD_GRAYSCALE) / 255
    mask[mask == 1] = np.inf
  else:
    mask = None

  # show the image
  mp_plt.figure(figsize=(16,16))
  ax1 = mp_plt.subplot(1,2,1)
  mp_plt.imshow(image_color[:,:,[2,1,0]])
  ax1.set_title('Color Image')
  ax2 = mp_plt.subplot(1,2,2)
  mp_plt.imshow(img, cmap='gray')
  ax2.set_title('Grayscale Image')
  
  if(USE_MASK is True):
    mp_plt.figure(figsize=(8,8))
    mp_plt.imshow(mask, cmap='gray')
    
  return image_gray, image_color, mask, NUM_REMOVE_SEAMS

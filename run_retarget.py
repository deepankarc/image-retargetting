import numpy as np
import cv2
import matplotlib.pyplot as mp_plt
import load_image
import process_image
import sys


def main_routine(ROOT_DIR, IMAGE_NAME, IMAGE_MASK, SEAM_TYPE, USE_MASK):
	kwargs = {
	'SEAM_TYPE': SEAM_TYPE, # 1. V- Vertical, 2. H - Horizontal
	'USE_MASK': USE_MASK
	}

	image_gray, image_color, mask, NUM_REMOVE_SEAMS = load_image.load_image(IMAGE_NAME, IMAGE_MASK, ROOT_DIR, kwargs)
	rtg_image = process_image.process_image(image_gray, image_color, mask, NUM_REMOVE_SEAMS, 
						  kwargs['SEAM_TYPE'], kwargs['USE_MASK'])
	cv2.imwrite(IMAGE_NAME[:-4]+".jpg",rtg_image,[cv2.IMWRITE_JPEG_QUALITY,50])
 
if __name__ == "__main__":
	ROOT_DIR = sys.argv[1]
	IMAGE_NAME = sys.argv[2]
	IMAGE_MASK = sys.argv[3]
	SEAM_TYPE = sys.argv[4]
	USE_MASK = sys.argv[5]
	main_routine(ROOT_DIR, IMAGE_NAME, IMAGE_MASK, SEAM_TYPE, USE_MASK)
	

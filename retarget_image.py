import numpy as np
import cv2

def retarget_image(rtg_img, rtg_imgcolor, seamtrace_img, NUM_REMOVE_SEAMS, USE_MASK, rtg_mask=None):
  
  for nrs in range(NUM_REMOVE_SEAMS):
    H,W = rtg_img.shape # update image width

    # compute edge image
  #   grad_x = abs(cv2.Sobel(rtg_img, ddepth=cv2.CV_64F, dx=1, dy=0))
  #   grad_y = abs(cv2.Sobel(rtg_img, ddepth=cv2.CV_64F, dx=0, dy=1))
    grad_x = abs(cv2.filter2D(rtg_img, ddepth=cv2.CV_64F, kernel=np.asarray([[0,0,0],[-1,0,1],[0,0,0]])))
    grad_y = abs(cv2.filter2D(rtg_img, ddepth=cv2.CV_64F, kernel=np.asarray([[0,-1,0],[0,0,0],[0,1,0]])))
    # energy matrix
    if(USE_MASK):
      E_map = grad_x + grad_y + rtg_mask
    else:
      E_map = grad_x + grad_y 

    # minimum energy accumulator
    minE_accum = np.empty((H,W))
    minE_accum[0,:] = E_map[0,:] # initialise first row

    # construct energy map
    for i in range(1,H):
      for j in range(W):
        minE_accum[i,j] = E_map[i,j] + min(minE_accum[i-1, max(0, j-1)],
                                           minE_accum[i-1, j], 
                                           minE_accum[i-1, min(j+1, W-1)])

    # minimum energy at last row
    min_c = np.argmin(minE_accum[H-1,:])
    seam = [(H-1)*W + min_c]

    # remove seam with minimum energy
    for i in range(H-1,0,-1):
      # update energy
      curr_energy = minE_accum[i, min_c]

      # check energy val
      left = minE_accum[i-1, max(0, min_c-1)] + E_map[i,min_c]
      center = minE_accum[i-1, min_c] + E_map[i,min_c]
      right = minE_accum[i-1, min(min_c+1, W-1)] + E_map[i,min_c]

      if(curr_energy == left):
        min_c = max(0, min_c-1)
        seam.append((i-1)*W + min_c)
      elif(curr_energy == center):
        seam.append((i-1)*W + min_c)
      else:
        min_c = min(min_c+1, W-1)
        seam.append((i-1)*W + min_c)

    # delete seam
    seamtrace_img[np.unravel_index(np.asarray(seam), (H,W))] = 0
    rtg_img = np.delete(rtg_img, seam)
    ch_b = np.delete(rtg_imgcolor[:,:,0], seam)
    ch_g = np.delete(rtg_imgcolor[:,:,1], seam)
    ch_r = np.delete(rtg_imgcolor[:,:,2], seam)

    # reshape back into image
    rtg_img = np.reshape(rtg_img, (H,W-1))
    rtg_imgcolor = np.reshape(np.stack((ch_r,ch_g,ch_b), axis=-1), (H,W-1,3))

    # reshape mask
    if(USE_MASK):
      rtg_mask = np.delete(rtg_mask, seam)
      rtg_mask = np.reshape(rtg_mask, (H,W-1))
      
  return [rtg_img, rtg_imgcolor, seamtrace_img]
  
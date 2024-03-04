# Starter code for cmpt120imageManip.py
import cmpt120imageProjHelper

# defining variables
img = cmpt120imageProjHelper.getImage("cat.jpg")
height = len(img)
width = len(img[0])
black = cmpt120imageProjHelper.getBlackImage(width,height)

#Basic Mode
#1 Red Filter
def redFilter(pixels):
  for y in range(height):
    for x in range(width):
      r = pixels[y][x][0]
      # setting green and blue values to 0 to show only red
      black[y][x] = [r,0,0]
  return black

#2 Green Filter
def greenFilter(pixels):
  for y in range(height):
    for x in range(width):
      green = pixels[y][x][1]
      # setting red and blue values to 0 to show only green 
      black[y][x] = [0,green,0]
  return black

#3 Blue Filter
def blueFilter(pixels):
  for y in range(height):
    for x in range(width):
      blue = pixels[y][x][2]
      # setting green and blue values to 0 to show only blue
      black[y][x] = [0,0,blue]
  return black 

#4 Sepia Filter
def sepiaFilter(pixels):
  for y in range(height):
    for x in range(width):
      r = pixels[y][x][0]
      g = pixels[y][x][1]
      b = pixels[y][x][2]
      # Calculating sepia colors
      sepia_red = int((r * 0.393) + (g * 0.769) + (b * 0.189))
      sepia_green = int((r * 0.349) + (g * 0.686) + (b * 0.168))
      sepia_blue = int((r * 0.272) + (g * 0.534) + (b * 0.131))
      # Applying the sepia colors to the original colors
      sepia_red = min(sepia_red,255)
      sepia_green = min(sepia_green,255)
      sepia_blue = min(sepia_blue,255)
      black[y][x] = [sepia_red,sepia_green,sepia_blue]
  return black 

#5 warmFilter
def warmFilter(pixels):
  for y in range(height):
    for x in range(width):
      # get RGB values for image
      r = pixels[y][x][0]
      g = pixels[y][x][1]
      b = pixels[y][x][2]
      # scale up for red pixels
      if r < 64: 
        r = int(r/64*80)
      elif r >= 64 and r < 128:
        r = int((r-64)/(128-64) * (160-80) + 80)
      # scale down for red pixels  
      else:
       r = int((r - 128) / (255-128) * (255-160)+ 160)
      # scale up for blue pixels
      if b < 64:
        b = int(b/64 * 50)
      elif b >= 64 and b < 128:
        b = int((b-64) / (128-64) * (100-50) + 50)
      # scale down for blue pixels  
      else:
        b = int((b-128)/(255-128) * (255-100) + 100)
      # appling warm effect to the original   
      r = min(r,255)
      g = min(g,255)
      b = min(b,255)
      black[y][x] = [r,g,b]
  return black 

#6 Cool Filter
def coolFilter(pixels):
  for y in range(height):
    for x in range(width):
      # get RGB values for image
      r = pixels[y][x][0]
      g = pixels[y][x][1]
      b = pixels[y][x][2]
      # scale up for red pixels 
      if r < 64: 
        r = int(r/64*50)
      elif r >= 64 and r < 128:
        r = int((r-64)/(128-64) * (100-50) + 50)
      # scale down for red pixels  
      else:
       r = int((r - 128) / (255-128) * (255-100)+ 100)
      # scale up for blue pixels
      if b < 64:
        b = int(b/64 * 80)
      elif b >= 64 and b < 128:
        b = int((b-64) / (128-64) * (160-80) + 80)
      # scale down for blue pixels  
      else:
        b = int((b-128)/(255-128) * (255-160) + 160)
      black[y][x] = [r,g,b]
  return black
  
#Advanced Mode
#1 Rotate Left
def rotateLeft(pixels): 
  # create black image
  height = len(pixels)
  width = len(pixels[0])
  black1 = cmpt120imageProjHelper.getBlackImage(height,width)
  # switch x & y values and negate to rotate image 
  for y in range(len(black1)):
    for x in range(len(black1[0])):
      black1[y][x] = pixels[x][-y]
  return black1

#2 Rotate Right
def rotateRight(pixels): 
  # create black image
  height = len(pixels)
  width = len(pixels[0])
  black2 = cmpt120imageProjHelper.getBlackImage(height,width)
  # switch x & y values and negate to rotate image 
  for y in range(len(black2)):
    for x in range(len(black2[0])):
      black2[y][x] = pixels[-x][y]
  return black2

#3 Double Size
def doubleSize(pixels):
  # create black image to not replace original image
  height = len(pixels)
  width = len(pixels[0])
  new_img = cmpt120imageProjHelper.getBlackImage((2*width), (2*height))
  for y in range(height):
    for x in range(width):
      # changing size of pixels
      new_img[(2*y)][(2*x)] = pixels[y][x]
      new_img[2*y][(2*x)+1] = pixels[y][x]
      new_img[(2*y)+1][2*x] = pixels[y][x]
      new_img[(2*y)+1][(2*x)+1] = pixels[y][x]
  return new_img

#4 Half Size
def halfSize(pixels):
  # create black image to not replace original image
  height = len(pixels)
  width = len(pixels[0])
  new_img = cmpt120imageProjHelper.getBlackImage((width//2),(height//2))
  for y in range(height//2):
    for x in range(width//2):
      # find the average of 4 pixels for RGB component from original image    
      r = (pixels[(2*y)][(2*x)][0]+pixels[(2*y)+1]\
      [(2*x)+1][0]+ pixels[(2*y)][(2*x)+1][0]+pixels[(2*y)+1][2*x][0])/4
      g = (pixels[(2*y)][(2*x)][1]+pixels[(2*y)+1]\
      [(2*x)+1][1]+ pixels[(2*y)][(2*x)+1][1]+pixels[(2*y)+1][2*x][1])/4
      b = (pixels[(2*y)][(2*x)][2]+pixels[(2*y)+1]\
      [(2*x)+1][2]+ pixels[(2*y)][(2*x)+1][2]+pixels[(2*y)+1][2*x][2])/4     
      # apply averaged colours to black image
      new_img[y][x]= r,g,b
  return new_img

#5 Locate Fish
def greenBox(pixels, bottom, top, left, right):
  # creating lines for greenBox 
  for y in pixels[bottom]:
    for x in range(left, right):
      pixels[bottom][x] = [0,255,0]
    for y in pixels[top]:
      for x in range(left, right):
        pixels[top][x] = [0,255,0]
    for y in range(bottom, top):
      pixels[y][left] = [0,255,0]
    for y in range(bottom, top):
      pixels[y][right] = [0,255,0]
  return pixels

  
def locateFish(pixels):
  width = len(pixels[0])
  height = len(pixels)
  fishblack = cmpt120imageProjHelper.getBlackImage(width,height)
  # make lists to add any values within colour range
  rows = []
  columns = []

  for y in range(height):
    for x in range(width):
      fishblack[y][x] = pixels[y][x]
      #change rgb to hsv
      r = fishblack[y][x][0]
      g = fishblack[y][x][1]
      b = fishblack[y][x][2]
      hsv = cmpt120imageProjHelper.rgb_to_hsv(r,g,b)
      h = hsv[0]
      s = hsv[1]
      v = hsv[2]
      # detecting hsv values that are yellow 
      if (47 < h < 72) and s > 39 and v > 55:
        rows.append(int(y))
        columns.append(int(x))
  # creating the boundaries around the fish from greenBox function
  bottom = min(rows)
  top = max(rows)
  left = min(columns)
  right = max(columns)
  # call greenBox function to colour in pixels
  greenBox(fishblack,bottom,top,left,right)
  return fishblack

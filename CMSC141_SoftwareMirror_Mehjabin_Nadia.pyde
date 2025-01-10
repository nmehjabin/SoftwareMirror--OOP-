# Nadia Mehjabin <nm6088@bard.edu>
# Oct 21 2021
# CMSC 141
# Software Mirror


# Warm-up:

       ## def setup():
            #global img
            #size(800,600)
            #img = loadImage("cat.jpeg")        #saving Pimage to img variable
            #img.resize(width,height)
            #fill(255,0,0)
    
        ##def draw():
            #global img
            #image(img,0,0)
            #tint(255,0,0)  
            
# Software Mirror:


def setup():
    global video
    size(800, 500)
    video = loadImage("cat.jpeg")     #loading the jpg img and saving it in "video" variable
    image(video, 0, 0)
    #video.resize()     #might be necessary

def draw():
    pass
    

def keyPressed():
    global video
    if key == 'i':                  ## invert image
        image(invert(video), 0, 0)
    elif key == 'l':                ## turn the image upside down
        image(flip(video), 0, 0)
    elif key == 'z':                ## flip the image upside down
        image(flip(invert(video)), 0, 0)
    elif key == "b" :               ## adds a constant amount to each color channel, or scales each by some factor.
        image (brighten(video),0,0)
    elif key == "d" :                ## dims the image
        image (dim(video),0,0)
    elif key == "w" :                ## swaping the red, green, blue channels
        image (swap(video),0,0)
    elif key == "g" :                ## turns the image into gray scale
        image (gray(video),0,0)
    elif key == "t" :                ## turn the image into a binary black & white image
        image (threshold(video),0,0)
    elif key == "s" :                ## raising red, green channel and lowering blue channel
        image (sepia(video),0,0)
    elif key == "f" :                ## rgbsumm controlling 4 colors
        image (fairey(video),0,0)
    elif key == "y" : 
        '''My EFFECT: PIXELATION '''               ## pixelation
        for x in range(0, width, 10):
            for y in range(0, height, 10):
                c = video.get(x, y)
                fill(c)
                noStroke()
                rect(x, y, 8, 8)

    else:
        image(video, 0, 0)
        
def invert(oimg):
    ''' creates a new image by inverting oimage'''
    img = oimg.get()
    img.loadPixels()
    for idx in range(len(img.pixels)):
        px = img.pixels[idx]
        r, g, b = red(px), green(px), blue(px)
        px = color(255 - r, 255 - g, 255 - b)
        img.pixels[idx] = px
    img.updatePixels()
    return img
    
def flip(oimg):
    ''' flip the oimg upside down'''
    img = oimg.get()
    img.loadPixels()
                                       
    for i in range(img.width):
        for j in range(img.height):
            idx = j * img.width + i
            nidx = (img.height - 1 - j) * img.width + i
            if nidx < (img.width * img.height)/2 :        ## this condition is controlling when to stop swapping pixels 
                saved = img.pixels[nidx]
                img.pixels[nidx] = img.pixels[idx]
                img.pixels[idx] = saved
       
    img.updatePixels() 
    return img

def brighten(oimg):
    ''' brightening the image'''
    img = oimg.get()
    img.loadPixels()
    for idx in range(len(img.pixels)):
        px = img.pixels[idx]
        r, g, b = red(px), green(px), blue(px)
        px = color(r*2, g*2, b*2)
        img.pixels[idx] = px
    img.updatePixels()
    return img

def dim(oimg):
    '''dims the image'''
    img = oimg.get()
    img.loadPixels()
    for idx in range(len(img.pixels)):
        px = img.pixels[idx]
        r, g, b = red(px), green(px), blue(px)
        px = color((r-50), (g-50), (b-50))
        img.pixels[idx] = px
    img.updatePixels()
    return img

def swap(oimg):
    '''swaping r,g, b position'''
    img = oimg.get()
    img.loadPixels()
    for idx in range(len(img.pixels)):
        px = img.pixels[idx]
        r, g, b = red(px), green(px), blue(px)
        px = color(b,g,r)
        img.pixels[idx] = px
    img.updatePixels()
    return img

def lum(R,G,B):

  RsRGB = R/255.00
  GsRGB = G/255.00
  BsRGB = B/255.00

  if RsRGB <= 0.03928:
    R = RsRGB/12.92 

  else: 
    R = ((RsRGB+0.055)/1.055) ** 2.4
    # print(R)
  if GsRGB <= 0.03928:
    G = GsRGB/12.92 

  else:
    G = ((GsRGB+0.055)/1.055) ** 2.4
    # print(G)
  if BsRGB <= 0.03928:
    B = BsRGB/12.92 
    
  else:
    B = ((BsRGB+0.055)/1.055) ** 2.4
    # print(B)
  
  L = 0.2126 * R + 0.7152 * G + 0.0722 * B 
  # print(L)
  return L

def gray(oimg):
    '''turns the r,g,b into gray  pixels'''
    img = oimg.get()
    img.loadPixels()
    for idx in range(len(img.pixels)):
        px = img.pixels[idx]
        r, g, b = red(px), green(px), blue(px)
        l = lum(r,g,b) * 255
        px = color(l,l,l)
        img.pixels[idx] = px
    img.updatePixels()
    return img

def threshold(oimg):
    '''turns the image into binary black & white'''
    img = oimg.get()
    img.loadPixels()
    for idx in range(len(img.pixels)):
        px = img.pixels[idx]
        r, g, b = red(px), green(px), blue(px)
        l = lum(r,g,b)
        if l <= 0.5 :
            px = color(0,0,0)
        elif l > 0.5 :
            px = color (255,255,255)

        img.pixels[idx] = px
    img.updatePixels()
    return img
    
def sepia(oimg):
    ''' raises the r and g channels but lowers blue channel'''
    img = oimg.get()
    img.loadPixels()
    for idx in range(len(img.pixels)):
        px = img.pixels[idx]
        r, g, b = red(px), green(px), blue(px)
        sepiaAmount = 20
        px = color(r + (2*sepiaAmount), g + (2*sepiaAmount), b-(sepiaAmount))
        img.pixels[idx] = px
    img.updatePixels()
    return img

def fairey(oimg):
    ''' changes the color based on rgbSum conditions'''
    img = oimg.get()
    img.loadPixels()
    for idx in range(len(img.pixels)):
        px = img.pixels[idx]
        r, g, b = red(px), green(px), blue(px)
        px = color(r, g, b)
        rgbSum = r +g + b
        if 0 < rgbSum <= 181 :
            px = color (0,51,76)
        if 181 < rgbSum <= 363 :
            px = color (217,26,33)   
        if 363 < rgbSum <=545 :
            px = color (112,150,158)
        if 545 < rgbSum <= 765 :
            px = color(252,227,166)
        
        
        img.pixels[idx] = px
    img.updatePixels()
    return img





    

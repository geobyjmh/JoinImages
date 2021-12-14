from PIL import Image

COLUMNS = 4
ROWS = 3

def Main():
    imageNames = FileToList('image_list.txt')  
    imgs = OpenImages(imageNames)

    blank_img = CreateNewBlankImage(imgs, ROWS, COLUMNS)
    new_img = AddIndividualImagesToNewImage(blank_img, imgs)
    scaled_img = ResizeImage(new_img)
    scaled_img.save('NewImage.jpg')
    
def FileToList(path):
    file = open(path)
    img_names = [line.strip() for line in file]
    file.close()
    return img_names

def OpenImages(iNames):
    images = [Image.open(x) for x in iNames]
    return images

def CreateNewBlankImage(images, row, col):
    imageWidth  = images[0].size[0] * col
    imageHeight = images[0].size[1] * row
    newImage = Image.new('RGB', (imageWidth, imageHeight))
    return newImage

def AddIndividualImagesToNewImage(work_image, images):
    maxWidth = work_image.size[0]
    x = 0
    y = 0
    for img in images:
        work_image.paste(img, (x,y))
        x, y = IncXandY(x, y, img.size[0], img.size[1], maxWidth)     
    return work_image

def IncXandY(xpos, ypos, xstep, ystep, xmax):
    next_x = xpos + xstep
    next_y = ypos
    if next_x >= xmax:
        next_x = 0
        next_y = ypos + ystep
    return next_x, next_y
        

def ResizeImage(image):
    scale = 10
    width = int(image.size[0]/scale)
    height = int(image.size[1]/scale)
    resizedImage = image.resize((width, height))
    return resizedImage

    
if __name__ == '__main__':
    Main()





from simpleimage import SimpleImage


DEFAULT_FILE = 'images/mt-rainier.jpg'




def mirror_reflected(filename):
   image = SimpleImage(filename)
   width = image.width
   height = image.height

   # Create new image to contain mirror reflection
   mirror = SimpleImage.blank(width*2, height)

   for y in range(height):
      for x in range(width):
        pixel = image.get_pixel(x,y)
        mirror.set_pixel(x, y, pixel)
        mirror.set_pixel((width * 2) - (x+1), y, pixel)
   return mirror


def water_reflected(filename):
   image = SimpleImage(filename)
   width = image.width
   height = image.height

   # Create new image to contain water reflection
   water = SimpleImage.blank(width, height*2)

   for y in range(height):
      for x in range(width):
        pixel = image.get_pixel(x,y)
        water.set_pixel(x, y, pixel)
        water.set_pixel(x, (height * 2) - (y+1), pixel)
   return water

def exposure_up(filename):
    image = SimpleImage(filename)
    for pixel in image:
        pixel.red *= 10
        pixel.green *= 10
        pixel.blue *= 10
    return image

def exposure_down(filename):
    image = SimpleImage(filename)
    for pixel in image:
        pixel.red /= 10
        pixel.green /= 10
        pixel.blue /= 10
    return image

def cip_filter(filename):
    image = SimpleImage(filename)
    for px in image:
        px.red *= 1.5
        px.green *= 0.7
        px.blue *= 1.5
    return image


def detect_red(filename):
    image = SimpleImage(filename)
    for px in image:
        average = (px.red+px.green+px.blue)/3
        if px.red>=average:
            px.red=255
            px.green=0
            px.blue=0
        else:
            px.red=average
            px.green=average
            px.blue=average
    return image


def detect_blue(filename):
    image = SimpleImage(filename)
    for px in image:
        average = (px.red+px.green+px.blue)/3
        if px.blue>=average:
            px.red=0
            px.green=0
            px.blue=255
        else:
            px.red=average
            px.green=average
            px.blue=average
    return image



def detect_green(filename):
    image = SimpleImage(filename)
    for px in image:
        average = (px.red+px.green+px.blue)/3
        if px.green>=average:
            px.red=0
            px.green=255
            px.blue=0
        else:
            px.red=average
            px.green=average
            px.blue=average
    return image

def bnw(filename):
    image = SimpleImage(filename)
    for px in image:
        average = (px.red+px.green+px.blue)/3
        px.red=average
        px.green=average
        px.blue=average
    return image


def contrast(filename):
    image = SimpleImage(filename)
    px_min = 127

    for px in image:
        average = (px.red+px.green+px.blue)/3
        if average>px_min:
            px.red*=1.2
            px.blue*=1.2
            px.green*=1.2
        if average<px_min:
            px.red/=1.2
            px.blue/=1.2
            px.green/=1.2
    return image

def warm(filename):
    image = SimpleImage(filename)
    for px in image:
        px.red *= 1.5
        px.green *=1.2
        px.blue /= 1.3
    return image
    
def cold(filename):
    image = SimpleImage(filename)
    for px in image:
        px.red /= 1.2
        px.green /=1.1
        px.blue *= 1.2
    return image

def back_choices():
    print("Do you want to make more edits?")
    print("1. go back \n2. exit")
    action3 = int(input(""))
    if action3 == 1:
        print("Functions: \n1. create mirror image \n2. create water image \n3. change exposure")
        print("4. Code in Place filter \n5. Detect red \n6. Detect Green \n7. Detect Blue \n8. Black and White ")
        print("9. Contrast \n10. Warm \n11. Cold")
        choice = int(input("Choose a function for your image: "))
        #functions
        if choice == 1:
            # Show the mirror reflected image
            original = SimpleImage(filename)
            original.show()
            mirror_image = mirror_reflected(filename)
            mirror_image.show()
            

        if choice ==2:
            # Show the water reflected image
            original = SimpleImage(filename)
            original.show()
            water_image = water_reflected(filename)
            water_image.show()
            

        if choice ==3:
            # Show the mirror reflected image
            original = SimpleImage(filename)
            original.show()
            exposure_image = exposure_up(filename)
            exposure_image.show()
            


        if choice ==4:
            # Show the mirror reflected image
            original = SimpleImage(filename)
            original.show()
            cip_image = cip_filter(filename)
            cip_image.show()
            


        if choice ==5:
            # Show the mirror reflected image
            original = SimpleImage(filename)
            original.show()
            red_image = detect_red(filename)
            red_image.show()
            

        if choice ==6:
            # Show the mirror reflected image
            original = SimpleImage(filename)
            original.show()
            blue_image = detect_blue(filename)
            blue_image.show()
            

        if choice ==7:
            # Show the mirror reflected image
            original = SimpleImage(filename)
            original.show()
            green_image = detect_green(filename)
            green_image.show()


        if choice ==8:
            # Show the mirror reflected image
            original = SimpleImage(filename)
            original.show()
            bnw_image = bnw(filename)
            bnw_image.show()

        if choice ==9:
            # Show the mirror reflected image
            original = SimpleImage(filename)
            original.show()
            contrast_image = contrast(filename)
            contrast_image.show()

        if choice ==10:
            # Show the mirror reflected image
            original = SimpleImage(filename)
            original.show()
            warm_image = warm(filename)
            warm_image.show()

        if choice ==11:
            # Show the mirror reflected image
            original = SimpleImage(filename)
            original.show()
            cold_image = cold(filename)
            cold_image.show()

    if action3==2:
        return 0




def main():

    

    #welcome
    print("Welcome to Mini Photoshop")

    #choose between greenscreeen and photo editing

        #ask for back function
        #if yes:
            #go back to select channel screen


        # Get file name from user input
    filename = get_file()
    print("Functions: \n1. create mirror image \n2. create water image \n3. change exposure")
    print("4. Code in Place filter \n5. Detect red \n6. Detect Green \n7. Detect Blue \n8. Black and White ")
    print("9. Contrast \n10. Warm \n11. Cold")
    choice = int(input("Choose a function for your image: "))
    #functions
    if choice == 1:
        # Show the mirror reflected image
        original = SimpleImage(filename)
        original.show()
        mirror_image = mirror_reflected(filename)
        mirror_image.show()
        
        

    if choice ==2:
        # Show the water reflected image
        original = SimpleImage(filename)
        original.show()
        water_image = water_reflected(filename)
        water_image.show()
        

    if choice ==3:
        # Show the mirror reflected image
        original = SimpleImage(filename)
        original.show()
        exposure_image = exposure_up(filename)
        exposure_image.show()
        


    if choice ==4:
        # Show the mirror reflected image
        original = SimpleImage(filename)
        original.show()
        cip_image = cip_filter(filename)
        cip_image.show()
        


    if choice ==5:
        # Show the mirror reflected image
        original = SimpleImage(filename)
        original.show()
        red_image = detect_red(filename)
        red_image.show()
        

    if choice ==6:
        # Show the mirror reflected image
        original = SimpleImage(filename)
        original.show()
        blue_image = detect_blue(filename)
        blue_image.show()
        

    if choice ==7:
        # Show the mirror reflected image
        original = SimpleImage(filename)
        original.show()
        green_image = detect_green(filename)
        green_image.show()


    if choice ==8:
        # Show the mirror reflected image
        original = SimpleImage(filename)
        original.show()
        bnw_image = bnw(filename)
        bnw_image.show()

    if choice ==9:
        # Show the mirror reflected image
        original = SimpleImage(filename)
        original.show()
        contrast_image = contrast(filename)
        contrast_image.show()

    if choice ==10:
        # Show the mirror reflected image
        original = SimpleImage(filename)
        original.show()
        warm_image = warm(filename)
        warm_image.show()

    if choice ==11:
        # Show the mirror reflected image
        original = SimpleImage(filename)
        original.show()
        cold_image = cold(filename)
        cold_image.show()
        



  
def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

if __name__ == '__main__':
    main()
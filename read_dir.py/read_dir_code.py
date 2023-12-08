import os
import uuid

#variable for uuid
myuuid = uuid.uuid4()


def create_image_array(directory_path):
    image_array = []

    # Check if the directory exists
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        # Iterate through the files in the directory
        for filename in os.listdir(directory_path):
            # Check if the file is an image (you can add more file extensions if needed)
            if filename.lower().endswith(('.jpg')):
                # Add the image filename to the array
                image_array.append(filename)

    return image_array

   

# Replace 'path/to/your/images/directory' with the actual path to your images directory
directory_path = '/Users/kayle/Documents/Clients/LensCalc/lens-calc2/public/images/ppm'
images = create_image_array(directory_path)

#create an object class
class ppmObject:
    def __init__(self, id, ppm, img):
        self.id = id
        self.ppm = ppm
        self.img = img
       

#new array for objects
array_of_objects = []

# I have an array of images now loop through to create an array of objects
for i in images:
    id = str(myuuid)
    # name is splicated from the beginning splice_beginning = name[9:-4]
    ppm = i[9:-7]
    img = i
    new_obj = ppmObject(id, ppm, img)
    array_of_objects.append(new_obj)


# Print the resulting array of objects
for obj in array_of_objects:
        print(f'{{"id": "{obj.id}", "ppm": "{obj.ppm}", "img": "./images/ppm/{obj.img}"}},')
        
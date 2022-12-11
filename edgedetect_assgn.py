from helper_functions import *

#-----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
datafolder = "C:/Users/mvsak/OneDrive/Desktop/LP1/Programming in python/Assignments/Edge Detection/images/"
imgpath = datafolder + "1.jpg" 

#----------------------------------------STARTER CODE----------------------------------------
# Convert the color image to grayscale and returns the grayscale pixels 
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2
#
#----------------------------------------WRITE YOUR CODE HERE----------------------------------------

# Data structure to store new pixel values using list comprehension
new_pixel_values = [[0] * numb_colns for _ in range(numb_rows)]

# 3x3 Sharpen kernel for masking the image
mask = ( (-1, -1, -1), (-1, 8, -1), (-1, -1, -1) )

# Call a function get slice 2d list() (to be implemented by you),
# which takes as input the pixel values, the position of the pixel being
# calculated, and returns the 3x3 patch of surrounding pixels as a list
# of lists. 
# For example, when updating the pixel shown in Figure 2,
# calling this function from within the nested for loop should return
# neighbor pixels = [[7, 5, 4], [3, 5, 3], [2, 1, 7]].
# Use list slicing on pixel values to extract the required neighboring
# pixels. Use list comprehension to create the 2D list neighbor pixels.


# Implement a function to slice a part from the image as a 2D list
def get_slice_2d_list(pixel_values, pixel_data_1, pixel_data_2):
    """_summary_

    Args:
        pixel_values (_type_): _description_
        pixel_data_1 (_type_): _description_
        pixel_data_2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    return [pixel_values[x][pixel_data_2 - 1:pixel_data_2 + 2] for x in range(pixel_data_1 - 1, pixel_data_1 + 2)]


# Function to flatten the 2D list/tuple into 1D using list comprehension 
def flatten(flatten_input):
    """_summary_

    Args:
        flatten_input (_type_): _description_

    Returns:
        _type_: _description_
    """    
    return [j for sub_list in flatten_input for j in sub_list]

# applying flatten to neighbor pixels and mask.
flatten_mask = flatten(mask)

# For each of the pixel values, excluding the boundary values
# Create little local 3x3 box using list slicing
for i in range(1, numb_rows+1):
    """_summary_

    Args:
        numb_rows (_type_): _description_
    """    ''''''
    for j in range(1, numb_colns+1):
        """_summary_

        Args:
            numb_colns (_type_): _description_
        """        ''''''
        neighbour_pixels = get_slice_2d_list(pixel_values, i, j )
        flatten_neigh = flatten(neighbour_pixels)
        # Apply the mask
        mult_result = map(lambda x, y: x * y, flatten_neigh, flatten_mask)    
        # Sum all the multiplied values and set the new pixel value
        pixel_sum = sum(mult_result)
        new_pixel_values[i-1][j-1] = pixel_sum
#        
#----------------------------------------END YOUR CODE HERE----------------------------------------
# Verify your result
verify_result(pixel_values, new_pixel_values, mask)
# View the original image and the edges of the image
view_images(imgpath, new_pixel_values)
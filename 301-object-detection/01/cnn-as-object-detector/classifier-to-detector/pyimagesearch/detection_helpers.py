# import the necessary packages
import imutils


def sliding_window(image, step, ws):
    '''Find where in the image an object is by sliding our 
       classification window from left-to-right (column-wise)
       and top-to-bottom (row-wise)
       
       Args:
        image: The input image that we are going to loop over
                and generate windows from.
        step: Our step size, which indicates how many pixels
                we are going to “skip” in both the (x, y) directions
        ws: The window size defines the width and height (in pixels)
                of the window we are going to extract from our image  

    Returns:
        generetor the slided window (note the It's a Generator)
 
    '''
    for y in range(0, image.shape[0] - ws[1], step):
        for x in range(0, image.shape[1] - ws[0], step):
            # yield the current window
            yield (x, y, image[y:y + ws[1], x:x + ws[0]])


def image_pyramid(image, scale=1.5, minSize=(224, 224)):
    '''Find where in the image an object is by sliding our
       classification window from left-to-right (column-wise)
       and top-to-bottom (row-wise)
       
       Args:
        image: The input image for which we wish to generate
               multi-scale representations.
        scale: scale factor controls how much the image is 
               resized at each layer.
        minSize: Controls the minimum size of an output image
                 (layer of our pyramid).

    Returns:
        generetor the pydamid image (note the It's a Generator)
 
    '''
    yield image

    # keep looping over the image pyramid
    while True:
        # compute the dimensions of the next image in the pyramid
        w = int(image.shape[1] / scale)
        image = imutils.resize(image, width=w)

        # if the resized image does not meet the supplied minimum
        # size, then stop constructing the pyramid
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break

        # yield the next image in the pyramid
        yield image

from skimage.transform import risize

def resize_image(image, proportion):
    assert 0 <= proportion <= 1, "Specify a valid proportion between 0 and 1."
    height = round(image.shope[0] * proportion)
    width = round(image.shope[1] * proportion)
    image_resized = resize(image, (height, width), anti_aliasing=True)
    return image_resized
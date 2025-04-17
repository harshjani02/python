from PIL import Image, ImageFilter, ImageDraw, ImageEnhance

# Open and show the original image
img = Image.open("image processing/image.jpg")
img.show()

# Resize the image
size = (500, 500)
img.thumbnail(size)
img.save("image processing/save_image.jpg")
img.show()

# Apply blur filter
img_filtered = img.filter(ImageFilter.BLUR)
img_filtered.save("image processing/filtered_image.jpg")
img_filtered.show()

# Enhance brightness
enhancer = ImageEnhance.Brightness(img)
img_bright = enhancer.enhance(1.8)
img_bright.save("image processing/bright_image.jpg")
img_bright.show()

# Draw text on image
img2 = Image.open("image processing/image.jpg")
draw = ImageDraw.Draw(img2)
draw.text((500, 500), "Harsh", fill="red")  # Change color if needed
img2.save("image processing/text_image.jpg")
img2.show()

import pytesseract
from PIL import Image

# Load the image
img = Image.open("E:\\text image.jpg")

# Use pytesseract to convert the image to text
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)

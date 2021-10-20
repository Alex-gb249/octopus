# import module
from pdf2image import convert_from_path # pip install pdf2image
# https://pypi.org/project/pdf2image/
 
 
# Store Pdf with convert_from_path function
images = convert_from_path('pres.pdf')
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')
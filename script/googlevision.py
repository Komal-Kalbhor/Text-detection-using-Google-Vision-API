import io
import os
import glob
import pandas as pd
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="path\\to\\jsonfile\\wherecrdentialsarestored\\file.json"

# Instantiates a client
client_google = vision.ImageAnnotatorClient()

# The name of the image file to annotate
imagesFolder = 'path\\to\\images\\folder'
video_file_name = imagesFolder.rsplit("\\",1)[-1]
images = glob.glob("%s/*.jpg"%(imagesFolder)) 

cols = ['image_file_name', 'text']
df = pd.DataFrame(columns=cols, index = range(len(images)))
ind = 0
# Loads the image into memory
for image in images:
    image_file_name = image.rsplit('\\', 1)[-1]
    with io.open(image, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    # Performs text detection
    response = client_google.text_detection(image=image)
    texts = response.full_text_annotation.text
    texts = [str(texts.replace("\n",","))]
    df.loc[ind].image_file_name = image_file_name
    df.loc[ind].text = texts
    ind += 1
print(ind,"images processed")  
filename = video_file_name + "_text"+ ".csv"
filename = os.path.join(imagesFolder,filename)
df.to_csv(filename,index = False)

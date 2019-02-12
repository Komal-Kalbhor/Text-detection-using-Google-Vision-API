### Text detection in images using Google Vision API

This respository contains a python script for text detection using Google Vision API

##### [Google cloud vision](https://cloud.google.com/vision/) derives insight from the images using powerful pretrained API models

#### Requirements :
1.  Latest python version
2.  [Google Cloud Vision package](https://pypi.org/project/google-cloud-vision/)

#### Steps followed :
1.  Most important step is to [enable the Google Cloud Vision API](https://cloud.google.com/vision/docs/before-you-begin)
2.  Once the API is enabled and billing account is set you are ready to use the API in your python script.
3.  pip install google-cloud-vision
4.  Import required libraries
5.  Set the environment variable "GOOGLE_APPLICATION_CREDENTIALS" to the json file in which credentials are stored
6.  Read the input:
        - Input can be a single image or multiple images. If multiple images make sure to loop through all images.
        - Input can be a video file from which images/frames need to be captured
                - Fuction to capture frames from video using [OpenCV](https://opencv.org/)
7.  Call the text detection API passing image as input
8.  The API returns json response
9.  Read the required text from json file
10. Store rsult as CSV

##### [Full python script for text detection](script/googlevision.py)

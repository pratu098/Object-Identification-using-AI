# Object Identification AI Project Web Application
This project aims to create a django based web application for object identification using AI. The web application uses a pre-trained model to identify objects in an image uploaded by the user and outputs the names of the identified objects.

## Installation
Clone the repository to your local machine
Install the required libraries using the following command:
            
     pip install -r requirements.txt

## Usage
1. Start the web application using the following command:
      
        python.exe \manage.py runserver
                    
2. Access the web application by navigating to http://localhost:8000/imageupload in your web browser.

3. Upload an image using the "Choose File" button.

4. Click the "Submit" button to identify the objects in the uploaded image.

5. The web application will output the names of the identified objects.

## Pre-trained Model
This project uses the pre-trained model provided by Keras. The model is based on the ImageNet dataset and has been trained on over 1 million images.

## Acknowledgments
This project was inspired by the Keras documentation and the work of many researchers in the field of computer vision and deep learning. The web application was built using the Django web framework.

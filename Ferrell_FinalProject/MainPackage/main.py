'''
Name: Aaron Paulson, Spiros Yotas, Addyson Stansel, Greysen Webb
email: Paulsoar@mail.uc.edu, Yotassg@mail.uc.edu, Stansean@mail.uc.edu, Webbgp@mail.uc.edu
Assignment: Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: We will collaborate with our team to develop an eclipse application and upload a picture through eclipse
Citations:
Anything else that's relevant: 
'''
import json
from PIL import Image
from FunctionsPackage.functions import decrypt_file
from FunctionsPackage.functions import *


decrypt_file()

team_photo = team_image("CrosleyPhoto.jpg")
team_photo.show(team_photo)
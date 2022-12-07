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
def decrypt_file():
    with open('encryptedgrouphints.json')as x:
        data=json.load(x)
    #this opens up the encryptedgrouphints.json file and stores it
    reference=(data['Ferrell'])
    #this stores the data for our group in a tuple

   
    with open ('english.txt')as y:
        lines=y.readlines()
    #opens and stores the english.txt file

    for i in range(len(reference)):
        value=int(reference[i])
        #this part of the loop takes the numbers from our group's tuple
        #and puts it in a variable called value
        print(lines[value], end='')
        #this uses that number to find the word associated with the lines list

def team_image ( filename ):
    myimage = Image.open(filename)
    myimage.load()
    return myimage


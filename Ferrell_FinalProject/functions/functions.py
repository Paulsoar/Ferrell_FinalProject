'''
Created on Dec 7, 2022

@author: webbgp
'''
import json

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

# To get a list of phone numbers, you can use whatsapp web and inspect element to inspect the group members text under the group title (when you open group). Bring it in here and search and replace "," with "','" and add comma before first number and after last number to convert the numbers in to a string array format.

import os
import time
import random
phone_numbers = [
   "+94 77 678 4668","+94 78 235 8749","+94 70 288 2416","+94715146636"
]

# file = open('./names.txt','w')

for phone_number in phone_numbers:
    
    # format each number for the mudslide tool
    phone_number = phone_number.replace(' ','')
    phone_number = phone_number.replace('+','')
    
    seconds = random.randrange(30,180,30)
    
    print(seconds)

    # to make the messages seem random
    time.sleep(seconds)

    # print(phone_number)
    
    # mudslide call
    os.system(f'npx mudslide@latest send {phone_number} "test2 [automated message]"')
    
    # just checking to pass only phone numbers and not names
    # if number[0] == '9':
    #     print(number)
    # else:
    #     file.write(number)
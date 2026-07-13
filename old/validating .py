import os, datetime
from datetime import datetime

def Validating(DataInput):
        if len(DataInput) != 6:
            return False
        return True

print('write here what you want to do and when')
task = input()

print(task)

AskDeadline = input ('is there any deadline? write YES/NO').upper()
Deadline = None


if AskDeadline == 'YES':
    Deadline = True    
    DataInput = input('what is the deadline? write in ddmmyy format (only numbers)')
    #you can put if else inside if statement

print(Validating(DataInput))
print(DataInput)
print(Deadline)



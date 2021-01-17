import zlib
import sys
import time
import os
from datetime import datetime
import ctypes
from inspect import getsourcefile
from os.path import abspath
ctypes.windll.kernel32.SetConsoleTitleW("LightFile") #this is for the window title
#takes a complete path (example: C:/Users/JohnDoe/Desktop/example.txt) and removes the file name (in this case, C:/Users/JohnDoe/Desktop)

def getPath(s):

    #reverse string
    
    reversedstr = ""

    for c in reversed(s):
        reversedstr = reversedstr + c

    #remove the rest of the path, leaving only the file name

    tempfn = ""
    shouldAdd = False
    
    for c in reversedstr:
        if(shouldAdd == True):
            tempfn = tempfn + c
        if(c == '\\' or c == '/'):
            shouldAdd = True
        
        

    #reverse the file name to make it valid again

    filename = ""
    
    for c in reversed(tempfn):
        filename = filename + c
    
    
    return filename

#takes a complete path (example: C:/Users/JohnDoe/Desktop/example.txt) and returns just the file name (in this case, example.txt)

# s = string containing the path

def getFileNameFromPath(s):

    #reverse string
    
    reversedstr = ""

    for c in reversed(s):
        reversedstr = reversedstr + c

    #remove the rest of the path, leaving only the file name

    tempfn = ""
    
    for c in reversedstr:
        if(c == '\\' or c == '/'):
            break
        tempfn = tempfn + c
        

    #reverse the file name to make it valid again

    filename = ""
    
    for c in reversed(tempfn):
        filename = filename + c
    
    
    return filename
    


root_path = '/'
File_ext = ".lfc"



#if no extra arguments give the standard selection
if(len(sys.argv) == 1):
    print("Shewected taw cawmpwweshsh.\nentew de inpwut fiwe")
    path_total = input(": ")
    print("Entew de pwath taw de awutpwut fawwdew")
    output_path = input (": ")
else:
    path_total = sys.argv[1]
    output_path = getPath(sys.argv[2])

path = getPath(path_total)
file_name = getFileNameFromPath(path_total)
    

#change to the system root path

os.chdir(root_path)

#try changing to the path of the file

try:
    os.chdir(path)
except FileNotFoundError:
    print("Diwectawwnye: {0} dawesh nawt exisht!".format(path))
except NotADirectoryError:
    print("{0} ish nawt da diwectawwnye!".format(path))
except PermissionError:
    print("Yawu daw nawt have pwewmishshiawnsh taw chanwe taw {0}".format(path))

#read the file

try:
    str = open(file_name, 'rb').read()
except FileNotFoundError:
  print("Thish fiwe dawesh nawt exisht!")

start_time = time.time()

print("waw shize:", sys.getsizeof(str))

compressed_data = zlib.compress(str, 9)

#change to the output location

os.chdir(root_path)
os.chdir(output_path)

print("cawmpwpwweshed shize:", sys.getsizeof(compressed_data))

#ask for name if not automated

if(len(sys.argv) == 1):
    print("Inshewt de new cawmpwweshshed fiwe name") #if it's blank simply default it to compressed.lfc
    new_compr_fn = input(": ")
else:
    new_compr_fn = getFileNameFromPath(sys.argv[2])

if (new_compr_fn == ""):
    new_compr_fn = "cawmpwweshshed" #nothing was chosen so change the selected name to compressed, as we default do it

#create the file and write the data to it

createfile = open(new_compr_fn + File_ext, 'w')
createfile.close()
savecomp = open(new_compr_fn + File_ext, 'wb')
savecomp.write(compressed_data)
savecomp.close()

app_root_path = getPath(abspath(getsourcefile(lambda:0)))

#history file
histfileopn = "history.lfh"

os.chdir(app_root_path)
current_datetime = datetime.now()
current_time = datetime.now().time()

# creating / opening the historu.lfh file

history = open(histfileopn, 'w')
history.write(path_total)
history.close()

#delete the file if the user wants.

if(len(sys.argv) == 1):
    print("daw nyeawu want taw dewete de awwiwinaw fiwe")
    delfile = input(": ")
else:
    delfile = "n"

if (delfile == "yes" or delfile == 'y' or delfile == "Y"):
    os.chdir(output_path)
    os.remove(file_name)

# print elapsed time
elapsed_time = time.time() - start_time
print("de cawmpwweshshiawn tawawk awnwnye:", round(elapsed_time),"shec" )

#wait 10 seconds and close if not run by commandline

if(len(sys.argv) == 1):
    print("cawmpwweshshiawn shucceshshfuw apwpw wiww cwawshe in 10 shec")
    time.sleep(10)

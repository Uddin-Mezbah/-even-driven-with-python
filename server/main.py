##############################
#                            #
# MD MEZBAH UDDIN            #
# Nantong University(China)  #
# CSE                        #
#                            #
##############################

import glob
import shutil
import os
import time
 
print("\nCreating source file...Please wait...\n")
time.sleep(2)

with open('../source/some.txt', "w") as file:
    for i in range (30):
        line = f"This is line {i+1}\n"
        file.write(line)
    file. close()

print("File created successfully!\n")
time.sleep(2)

# file_path = os.path.join('./', 'display')
# os.mkdir(file_path)
isExist = os.path.exists("./display")
if not isExist:
    os.mkdir("display")
file_path = os.path.join('./', 'display')
print("Disply folder created successfully!\n")

source_path = '..\source\*'
destination_path = '..\destination'

postfix = [1, 2, 3]

while True:
    source_object = glob.glob(source_path)
    
    if len(source_object)>0:

        object_path = source_object[0]
        server_path = object_path.split('\\')[-1]

        print("objectpath", server_path)

        object_name = object_path.split('\\')[-1].split('.')
        prefix = object_name[0]
        postfix2 = object_name[1]

        print("objectname",postfix2)
        file_path = object_path
        
        if (postfix2 == 'txt'):
            lines = []
            
            with open(file_path, "r") as file:
                lines = file.readlines()
                # print(lines)
            file.close()
            i = 10

            print(" creat as zip file....please wait...\n")
            time.sleep(2)

            for item in range(len(postfix)):
                filename = prefix + '_' + str(postfix[item]) + '.' + postfix2
                # print(filename)

                new_list = lines[:i]
                with open(filename, "w") as file:
                    for line in new_list:
                        # print('=>',line)
                        file.write(line)
                file.close()
                i+=10
                # print(i,new_list)

                shutil.move(filename, f"./display/{filename}")
                shutil.make_archive('display', 'zip', "./display/")

            shutil.move('./display.zip', f"{destination_path}/")
            print("Zip file created!\n")

            shutil.unpack_archive('./../destination/display.zip', './../destination', "zip")
            print("Unpacking zip to the destination folder....please wait...\n")
            os.remove('./../destination/display.zip')
            # os.remove("../server/display.zip")

            time.sleep(3)

            print("Unpacked successfully!\n")
            os.remove(object_path)
            print("Deleted!")
            temp = glob.glob('../server/display/*')
            for f in temp:
                os.remove(f)
            # print(temp)

        elif (postfix2 == 'py'):
            
            try:
                exec(open(f'../source/{server_path}').read())
                shutil.move(filename, f"../server/{filename}")
            except Exception as e:
                print('Error ',e) 
            finally:
                os.remove(f'../source/{server_path}')



            


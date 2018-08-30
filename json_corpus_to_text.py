import os
import ijson

state = int(input("Modes: \n [1] JSON to corpus based text \n [2] JSON to document based text \n [3] Both \n Choose a converting mode: "))


if state == 1 or state == 3:
    for root, dirs, files in os.walk(os.getcwd()):
        files = [fi for fi in files if fi.endswith(".json")]
        print("Converting JSON files to corpus based text files...")
        for file_ in files:
            print("Currently processing" + " " + str(file_) + " ...")
            with open(file_, "r") as f:
                my_json = ijson.items(f, 'data.item')
                for row in my_json:
                    with open(os.path.join(os.path.splitext(file_)[0] + ".txt"), 'w') as outfile:
                        outfile.write(row['text'])


if state == 2 or state == 3:
    for root, dirs, files in os.walk(os.getcwd()):
        files = [fi for fi in files if fi.endswith(".json")]
        print("Converting JSON files to document based text files...")
        for file_ in files:
        	print("Creating folders...")
        	if not os.path.isdir(os.path.splitext(file_)[0]):
           	    os.system("mkdir " + os.path.splitext(file_)[0]) 
        for file_ in files:
            print("Currently processing" + " " + str(file_) + " ...")
            with open(file_, "r") as f:
                my_json = ijson.items(f, 'data.item')
                for row in my_json:
                    with open(os.path.splitext(file_)[0] +"/"+ os.path.splitext(row['user'])[0] + ".txt", 'a') as outfile:
                        outfile.write(row['text'])

else:
    print("Choose a valid mode. \n Process terminated.")

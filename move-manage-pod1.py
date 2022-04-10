import os
import os.path
import shutil

#move this line to be right before the moving of file
#concatinate string so that uses counter to keep proper file name
#os.path.join(save_path,a)

list_of_files=[]
i=0
#os.chdir(".")
for dirpath, dirnames, filenames in os.walk("Pod1RepoTest"):
    for filename in [f for f in filenames if f.startswith("manage")]:
        obi=dirpath
        list_of_files.append(filename)
        b=filename.split(" (")
        # save_path=r"C:\Users\capta\dev\LCSPods\FinalShowcaseGenerator\manage.py\Pod1"+r"\manage ("+str(b[1][0])+r").py"
        # firstpart=r'C:\Users\capta\dev\LCSPods\FinalShowcaseGenerator'
        save_path="C:\\Users\\capta\\dev\\LCSPods\\FinalShowcaseGenerator\\manage.py\\Pod1"+"\\manage ("+str(b[1][0])+").txt"
        firstpart='C:\\Users\\capta\\dev\\LCSPods\\FinalShowcaseGenerator\\'
        lastpart="\\manage ("+str(b[1][0])+").py"  #talk to nausher, figure way out to do it with py files

        ligma=firstpart+obi+lastpart



        #we'll do firstpart+obi+lastpart


        #could be worth adding below path to save_path
        #\manage ("+str(b[1][0])+r").py"
        #save_path=r"C:\Users\capta\dev\LCSPods\FinalShowcaseGenerator\manage.py\Pod1"

        #doesnt move the files to the desired directory when shutil is uncommented

        dest=shutil.move(ligma,save_path)
        i+=1



print(list_of_files)
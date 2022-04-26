import os
import os.path
import shutil

#move this line to be right before the moving of file
#concatinate string so that uses counter to keep proper file name
#os.path.join(save_path,a)

list_of_files=[]
i=0
#os.chdir(".")
for dirpath, dirnames, filenames in os.walk("Pod2RepoTest"):
    for filename in [f for f in filenames if f.startswith("urls") and f.endswith(".py")]:
        obi=dirpath
        list_of_files.append(filename)
        b=filename.split(" (")
        print(b)
        print(b[1])
        a=b[1].split(')')
        print(a[0]) 
            
        # save_path=r"C:\Users\capta\dev\LCSPods\FinalShowcaseGenerator\manage.py\Pod1"+r"\manage ("+str(b[1][0])+r").py"
        # firstpart=r'C:\Users\capta\dev\LCSPods\FinalShowcaseGenerator'
       

        #uncomment

        save_path="C:\\Users\\capta\\dev\\LCSPods\\FinalShowcaseGenerator\\urls.py\\Pod2"+"\\urls ("+str(b[1][0])+").txt"
        firstpart='C:\\Users\\capta\\dev\\LCSPods\\FinalShowcaseGenerator\\'
        lastpart="\\urls ("+(a[0])+").py"  #talk to nausher, figure way out to do it with py files

        ligma=firstpart+obi+lastpart

        #uncomment



        #we'll do firstpart+obi+lastpart


        #could be worth adding below path to save_path
        #\manage ("+str(b[1][0])+r").py"
        #save_path=r"C:\Users\capta\dev\LCSPods\FinalShowcaseGenerator\manage.py\Pod1"

        #doesnt move the files to the desired directory when shutil is uncommented

        #uncomment

        dest=shutil.move(ligma,save_path)
        i+=1
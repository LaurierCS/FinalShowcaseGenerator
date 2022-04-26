import os
import os.path
i=1
for dirpath, dirnames, filenames in os.walk("Pod2RepoTest"):
    for filename in [f for f in filenames if (f.endswith(".py") and f.startswith("urls"))]:
        a=(os.path.join(dirpath, filename))
        print(a)
        b=a.split(".py")
        name_of_file=b[0]+" ("+str(i)+").py"
        os.rename(a,name_of_file)
        i+=1
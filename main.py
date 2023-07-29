import os

def display(directory):
    import os 
    
    for file in os.listdir(directory):
        s = os.path.splitext(file)
        print(s)
        
        file_path = os.path.join(directory, file)

        if os.path.isdir(file_path) and file[0] != '.':

            print(file)
            path = directory + "/" + file
            
            display(path)


def recfolder(inp, directory, record,):
    
    def chunkin(word, otword):
        counts = 0
        half = len(word) / 2
        for i in range(1, len(otword)):
            if otword[:i] in word:
                counts += 1
                
        if counts >= (half+2):
            return True
        else: 
            return False
    
    
    import os


    found = False 
    if not found:
        for file in os.listdir(directory):

            s = os.path.splitext(file)
            
            if s[0] == inp:
                end_path = directory + "/" + file
                
                print()
                print(f"Found {file} in Directory:   {end_path}")
                print(f"Go to: {directory}")
                print()
                found = True
                
                
            elif chunkin(inp, s[0] ) == True:
                if "." not in file:
                    record.append(file + " (folder)")
                else:

                    record.append(file)
        
            if found == False:
                file_path = os.path.join(directory, file)

                if os.path.isdir(file_path) and file[0] != '.':

                    path = directory + "/" + file
                    
                    recfolder(inp, path, record)
                    
   
    record = sorted(record)
    
    if len(record) > 0:
        return "Other Files Close To File: ", record
    elif len(record) == 0:
        return "File Not Found"




print(f"Current Directory: {os.getcwd()}")

inpy = input("What would you like to do (for display enter display and the directory)(for find input, find, name, and directory): ")
opt = inpy.split(" ")


storage = []

if opt[0] == "display":
  if opt[1] == "current":
    display(os.getcwd())
  else:
    display(opt[1])
elif opt[0] == "find":
  if opt[2] == "current":  
    print(recfolder(opt[1], os.getcwd(), storage))
  else:
    print(recfolder(opt[1], opt[2], storage))
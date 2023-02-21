import os

def read_data(dataFile):
    time = []
    displacement = []
    moment = []
    f = open(dataFile,'r')
    for i in range(16):
        f.readline() # skip unnecessary 19 lines
    aLine = f.readline()
    #print(aLine)
    myStr = aLine
    myStr = myStr.replace('\n', '').split(' ')
    #print(myStr)
    x = float(myStr[2])
    y = float(myStr[3])
    z = float(myStr[4])
    print(x,y,z)


def list_file():
    
    file_path=os.getcwd()+r"/"
    file_list = []
    for i in range(1,200,2):
        afile = file_path+str(i+1)+r"/uniform/sixDoFRigidBodyMotionState"
        file_list.append(afile)
    #print(file_list)
    return file_list


f_list=list_file()
#exit()
for aFile in f_list:
    read_data(aFile)
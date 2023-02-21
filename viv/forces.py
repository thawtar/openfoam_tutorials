


def read_data(dataFile):
    time = []
    Fx = []
    Fy = []
    Fz = []
    moment = []
    f = open(dataFile,'r')
    for i in range(4):
        f.readline()
    lineNo = 1
    for line in f:
        
        myStr = line
        myStr = myStr.replace('\n','').split(' ')
       
        data =[]
        for item in myStr:
            if(item != ''):
                data.append(item)
        #print(data)
    
        time.append(float(data[0]))
        Fx.append(float(data[1]))
        Fy.append(float(data[2]))
        Fz.append(float(data[3]))
        lineNo = lineNo+1
    #print(time, Fx,Fy,Fz)
    return (time, Fx,Fy,Fz)


def writeData(data,file="testOutput.CSV"):
    (t,Fx,Fy,Fz) = data
    output = open(file,"w")
    for i in range(len(t)):
        outStr = str(t[i])+","+str(Fx[i])+","+str(Fy[i])+","+str(Fy[i])+"\n"
        output.write(outStr)
    output.close()


fileName = "force.dat"
outfile = fileName[:-4]+"out.CSV"
(time, Fx,Fy,Fz) = read_data(fileName)
writeData((time,Fx,Fy,Fz),outfile)
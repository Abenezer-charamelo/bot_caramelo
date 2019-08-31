def rd_updd(file):
    opp=open(file,"r")
    lst=opp.read()
    opp.close()
    return(lst)
def loging(logfile,file):
    opp=open(logfile,"a")
    opp.write(rd_updd("{}".format(file)))
    opp.write("\n")
    opp.close()
def wr_updd(file,txt):
    opp=open(file,"w")
    opp.write(txt)
    opp.close()
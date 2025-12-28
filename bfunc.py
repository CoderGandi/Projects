#Function1
def matchplayers(players):
    with open("BadmintonSysPaper.txt","w") as b:
        pass
    try:
        players=players[1:-1].split(",")
    except:
         pass
    for i in players:
        for j in players:
            if i==j:
                continue
            else:
                with open("BadmintonSysPaper.txt","a") as b:
                    b.write(f"{i} vs {j}\n")
    print("Go to the file")
#Function2
def Decrypt(code):
    code=code[1:]
    code=code[::-1]
    dct={'8':"h",'5':"e",'9':"r",'6':"o"}
    corr=''
    for i in code:
        corr=str(dct[i])+corr
    return corr
#Function3
def pointcount(tallies):
     dct2={}
     for i in tallies:
         dct2[i]=dct2.get(i,0)+1
     return dct2
#Function4
def announce(result):
    use=dict(sorted(result.items(),key=lambda item:item[1],reverse=True))
    for i,j in use.items():
       with open("BadmintonSysPaper2.txt","a") as x:
           x.write(f"{i} with {j} points\n")
    print("Go to the file")
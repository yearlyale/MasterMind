import random

def resolver():
    gam = 1
    inte = 0
    z = 0
    while gam == 1:
        B=[]
        P=[]
        F1=[]
        F2=[]
        F3=[]
        F4=[]
        c1=0
        c2=0
        c3=0
        c4=0
        re1=0
        re2=0
        re3=0
        con=0
        while con==0:
            if P[0]==P[1]:
                re1=re1+1
            if P[0]==P[2]:
                re1=re1+1
            if P[0]==P[3]:
                re1=re1+1
            if P[0]!=P[1]:
                if P[1]==P[2]:
                    re2=re2+1
                if P[1]==P[3]:
                    re2=re2+1
            if P[1]!=P[2]:
                if P[2]==P[3]:
                    re3=re3+1
            for i in range(len(B)):
                if P[0]==B[i]:
                    if i==0:
                        c1=1
                    else:
                        if c1!=1:
                            c1=2
                elif c1!=2 and c1!=1:
                    c1=3
                if P[1]==B[i]:
                    if i==1:
                        c2=1
                    else:
                        if c2!=1:
                            c2=2
                elif c2!=2 and c2!=1:
                    c2=3
                if P[2]==B[i]:
                    if i==2:
                        c3=1
                    else:
                        if c3!=1:
                            c3=2
                elif c3!=2 and c3!=1:
                    c3=3
                if P[3]==B[i]:
                    if i==3:
                        c4=1
                    else:
                        if c4!=1:
                            c4=2
                elif c4!=2 and c4!=1:
                    c4=3
            
            reps=0
            for i in range(len(B)):
                if re1>=1:
                    for q in range(len(B)):
                        if P[0]==B[q]:
                            reps=reps+1
                    if reps<re1:
                        if P[0]==P[1]:
                            if c1<c2:
                                if c2!=1:
                                    c2=3
                            else:
                                if c1!=1:
                                    c1=3
                        if P[0]==P[2]:
                            if c1<c3:
                                if c3!=1:
                                    c3=3
                            else:
                                if c1!=1:
                                    c1=3
                        if P[0]==P[3]:
                            if c1<c4:
                                if c4!=1:
                                    c4=3
                            else:
                                if c1!=1:
                                    c1=3
                reps=0
                if re2>=1 or P[0]==P[1]:
                    for q in range(len(B)):
                        if P[1]==B[q]:
                            reps=reps+1
                    if reps<re2:
                        if P[1]==P[2]:
                            if c2<c3:
                                if c3!=1:
                                    c3=3
                            else:
                                if c2!=1:
                                    c2=3
                        elif P[1]==P[3]:
                            if c2<c4:
                                if c4!=1:
                                    c4=3
                            else:
                                if c2!=1:
                                    c2=3
                reps=0
                if re3>=1 or P[1]==P[2]:
                    for q in range(len(B)):
                        if P[2]==B[q]:
                            reps=reps+1
                    if reps<re3:
                        if P[2]==P[3]:
                            if c3<c4:
                                if c4!=1:
                                    c4=3
                            else:
                                if c3!=1:
                                    c3=3
                                
            if c1==3 or c1==2:
                F1.append(P[0])
        
            if c2==3 or c2==2:
                F2.append(P[1])
                
            if c3==3 or c3==2:
                F3.append(P[2])
        
            if c4==3 or c4==2:
                F4.append(P[3])
                
            print(P)        
            print(c1,c2,c3,c4)
            z=c1+c2+c3+c4
            if z!=4:
                if c1!=1:
                    r=0
                    while r==0:
                        cont=0
                        P1=random.randint(0, 7)
                        for i in range(len(F1)):
                            if P1==F1[i]:
                                cont=cont+1
                        if cont<1:
                            r=1
                        if cont==8:
                            r=1
                    P[0]=P1
                
                if c2!=1:
                    r=0
                    while r==0:
                        cont=0
                        P2=random.randint(0, 7)
                        for i in range(len(F2)):
                            if P2==F2[i]:
                                cont=cont+1
                        if cont<1:
                            r=1
                        if cont==8:
                            r=1
                    P[1]=P2
                    
                if c3!=1:
                    r=0
                    while r==0:
                        cont=0
                        P3=random.randint(0, 7)
                        for i in range(len(F3)):
                            if P3==F3[i]:
                                cont=cont+1
                        if cont<1:
                            r=1
                        if cont==8:
                            r=1
                    P[2]=P3
                    
                if c4!=1:
                    r=0
                    while r==0:
                        cont=0
                        P4=random.randint(0, 7)
                        for i in range(len(F4)):
                            if P4==F4[i]:
                                cont=cont+1
                        if cont<1:
                            r=1
                        if cont==8:
                            r=1
                    P[3]=P4
                
            
            if z==4:
                print("gano")
                print(B)
                print(P)
                con=1
            else:
                inte=inte+1
            print("intento",inte)
            if inte==10:
                con=1
        inte=0
        w=int(input("desea repetir 1/si 0/no"))
        gam=w

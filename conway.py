def conway(n=0):
    if n == 0:
        return 'Provide number'
    else:
        u="1"
        v=""
        w=""
        for k in range(n-1):
            print("Traitement n°",k+1,"/",n," ...")
            counted = u[0]
            v=""
            many=0
            i=0
            can = True
            while can and u[i] == counted:
                many=many+1
                if len(u)<=i+1:
                    can = False
                else:
                    i=i+1
                if u[i] != counted:
                    w=w+str(many)
                    w=w+str(counted)
                    counted=u[i]
                    many=0
            for i in range(len(w)):
                v=v+str(w[i])
            w=""
            v=v+str(many)
            v=v+str(counted)
            u=""
            for i in range(len(v)):
                u=u+str(v[i])
    return u
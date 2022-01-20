#크로아티아 알파벳
A=input()
def fi(v):
    global A
    if v in A:
        A=A.replace(v," ")
        return A
    else:
        return A
fi('c=')
fi('c-')
fi('dz=')
fi('d-')
fi('lj')
fi('nj')
fi('s=')
fi('z=')
print(len(A))

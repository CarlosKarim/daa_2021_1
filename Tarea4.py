def ejemplo4(n):
    count=0
    i=n
    print("nivel 1")
    while i>=1:
        count += 1
        i=i//2
        print("nivel 2")
    basura =3+2
    print(count)
    return count

ejemplo4(7)
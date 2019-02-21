print("----Latihan 2---")
print("menampilkan bilangan berhenti ketika bilangann 0 dan menampilkan bilangan terbersar")

max=0
while True:
    a=int(input("masukan bilangan: "))
    if max < a :
        max = a
    if a==0:
        break
print("bilangan terbesar adalah = ",max)

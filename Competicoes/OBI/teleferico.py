# 100/100

# c -> capacidadeViagem | a -> totalAlunos
c = int(input())
a = int(input())

if(a%(c-1) == 0):
    print(int(a/(c-1)))
else:
    print(int((a/(c-1))+1))

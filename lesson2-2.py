
st = []

n = int(input("Введите количество элементов списка : "))
i=0
for i in range(0, n):
    ele = int(input())
    st.append(ele)
print(st)

j = 0

for i in range(int(len(st) / 2)):
    st[j], st[j + 1] = st[j + 1], st[j]
    j += 2

print(st)
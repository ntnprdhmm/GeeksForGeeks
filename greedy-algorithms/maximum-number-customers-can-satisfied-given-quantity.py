n, total = map(int, input().split())
size_a, size_b = map(int, input().split())

# calculate the rice quantity each customer wants
customers = [0] * n
for i in range(n):
    x, y = map(int, input().split())
    customers[i] = (str(i+1), x*size_a + y*size_b)
# sort by wanted quantity
customers.sort(key=lambda x: x[1])
# check how many customers we can satisfy
i = 0
while i < n and total >= customers[i][1]:
    total -= customers[i][1]
    i += 1
print(i)
print(' '.join(customers[j][0] for j in range(i)))

def generator():
	i = 0
	while i < 10:
		yield i 
		i += 1

gene = generator()

print(gene.__next__())
print(gene.__next__())
print(gene.__next__())
print(gene.__next__())
print(gene.__next__())
print(gene.__next__())
print(gene.__next__())
print(gene.__next__())
print(gene.__next__())
print(gene.__next__())


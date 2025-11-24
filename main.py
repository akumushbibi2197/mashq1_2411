#1-misol
import random
print(random.randint(1, 100))

#2-misol
print(random.random())

#3-misol
fruits = ["olma", "banan", "gilos", "shaftoli"]
print(random.choice(fruits))

#4-misol
even_number = random.randrange(2, 51, 2)
print(even_number)

#5-misol
numbers = [random.randint(1, 100) for _ in range(5)]
print(numbers)

#6-misol
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)

#7-misol
selected = random.sample(range(1, 11), 3)
print(selected)

#8-misol
print(random.choice(["yutdingiz", "yutqazdingiz"]))

#9-misol
num = random.choice([i for i in range(100, 201) if i % 5 == 0])
print(num)

#10-misol
color = random.choice(["qizil", "yashil", "ko'k"])
print(color)

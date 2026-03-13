## Multiple Choice Questions

### Question 1

What will be printed?

```python
numbers = [10, 20, 30, 40]
numbers.remove(20)
numbers.append(50)
print(numbers[1:3])
```

A. [20, 30]  
B. [30, 40]  
C. [30, 40, 50]  
D. [10, 30, 40]

---

### Question 2

What will be printed?

```python
count = 1

while count <= 3:
    print(count)
    count = count + 1
```

A.
```
1
2
3
```

B.
```
1
2
3
4
```

C.
```
0
1
2
3
```

D.
```
1
1
1
```

---

### Question 3

What will be printed?

```python
score = 75

if score >= 90:
    print("A")
elif score >= 70 and score < 90:
    print("B")
else:
    print("C")
```

A. A  
B. B  
C. C  
D. Nothing

---

## Programming Task

### Dice Game

Write a program that simulates rolling a dice.

Each round, the program should:

1. Generate a random number between **1 and 6** using `random.randint()`
2. Print the number
3. If the number is **6**, print `"Jackpot!"`

The game continues **while the number is not 6**.

Example output:

```
Roll: 2
Roll: 5
Roll: 3
Roll: 6
Jackpot!
```

Hint:

- Use a `while` loop
- Use `random.randint(1, 6)`
- Use `if` to check if the number is 6

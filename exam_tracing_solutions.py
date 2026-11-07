# ==============================================================
# TU CN101 - Final Exam Practice & Tracing Solutions
# ทดสอบรันและดูผลลัพธ์ของข้อสอบ Tracing ทุกข้อ
# ==============================================================

print("=== Q1: Tuple & List Slicing ===")
my_list = [10, 50, 30, 5, 7]
your_list = tuple(my_list[3:]) * 3
print("your_list =", your_list)
print("min & max =", min(my_list), max(your_list))
# Output: (5, 7, 5, 7, 5, 7) \n 5 7

print("\n=== Q2: 2D List Modification ===")
numbers = [[1, 5], [6, 7]]
numbers[0][0] = 9
numbers[1][1] = 10
print("numbers =", numbers)
# Output: [[9, 5], [6, 10]]

print("\n=== Q3: String split & append ===")
list1 = "aa bb cc".split()
list1.append("xx")
list1[0] = "k"
print("list1 =", list1)
# Output: ['k', 'bb', 'cc', 'xx']

print("\n=== Q4: Delimiter split & int ===")
temp = "10:20"
words = temp.split(":")
first = int(words[0])
second = int(words[1])
print("sum =", first + second)
# Output: 30

print("\n=== Q5: Default & Keyword Arguments ===")
def do_something(total, rate=0.8):
    return total + 5 * rate

print(do_something(10))
print(do_something(10, 0.1))
print(do_something(rate=0.3, total=5))
# Output: 14.0, 10.5, 6.5

print("\n=== Q6: Variable Scope (Local vs Global) ===")
my_string = "Hello"
def do_another():
    my_string = "Hello There"
    my_string = my_string[7:]
    print("inside:", my_string * 3)

do_another()
print("outside:", my_string)
# Output: hereherehere \n Hello

print("\n=== Q7: Dictionary Update ===")
my_dict = {'Alice': 10, 'Bob': 20, 'Chris': 30}
my_dict['Pat'] = 50
my_dict['Alice'] = 99
print("my_dict =", my_dict)
# Output: {'Alice': 99, 'Bob': 20, 'Chris': 30, 'Pat': 50}

print("\n=== Q8: List Comprehension with condition ===")
list_c = [(t // 2) for t in range(7) if t % 2 == 0]
print("sum =", sum(list_c))
print("list_c =", list_c)
# Output: 6 \n [0, 1, 2, 3]

print("\n=== Q9: DNA Frequency Dictionary Counter ===")
dna = "A C C T T G C C"
dna_list = dna.split(" ")
dna_dict = {}
for g in dna_list:
    dna_dict[g] = dna_dict.get(g, 0) + 1
print("dna_dict =", dna_dict)
# Output: {'A': 1, 'C': 4, 'T': 2, 'G': 1}

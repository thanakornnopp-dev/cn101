# 🎓 TU CN101 (2568/1) Final Exam Master Study Portal & Recap Vault
> คลังสรุปเนื้อหาเตรียมสอบ Final วิชา **CN101: Introduction to Computer Programming**  
> คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์ (TSE)  
> อาจารย์ผู้สอน: อ.ดร.ณัฐชนน ยงเสถียรโชติ (อ.นัท)

---

## 📌 ข้อมูลสำคัญการสอบ Final
* **วัน-เวลาสอบ:** วันพุธที่ 27 พฤศจิกายน 2568 เวลา 13:00 - 16:00 น.
* **สัดส่วนคะแนน:** **45%** (สูงที่สุดในรายวิชา)
* **รูปแบบการสอบ:** ข้อสอบเขียนตอบและเขียนโค้ดด้วยลายมือลงบนกระดาษ (Handwritten Exam)
  1. **Part 1:** Code Tracing / ทายผลลัพธ์ Output & เติมคำในช่องว่าง
  2. **Part 2:** Short Programming (เขียนฟังก์ชันย่อย 1 ฟังก์ชัน)
  3. **Part 3:** Long Programming (เขียนโปรแกรมเต็มตามขั้นตอน Pseudocode แบ่งเป็น 3 ฟังก์ชัน)

---

## 🌐 เข้าชมหน้าเว็บ Study Portal & Interactive Quiz
👉 **[คลิกเพื่อเปิดเว็บพอร์ทัลสรุปเนื้อหาและทดลองทำข้อสอบ (GitHub Pages)](https://thanakornnopp-dev.github.io/cn101/)**  
*(หรือเปิดไฟล์ `index.html` บนเครื่องเบราว์เซอร์ได้ทันที)*

---

## 📑 สรุปหัวข้อเนื้อหาหลัง Midterm ทั้งหมด (สิ่งที่ออกสอบ)

### 1. List 2, 2D Lists & List Comprehension
* **Slicing เชิงลึก:** `list[start:stop:step]` (เช่น `list[-3:]`, `list[::-1]`)
* **2D List:** การเข้าถึงสมาชิกแถวและหลัก `matrix[row][col]` และการซ้อน Nested Loop
* **List Comprehension:** ยุบ Loop ให้เหลือบรรทัดเดียว
  * แบบมี `if`: `[exp for x in iterable if condition]`
  * แบบมี `if-else`: `[exp1 if condition else exp2 for x in iterable]`

### 2. Functions (ฟังก์ชันและการส่งผ่านค่า)
* **การนิยามและการคืนค่า:** `def func_name(params):` และ `return value` (ถ้าไม่มี return จะได้ `None`)
* **Scope ของตัวแปร:** Local Variables ในฟังก์ชันมองไม่เห็นจากภายนอก และการส่งค่าตัวแปรพื้นฐานเป็นแบบ *Pass by Value*
* **Default & Keyword Arguments:** พารามิเตอร์เริ่มต้นต้องอยู่ท้ายสุด และสามารถส่งค่าแบบระบุชื่อได้สลับที่ได้
* **Multiple Return Values:** คืนค่าหลายตัวคั่นด้วยจุลภาค `return a, b` รับค่าด้วย `x, y = func()`
* **โมดูลมาตรฐาน:**
  * `import math`: `math.pi`, `math.sqrt()`, `math.hypot()`, `math.radians()`, `math.cos()`
  * `import random`: `random.seed(100)`, `random.randint(min, max)`, `random.uniform(a, b)`

### 3. Tuples & Strings
* **Immutability:** แก้ไขค่าสมาชิกใน Tuple และ String โดยตรงไม่ได้ (`t[0] = 1` จะเกิด Error)
* **String Methods ยอดฮิต:**
  * `.split(delimiter)`: แยกข้อความออกเป็น List of Strings
  * `delimiter.join(list)`: รวม List กลับเป็น String
  * `.upper()`, `.lower()`, `.strip()`, `.isdigit()`, `.replace()`
* **Slicing & Repetition:** `"hello"[1:4]` ได้ `'ell'`, `(1, 2) * 3` ได้ `(1, 2, 1, 2, 1, 2)`

### 4. Dictionaries (ดิกชันนารี & การนับความถี่)
* **โครงสร้าง Key-Value:** `{key: value}` คีย์ต้องไม่ซ้ำและเป็น Immutable
* **การเพิ่ม/แก้ข้อมูล:** `dict[key] = value`
* **การดึงค่าอย่างปลอดภัย:** `dict.get(key, default)` ไม่เกิด KeyError
* **Frequency Counting Pattern (ออกสอบชัวร์):**
  ```python
  d[item] = d.get(item, 0) + 1
  ```

---

## 🔗 สารบัญคลิปสอน, สไลด์ PDF และ Colab ทางการของ อ.นัท

| วันที่ | หัวข้อ | คลิปวิดีโอ (YouTube) | สไลด์ PDF | Colab Lab & Sol |
| :--- | :--- | :---: | :---: | :---: |
| 3 ต.ค. | **List 2 (2D Lists & Comprehension)** | [▶ ชมคลิป](https://youtu.be/42R3DX_gWWA) | [📄 PDF](https://github.com/yongsa-nut/TU_CN101_68-1/blob/main/List%202%20lecture%20note.pdf) | [💻 Colab Sol](https://colab.research.google.com/github/yongsa-nut/TU_CN101_68-1/blob/main/List_Lab_2568_(sol).ipynb) |
| 10 ต.ค. | **Function 1 (Intro & Calling)** | [▶ ชมคลิป](https://youtu.be/EW8Se1asaCQ) | [📄 PDF](https://github.com/yongsa-nut/TU_CN101_68-1/blob/main/fuction1.pdf) | [💻 Colab Sol](https://colab.research.google.com/github/yongsa-nut/TU_CN101_68-1/blob/main/Function_Lab_1_2568_(sol).ipynb) |
| 17 ต.ค. | **Function 2 (Args, Returns, Modules)** | [▶ ชมคลิป](https://youtu.be/EDPc4dfZEdE) | [📄 PDF](https://github.com/yongsa-nut/TU_CN101_68-1/blob/main/Function%202.pdf) | [💻 Colab Sol](https://colab.research.google.com/github/yongsa-nut/TU_CN101_68-1/blob/main/Function_Lab_2_2568_(sol).ipynb) |
| 24 ต.ค. | **Tuple & String** | [▶ ชมคลิป](https://youtu.be/k_aayrn2e9Y) | [📄 PDF](https://github.com/yongsa-nut/TU_CN101_68-1/blob/main/Tuple%20%26%20String.pdf) | [💻 Colab Sol](https://colab.research.google.com/github/yongsa-nut/TU_CN101_68-1/blob/main/String_Lab_2568_(sol).ipynb) |
| 31 ต.ค. | **Dictionary** | [▶ ชมคลิป](https://youtu.be/ANXtNcAAynY) | [📄 PDF](https://github.com/yongsa-nut/TU_CN101_68-1/blob/main/Dictionary.pdf) | [💻 Colab Sol](https://colab.research.google.com/github/yongsa-nut/TU_CN101_68-1/blob/main/Dictionary_Lab_2568_(sol).ipynb) |
| 12 พ.ย. | **Final Recap (สรุปเนื้อหาเตรียมสอบ)** | [▶ ชมคลิป](https://youtu.be/X0o3CY5D2hM) | [📄 PDF](https://github.com/yongsa-nut/TU_CN101_68-1/blob/main/Final%20Recap.pdf) | [💻 Colab Sol](https://colab.research.google.com/github/yongsa-nut/TU_CN101_68-1/blob/main/Final_Recap_Lab_CN101_2568_(sol).ipynb) |
| 19 พ.ย. | **Final Prep 1 (ติวข้อสอบบนกระดาษ)** | [▶ ชมคลิป](https://youtu.be/4C7RcvBPH9M) | - | - |
| 21 พ.ย. | **Final Prep 2 (ติวข้อสอบบนกระดาษ)** | [▶ ชมคลิป](https://youtu.be/7P7EfdXYMqE) | - | - |

---

## 🎯 ตัวอย่างโค้ดข้อสอบใหญ่ (Long Programming - Linear Function)
```python
import random

def gen_data(w, b, n):
    X = []
    Y = []
    for i in range(n):
        x = random.randint(1, 8)
        y = w * x + b
        X.append(x)
        Y.append(y)
    return X, Y

def sum_squared_diff(X, Y):
    total_X = 0
    total_Y = 0
    for i in range(len(X)):
        total_X += X[i] ** 2
        total_Y += Y[i] ** 2
    return total_X, total_Y, total_X - total_Y

def main():
    random.seed(100)
    w = float(input('Enter w: '))
    b = float(input('Enter b: '))
    n = int(input('Enter n: '))
    X, Y = gen_data(w, b, n)
    X_ss, Y_ss, XY_diff = sum_squared_diff(X, Y)
    print(f"SSX = {X_ss}, SSY = {Y_ss}, Diff = {XY_diff}")

if __name__ == '__main__':
    main()
```

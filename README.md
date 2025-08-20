

# 🔐 PyEncode

**PyEncode** is a lightweight Python tool that **encodes your Python scripts** using **Base64** and generates a new `.py` file that can be executed normally.  
No external libraries required — just **Python 3**.

---

## 🚀 Features
- ✅ Encode Python scripts using **Base64**
- ✅ Generates a **self-contained executable Python file**
- ✅ No external libraries required
- ✅ Simple and lightweight

---

## 📥 Installation

```bash
git clone https://github.com/quadra-v69/pyencode.git
cd pyEncode
````

> **Note:** You must have **Python 3** installed.

---

## 🛠️ Usage

```bash
python3 pyEncode.py
```

* The script will ask for the path of your Python file.
* It will generate a new **encoded** `.py` file.
* Run the encoded file like a normal Python script.

---

## 📌 Example

### Original Script (`hello.py`)

```python
def greet():
    print("Hello, World!")

greet()
```

### After Encoding

PyEncode generates a file like:

```python
import base64
exec(base64.b64decode(
    b'ZGVmIGdyZWV0KCk6CiAgICBwcmludCgiSGVsbG8sIFdvcmxkISIpCmdyZWV0KCk='
))
```

Running this encoded script will give the same output:

```bash
python3 hello_encoded.py
# Output:
Hello, World!
```

---

## 👤 Developer

**Rantu** aka **Quadra\_v69**

* 🌐 **GitHub**: [github.com/quadra-v69](https://github.com/quadra-v69)
* 📷 **Instagram**: [instagram.com/reflame.x](https://instagram.com/reflame.x)
* 🐦 **X (Twitter)**: [x.com/quadra\_v69](https://x.com/quadra_v69)
* 💼 **LinkedIn**: [linkedin.com/in/rantu-dev](https://linkedin.com/in/rantu-dev)

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes** and **code protection** only.
The developer is **not responsible** for any misuse.




```

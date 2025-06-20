j# 🎲 Flask Number Guessing Game

This is a simple web-based number guessing game built with **Flask**. It includes a playful guessing interface and a route that demonstrates the use of **Python decorators** to style text with HTML.

---

## 🚀 Features

* Generates a random secret number between 1 and 100.
* Users can guess the number by entering it in the URL.
* Provides feedback: `Too High`, `Too Low`, or `Correct`.
* Fun visuals using GIFs from Giphy.
* Includes a route to demonstrate chaining Python decorators for bold, italic, and underline styling.

---

## 🔪 How to Run

1. Make sure Flask is installed:

```bash
pip install flask
```

2. Save the Python script to a file, e.g., `app.py`.

3. Run the app:

```bash
python app.py
```

4. Open your browser and go to:

```
http://localhost:5000
```

Start guessing numbers like:

```
http://localhost:5000/50
```

To see the decorator test, go to:

```
http://localhost:5000/decorated_test
```

---

## 💡 Decorator Demo

The `/decorated_test` route uses 3 decorators:

```python
@make_bold
@make_emphasis
@make_underline
```

This transforms the returned string to:

```html
<u><em><b>Decorator Tests... wkwkwkkw</b></em></u>
```

---

## 🧰 Requirements

* Flask

You can install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 📄 requirements.txt

```txt
Flask
```

---

# 🎲 Flask Number Guessing Game

This is a simple web-based number guessing game built with **Flask**. It includes a playful guessing interface and a route that demonstrates the use of **Python decorators** to style text with HTML.

---

## 🚀 Features

* Generates a random secret number between 1 and 100.
* Users can guess the number by entering it in the URL.
* Provides feedback: `Too High`, `Too Low`, or `Correct`.
* Fun visuals using GIFs from Giphy.
* Includes a route to demonstrate chaining Python decorators for bold, italic, and underline styling.

---

## 🔪 How to Run

1. Make sure Flask is installed:

```bash
pip install flask
```

2. Save the Python script to a file, e.g., `app.py`.

3. Run the app:

```bash
python app.py
```

4. Open your browser and go to:

```
http://localhost:5000
```

Start guessing numbers like:

```
http://localhost:5000/50
```

To see the decorator test, go to:

```
http://localhost:5000/decorated_test
```

---

## 💡 Decorator Demo

The `/decorated_test` route uses 3 decorators:

```python
@make_bold
@make_emphasis
@make_underline
```

This transforms the returned string to:

```html
<u><em><b>Decorator Tests... wkwkwkkw</b></em></u>
```

---

## 🧰 Requirements

* Flask

You can install all dependencies with:

```bash
pip install Flask
```
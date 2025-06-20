# 📜 Flask Blog Website

This is a minimal **Flask-based blog application** that dynamically fetches blog post content from a remote JSON API and renders it using HTML templates.

---

## 🚀 Features

* Home page listing blog post titles and subtitles.
* Each post has a detailed view (accessible by post ID).
* Blog content is retrieved dynamically from a remote API (via `npoint.io`).
* Uses Flask's built-in Jinja templating system.

---

## 🔪 How to Run

1. Install Flask and requests:

```bash
pip install flask requests
```

2. File Structure:

```
project_folder/
|-- app.py
|-- post.py
|-- templates/
|   |-- index.html
|   |-- post.html
```

3. Run the app:

```bash
python app.py
```

4. Visit in browser:

```
http://localhost:5000/
```

Click on any post title to view its content.

---

## 🔎 Example JSON API Format

```json
[
  {
    "id": 1,
    "title": "First Blog Post",
    "subtitle": "This is a subtitle",
    "body": "This is the full blog post body."
  },
  ...
]
```

This API must be hosted at: `https://api.npoint.io/7bce33b15a477a7a6c81`

---

## 🧰 Requirements

```txt
Flask
requests
```
---

# 📝 Text Helper App

A simple and elegant **Streamlit** dashboard that lets you upload, preview, transform, and save text files.  
It provides quick string manipulation tools and an optional append-and-save feature — all in a clean, blue-accented UI.

---

## 🚀 Features

- 📤 Upload `.txt` files (only plain text supported)
- 👁️ Preview the first 20 lines of your text
- 📊 View file statistics (line, word, and character counts)
- ✏️ Perform quick string operations:
  - **UPPERCASE**
  - **lowercase**
  - **strip (remove spaces)**
  - **replace** (replace one string with another)
  - **count** (find how many times a substring appears)
- 💾 **Append Mode** — add extra text and download the processed file
- 🕒 Adds a final timestamp line on save  
- ❌ Non-`.txt` uploads are rejected with a friendly message

---

## 🧠 Modes

| Mode | Description |
|------|--------------|
| **Read** | You can preview and transform text, but saving is disabled. |
| **Append** | You can append new text and download the final processed file. |

---

## 🎨 Custom Styling

- Blue accent theme  
- Soft shadows and rounded containers  
- Clean monospace preview area  
- Responsive layout for large and small screens  

---

## 🛠️ Installation & Setup

1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/text-helper-app.git
   cd text-helper-app

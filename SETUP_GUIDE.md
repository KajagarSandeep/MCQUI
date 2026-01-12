# MCQ UI Application - Quick Start Guide

## 🚀 What Has Been Built

A complete web-based MCQ (Multiple Choice Questions) answer checker with:

✅ **PDF Upload Functionality** - Upload your answer key as a PDF file  
✅ **Two Testing Modes:**
   - **Mode 1: Immediate Feedback** - Get instant green/red feedback for each answer
   - **Mode 2: Submit Mode** - Answer all questions, then submit to see results  
✅ **Beautiful, Responsive UI** - Works on desktop and mobile  
✅ **Detailed Results** - Score breakdown with correct/incorrect/unanswered counts  
✅ **Modern Backend** - Flask API with PDF parsing  

---

## 📋 Project Files Created

```
├── app.py                      # Flask backend server
├── templates/
│   └── index.html             # Frontend UI (HTML/CSS/JavaScript)
├── uploads/                   # Directory where PDFs are stored
├── MCQUI_README.md           # Detailed documentation
└── Assets/
    └── UPCS_CSE_Prelims_2024_Answer_Key_GS1 (1).pdf  # Sample answer key
```

---

## 🛠️ Setup Instructions

### Step 1: Install Dependencies
```bash
cd /Users/sandeepkajagar/Repo/MCQUI
pip3 install flask pypdf flask-cors
```

### Step 2: Start the Application
```bash
python3 app.py
```

### Step 3: Access the Application
Open your browser and go to:
```
http://localhost:5000
```

You should see the MCQ Answer Checker UI with a purple gradient background and an upload area.

---

## 📖 How to Use

### Uploading an Answer Key

1. **Click "Choose File"** or **drag & drop** your PDF into the upload area
2. The application will parse the PDF and extract the answer key
3. Success message will show how many questions were found
4. You can now select a testing mode

### Testing Mode 1: Immediate Feedback ⚡

1. **Select Mode 1** button
2. **Click on an answer option** (A, B, C, or D)
3. **Instant feedback:**
   - ✅ Green background = Correct answer
   - ❌ Red background = Wrong answer (correct answer shown in green)
4. Repeat for all questions

### Testing Mode 2: Submit All 📝

1. **Select Mode 2** button
2. **Click to select** your answers (they'll be highlighted in blue)
3. **Click "Submit Answers"** button when done
4. **View Results:**
   - Score percentage displayed
   - Count of Correct/Incorrect/Unanswered questions
   - Detailed breakdown of each question with your answer vs correct answer

### Viewing Results

After Mode 2 submission, you'll see:
- **Score Cards** showing: Correct, Incorrect, Unanswered, and Overall Score %
- **Detailed List** showing question-by-question results

### Try Again

Click **"Try Again"** to reset and take another test.

---

## 📊 Supported PDF Format

The application expects answer keys in one of these formats:

**Format 1 (Recommended):**
```
1 A
2 B
3 C
4 D
5 A
...
```

**Format 2:**
```
Q.1 A
Q.2 B
Q.3 C
...
```

**Format 3:**
```
Question 1 A
Question 2 B
...
```

Each line should contain: `[Question Number] [Answer Option (A-D)]`

---

## 🔧 Backend API Endpoints

### POST /api/upload
Upload and parse a PDF answer key
- **Input:** PDF file
- **Output:** JSON with parsed answer key and total questions

### GET /api/answer-key
Get the currently loaded answer key
- **Output:** JSON with question numbers and answers

### POST /api/check-answers
Check user answers against the answer key
- **Input:** JSON with user answers
- **Output:** Detailed results with correct/incorrect counts

---

## 🎨 Features Explained

### Mode 1: Immediate Check
- **Best for:** Learning with instant feedback
- **How it works:** 
  - Each option click triggers immediate validation
  - Correct answer shown in green
  - Wrong answer shown in red with correct answer displayed
  - No submit button needed

### Mode 2: Submit All
- **Best for:** Full mock tests and assessments
- **How it works:**
  - Select all answers first
  - Submit button to validate all at once
  - Comprehensive results page with statistics
  - See your score percentage

---

## 💡 Tips & Tricks

1. **Drag & Drop:** Simply drag your PDF onto the upload area - no need to click
2. **Mobile Friendly:** The UI is fully responsive and works on phones/tablets
3. **Switch Modes:** You can switch between Mode 1 and Mode 2 anytime
4. **Sample PDF:** Use the provided sample in `/Assets/` to test the application

---

## 🐛 Troubleshooting

### Application won't start
```bash
# Make sure Flask is installed
pip3 install flask

# Check if port 5000 is available
lsof -i :5000

# If port is in use, modify app.py line:
# app.run(debug=True, port=5001)  # Change to any available port
```

### PDF not parsing
- Ensure the PDF is text-based (not scanned/image)
- Check that answers are clearly formatted (e.g., "1 A" or "Q.1 A")
- Make sure questions are numbered sequentially
- File size should be under 50MB

### No file upload button appearing
- Clear browser cache: `Ctrl+Shift+Delete` (Windows) or `Cmd+Shift+Delete` (Mac)
- Try a different browser
- Check browser console for errors: `F12` → Console tab

---

## 📁 Directory Structure

```
MCQUI/
├── app.py                      # Main Flask application
├── MCQUI_README.md            # Detailed documentation
├── SETUP_GUIDE.md             # This file
├── templates/
│   └── index.html             # Web UI
├── uploads/                   # Uploaded PDFs storage
├── Assets/                    # Sample files
│   └── UPCS_CSE_Prelims_2024_Answer_Key_GS1 (1).pdf
└── README.md                  # Project info
```

---

## 🚀 Deployment Options

### Local Development (Current)
```bash
python3 app.py
```
- Server runs on `http://localhost:5000`
- Perfect for testing and development

### Production Deployment
For deploying to a server, use WSGI servers like:
```bash
pip3 install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Docker (Optional)
Create a `Dockerfile` to containerize the application for easy deployment.

---

## 📞 Support & Next Steps

### Current Features
✅ PDF upload with automatic parsing  
✅ Two testing modes  
✅ Real-time feedback  
✅ Score calculation  
✅ Responsive design  

### Potential Enhancements
- Database to store test results
- User authentication
- Test history and analytics
- Timer for timed tests
- Multiple answer key templates
- Export results to PDF
- Difficulty level tracking

---

## 🎓 Learning Resources

- **Flask Documentation:** https://flask.palletsprojects.com/
- **PyPDF Documentation:** https://pypdf.readthedocs.io/
- **Vanilla JavaScript:** https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide

---

## ✨ Summary

Your MCQ UI application is ready to use! Simply:

1. Run `python3 app.py`
2. Go to `http://localhost:5000`
3. Upload your answer key PDF
4. Choose a testing mode and start answering questions
5. Get instant or detailed feedback

Enjoy! 🎉

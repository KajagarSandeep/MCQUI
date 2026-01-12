# MCQ Answer Checker UI

A modern, interactive web application for uploading MCQ answer keys and testing yourself with two different modes of checking.

## Features

✨ **Two Testing Modes:**
1. **Mode 1: Immediate Check** - Get instant feedback (green for correct, red for wrong) as you select each answer
2. **Mode 2: Submit All** - Select all answers first, then click submit to see complete results with score breakdown

✨ **PDF Upload** - Upload your MCQ answer key PDF file
✨ **Beautiful UI** - Modern, responsive design with smooth animations
✨ **Detailed Results** - View your score, correct/incorrect/unanswered counts, and detailed breakdown
✨ **Mobile Friendly** - Works seamlessly on desktop and mobile devices

## Setup & Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation Steps

1. **Navigate to the project directory:**
   ```bash
   cd /Users/sandeepkajagar/Repo/MCQUI
   ```

2. **Install required dependencies:**
   ```bash
   pip3 install flask pypdf flask-cors
   ```

3. **Start the Flask development server:**
   ```bash
   python3 app.py
   ```

4. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

## Usage

### Uploading Answer Key

1. **PDF Format Requirements:**
   - The PDF should contain questions numbered with their answers
   - Expected format: `1 A`, `2 B`, `3 C`, etc. (question number followed by answer option)
   - Alternative formats supported: `Q.1 A`, `Question 1 A`, etc.

2. **Upload Process:**
   - Click on the upload area or drag & drop your PDF
   - Wait for the PDF to be processed
   - Success message will show the total number of questions found

### Testing Modes

#### Mode 1: Immediate Check ✓
- **How it works:** 
  - Click on an option to submit your answer
  - Immediately see if you're correct (green) or incorrect (red)
  - If incorrect, the correct answer is shown in green
- **Best for:** Learning and practicing with instant feedback

#### Mode 2: Submit All 📋
- **How it works:**
  - Select all your answers by clicking the options
  - Selected options are highlighted in blue
  - Click "Submit Answers" button when done
  - See detailed results with score percentage
- **Best for:** Taking mock tests and full assessments

### Viewing Results

After submitting answers in Mode 2, you'll see:
- **Score Cards:** Total correct, incorrect, and unanswered questions
- **Overall Score:** Percentage score
- **Detailed Breakdown:** Question-by-question review showing:
  - Your answer
  - Correct answer
  - Whether you were correct or incorrect

### Try Again

Click the "Try Again" button to reset and take another test or switch modes.

## Project Structure

```
MCQUI/
├── app.py                    # Flask backend application
├── templates/
│   └── index.html           # Frontend UI with HTML/CSS/JavaScript
├── uploads/                 # Folder where uploaded PDFs are stored
└── Assets/                  # Sample PDF files
    └── UPCS_CSE_Prelims_2024_Answer_Key_GS1.pdf
```

## File Details

### `app.py` - Backend
- Handles PDF file uploads
- Parses answer key from PDF using regex patterns
- Provides API endpoints for checking answers
- Returns detailed results in JSON format

### `templates/index.html` - Frontend
- Modern, responsive UI built with HTML5, CSS3, and Vanilla JavaScript
- Drag & drop file upload functionality
- Two testing modes with different UI behaviors
- Real-time feedback and results display

## API Endpoints

### `POST /api/upload`
Upload a PDF file and get the parsed answer key
- **Request:** multipart/form-data with PDF file
- **Response:** JSON with success status and parsed answer key

### `GET /api/answer-key`
Get the current loaded answer key
- **Response:** JSON object with question number as key and answer as value

### `POST /api/check-answers`
Check user answers against the answer key
- **Request:** JSON with user answers
- **Response:** JSON with detailed results

## Sample PDF Format

The sample answer key PDF should follow this format:

```
1 A
2 C
3 B
4 D
5 A
...
```

Or with question indicators:

```
Q.1 A
Q.2 C
Question 3 B
...
```

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Troubleshooting

### PDF not parsing correctly
- Ensure the PDF contains answers in a recognizable format (e.g., "1 A", "Q.1 A")
- The answer key should be text-based, not scanned images
- Try reformatting the PDF with clear answer indicators

### Port already in use
If port 5000 is already in use, modify the `app.py` file:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change 5000 to any available port
```

### File upload fails
- Check file size (max 50MB)
- Ensure file is a valid PDF
- Check browser console for detailed error messages

## Development Notes

- The application uses Flask for backend and vanilla JavaScript for frontend (no external dependencies needed)
- Responsive design works on mobile and desktop
- Answer key is stored in memory during the session
- Real-time parsing with error handling

## Future Enhancements

- [ ] Database integration to save test results
- [ ] User authentication and accounts
- [ ] Analytics and performance tracking
- [ ] Support for different question formats
- [ ] Export results to PDF/Excel
- [ ] Multiple language support
- [ ] Timer feature for mock tests

## License

Open source - feel free to use and modify for your needs!

## Support

For issues or questions, check the sample PDF in `/Assets/` folder to understand the expected format.

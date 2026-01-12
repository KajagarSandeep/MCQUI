from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from pypdf import PdfReader
import re
import json

app = Flask(__name__)
CORS(app)

# Configuration
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store current answer key in memory
current_answer_key = {}

def parse_answer_key_from_pdf(pdf_path):
    """
    Parse MCQ answer key from PDF
    Expected format: Question# AnswerOption (e.g., "1 A", "2 B", etc.)
    """
    answer_key = {}
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        
        # Find patterns like "1 A", "2 B", etc. or "Q.1 A", "Q.2 B"
        # Try multiple patterns
        patterns = [
            r'(?:Q\.?|Question\s?)(\d+)\s+([A-D])',  # Q.1 A or Question 1 A
            r'^(\d+)\s+([A-D])$',  # 1 A (on separate lines)
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text, re.MULTILINE)
            if matches:
                for q_num, answer in matches:
                    answer_key[int(q_num)] = answer.strip()
                break
        
        # If still empty, try a more lenient approach
        if not answer_key:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                # Try to match simple patterns
                parts = line.split()
                if len(parts) >= 2:
                    try:
                        q_num = int(parts[0])
                        answer = parts[1].upper()
                        if answer in ['A', 'B', 'C', 'D']:
                            answer_key[q_num] = answer
                    except ValueError:
                        continue
        
        return answer_key
    
    except Exception as e:
        print(f"Error parsing PDF: {e}")
        return {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    global current_answer_key
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if not file.filename.endswith('.pdf'):
        return jsonify({'error': 'Only PDF files are allowed'}), 400
    
    try:
        # Save the file
        filepath = os.path.join(UPLOAD_FOLDER, 'answer_key.pdf')
        file.save(filepath)
        
        # Parse the answer key
        current_answer_key = parse_answer_key_from_pdf(filepath)
        
        if not current_answer_key:
            return jsonify({'error': 'Could not parse answer key from PDF'}), 400
        
        return jsonify({
            'success': True,
            'message': f'Answer key uploaded successfully. Found {len(current_answer_key)} questions.',
            'totalQuestions': len(current_answer_key),
            'answerKey': current_answer_key
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/answer-key', methods=['GET'])
def get_answer_key():
    if not current_answer_key:
        return jsonify({'error': 'No answer key loaded'}), 400
    return jsonify(current_answer_key)

@app.route('/api/check-answers', methods=['POST'])
def check_answers():
    """Check user answers against the answer key"""
    user_answers = request.json.get('answers', {})
    
    if not current_answer_key:
        return jsonify({'error': 'No answer key loaded'}), 400
    
    results = {
        'correct': 0,
        'wrong': 0,
        'unanswered': 0,
        'details': {}
    }
    
    # Convert user_answers keys to integers
    user_answers = {int(k): v for k, v in user_answers.items()}
    
    for q_num, correct_answer in current_answer_key.items():
        if q_num not in user_answers:
            results['unanswered'] += 1
            results['details'][q_num] = {'isCorrect': False, 'userAnswer': None, 'correctAnswer': correct_answer}
        else:
            user_answer = user_answers[q_num].upper()
            is_correct = user_answer == correct_answer
            if is_correct:
                results['correct'] += 1
            else:
                results['wrong'] += 1
            results['details'][q_num] = {'isCorrect': is_correct, 'userAnswer': user_answer, 'correctAnswer': correct_answer}
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

import time

# ফাইল থেকে প্রশ্ন পড়া
def load_questions(file_path):
    questions = []
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read().split("\n\n")
        for item in data:
            # প্রতিটি প্রশ্ন এবং উত্তর আলাদা করা
            parts = item.split("\n")
            question_text = parts[0].split("Answer: ")[0].strip()  # প্রশ্নটি
            answer = parts[0].split("Answer: ")[1].strip()  # সঠিক উত্তর

            # অপশনগুলো আলাদা করা
            options = []
            for line in parts[1:]:
                if ")" in line:
                    options.append(line.split(") ")[1].strip())

            # যদি অপশন না থাকে, তাহলে এই প্রশ্নটি বাদ দেওয়া হবে
            if len(options) >= 4:
                questions.append({
                    'question': question_text,
                    'options': options,
                    'answer': answer
                })
    return questions

# টাইমার সেট করা
def start_timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"Time remaining: {i}s", end='\r')
        time.sleep(1)

# প্রধান গেম ফাংশন
def play_game():
    questions = load_questions('questions.txt')
    score = 0
    
    for q in questions:
        print("\n" + q['question'])
        for idx, option in enumerate(q['options']):
            print(f"{chr(65 + idx)}) {option}")
        
        start_timer(15)  # 15 সেকেন্ড সময়

        answer = input("\nEnter your answer (A/B/C/D): ").upper()
        
        if answer == q['answer']:
            print("\033[32mCorrect Answer!\033[0m")
            score += 1
        else:
            print(f"\033[31mWrong Answer! The correct answer is {q['answer']}\033[0m")

    print(f"\nYour final score is: {score}/{len(questions)}")

# গেম শুরু করা
if __name__ == "__main__":
    play_game()

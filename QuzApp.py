# Step 1: Define quiz questions and answers
from pydoc import stripid

quiz = [
    {"question": "What is the capital of IRAN?", "answer": "Tehran"},
    {"question": "What is 15 + 17?", "answer": "32"},
    {"question": "What is the color of the sky on a clear day?", "answer": "blue"},
    {"question": "What programming language are you learning?", "answer": "python"}
]
#Step 2 : Welcome message
print("welcome to the Quiz!!!")
name = input("Enter your name: ")
print(f"Hi {name} , let's begin!\n")

# Step 3: Initialize score
score = 0

# Step 4: Loop through questions
for i, q in enumerate(quiz):
    print(f"Q{i+1}: {q['question']}")
    user_answer = input("Your answer:  ").lower().strip()
    if user_answer == q['answer']:
        print("✅ Correct!\n")
        score +=1
    else:
        print(f"❌ Wrong! The correct answer was: {q['answer']}\n")

# Step 5: Final score
print("📊 Quiz Completed!")
print(f"🎉 {name}, your score is {score} out of {len(quiz)}")
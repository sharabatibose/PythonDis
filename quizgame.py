#a simple quiz game using collections in PYTHON, with proper formatting
questions= ("What is the capital of France?",
            "What is 2 + 2?", 
            "What is the hottest planet in our solar system?", 
            "What is the largest mammal?")
options= (("A. Paris", "B. London", "C. Berlin", "D. Madrid"),
          ("A. 3", "B. 4", "C. 5", "D. 6"),
          ("A. Earth", "B. Venus", "C. Mars", "D. Jupiter"),
          ("A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"))
answers=("A", "B", "B", "B")
guesses=[]
score=0
for i in questions:
    print("------------------------- ")
    print(i)
    print("------------------------- ")
    index=questions.index(i)
    for j in options[index]:
        print(j)
    guess=input("Enter (A/ B/ C/ D): ")
    guesses.append(guess)
    if guesses[index].upper()==answers[index]:
        score+=1
        print("Your answer is CORRECT!")
    else:
        print(f"Wrong! The correct answer is {answers[index]}")
print("------------------------- ")
print("         QUIZ RESULTS        ")
print(f"your TOTAL score is {score/len(questions):.2%}".upper())
        

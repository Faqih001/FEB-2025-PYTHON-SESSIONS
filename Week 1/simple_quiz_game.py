def quiz_game():
    questions = [
        {"question": "What is the capital of France?", "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"], "answer": "C"},
        {"question": "Which programming language is known as the ‘snake’ language?", "options": ["A) C++", "B) Python", "C) Java", "D) Ruby"], "answer": "B"},
        {"question": "Who directed the movie 'Inception'?", "options": ["A) Steven Spielberg", "B) Christopher Nolan", "C) Quentin Tarantino", "D) James Cameron"], "answer": "B"}
    ]

    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

    print(f"\n🏆 Your final score: {score}/{len(questions)}")
    if input("Do you want to play again? (yes/no): ").strip().lower() == "yes":
        quiz_game()

quiz_game()

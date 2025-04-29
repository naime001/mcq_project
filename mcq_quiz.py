import time
from termcolor import colored

# প্রশ্ন এবং উত্তর ফাইল লোড
with open("questions.txt", "r") as qf:
    questions_raw = qf.read().strip().split("\n\n")

with open("answers.txt", "r") as af:
    correct_answers = af.read().strip().splitlines()

for i, block in enumerate(questions_raw):
    lines = block.strip().split("\n")
    print("\n".join(lines))
    answer = input("\nYour answer (A/B/C/D): ").strip().upper()

    if answer == correct_answers[i]:
        print(colored("Correct!", "green"))
    else:
        print(colored("Incorrect!", "red"))
        print(f"Correct Answer: {colored(correct_answers[i], 'green')}")
    print("-" * 30)
    time.sleep(1)

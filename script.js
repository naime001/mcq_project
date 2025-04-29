// প্রশ্ন এবং উত্তর ফাইল লোড
const questions = [];
const correctAnswers = [];

fetch('questions.txt')
    .then(response => response.text())
    .then(data => {
        questions.push(...data.split("\n\n"));
        loadQuiz();
    });

fetch('answers.txt')
    .then(response => response.text())
    .then(data => {
        correctAnswers.push(...data.split("\n"));
    });

let currentQuestionIndex = 0;

function loadQuiz() {
    const quizElement = document.getElementById("quiz");
    const question = questions[currentQuestionIndex];
    quizElement.innerHTML = `
        <h2>${question}</h2>
        <div>
            <button onclick="checkAnswer('A')">A</button>
            <button onclick="checkAnswer('B')">B</button>
            <button onclick="checkAnswer('C')">C</button>
            <button onclick="checkAnswer('D')">D</button>
        </div>
    `;
}

function checkAnswer(selectedAnswer) {
    const answer = correctAnswers[currentQuestionIndex];
    const answerElement = document.getElementById("answer");
    if (selectedAnswer === answer) {
        answerElement.innerHTML = "<span class='correct'>Correct!</span>";
    } else {
        answerElement.innerHTML = `<span class='incorrect'>Incorrect! Correct Answer: ${answer}</span>`;
    }
}

function nextQuestion() {
    if (currentQuestionIndex < questions.length - 1) {
        currentQuestionIndex++;
        loadQuiz();
    } else {
        alert("Quiz Finished!");
    }
}

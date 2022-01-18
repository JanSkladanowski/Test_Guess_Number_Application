'use strict';
let secretNumber = Math.trunc(Math.random()*20)+1;
let score = 20;
document.querySelector('.test').textContent = secretNumber

console.log(document.querySelector('.test').textContent);
console.log(secretNumber);

document.querySelector('.check').addEventListener(
    'click', function(){
        const guess = Number (document.querySelector('.guess').value);
        console.log(guess, typeof guess);
        
        // When there is no input
        if (!guess) {
            if (score>1){
                document.querySelector('.message').textContent = "No number!"
                score--
                document.querySelector(".score").textContent= score;
            } else {
            document.querySelector(".message").textContent = "You lost!"
            document.querySelector(".score").textContent = 0
            }

            //When player win
        } else if (guess === secretNumber) {
            document.querySelector('.message').textContent = "You win!!";
            if (document.querySelector(".score").textContent>document.querySelector('.highscore').textContent){
                document.querySelector('.highscore').textContent = document.querySelector(".score").textContent;
            }
            document.querySelector('.number').textContent = secretNumber
            document.querySelector('body').style.backgroundColor = '#60b347';
            document.querySelector('.number').style.width ='30rem'

            // When it is wrong
        } else if (guess !== secretNumber){
            if (score>1){
                document.querySelector(".message").textContent = guess > secretNumber ? "To high!" : " To low!"
                score--
                document.querySelector(".score").textContent= score;
            }else {
                document.querySelector(".message").textContent = "You lost!"
                document.querySelector(".score").textContent = 0
            }

            // When guess is too high
        // } else if (guess > secretNumber){
        //     if (score>1){
        //         document.querySelector(".message").textContent = "To high!"
        //         score--
        //         document.querySelector(".score").textContent= score;
        //     }else {
        //         document.querySelector(".message").textContent = "You lost!"
        //         document.querySelector(".score").textContent = 0
        //     }

        //     // When guess is too low
        // } else if (guess < secretNumber){
        //     if (score>1){
        //         document.querySelector(".message").textContent = " To low!"
        //         score--
        //         document.querySelector(".score").textContent= score;
        //     } else {
        //         document.querySelector(".message").textContent = "You lost!"
        //         document.querySelector(".score").textContent = 0
        //     }
        // }
        
    }});

document.querySelector('.again').addEventListener(
    'click', function(){
        document.querySelector('.test').textContent = secretNumber
        document.querySelector('.number').style.width ='15rem';
        document.querySelector('.number').textContent ='?';
        document.querySelector('body').style.backgroundColor = '#222';
        document.querySelector(".message").textContent = "Start guessing...";
        score = 20;
        document.querySelector(".score").textContent = score;
        secretNumber = Math.trunc(Math.random()*20)+1;
        document.querySelector('.guess').value = '';
        document.querySelector('.test').textContent = secretNumber
    }
)





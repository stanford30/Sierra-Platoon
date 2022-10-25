console.log('HELLO SIERRA PLATOON!');
// Your function(s) should go here that will interact with the webpage or DOM
const startBtn = document.querySelector('.start-game');
const guessBtn = document.querySelector('.guess-btn');
const resetBtn = document.querySelector('.reset-btn');
const guessInput = document.querySelector('input');
const announcement = document.querySelector('.announcement');
const triesAnnouncement = document.querySelector('.tries span');
// console.log(triesAnnouncement);

let answer;
let tries = 0;
let playing;
const startGame = () => {
  startBtn.classList.add('hidden');
  guessBtn.classList.toggle('hidden');
  guessInput.classList.toggle('hidden');
  answer = Math.floor(Math.random() * 101);
  playing = true;
};

const submitGuess = () => {
  if (!playing) return;

  let inp = +guessInput.value;
  console.log(answer);
  if (inp < answer) {
    announcement.textContent = 'Higher!';
  } else if (inp > answer) {
    announcement.textContent = 'Lower!';
  } else {
    announcement.textContent = 'You win :)';
    toggleHidden();

    playing = false;
  }
  tries++;
  triesAnnouncement.textContent = tries;
  if (tries > 9) {
    announcement.textContent = 'You lose :(';
    toggleHidden();

    playing = false;
  }
};

const resetGame = () => {
  playing = true;
  answer = Math.floor(Math.random() * 101);
  tries = 0;
  triesAnnouncement.textContent = tries;
  announcement.textContent = "Let's Play the Guessing Number Game!";
  toggleHidden();
};

const toggleHidden = () => {
  resetBtn.classList.toggle('hidden');
  guessBtn.classList.toggle('hidden');
};

guessInput.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') submitGuess();
});

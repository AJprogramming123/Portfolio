// static/js/intro.js

const lines = [
  "[System Booting...]",
  "> Initializing containers...",
  "> Establishing secure tunnel...",
  "> Deploying Flask instance...",
  "> Connecting to ajprogramming123.xyz...",
  "",
  "Welcome to the portfolio."
];

let lineIndex = 0;
let charIndex = 0;
const speed = 30; 
const bootText = document.getElementById("boot-text");
const prompt = document.getElementById("prompt");

function typeLine() {
  if (lineIndex < lines.length) {

    if (charIndex < lines[lineIndex].length) {
      bootText.innerHTML += lines[lineIndex].charAt(charIndex);
      charIndex++;
      setTimeout(typeLine, speed);

    } else {
      bootText.innerHTML += "\n";
      lineIndex++;
      charIndex = 0;
      setTimeout(typeLine, speed);
    }

  } else {
    prompt.classList.remove("hidden");
    document.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        window.location.href = "/home";
      }
    });
  }
}

document.addEventListener("DOMContentLoaded", typeLine);

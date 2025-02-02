<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>💖 Valentine's Day Love Calculator 💖</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background-color: #ffcccb;
      font-family: 'Arial', sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      text-align: center;
      overflow: hidden;
    }
    .container {
      background-color: white;
      padding: 30px;
      border-radius: 15px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
      max-width: 400px;
      width: 100%;
      position: relative;
      z-index: 1;
    }
    h1 {
      color: #ff1493;
      font-size: 2.5rem;
      margin-bottom: 20px;
    }
    input {
      width: 80%;
      padding: 10px;
      margin: 10px 0;
      border: 2px solid #ff1493;
      border-radius: 5px;
      font-size: 1rem;
    }
    button {
      background-color: #ff1493;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 5px;
      font-size: 1rem;
      cursor: pointer;
      margin-top: 10px;
    }
    button:hover {
      background-color: #ff69b4;
    }
    .result {
      margin-top: 20px;
      font-size: 1.5rem;
      color: #ff1493;
      font-weight: bold;
    }
    .hidden {
      display: none;
    }
    .heart {
      position: absolute;
      top: -50px;
      font-size: 3rem;
      animation: spin 2s linear infinite;
    }
    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    .confetti {
      position: absolute;
      width: 10px;
      height: 10px;
      background-color: #ff1493;
      border-radius: 50%;
      animation: confetti 3s linear infinite;
    }
    @keyframes confetti {
      0% { transform: translateY(0) rotate(0deg); }
      100% { transform: translateY(100vh) rotate(720deg); }
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>💖 Love Calculator 💖</h1>
    <p>Enter two names to calculate their love compatibility:</p>
    <input type="text" id="name1" placeholder="Your Name" />
    <input type="text" id="name2" placeholder="Crush's Name" />
    <button onclick="calculateLove()">Calculate Love</button>
    <div class="result hidden" id="result"></div>
    <button class="hidden" id="shareButton" onclick="shareResult()">Share Result</button>
  </div>

  <!-- Heart Animation -->
  <div class="heart">💖</div>

  <!-- Confetti Animation -->
  <div id="confetti-container"></div>

  <!-- Audio for Sound Effect -->
  <audio id="sound-effect" src="https://assets.mixkit.co/active_storage/sfx/2993/2993-preview.mp3"></audio>

  <script>
    const loveMessages = [
      "Sorry, it's a 0% match. Better luck next time! 😅",
      "Wow! 10% match. Maybe just stay friends? 😬",
      "30% match. It's... complicated. 🤔",
      "50% match. Not bad, but not great either. 😐",
      "75% match. There's potential here! 😍",
      "99% match! Soulmates alert! 💖",
      "100% match! It's destiny! 💘",
      "Oops! Negative compatibility. Run! 🏃‍♂️💨",
      "42% match. The answer to life, but not love. 🤷‍♂️",
      "69% match. Nice. 😏",
    ];

    function calculateLove() {
      const name1 = document.getElementById('name1').value.trim();
      const name2 = document.getElementById('name2').value.trim();
      const resultDiv = document.getElementById('result');
      const shareButton = document.getElementById('shareButton');

      if (!name1 || !name2) {
        alert("Please enter both names!");
        return;
      }

      // Fake calculation: Randomly pick a message
      const randomMessage = loveMessages[Math.floor(Math.random() * loveMessages.length)];
      resultDiv.textContent = `💔 ${name1} & ${name2}: ${randomMessage}`;
      resultDiv.classList.remove('hidden');
      shareButton.classList.remove('hidden');

      // Play sound effect
      const soundEffect = document.getElementById('sound-effect');
      soundEffect.play();

      // Add confetti
      addConfetti();
    }

    function addConfetti() {
      const confettiContainer = document.getElementById('confetti-container');
      for (let i = 0; i < 50; i++) {
        const confetti = document.createElement('div');
        confetti.classList.add('confetti');
        confetti.style.left = `${Math.random() * 100}vw`;
        confetti.style.animationDelay = `${Math.random() * 2}s`;
        confettiContainer.appendChild(confetti);
      }
    }

    function shareResult() {
      const name1 = document.getElementById('name1').value.trim();
      const name2 = document.getElementById('name2').value.trim();
      const result = document.getElementById('result').textContent;
      const shareText = `Check out this hilarious love compatibility result: ${result}`;
      const shareUrl = window.location.href;

      if (navigator.share) {
        navigator.share({
          title: 'Love Calculator Result',
          text: shareText,
          url: shareUrl,
        });
      } else {
        alert("Sharing not supported in this browser. Copy the link manually!");
      }
    }
  </script>
</body>
</html>
const startBtn = document.getElementById("start-btn");
const stopBtn = document.getElementById("stop-btn");
const userQuery = document.querySelector(".query-text");
const assistantResponse = document.querySelector(".response-text");

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
recognition.lang = "en-US";
recognition.interimResults = false;

let isListening = false;

// Start Listening
startBtn.addEventListener("click", () => {
  if (!isListening) {
    recognition.start();
    isListening = true;
    assistantResponse.textContent = "Listening...";
  }
});

// Stop Listening
stopBtn.addEventListener("click", () => {
  if (isListening) {
    recognition.stop();
    isListening = false;
    assistantResponse.textContent = "Stopped.";
  }
});

// Handle Speech Input
recognition.onresult = async (event) => {
  const userCommand = event.results[0][0].transcript.toLowerCase();
  userQuery.textContent = userCommand;

  // Handle Commands
  let response;
  if (userCommand.includes("show my schedule")) {
    response = "Fetching your schedule.";
    fetch("/assistant/schedule/")
      .then((res) => res.json())
      .then((data) => {
        response = `Here is your schedule: ${JSON.stringify(data.schedule)}`;
        speak(response);
        assistantResponse.textContent = response;
      });
  } else if (userCommand.includes("open pomodoro timer")) {
    response = "Opening the Pomodoro Timer.";
    window.location.href = "/pomodoro/";
  } else if (userCommand.includes("add a task")) {
    response = "Redirecting you to the Add Task page.";
    window.location.href = "/schedule/";
  } else if (userCommand.includes("what is learnease portal about")) {
    response = "LearnEase is a platform that provides students with study materials, task management tools, and educational resources to enhance learning.";
  } else if (userCommand.includes("how to add a task")) {
    response = "Go to the Explore menu, click on Task Hive, and fill out the form to add a task.";
  } else if (userCommand.includes("how to view my schedule")) {
    response = "Your schedule can be accessed in the My Schedule section under the dashboard.";
  } else if (userCommand.includes("what features does learnease provide")) {
    response = "LearnEase offers study material searches, a Pomodoro Timer, a task manager, and more.";
  } else if (userCommand.includes("how to use the pomodoro timer")) {
    response = "Click on the Pomodoro Timer option in the dashboard and set your session time.";
  } else if (userCommand.includes("how to create notes")) {
    response = "Visit the Notes section under your dashboard, and click on Create Notes.";
  } else if (userCommand.includes("how to view my to-do list")) {
    response = "Your to-do list can be accessed under the To-Do List section in the dashboard.";
  } else if (userCommand.includes("how to use the dictionary")) {
    response = "In the Dictionary section, type the word you want to search for and get its meaning.";
  } else if (userCommand.includes("how to search for study material")) {
    response = "Use the Study Material section to search by topic or keywords.";
  } else if (userCommand.includes("how to explore new books")) {
    response = "Go to the Explore menu and select Books to see a list of available books.";
  } else {
    response = "Sorry, I didn't understand that command.";
  }

  assistantResponse.textContent = response;
  speak(response);
};

// Speak Response
function speak(message) {
  window.speechSynthesis.cancel(); // Clear any ongoing speech
  const speech = new SpeechSynthesisUtterance(message);
  speech.lang = "en-US";
  speech.rate = 1; // Set speaking rate
  speech.pitch = 1; // Set pitch
  window.speechSynthesis.speak(speech);
}

// Handle Errors
recognition.onerror = (event) => {
  assistantResponse.textContent = "Error occurred: " + event.error;
};

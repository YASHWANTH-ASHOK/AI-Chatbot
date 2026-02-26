async function sendMsg() {
    let msg = document.getElementById("userInput").value.trim();
    if (!msg) return;

    appendMessage(msg, "user");
    document.getElementById("userInput").value = "";

    try {
        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: msg })
        });

        const data = await response.json();
        appendMessage(formatBotText(data.reply), "bot");
    }
    catch (err) {
        appendMessage("⚠ Error connecting to server!", "bot");
    }
}

// Format bot response for readability
function formatBotText(text) {
    return text
        .replace(/\\(.?)\\*/g, "<strong>$1</strong>")         // Bold text
        .replace(/### (.*?)(<br>|$)/g, "<h3>$1</h3>")             // Headings
        .replace(/- (.*?)(<br>|$)/g, "<li>$1</li>")               // Bullet points
        .replace(/\n/g, "<br>");                                 // Line breaks
}

// Append messages to chatbox
function appendMessage(message, sender) {
    const chat = document.getElementById("chat");
    const div = document.createElement("div");
    div.classList.add("message", sender);
    div.innerHTML = message;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}
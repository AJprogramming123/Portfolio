(() => {
  console.log("Chatbot JS loaded");
  const messagesDiv = document.getElementById('chatbot-messages');
  const form = document.getElementById('chatbot-form');
  const input = document.getElementById('chatbot-input');

  function appendMessage(sender, text) {
    const div = document.createElement('div');
    div.classList.add('px-2', 'py-1', 'rounded');
    if (sender === 'user') {
      div.classList.add('bg-indigo-700', 'text-right');
    } else {
      div.classList.add('bg-gray-700');
    }
    div.textContent = text;
    messagesDiv.appendChild(div);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
  }

  form.addEventListener('submit', async e => {
    e.preventDefault();
    const userText = input.value.trim();
    if (!userText) return;

    appendMessage('user', userText);
    input.value = '';
    input.disabled = true;

    try {
      const response = await fetch('/chatbot/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userText }),
      });

      console.log('Fetch response status:', response.status);

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log('Response JSON:', data);

      if (!data.response) {
        appendMessage('bot', 'Error: No response from server. You've been blocked for a while');
      } else {
        appendMessage('bot', data.response);
      }
    } catch (err) {
      console.error('Fetch error:', err);
      appendMessage('bot', 'Error: Unable to get response. You've been blocked for a while');
    } finally {
      input.disabled = false;
      input.focus();
    }
  });
})();

const form = document.getElementById('prompt-form');
const promptInput = document.getElementById('prompt-input');
const statusMessage = document.getElementById('status-message');

form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const prompt = promptInput.value;
    statusMessage.textContent = 'Generating podcast...';
    console.log('Form submitted!')
    fetch('/generate-podcast', {
        mode:'no-cors',
        method: 'POST',
        headers: {
         'Content-Type': 'application/json'
         },
        body: JSON.stringify({ prompt: prompt })
    })
    .then(response => {
        statusMessage.textContent = 'Podcast generated! (Demo)';
        // In a real app, you might add audio playback here
    })
    .catch(error => {
        console.error('Error:', error);
        statusMessage.textContent = 'Something went wrong';
    });
});
# from lib2to3.pgen2.grammar import line

from flask import Flask, request, render_template, send_file
import cohere

from gtts import gTTS

app = Flask(__name__, template_folder='templates')

# Cohere Key
co = cohere.Client("XF6ktIy6aP2ZS8CpO7LkLEnrEgg2UgGr0fRr8UMU")


@app.route('/generate_podcast', methods=['POST'])
def generate_podcast():
    prompt = request.form['prompt']
    print("Received Prompt:", prompt)  # Verify prompt reception

    # generated Content
    content = generate_content(prompt)

    audio_path = prompt + "_podcast.mp3"

    tts = gTTS(text=content, lang='en', slow=False)  # Adjust 'en' for desired language
    tts.save(audio_path)

    return send_file(audio_path, as_attachment=True)


def generate_content(prompt):
    # generating content
    response = co.generate(
        prompt=prompt,
        max_tokens=500,
        temperature=0.5,
    )
    generated_content = response.generations[0].text
    return generated_content


@app.route('/')
def serve_frontend():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

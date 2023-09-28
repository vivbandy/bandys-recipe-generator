from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Initialize OpenAI API (assuming you're using ChatGPT)
openai.api_key = "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"

@app.route('/', methods=['GET', 'POST'])
def index():
    recipe = ""
    if request.method == 'POST':
        ingredient1 = request.form['ingredient1']
        ingredient2 = request.form['ingredient2']
        ingredient3 = request.form['ingredient3']
        prompt = f"Generate a recipe with {ingredient1}, {ingredient2}, {ingredient3} and respond only within 100 tokens"
        try:
            response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=150)
    # Process the response...
        except openai.error.RateLimitError:
            return render_template('index.html', recipe="Sorry, we've hit our API limit. Please try again later.")

        recipe = response.choices[0].text.strip()
    return render_template('index.html', recipe=recipe)

if __name__ == '__main__':
    app.run(debug=True)

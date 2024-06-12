from flask import Flask, render_template, request, jsonify
from langchain_community.llms import Ollama

app = Flask(__name__)

# Инициализация модели Ollama
llm = Ollama(model="llama3", temperature=0.7)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if user_input:
        try:
            response = llm.invoke(user_input)  # Передаем строку напрямую
            return jsonify({"response": response})
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"response": str(e)}), 500
    return jsonify({"response": "No input provided"})

if __name__ == '__main__':
    app.run(debug=True)

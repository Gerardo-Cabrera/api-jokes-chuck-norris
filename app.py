from flask import Flask, jsonify
import requests
import concurrent


app = Flask(__name__)

def get_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        joke_value = joke_data.get('value')
        return joke_value
    
@app.route('/jokes', methods=['GET'])
def get_jokes():
    jokes = set()
    limit = 25

    # Se agrega concurrencia para que sea mucho más rápido obtener chistes aleatorios y en cada petición se muestren 25 chistes diferentes
    with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
        next_joke = {executor.submit(get_joke): i for i in range(25)}
        for joke in concurrent.futures.as_completed(next_joke):
            joke_value = joke.result()

            if joke_value is not None and joke_value not in jokes:
                jokes.add(joke_value)

            if len(jokes) == limit:
                break

    return jsonify(list(jokes))

if __name__ == '__main__':
    app.run(debug=True)

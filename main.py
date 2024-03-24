
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    images = requests.get('http://localhost:5000/images').json()
    return render_template('index.html', images=images)

@app.route('/image/<int:image_id>')
def image_detail(image_id):
    image = requests.get(f'http://localhost:5000/images/{image_id}').json()
    return render_template('image_detail.html', image=image)

@app.route('/images')
def get_images():
    images = [
        {
            'id': 1,
            'title': 'Mona Lisa',
            'artist': 'Leonardo da Vinci',
            'description': 'The Mona Lisa is a famous oil painting by Leonardo da Vinci from the Italian Renaissance. It is housed at the Louvre Museum in Paris, France.',
            'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/1200px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg'
        },
        {
            'id': 2,
            'title': 'Starry Night',
            'artist': 'Vincent van Gogh',
            'description': 'The Starry Night is an oil on canvas painting by Dutch artist Vincent van Gogh. It is one of the most famous paintings in the world and is currently housed at the Museum of Modern Art in New York City.',
            'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Vincent_Willem_van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1200px-Vincent_Willem_van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg'
        },
        {
            'id': 3,
            'title': 'The Scream',
            'artist': 'Edvard Munch',
            'description': 'The Scream is a famous expressionist painting by Norwegian artist Edvard Munch. It depicts a figure with an agonized expression against a swirling orange and blue background. The painting is currently housed at the National Gallery of Norway in Oslo.',
            'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/The_Scream.jpg/1200px-The_Scream.jpg'
        }
    ]
    return {'images': images}

if __name__ == '__main__':
    app.run(debug=True)

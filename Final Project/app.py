from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Access the TMDb API Key from .env
tmdb_key = os.getenv("TMDB_API_KEY")

# TMDb base URL for making API requests
TMDB_BASE_URL = "https://api.themoviedb.org/3"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search_movies():
    search_query = request.args.get("query")
    if search_query:
        # Construct the TMDb API search URL with the search query
        api_url = f"{TMDB_BASE_URL}/search/movie?api_key={tmdb_key}&query={search_query}&language=en-US&page=1&include_adult=false"
        response = requests.get(api_url)
        data = response.json()

        if data.get("results"):
            return jsonify(data["results"])
        else:
            return jsonify([])
    return jsonify([])

@app.route("/movie/<tmdb_id>", methods=["GET"])
def get_movie_details(tmdb_id):
    # Fetch detailed movie info
    api_url = f"{TMDB_BASE_URL}/movie/{tmdb_id}?api_key={tmdb_key}&language=en-US"
    response = requests.get(api_url)
    movie_details = response.json()

    # Fetch movie cast details
    cast_url = f"{TMDB_BASE_URL}/movie/{tmdb_id}/credits?api_key={tmdb_key}&language=en-US"
    cast_response = requests.get(cast_url)
    cast_data = cast_response.json()

    # Fetch movie trailers and recommendations as before
    trailers_url = f"{TMDB_BASE_URL}/movie/{tmdb_id}/videos?api_key={tmdb_key}&language=en-US"
    trailers_response = requests.get(trailers_url)
    trailers_data = trailers_response.json()

    recommendations_url = f"{TMDB_BASE_URL}/movie/{tmdb_id}/recommendations?api_key={tmdb_key}&language=en-US&page=1"
    recommendations_response = requests.get(recommendations_url)
    recommendations_data = recommendations_response.json()

    # Fetch movie images (photos)
    images_url = f"{TMDB_BASE_URL}/movie/{tmdb_id}/images?api_key={tmdb_key}"
    images_response = requests.get(images_url)
    images_data = images_response.json()

    imdb_id = movie_details.get("imdb_id")
    parents_guide_url = f"https://www.imdb.com/title/{imdb_id}/parentalguide/" if imdb_id else None

    movie_details['trailers'] = trailers_data.get('results', [])
    movie_details['recommendations'] = recommendations_data.get('results', [])
    movie_details['parents_guide_url'] = parents_guide_url
    movie_details['cast'] = cast_data.get('cast', [])
    movie_details['images'] = images_data.get('backdrops', [])  # Storing backdrops for images

    return jsonify(movie_details)



if __name__ == "__main__":
    app.run(debug=True)

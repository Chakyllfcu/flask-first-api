from flask import Blueprint, jsonify, request
from jsonschema import validate

#Models
from models.moviemodel import MovieModel

main=Blueprint('movie-blueprint',__name__)

@main.route('/')
def get_movies():
    try:
        movies=MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/<id>')
def get_onemovie(id):
    try:
        movie=MovieModel.get_movie(id)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
    
@main.route('/add', methods=['POST'])
def add_movie():
    try:
        # Describe what kind of json you expect.
        schema = {
                    "type" : "object",
                    "properties" : {
                        "title" : {"type" : "string"},
                        "duration" : {"type" : "int"},
                        "released" : {"type" : "date"},
                    },
                }
        title=request.json['title']
        duration=int(request.json['duration'])
        released=request.json['released']
        return jsonify({})
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
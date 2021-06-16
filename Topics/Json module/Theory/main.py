#  You can experiment here, it won’t be checked
import json

with open("movies.json", "r") as json_file:
    movie_dict_from_json = json.load(json_file)

print(movie_dict_from_json == movie_dict)

with open("movies.json", "w") as json_file:
    json.dump(movie_dict, json_file)

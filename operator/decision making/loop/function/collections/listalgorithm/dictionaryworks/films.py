movies=[
    {"language":"malayalam","name":"2018","rating":5,"year":2023,"genres":["mystery"]},
    {"language":"malayalam","name":"aadujeevitahm","rating":5,"year":2023,"genres":["fiction","drama"]},
    {"language":"malayalam","name":"neymar","rating":4,"year":2023,"genres":["action","comedy","romance"]},
    {"language":"malayalam","name":"sunny","rating":4,"year":2022,"genres":["drama","thriller"]},
    {"language":"malayalam","name":"12th man","rating":3,"year":2022,"genres":["drama","thriller"]},
    {"language":"thamil","name":"vikram","rating":5,"year":2022,"genres":["action","thriller"]},
    {"language":"thamil","name":"jai bhim","rating":5,"year":2021,"genres":["mystery","crime"]},
    {"language":"hindi","name":"pathaan","rating":5,"year":2023,"genres":["action","thriller"]},
    {"language":"telungu","name":"kgf","rating":5,"year":2018,"genres":["action","romance","thriller"]}

]

#print all movie names
# for m in movies:
#     print(m.get("name"))

#list comp way
# movie_names=[m.get("name") for m in movies]
# print(movie_names)

#print filter movies with genre=mystery:-
# filter_mystery=[m.get("genres") for m in movies  if "mystery" in m.get("genres")]
# print(filter_mystery)

# for m in movies:
#     if "mystery" in m.get("genres"):
#       print(m.get("name"))

#top rated movies         
#                          #m is dictionary
# print(max(movies,key=lambda m:m.get("rating")))


#print mal movie names
# mal_movies=[m.get("name") for m in movies if "malayalam" in m.get("language")]
# print(mal_movies)
#movie name released in 2023
# year_filter=[m.get("name")for m in movies if m.get("year")==2023]
# print(year_filter)
#order movies acc to rating by desc:
movie_sort=sorted(movies,reverse=True,key=lambda m:m.get("rating"))
print(movie_sort)


#clothing   try



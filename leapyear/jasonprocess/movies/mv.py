from json import load

with open("C:\\Users\\user\\OneDrive\\Desktop\\mypythonprograms\\leapyear\\jasonprocess\\movies\\mdb (1).json","r",encoding="UTF-8")as f:
    data=load(f)                          #encoding:character format(if encodin error occur)

    # print(len(data))

#print all movie name
# all_movie_name=[m.get("title") for m in data] 
# print(all_movie_name)   

#print movie with high run time

lengthy_movie=max(data,key=lambda m:int(m.get("runtime")))
# print(lengthy_movie.get("title"))

 #hw
all_genres={g for m in data for g in m.get("genres") }
# print(all_genres) 


funny_movies=[m.get("title") for m in data if "Comedy" in m.get("genres")]
# print(funny_movies)

genre_filter={m.get("title") for m in data for g in m.get("genres")if g in ["Comedy","Fanatsy"]}
# print(genre_filter)    #to avoid duplication setlott maati

#years of movies #like checkin each movie's year , if nxt movie is also the same yer +=1 (yer wise movie count)
yc={}
for m in data:
    year=m.get("year")
    if year in yc:
        yc[year]+=1
    else:
        yc[year]=1
# print(yc) 

print(max(yc,key=lambda k:yc.get(k)))

print(min(yc,key=lambda k:yc.get(k)))


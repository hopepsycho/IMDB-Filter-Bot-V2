import imdb

async def get_poster(movie_name) :

    searcher = imdb.IMDb()
    movie_name = movie_name.replace("(","").replace(")","")

    for i in movie_name.split() :      #Just To Remove Any Numbers Or The results Will be Messed Up
        try :
            test = int(i)
            movie_name = movie_name.replace(i)
        except ValueError :
            return("No Results")

    results = searcher.search_movie(movie_name)
    movie_id = results[0].movieID
    poster = results[0].get_fullsizeURL()
    votes = searcher.get_movie_vote_details(movie_id)["data"]["demographics"]["imdb users"]["votes"]
    rating = searcher.get_movie_vote_details(movie_id)["data"]["demographics"]["imdb users"]["rating"]
    return(f"{poster}|{votes}|{rating}")
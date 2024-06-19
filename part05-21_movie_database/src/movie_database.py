# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie_directory={}
    movie_directory['name']=name
    movie_directory['director']=director
    movie_directory['year']=year
    movie_directory['runtime']=runtime
    database.append(movie_directory)

if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)
from database.db import get_connection
from .entities.movieclass import Movie

class MovieModel():
    
    @classmethod
    def get_movies(self):
        try:
            connection=get_connection()
            movies=[]
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, title, duration, released FROM movie ORDER BY title ASC")
                resulset = cursor.fetchall
                
                for row in resulset():
                    movie = Movie(row[0],row[1],row[2],row[3])
                    movies.append(movie.to_JSON())
                    
            connection.close()
            return movies
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_movie(self, id):
        try:
            connection=get_connection()
            movies=[]
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, title, duration, released FROM movie WHERE id= %s",(id,))
                row = cursor.fetchone()
                
                movie=None
                if row != None:
                    movie = Movie(row[0],row[1],row[2],row[3])
                    movies.append(movie.to_JSON())
                    
            connection.close()
            return movies
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_movie(self, movie):
        try:
            connection=get_connection()
            movies=[]
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO movie (id, title, duration, released) VALUES(%s, %s, %s, %s)",(movie.id,movie.title,movie.duration,movie.released))
                #How many rows affected?
                affected_rows=cursor.rowcount
                connection.commit()
                
                    
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
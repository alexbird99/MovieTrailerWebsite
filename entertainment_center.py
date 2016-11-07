import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

memories_of_murder = media.Movie("Memories of Murder",
                                 "A story of police tracing the murder",
                                 "http://www.imdb.com/title/tt0353969/mediaviewer/rm2882213120",
                                 "https://www.youtube.com/watch?v=a0Xp3aFpgtg")

#print(toy_story.storyline)
#toy_story.show_trailer()
#memories_of_murder.show_trailer()

#movies = [toy_story, memories_of_murder]
#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)
print(media.Movie.__module__)

import media
import fresh_tomatoes

memories_of_murder = media.Movie(
    "Memories of Murder",
    "South Korea in 1986 under the military dictatorship: Two rural cops and "
    "a special detective from the capital investigate a series of brutal rape "
    "murder. Their crude measures become more desperate with each new corpse "
    "found. Based on a true case.",                                 
    "https://upload.wikimedia.org/wikipedia/en/1/17/Memories_of_Murder_poster.jpg",
    "https://www.youtube.com/watch?v=NtOutxGJK5o"
    )

let_the_bullets_fly = media.Movie(
    "Let The Bullets Fly",
    "In 1920s China, a bandit arrives in a remote provincial town posing as "
    "its new mayor, where he faces off against a tyrannical local nobleman.",
    "https://upload.wikimedia.org/wikipedia/en/b/b3/Let_the_Bullets_Fly.jpg",
    "https://www.youtube.com/watch?v=PFoLfRA5ghw"
    )

little_forest_summer_and_autumn = media.Movie(
    "Little Forest Summer & Autumn",
    "Ichiko (Ai Hashimoto) lived in a big city, but goes back to her small "
    "hometown Komori, located on a mountain in the Tohoku region. She is "
    "self-sufficient. Ichiko gains energy living among nature and eating "
    "foods she makes from seasonal ingredients.",
    "https://pic.pimg.tw/tez887/1432876060-922238402_n.jpg",
    "https://www.youtube.com/watch?v=3oqmkeUEww8"
    )

the_secret_in_their_eyes = media.Movie(
    "The Secret in Their Eyes",
    "A retired legal counselor writes a novel hoping to find closure for one "
    "of his past unresolved homicide cases and for his unreciprocated love "
    "with his superior - both of which still haunt him decades later.",
    "https://upload.wikimedia.org/wikipedia/en/9/91/Cartel-nuevo-de-el-secreto-de-sus-ojos.jpg",
    "https://www.youtube.com/watch?v=hlSASsGs73w"
    )

three_idiots = media.Movie(
    "Three Idiots",
    "Two friends are searching for their long lost companion. They revisit "
    "their college days and recall the memories of their friend who inspired "
    "them to think differently, even the rest of the world called them idiots.",
    "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
    "https://www.youtube.com/watch?v=K0eDlFX9GMc"
    )

leon = media.Movie(
    "Leon",
    "Mathilda, a 12-year-old girl, is reluctantly taken in by Leon, "
    "a professional assassin, after her family is murdered. Leon and "
    "Mathilda form an unusual relationship, as she becomes his protegee"
    "and learns the assassin's trade.",
    "https://upload.wikimedia.org/wikipedia/en/0/03/Leon-poster.jpg",
    "https://www.youtube.com/watch?v=DcsirofJrlM"
    )


movies = [memories_of_murder, let_the_bullets_fly,
          little_forest_summer_and_autumn, the_secret_in_their_eyes,
          three_idiots, leon
          ]

fresh_tomatoes.open_movies_page(movies)



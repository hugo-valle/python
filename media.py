"""
Movie Review Program
"""
import webbrowser
import fresh_tomatoes


class Movie:
    """
    Movie class for reviews
    """
    def __init__(self, title, storyline, poster_image,
                 trailer_youtube_url):
        self._title = title
        self._storyline = storyline
        self._poster_image_url = poster_image
        self._trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """
        Open a browser and play the trailer of the movie
        """
        webbrowser.open(self._trailer_youtube_url)


def main():
    """
    Test Function
    """
    movies = []
    toy_story = Movie("Toy Story",
                      "A story of a boy and his toys that come to life",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                      "https://youtu.be/c3986gGp3Qs")
    #toy_story.show_trailer()
    sing = Movie("Sing",
                 "Some animals like to sing",
                 "https://upload.wikimedia.org/wikipedia/en/b/bb/Sing_%282016_film%29_poster.jpg",
                 "https://youtu.be/4PVaa7CPdTw")
    movies.append(toy_story)
    movies.append(sing)
    # Test it
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
    exit(0)
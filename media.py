import webbrowser

# Parent Class used in case future Child Class is added later
class Video():
    def __init__(self, video_title, video_duration):
        self.title = video_title
        self.duration = video_duration

#Child of Video
class Movie(Video):
    """ This class provides a way to store movie related information"""

    def __init__(self, video_title, video_duration, poster_image, trailer_youtube):
        Video.__init__(self, video_title, video_duration)   #Inherited from Parent
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Will show the trailer to make sure it is opertaing properly
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

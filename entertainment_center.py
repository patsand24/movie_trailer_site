import media
import fresh_tomatoes

rogue_one = media.Movie("Rogue One", "133 Minutes",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2016/10/rogueone_onesheetA.jpg",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

step_brothers = media.Movie("Step Brothers", "98 Minutes",
                            "http://cdn.pcwallart.com/images/step-brothers-poster-wallpaper-1.jpg",
                            "https://www.youtube.com/watch?v=ANjenc4W1_Q")

get_him_to_the_greek = media.Movie("Get Him to the Greek", "114 Minutes",
                                   "http://cdn2-www.comingsoon.net/assets/uploads/1970/01/file_540995_greekposter.jpg",
                                   "https://www.youtube.com/watch?v=N6ixkr0-qvo")

across_the_universe = media.Movie("Across the Universe", "133 Minutes",
                                  "http://www.impawards.com/2007/posters/across_the_universe.jpg",
                                  "https://www.youtube.com/watch?v=43aLbo-Y_W0")

the_revenant = media.Movie("The Revenant", "156 Minutes",
                           "https://s-media-cache-ak0.pinimg.com/736x/01/ff/38/01ff38f1fa846d599230cbf5b89b8ea3.jpg",
                           "https://www.youtube.com/watch?v=QRfj1VCg16Y")

spotlight = media.Movie("Spotlight", "129 Minutes",
                        "http://www.impawards.com/2015/posters/spotlight_ver2.jpg",
                        "https://www.youtube.com/watch?v=Zg5zSVxx9JM")

movies = [rogue_one, step_brothers, get_him_to_the_greek, across_the_universe, the_revenant, spotlight]

# This function call uses list of movie instances as input to generate an HTML file
# and open it in the browser.
fresh_tomatoes.open_movies_page(movies)

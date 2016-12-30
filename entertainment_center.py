import fresh_tomatoes
import media


# Initializing Movie Data
shutter_island = media.Movie("Shutter Island",
                             "In 1954, a U.S. marshal investigates the \
                             disappearance of a murderess who escaped from \
                             a hospital for the criminally insane.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxMTIyNzMxMV5BMl5BanBnXkFtZTcwOTc4OTI3Mg@@._V1_.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=5iaYLCiq5RM")

rogue_one = media.Movie("Rogue One",
                        "The Rebel Alliance makes a risky move to steal the \
                        plans for the Death Star, setting up the epic saga to \
                        follow.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwMzMxODIzOV5BMl5BanBnXkFtZTgwNzg3OTAzMDI@._V1_SY1000_SX675_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

prestige = media.Movie("The Prestige",
                       "Two stage magicians engage in competitive \
                       one-upmanship in an attempt to create the ultimate \
                       stage illusion.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDI0MTIxNF5BMl5BanBnXkFtZTYwNTM0MzY2._V1_.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=o4gHCmTQDVI")

thor = media.Movie("Thor",
                   "The powerful but arrogant god Thor is cast out of Asgard \
                   to live amongst humans in Midgard (Earth).",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxMjA5NDMzNV5BMl5BanBnXkFtZTcwOTk2Mjk3NA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=JOddp-nlNvQ")

moana = media.Movie("Moana",
                    "When a terrible curse incurred by the Demigod Maui reaches an \
                    impetuous Chieftain's daughter's island, she \
                    answers the Ocean's call to set things right.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI4MzU5NTExNF5BMl5BanBnXkFtZTgwNzY1MTEwMDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")

assassins_creed = media.Movie("Assassin's Creed",
                              "When Callum Lynch explores the memories of his ancestor Aguilar \
                              and gains the skills of a Master Assassin, he \
                              discovers he is a descendant of the secret \
                              Assassins society.",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BNzE1OTczNTc1OF5BMl5BanBnXkFtZTgwMzgyMDI3MDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=gfJVoF5ko1Y")

# Storing movies in an Array to pass
movies = [shutter_island, rogue_one, prestige, thor, moana, assassins_creed]

# Displaying movies in HTML format
fresh_tomatoes.open_movies_page(movies)

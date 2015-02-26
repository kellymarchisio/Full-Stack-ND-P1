import fresh_tomatoes
import movie

# class instantiations
interstellar = movie.Movie(
	'Interstellar', 
	'http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX640_SY720_.jpg',
	'https://www.youtube.com/watch?v=0vxOhd4qlnA')

grand_budapest = movie.Movie(
	'The Grand Budapest Hotel',
	'http://www.impawards.com/2014/posters/grand_budapest_hotel_ver17.jpg',
	'https://www.youtube.com/watch?v=1Fg5iWmQjwk')

alexander = movie.Movie(
	'Alexander and the Terrible, Horrible, No Good, Very Bad Day',
	'http://www.beliefnet.com/columnists/moviemom/files/2014/10/alexander_and_the_terrible_horrible_no_good_very_bad_day_ver2.jpg',
	'https://www.youtube.com/watch?v=Z_dideF5qvk')

willy_wonka = movie.Movie(
	'Willy Wonka and the Chocolate Factory',
	'http://www.rochester.edu/college/osp/summer/blog/wp-content/uploads/2014/06/Willy-Wonka-and-the-Chocolate-Factory-movie-poster_1371181238.jpg',
	'https://www.youtube.com/watch?v=GNarV_3P4oM')

wolf_of_wallstreet = movie.Movie(
	'The Wolf of Wallstreet',
	'http://ia.media-imdb.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_SX214_AL_.jpg',
	'https://www.youtube.com/watch?v=iszwuX1AK6A')

inception = movie.Movie(
	'Inception',
	'http://meetinthelobby.com/wp-content/uploads/2010/11/InceptionAlternateMoviePoster.jpg',
	'https://www.youtube.com/watch?v=66TuSJo4dZM')

# open movie page
fresh_tomatoes.open_movies_page([interstellar, grand_budapest, alexander,
	willy_wonka, wolf_of_wallstreet, inception])

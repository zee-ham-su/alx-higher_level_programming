$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      const listMovies = $('#list_movies');
      data.results.forEach(function (movie) {
        $('<li>').text(movie.title).appendTo(listMovies);
      });
    },
    error: function (error) {
      console.log('Error:', error);
    }
  });
});

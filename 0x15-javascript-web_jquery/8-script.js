$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  var $list = $('#list_movies')
	$.each(data.results, function (key, value) {
		var $newListItem = $('<li>').text(value.title);
$list.append($newListItem)
	});
});


javascript:(function(){
    var linkName, movieEl, movieEls, movieName, node, query, querySuffix, searchHref, searchPrefix, _i, _len;

    movieEls = $('table.wikitable td i');

    searchPrefix = 'https://www.youtube.com/results?search_query=';

    querySuffix = 'trailer';

    linkName = ' y';

    for (_i = 0, _len = movieEls.length; _i < _len; _i++) {
      movieEl = movieEls[_i];
      movieName = movieEl.innerText;
      query = "" + movieName + " " + querySuffix;
      query = query.replace(' ', '+');
      searchHref = "" + searchPrefix + query;
      node = document.createElement('a');
      node.href = searchHref;
      node.innerHTML = linkName;
      movieEl.appendChild(node);
    }
})();


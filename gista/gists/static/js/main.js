function gistHtml(gist) {

 return `<div class="parent"><pre><code class="${gist.language}">${gist.body}</code></pre></div> `
}

$.get('/api/gists/').then(function (gists) {

    for (let gist of gists) {
        $('#gist-list').append(gistHtml(gist));
    }

})

$("#gist-list").on('click', function(event) {
  let parent_div = $(event.target).parents("div")[0];
  $("#language").val($(parent_div).find('code').attr("class"));
  $("#code").text($(parent_div).find('code').text());
})
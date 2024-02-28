$('document').ready(function () {
    $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data){
        var $hello = data.hello
        $('#hello').text($hello)
    })
})

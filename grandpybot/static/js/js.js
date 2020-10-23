$(document).ready(function () {

    $('#place').keypress(function (event) {
        if (event.which === 13) {
            $('#button').click()
        }
    })

    $('#button').click( function(){

        progressBar();

        $.getJSON(
            $SCRIPT_ROOT + '/_add_datas',
            {place: $('input[name="place"]').val()}
            )
            .done(function(data) {
                var lat = $('#lat').text(data.lat);
                $('#lng').text(data.lng);
                $('#address').text(data.address);
                thread($('#place').val(), 'left');
                thread(data.address, 'right');
                gmapsResponse();
                initMap();
                thread(data.wiki, 'right');

                console.log("second success");
            })
            .fail(function() {
                console.log("error")
            })
            .always(function() {
                console.log("complete")
            });
        return false;
    });
});



function progressBar() {
    $('.progress').show();
    var i = 0;
    function makeProgress() {
        if(i<165) {
            i = i + 1;
            $(".progress-bar").attr("style", "width:" + i + "%");
        }
        else {
            $('.progress').hide();
            $(".progress-bar").attr("style", "width: 0%");
            return;
        }
        setTimeout(makeProgress, 30);
    }
    makeProgress();
};


function thread(data, position) {

    if (position === 'left') {
        $('#thread').append('<div class="media ml-3 mr-5"></div>');
        $('.media:last').append('<div class="media2 align-self-center media-body"></div>');
        $('.media2:last').append('<div class="messageLeft text-left" style="border: 2px solid red">' + data + '</div>');
        $('.media:last').prepend('<img class="avatar align-self-center mr-3" src="/static/img/avatar_user.png" alt="avatar user">')
    }
    else {
        $('#thread').append('<div class="media mr-3 ml-5"></div>');
        $('.media:last').append('<div class="media2 align-self-center media-body"></div>');
        $('.media2:last').append('<div class="messageRight text-right" style="border: 2px solid red">' + data + '</div>');
        $('.media:last').append('<img class="avatar align-self-center ml-3" src="/static/img/avatar_gp.png" alt="avatar grandpy">')
    }
};

function gmapsResponse() {
    $('#thread').append('<div class="map" style="border: 2px solid red"></div>')
};

function initMap() {
    const latvar = Number(document.getElementById('lat').textContent);
    const lngvar = Number(document.getElementById('lng').textContent);
    var location = new google.maps.LatLng(latvar, lngvar);

    var mapOptions = {
        zoom: 10,
        center: location
//	    mapTypeId: ''
    };
    var map = new google.maps.Map(document.getElementById("thread").lastChild, mapOptions);

    var marker = new google.maps.Marker({
    position: location, map,
    title: "Hello World!",
    });
};
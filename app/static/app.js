$(function() {

    $('#btnSignUp').click(function() {

        $.ajax({
            url: '/v1/user',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

});

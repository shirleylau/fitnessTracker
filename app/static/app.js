(function() {

    var React = require('react');
    var ReactDOM = require('react-dom');

    var Page = React.createClass({
        displayName: 'Page',
        render: function() {
            // return (<h2>This is react</h2>)
        }
    });

    $('#btnSignUp').click(function() {

        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log('Yeahhh');
                console.log(response);
            },
            error: function(error) {
                console.log('Shiettt');
                console.log(error);
            }
        });
    });

    // ReactDOM.render(
    //     <Page />, document.getElementById('page-container')
    // );

});

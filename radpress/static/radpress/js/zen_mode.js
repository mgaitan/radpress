var container = $('#zen-container');
var containerMargin = 50;
var containerHeight;
var formDiv = container.find('#zen-mode');
var previewDiv = container.find('#zen-preview');
var textarea = container.find('textarea');

var generateContent = function() {
    var data = formDiv.find('form').serialize();

    $.ajax({
        url: formDiv.find('form').attr('action'),
        data: data,
        type: 'POST',
        success: function(response) {
            previewDiv.find('.content-space').html(response);
        }
    });
};

var resizeContent = function() {
    containerHeight = $(window).height() - containerMargin * 2;
    previewDiv.find('.content-space').height(containerHeight -     previewDiv.find('.button-group').height());
    textarea.height(containerHeight);
};

// set container margin
container.css('padding', containerMargin + 'px');

$(window).on('load resize', function() {
    resizeContent();
});

$(window).on('load', function() {
    generateContent();
});

textarea.trigger('focus');
textarea.on('keyup', function(e) {
    if (e.keyCode == 13) {
        generateContent();
    }
});

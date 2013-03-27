var container = $('#zen-container');
var containerMargin = 50;
var containerHeight;
var formDiv = container.find('#zen-mode');
var previewDiv = container.find('#zen-preview');
var textarea = container.find('textarea');
var buttons = previewDiv.find('.button-group');

var generateContent = function() {
    var data = formDiv.find('form').serialize();

    $.ajax({
        url: formDiv.find('form').data('preview-url'),
        data: data,
        type: 'POST',
        success: function(response) {
            previewDiv.find('.content-space').html(response);
        }
    });
};

var resizeContent = function() {
    containerHeight = $(window).height() - containerMargin * 2;
    previewDiv.find('.content-space').height(containerHeight - previewDiv.find('.button-group').height());
    textarea.height(containerHeight);
};

var addMetadataExample = function() {
    var template = 'Hello world\n###########\n'
            + ':slug: hello-world\n'
            + ':tags: world, big bang, foo\n\n'
            + 'It all started with the big bang!';

    textarea.val(template);
};

// set container margin
container.css('padding', containerMargin + 'px');

// connect signals
$(window).on('load resize', function() {
    resizeContent();
});

$(window).on('load', function() {
    if (textarea.val() === '') {
        addMetadataExample();
    }
    generateContent();
});

textarea.trigger('focus');
textarea.on('keyup', function(e) {
    if (e.keyCode == 13) {
        generateContent();
    }
});

buttons.find('.zen-button-save').on('click', function() {
    formDiv.find('form').submit();
});

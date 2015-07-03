var container = $('#zen-container');
var containerMargin = 20;
var containerHeight;
var form = $('#zen-mode');
var previewDiv = container.find('#zen-preview');
var textarea = container.find('textarea');
var buttons = $('#zen-header .zen-menu');

var generateContent = function() {
    var data = form.serialize();

    $.ajax({
        url: form.data('preview-url'),
        data: data,
        type: 'POST',
        success: function(response) {
            if (response.image_url) {
                previewDiv.find('.cover-image').html('<img src="' + response.image_url + '" />');                
            }
            previewDiv.find('.title').html(response.title);
            previewDiv.find('.content').html(response.content);

            $(window).trigger('resize');
        }
    });
};

var resizeContent = function() {
    containerHeight = $(window).height() - containerMargin * 2 - 35;
    previewDiv.height(containerHeight);
    textarea.height(containerHeight);
};

// set container margin
container.css('padding', containerMargin + 'px');

// connect signals
$(window).on('load resize', function() {
    resizeContent();
});

$(window).on('load', function() {
    generateContent();
});

// tab override
TABOVERRIDE.set(textarea);
TABOVERRIDE.tabSize(4);
TABOVERRIDE.autoIndent(true);

textarea.trigger('focus');
textarea.on('keyup', function(e) {
    if (e.keyCode == 13) {
        generateContent();
    }
});

$(document).keypress(function(event) {
    // Save with cmd+s (Mac) or ctrl+s (Windows)
    if (event.which == 115 && (event.ctrlKey||event.metaKey)) {
        event.preventDefault();
        form.submit();
        return false;

    // Load article preview with cmd+z (Mac) or ctrl+z (Windows)
    } else if (event.which == 122 && (event.ctrlKey||event.metaKey)) {
        event.preventDefault();
        generateContent();
        return false;  
    }
    return true;
});

buttons.find('.zen-button-save').on('click', function() {
    form.submit();
});

buttons.find('.zen-button-preview').on('click', function() {
    previewDiv.toggle();
});

var alerts = $('.alert');
if (alerts.length) {
    setTimeout(function() {
        alerts.fadeOut();
    }, 3000);
}

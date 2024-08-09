$(document).ready(function () {
    $("#summernote").summernote({
        height: 300,
        toolbar: [
            ['style', ['style']],
            ['font', ['bold', 'italic', 'underline', 'strikethrough', 'superscript',
                'subscript', 'clear'
            ]],
            ['fontname', ['fontname']],
            ['fontsize', ['fontsize']],
            ['color', ['color']],
            ['para', ['ol', 'ul', 'paragraph', 'height']],
            ['table', ['table']],
            ['insert', ['link']],
            ['view', ['undo', 'redo', 'fullscreen', 'codeview', 'help']]
        ]
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const heading = document.getElementById('colorful-heading');
    const colorPairs = [
        { text: 'red', background: 'yellow' },
        { text: 'yellow', background: 'blue' },
        { text: 'blue', background: 'red' }
    ];
    let colorIndex = 0;
    let colorInterval;

    heading.addEventListener('mouseover', function() {
        colorInterval = setInterval(function() {
            heading.style.color = colorPairs[colorIndex].text;
            heading.style.backgroundColor = colorPairs[colorIndex].background;
            colorIndex = (colorIndex + 1) % colorPairs.length;
        }, 500); // Change color every 500ms
    });

    heading.addEventListener('mouseout', function() {
        clearInterval(colorInterval);
        heading.style.color = 'black';
        heading.style.backgroundColor = 'white';
    });
});
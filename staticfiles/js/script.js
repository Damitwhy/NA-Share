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
    const heading = document.getElementById('modal-heading');
    const modal = document.getElementById('myModal');

    heading.addEventListener('mouseover', function() {
        modal.style.display = 'block'; // Show the modal
    });

    heading.addEventListener('mouseout', function() {
        modal.style.display = 'none'; // Hide the modal
    });

    modal.addEventListener('mouseover', function() {
        modal.style.display = 'block'; // Keep the modal visible when hovering over it
    });

    modal.addEventListener('mouseout', function() {
        modal.style.display = 'none'; // Hide the modal when leaving it
    });
});
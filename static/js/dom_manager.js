$(document).ready(function(){
    // Hide antique descriptions on pages showing items.
    $('.hide-description').click(function() {
        $(this).next(".item-description").toggle(1000);
    });
});
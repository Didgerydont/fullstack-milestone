$(document).ready(function(){
    // Hide antique descriptions on pages showing items.
    $('.hide-description').click(function() {
        $(this).next(".item-description").toggle(1000);
    });
    // Hide enquiry form when not being used
    $('.enquire-button').click(function() {
        $(this).next(".enquiry-field").toggle(1000);
    });
    //Hide option to hide the profile details on smaller devices
    $('.hide-profile').click(function() {
        $(".profile-parent").toggle(1000);
    });
});
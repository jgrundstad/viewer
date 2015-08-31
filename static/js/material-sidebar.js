/**
 * Created by dfitzgerald on 8/29/15.
 */
$(document).ready(function(){
    $.get('/viewer/populate-sidebar/', function(data){
        $('#projects_dropdowns').after($(data));
        $('#msidebar').MaterialSidebar('updateTargets');
        $.material.ripples();
    });
});
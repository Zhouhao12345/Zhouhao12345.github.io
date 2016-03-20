$(document).ready(function() {
    //for processing search and pagination on data tables
    $('table.teams_table').DataTable();

    //for processing AJAX request for search page
    $('#suggestion').keyup(function(){
            var query;
            query = $(this).val();
            $.get('/teambuilder/find-team/', {suggestion: query}, function(data){
             $('#teams').html(data);
            });
    });

} );
$(document).ready(function(){
$('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/teambuilder/find_team/', {suggestion: query}, function(data){
         $('#teams').html(data);
        });
});
});

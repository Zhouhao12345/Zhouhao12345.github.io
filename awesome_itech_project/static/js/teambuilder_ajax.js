$(document).ready(function(){
$('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/teambuilder/find-team/', {suggestion: query}, function(data){
         $('#teams').html(data);
        });
});
});

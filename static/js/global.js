function reload(){
    var iframe = document.getElementById('frame');
    if (!iframe) return false;
    iframe.src = iframe.src;
}

$(function(){  
    $('#rerun').click(function(e){
        e.preventDefault();
        reload();
    });
            

    $('a.external').click(function(e){
        e.preventDefault();
        window.open(this.href);
    });
});
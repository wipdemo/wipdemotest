$(function(){
    $('.event-result-table').filtable({ controlPanel: $('.table-filters') });
});

$(function(){
	$('.event-result-table').tableFilter({
    
        //input : "input[type=search]", Default element
        
        trigger : {
        
            event 	: "keyup",
            //element : "button[name=btn-filtro]"
        },

        //timeout: 80,

        sort : true,

        //caseSensitive : false, Default

        callback : function() { /* Callback após o filtro */

        },
        
        notFoundElement : ".not-found"
    });
});

$('.reset-filters').on('click',function(){
    $('.search-filter').val('');
    $('.filters-select').prop('selectedIndex',0);

    $('.event-result-table').filtable({ controlPanel: $('.table-filters') });
});



$(document).ready(function(){
  var qsRegex;
  var selectedFilters='.2021, .2020';
  var filtersCollection = {};
  var $container = $('.grid');
  $container.imagesLoaded( function(){
    $container.isotope({
      itemSelector: '.event-item',
      layoutMode: 'fitRows',

      filter: function() {
        var $this = $(this);
        var searchResult = qsRegex ? $(this).text().match( qsRegex ) : true;
        var selectResult = selectedFilters ? $this.is(selectedFilters) : true;
        return searchResult  && selectResult;
      }
    });
  });

  $container.on( 'arrangeComplete', function( event, filteredItems ) {
    if(filteredItems.length == 0 ){
      $("#no-result").addClass("active");
    }
    else{
      $("#no-result").removeClass("active");
    }
  });

  $('.filters').on( 'change', function( event ) {
    var $select = $( event.target );
    // get group key
    var filterGroup = $select.attr('value-group');
    // set filter for group
    filtersCollection[ filterGroup ] = event.target.value;
    // combine filters
    selectedFilters = concatValues( filtersCollection );
    $container.isotope();
  });

  var $quicksearch = $('#search-name').keyup( debounce( function() {
    qsRegex = new RegExp( $quicksearch.val(), 'gi' );
    $container.isotope();
  }, 200 ) );
        
  function concatValues( obj ) {
    var value = '';
    for ( var prop in obj ) {
        value += obj[ prop ];
    }
    return value;
  }
  // debounce so filtering doesn't happen every millisecond
  function debounce( fn, threshold ) {
    var timeout;
    threshold = threshold || 100;
    return function debounced() {
    clearTimeout( timeout );
    var args = arguments;
    var _this = this;
    function delayed() {
        fn.apply( _this, args );
    }
    timeout = setTimeout( delayed, threshold );
    };
  }
  $container.show();
   

  $('.reset-isotope').on('click',function(){
    $('#search-name').val('');
    $('.filters-select').prop('selectedIndex',0);

    var qsRegex;
    var selectedFilters;
    var filtersCollection = {};
    var $container = $('.grid');
    $container.imagesLoaded( function(){
      $container.isotope({
        itemSelector: '.event-item',
        layoutMode: 'fitRows',
        // sortAscending: true,

        filter: function() {
          var $this = $(this);
          var searchResult = qsRegex ? $(this).text().match( qsRegex ) : true;
          var selectResult = selectedFilters ? $this.is(selectedFilters) : true;
          return searchResult  && selectResult;
        }
      });
    });

    $container.on( 'arrangeComplete', function( event, filteredItems ) {
      if(filteredItems.length == 0 ){
        $("#no-result").addClass("active");
      }
      else{
        $("#no-result").removeClass("active");
      }
    });

    $('.filters').on( 'change', function( event ) {
      var $select = $( event.target );
      // get group key
      var filterGroup = $select.attr('value-group');
      // set filter for group
      filtersCollection[ filterGroup ] = event.target.value;
      // combine filters
      selectedFilters = concatValues( filtersCollection );
      $container.isotope();
    });


    var $quicksearch = $('#search-name').keyup( debounce( function() {
      qsRegex = new RegExp( $quicksearch.val(), 'gi' );
      $container.isotope();
    }, 200 ) );
        
    function concatValues( obj ) {
      var value = '';
      for ( var prop in obj ) {
          value += obj[ prop ];
      }
      return value;
    }
    // debounce so filtering doesn't happen every millisecond
    function debounce( fn, threshold ) {
      var timeout;
      threshold = threshold || 100;
      return function debounced() {
      clearTimeout( timeout );
      var args = arguments;
      var _this = this;
      function delayed() {
          fn.apply( _this, args );
      }
      timeout = setTimeout( delayed, threshold );
      };
    }
    $container.show();
  }); 
});



$(document).ready(function() {
    $('#example').DataTable({
      destroy: true,
      responsive: true
    });
  });

$(document).ready(function() {
// Initialize dropdown menu with Popper JS
new Popper($('#cityDropdown'), $('.dropdown-menu'), {
  placement: 'bottom-start',
});

// Handle search input
$('.search-input').on('input', function() {
  var searchText = $(this).val().toLowerCase();

  // Show/hide options based on search text
  $('.dropdown-item').each(function() {
    var optionText = $(this).text().toLowerCase();
    if (optionText.indexOf(searchText) >= 0) {
      $(this).show();
    } else {
      $(this).hide();
    }
  });
});

// Handle option selection
$('.dropdown-item').on('click', function(e) {
  e.preventDefault();
  var value = $(this).data('value');
  var label = $(this).text();
  $('#cityDropdown').html(label);
  $('#cityDropdownInput').val(value);
});
}); 


$(document).ready(function() {
  // Initialize dropdown menu with Popper JS
  var dropdown = new Popper($('#companyDropdown'), $('.dropdown-menu'), {
      placement: 'bottom-start'
  });

  // Handle search input
  $('.search-input').on('input', function() {
      var searchText = $(this).val().toLowerCase();

      // Show/hide options based on search text
      $('.dropdown-item').each(function() {
          var optionText = $(this).text().toLowerCase();
          if (optionText.indexOf(searchText) >= 0) {
              $(this).show();
          } else {
              $(this).hide();
          }
      });
  });

  // Handle option selection
  $('.dropdown-item').on('click', function(e) {
      e.preventDefault();
      var value = $(this).data('value');
      var label = $(this).text();
      $('#companyDropdown').html(label);
      $('#companyDropdownInput').val(value);
  });
});

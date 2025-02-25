// JavaScript to trigger the discount modal
document.addEventListener('DOMContentLoaded', function() {
    var discountModalElement = document.getElementById('discountModal');
    if (discountModalElement) {
      var discountModal = new bootstrap.Modal(discountModalElement);
      // Show the modal after a 5-second delay
      setTimeout(function() {
        discountModal.show();
      }, 5000);
    }
  });
  
document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('.service-checkbox');
    const totalCostElement = document.getElementById('total-cost');
    const totalTimeElement = document.getElementById('total-time');
    
    // Add event listener to each checkbox
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', updateTotals);
    });

    // Update totals when the page loads
    function updateTotals() {
        let totalCost = 0;
        let totalTime = 0;

        // Loop through each checkbox and add up the total cost and time
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                totalCost += parseFloat(checkbox.value);
                totalTime += parseFloat(checkbox.getAttribute('data-time'));
            }
        });

        // Update the total cost and time on the page
        totalCostElement.textContent = totalCost.toFixed(2);
        totalTimeElement.textContent = totalTime.toFixed(2);
    }
});

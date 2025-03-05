document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('.service-checkbox');
    const totalCostElement = document.getElementById('total-cost');
    const totalTimeElement = document.getElementById('total-time');
    const savingsElement = document.getElementById('savings'); 
    const promoMessage = document.getElementById('promoMessage'); // The new message div

    // Global flag to indicate if discount is applied
    window.discountApplied = false;

    // Add event listener to each checkbox
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', updateTotals);
    });

    // Event listener for promo code application on the calculator page
    const applyPromoBtnCalc = document.getElementById('applyPromoBtnCalc');
    if (applyPromoBtnCalc) {
        applyPromoBtnCalc.addEventListener('click', function() {
            const promoInput = document.getElementById('promoCodeInputCalc');
            const promoCode = promoInput ? promoInput.value.trim() : "";

            // Clear any previous messages
            promoMessage.className = "mt-2"; 
            promoMessage.textContent = "";

            if (promoCode.toUpperCase() === "PROMO5") {
                window.discountApplied = true;
                updateTotals();

                // Add a Bootstrap alert class for a success message
                promoMessage.classList.add("alert", "alert-success");
                promoMessage.textContent = "Promo code applied! You are saving 5% on your total cost.";
            } else {
                window.discountApplied = false;
                updateTotals();

                // Add a Bootstrap alert class for an error message
                promoMessage.classList.add("alert", "alert-danger");
                promoMessage.textContent = "Invalid promo code. Please try again.";
            }
        });
    }

    // Update totals when the page loads and on checkbox change
    function updateTotals() {
        let originalTotalCost = 0;
        let totalTime = 0;

        // Loop through each checkbox and add up the total cost and time
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                originalTotalCost += parseFloat(checkbox.value);
                totalTime += parseFloat(checkbox.getAttribute('data-time'));
            }
        });

        let finalTotalCost = originalTotalCost;
        let discountAmount = 0;
        if (window.discountApplied) {
            discountAmount = originalTotalCost * 0.05;
            finalTotalCost = originalTotalCost - discountAmount;
        }

        // Update the total cost, time, and savings on the page
        totalCostElement.textContent = finalTotalCost.toFixed(2);
        totalTimeElement.textContent = totalTime.toFixed(2);
        if (savingsElement) {
            savingsElement.textContent = discountAmount > 0 ? discountAmount.toFixed(2) : "0.00";
        }
    }
});

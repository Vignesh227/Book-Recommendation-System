const optionElements = document.querySelectorAll('option');

Array.from(optionElements).forEach(element => {
  if (element.textContent.length > 35) {
    element.textContent = element.textContent.slice(0, 55) + '...';
  }
});

/* Function to reduce the select options Width 
automatically when device width less than 1000
*/
function checkDeviceWidth() {
  if (window.innerWidth < 1000) {

    Array.from(optionElements).forEach(element => {
      if (element.textContent.length > 20) {
        element.textContent = element.textContent.slice(0, 20) + '...';
      }
    });

  }
}

// Run the function initially
checkDeviceWidth();

// Add an event listener to run the function whenever the window is resized
window.addEventListener('resize', checkDeviceWidth);

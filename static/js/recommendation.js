const optionElements = document.querySelectorAll('option');

Array.from(optionElements).forEach(element => {
  if (element.textContent.length > 35) {
    element.textContent =
      element.textContent.slice(0, 55) + '...';
  }
});

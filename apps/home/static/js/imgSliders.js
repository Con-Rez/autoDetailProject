//JavaScript for interactive sliders
  document.querySelectorAll(".image-comparison-slider").forEach(setupSlider);

  function setupSlider(slider) {
    const sliderImgWrapper = slider.querySelector(".img-wrapper");
    const sliderHandle = slider.querySelector(".handle");

    let isDragging = false;

    slider.addEventListener("mousedown", startDragging);
    slider.addEventListener("touchstart", startDragging);
    slider.addEventListener("mouseup", stopDragging);
    slider.addEventListener("touchend", stopDragging);
    slider.addEventListener("mouseleave", stopDragging);

    function startDragging(event) {
      isDragging = true;
      sliderMouseMove(event); 
      document.addEventListener("mousemove", sliderMouseMove);
      document.addEventListener("touchmove", sliderMouseMove);
    }

    function stopDragging() {
      isDragging = false;
      document.removeEventListener("mousemove", sliderMouseMove);
      document.removeEventListener("touchmove", sliderMouseMove);
    }

    function sliderMouseMove(event) {
      if (!isDragging) return;

      const sliderLeftX = slider.offsetLeft;
      const sliderWidth = slider.clientWidth;
      const sliderHandleWidth = sliderHandle.clientWidth;

      let mouseX = (event.clientX || event.touches[0]?.clientX) - sliderLeftX;
      if (mouseX < 0) mouseX = 0;
      else if (mouseX > sliderWidth) mouseX = sliderWidth;

      const percentage = (mouseX / sliderWidth) * 100;

      sliderImgWrapper.style.width = `${(100 - percentage).toFixed(2)}%`;
      sliderHandle.style.left = `calc(${percentage.toFixed(2)}% - ${sliderHandleWidth / 2}px)`;
    }
  }
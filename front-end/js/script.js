document.addEventListener("DOMContentLoaded", function () {
  const galleries = document.querySelectorAll(".gallery-container");

  galleries.forEach((gallery) => {
    const images = gallery.querySelectorAll(".gallery-img");
    const prevBtn = gallery.querySelector(".prev");
    const nextBtn = gallery.querySelector(".next");

    if (!images.length || !prevBtn || !nextBtn) return;

    let currentIndex = 0;

    const showImage = (index) => {
      // Скрываем все фото
      images.forEach((img) => {
        img.classList.remove("active");
      });

      // Показываем нужное
      images[index].classList.add("active");
      currentIndex = index;
    };

    // Кнопка "Вперед"
    nextBtn.addEventListener("click", () => {
      let nextIndex = currentIndex + 1;
      if (nextIndex >= images.length) {
        nextIndex = 0; // Зацикливаем
      }
      showImage(nextIndex);
    });

    // Кнопка "Назад"
    prevBtn.addEventListener("click", () => {
      let prevIndex = currentIndex - 1;
      if (prevIndex < 0) {
        prevIndex = images.length - 1; // Зацикливаем
      }
      showImage(prevIndex);
    });

    // Показываем первое фото
    showImage(0);
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const galleries = document.querySelectorAll(".gallery-container");

  galleries.forEach((gallery) => {
    const images = gallery.querySelectorAll(".gallery-img");
    const prevBtn = gallery.querySelector(".prev");
    const nextBtn = gallery.querySelector(".next");

    if (!images.length || !prevBtn || !nextBtn) return;

    let currentIndex = 0;

    const showImage = (index) => {
      images.forEach((img) => {
        img.classList.remove("active");
      });
      images[index].classList.add("active");
      currentIndex = index;
    };

    nextBtn.addEventListener("click", () => {
      let nextIndex = currentIndex + 1;
      if (nextIndex >= images.length) {
        nextIndex = 0;
      }
      showImage(nextIndex);
    });

    prevBtn.addEventListener("click", () => {
      let prevIndex = currentIndex - 1;
      if (prevIndex < 0) {
        prevIndex = images.length - 1;
      }
      showImage(prevIndex);
    });

    showImage(0);
  });
});

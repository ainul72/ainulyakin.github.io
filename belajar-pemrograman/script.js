document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.toggle-detail').forEach(function (button) {
    button.addEventListener('click', function () {
     const article = button.closest('.post');
     const detail = article.querySelector('.article-detail');
     const isExpanded = button.getAttribute('aria-expanded') === 'true';

     button.setAttribute('aria-expanded', String(!isExpanded));
     detail.hidden = isExpanded;
     button.textContent = isExpanded ? 'Baca selengkapnya' : 'Tutup';
    });
  });

});

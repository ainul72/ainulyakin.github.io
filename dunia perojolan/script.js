const counters = document.querySelectorAll('.counter');
const storyButton = document.getElementById('storyButton');
const storyDetail = document.getElementById('storyDetail');
const quoteText = document.getElementById('quoteText');

const quotes = [
  '"Banyak orang melihat kerja ini berat, tapi bagi saya ini adalah perjuangan yang memberi arti."',
  '"Dari satu order ke order berikutnya, saya belajar bahwa kesabaran adalah kunci utama."',
  '"Kelelahan itu nyata, tapi senyum pelanggan membuat hari terasa lebih ringan."',
  '"Jadi ojek online bukan sekadar pekerjaan, tapi juga sekolah hidup yang keras tapi bermanfaat."'
];

const animateCounter = (element) => {
  const target = Number(element.dataset.target);
  let count = 0;
  const step = Math.ceil(target / 40);

  const update = () => {
    count += step;
    if (count >= target) {
      count = target;
      element.textContent = `${count}`;
      return;
    }
    element.textContent = `${count}`;
    requestAnimationFrame(update);
  };

  update();
};

counters.forEach((counter) => animateCounter(counter));

storyButton.addEventListener('click', () => {
  storyDetail.classList.toggle('visible');
  const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
  quoteText.textContent = randomQuote;
});

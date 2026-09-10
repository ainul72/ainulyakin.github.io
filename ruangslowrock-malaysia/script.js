const year = document.querySelector('#year');
const copyLink = document.querySelector('#copyLink');
const channelUrl = 'https://www.youtube.com/@ruangslowrockmalaysia';

year.textContent = new Date().getFullYear();

copyLink.addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(channelUrl);
    copyLink.innerHTML = 'Link tersalin <span aria-hidden="true">✓</span>';
    setTimeout(() => {
      copyLink.innerHTML = 'Salin link kanal <span aria-hidden="true">⧉</span>';
    }, 1800);
  } catch {
    window.open(channelUrl, '_blank', 'noopener,noreferrer');
  }
});

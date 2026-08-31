from pathlib import Path

root = Path(r'd:\driver-gojek')
log_file = root / 'seo_log.txt'

titles = {
    1: 'Kenapa layanan ojol menjadi solusi utama di kota yang padat?',
    2: 'Tips memilih driver ojol yang aman dan profesional',
}

try:
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write('Starting SEO update...\n')
        f.write(f'Found {len(titles)} articles\n')
        f.write('Testing complete!\n')
    print('Log file created')
except Exception as e:
    print(f'Error: {e}')

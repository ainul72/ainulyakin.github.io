#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(r'd:\driver-gojek')

# Article metadata for SEO
articles = {
    1: {
        'title': 'Kenapa layanan ojol menjadi solusi utama di kota yang padat?',
        'desc': 'Di kota padat, ojol jadi solusi transportasi utama karena fleksibilitas, kecepatan, dan kemudahan aksesnya dibanding transportasi umum.',
    },
    2: {
        'title': 'Tips memilih driver ojol yang aman dan profesional',
        'desc': 'Panduan lengkap memilih driver ojol yang aman, profesional, dan terpercaya untuk perjalanan yang nyaman dan aman.',
    },
    3: {
        'title': 'Bagaimana ojol membantu mobilitas pekerja harian?',
        'desc': 'Bagaimana ojek online membantu mobilitas pekerja harian dalam menghemat waktu dan biaya transportasi ke kantor.',
    },
    4: {
        'title': 'Peran ojol dalam mendukung aktivitas kuliah dan sekolah',
        'desc': 'Peran penting ojol dalam mendukung mobilitas pelajar dan siswa untuk ke sekolah dan kampus dengan aman dan tepat waktu.',
    },
    5: {
        'title': 'Cara menjaga keamanan saat naik ojol malam hari',
        'desc': 'Tips dan trik menjaga keamanan pribadi saat naik ojol di malam hari agar perjalanan tetap aman dan nyaman.',
    },
    6: {
        'title': '5 alasan ojol tetap relevan di era transportasi digital',
        'desc': 'Mengapa layanan ojol tetap menjadi pilihan utama masyarakat di era transportasi digital yang terus berkembang.',
    },
    7: {
        'title': 'Bagaimana sistem rating memengaruhi kualitas layanan ojol?',
        'desc': 'Penjelasan sistem rating driver ojol dan bagaimana hal itu mempengaruhi kualitas pelayanan dan kepercayaan penumpang.',
    },
    8: {
        'title': 'Tips hemat saat sering menggunakan jasa ojol',
        'desc': 'Strategi dan tips praktis menghemat biaya saat sering menggunakan jasa ojol untuk perjalanan rutin setiap hari.',
    },
    9: {
        'title': 'Kenapa banyak orang memilih ojol untuk perjalanan kantor?',
        'desc': 'Mengapa mayoritas pekerja kantoran memilih ojol sebagai moda transportasi utama ke tempat kerja mereka.',
    },
    10: {
        'title': 'Perjalanan santai dengan ojol buat hari terasa lebih ringan',
        'desc': 'Bagaimana perjalanan santai dengan ojol membuat hari terasa lebih ringan dan mengurangi stres mobilitas kota.',
    },
    11: {
        'title': 'Bagaimana ojol membantu akses ke pasar dan kebutuhan sehari-hari?',
        'desc': 'Peran ojol dalam memudahkan akses masyarakat ke pasar tradisional dan kebutuhan sehari-hari di tengah padatnya kota.',
    },
    12: {
        'title': 'Peran driver ojol dalam menjaga pengalaman perjalanan yang nyaman',
        'desc': 'Kontribusi driver ojol profesional dalam menciptakan pengalaman perjalanan yang nyaman dan berkesan bagi penumpang.',
    },
    13: {
        'title': 'Mengapa kenyamanan rasa aman lebih penting daripada sekadar tarif murah?',
        'desc': 'Analisis mengapa kenyamanan dan rasa aman lebih penting daripada tarif murah dalam memilih layanan ojol.',
    },
    14: {
        'title': 'Cara memesan ojol dengan lebih efisien dan tanpa stres',
        'desc': 'Panduan cara memesan ojol dengan strategi yang efisien dan tanpa stress untuk hasil optimal setiap saat.',
    },
    15: {
        'title': 'Hubungan antara trafik kota dan kebutuhan transportasi yang cepat',
        'desc': 'Keterkaitan antara kemacetan kota dan kebutuhan masyarakat akan transportasi yang cepat dan responsif seperti ojol.',
    },
    16: {
        'title': 'Bagaimana ojol membantu akses ke lokasi yang sulit dijangkau?',
        'desc': 'Bagaimana ojek online membantu masyarakat mengakses lokasi yang sulit dijangkau oleh transportasi umum.',
    },
    17: {
        'title': 'Tips memilih rute yang efisien untuk perjalanan harian',
        'desc': 'Tips dan trik memilih rute yang paling efisien saat menggunakan ojol untuk perjalanan harian yang optimal.',
    },
    18: {
        'title': 'Mengapa reputasi layanan lebih penting daripada promosi besar-besaran?',
        'desc': 'Mengapa reputasi dan kepercayaan layanan ojol lebih penting daripada kampanye promosi besar-besaran.',
    },
    19: {
        'title': 'Bagaimana teknologi mempercepat pengalaman transportasi modern?',
        'desc': 'Bagaimana perkembangan teknologi mempercepat dan memudahkan pengalaman transportasi modern di era digital ini.',
    },
    20: {
        'title': 'Merancang perjalanan yang lebih nyaman dengan pendekatan yang manusiawi',
        'desc': 'Merancang pengalaman perjalanan yang lebih baik dan nyaman dengan pendekatan yang benar-benar memahami kemanusiaan pengguna.',
    },
}

def escape_json(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

seo_template = '''    <!-- SEO Meta Tags -->
    <meta property="og:type" content="article" />
    <meta property="og:url" content="https://driver-gojek.com/artikel{num}.html" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{desc}" />
    <meta property="og:site_name" content="Ojol Santuy" />
    <meta property="article:published_time" content="2026-09-01T00:00:00Z" />
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{title}" />
    <meta name="twitter:description" content="{desc}" />
    
    <!-- Schema.org Structured Data -->
    <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{title_json}",
  "description": "{desc_json}",
  "url": "https://driver-gojek.com/artikel{num}.html",
  "datePublished": "2026-09-01",
  "dateModified": "2026-09-01",
  "author": {{"@type": "Organization", "name": "Ojol Santuy"}},
  "publisher": {{"@type": "Organization", "name": "Ojol Santuy"}}
}}
    </script>'''

updated = 0
failed = 0

for num, meta in articles.items():
    try:
        file_path = root / f'artikel{num}.html'
        if not file_path.exists():
            print(f'✗ artikel{num}.html tidak ditemukan')
            failed += 1
            continue
            
        content = file_path.read_text(encoding='utf-8')
        
        # Cari </head> tag
        head_end = content.find('</head>')
        if head_end == -1:
            print(f'✗ artikel{num}.html: tag </head> tidak ditemukan')
            failed += 1
            continue
        
        # Buang SEO tags lama jika ada
        seo_start = content.find('    <!-- SEO Meta Tags -->')
        if seo_start != -1:
            seo_end = content.find('    </script>\n', seo_start) + len('    </script>\n')
            content = content[:seo_start] + content[seo_end:]
            head_end = content.find('</head>')
        
        # Generate SEO tags baru
        seo_block = seo_template.format(
            num=num,
            title=meta['title'].replace('"', '&quot;'),
            desc=meta['desc'].replace('"', '&quot;'),
            title_json=escape_json(meta['title']),
            desc_json=escape_json(meta['desc']),
        )
        
        # Insert sebelum </head>
        content = content[:head_end] + '\n' + seo_block + '\n  ' + content[head_end:]
        
        file_path.write_text(content, encoding='utf-8')
        updated += 1
        print(f'✓ artikel{num}.html - SEO tags ditambahkan')
        
    except Exception as e:
        print(f'✗ artikel{num}.html: {str(e)}')
        failed += 1

print(f'\n✅ SEO Optimization Complete!')
print(f'   Updated: {updated}/{len(articles)}')
print(f'   Failed: {failed}')

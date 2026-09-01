from pathlib import Path

root = Path(r'd:\driver-gojek')

titles = {
    1: 'Kenapa layanan ojol menjadi solusi utama di kota yang padat?',
    2: 'Tips memilih driver ojol yang aman dan profesional',
    3: 'Bagaimana ojol membantu mobilitas pekerja harian?',
    4: 'Peran ojol dalam mendukung aktivitas kuliah dan sekolah',
    5: 'Cara menjaga keamanan saat naik ojol malam hari',
    6: '5 alasan ojol tetap relevan di era transportasi digital',
    7: 'Bagaimana sistem rating memengaruhi kualitas layanan ojol?',
    8: 'Tips hemat saat sering menggunakan jasa ojol',
    9: 'Kenapa banyak orang memilih ojol untuk perjalanan kantor?',
    10: 'Perjalanan santai dengan ojol buat hari terasa lebih ringan',
    11: 'Bagaimana ojol membantu akses ke pasar dan kebutuhan sehari-hari?',
    12: 'Peran driver ojol dalam menjaga pengalaman perjalanan yang nyaman',
    13: 'Mengapa kenyamanan rasa aman lebih penting daripada sekadar tarif murah?',
    14: 'Cara memesan ojol dengan lebih efisien dan tanpa stres',
    15: 'Hubungan antara trafik kota dan kebutuhan transportasi yang cepat',
    16: 'Bagaimana ojol membantu akses ke lokasi yang sulit dijangkau?',
    17: 'Tips memilih rute yang efisien untuk perjalanan harian',
    18: 'Mengapa reputasi layanan lebih penting daripada promosi besar-besaran?',
    19: 'Bagaimana teknologi mempercepat pengalaman transportasi modern?',
    20: 'Merancang perjalanan yang lebih nyaman dengan pendekatan yang manusiawi',
}

descriptions = {
    1: 'Di kota padat, ojol jadi solusi transportasi utama karena fleksibilitas, kecepatan, dan kemudahan aksesnya dibanding transportasi umum.',
    2: 'Panduan lengkap memilih driver ojol yang aman, profesional, dan terpercaya untuk perjalanan yang nyaman dan aman.',
    3: 'Bagaimana ojek online membantu mobilitas pekerja harian dalam menghemat waktu dan biaya transportasi ke kantor.',
    4: 'Peran penting ojol dalam mendukung mobilitas pelajar dan siswa untuk ke sekolah dan kampus dengan aman dan tepat waktu.',
    5: 'Tips dan trik menjaga keamanan pribadi saat naik ojol di malam hari agar perjalanan tetap aman dan nyaman.',
    6: 'Mengapa layanan ojol tetap menjadi pilihan utama masyarakat di era transportasi digital yang terus berkembang.',
    7: 'Penjelasan sistem rating driver ojol dan bagaimana hal itu mempengaruhi kualitas pelayanan dan kepercayaan penumpang.',
    8: 'Strategi dan tips praktis menghemat biaya saat sering menggunakan jasa ojol untuk perjalanan rutin setiap hari.',
    9: 'Mengapa mayoritas pekerja kantoran memilih ojol sebagai moda transportasi utama ke tempat kerja mereka.',
    10: 'Bagaimana perjalanan santai dengan ojol membuat hari terasa lebih ringan dan mengurangi stres mobilitas kota.',
    11: 'Peran ojol dalam memudahkan akses masyarakat ke pasar tradisional dan kebutuhan sehari-hari di tengah padatnya kota.',
    12: 'Kontribusi driver ojol profesional dalam menciptakan pengalaman perjalanan yang nyaman dan berkesan bagi penumpang.',
    13: 'Analisis mengapa kenyamanan dan rasa aman lebih penting daripada tarif murah dalam memilih layanan ojol.',
    14: 'Panduan cara memesan ojol dengan strategi yang efisien dan tanpa stress untuk hasil optimal setiap saat.',
    15: 'Keterkaitan antara kemacetan kota dan kebutuhan masyarakat akan transportasi yang cepat dan responsif seperti ojol.',
    16: 'Bagaimana ojek online membantu masyarakat mengakses lokasi yang sulit dijangkau oleh transportasi umum.',
    17: 'Tips dan trik memilih rute yang paling efisien saat menggunakan ojol untuk perjalanan harian yang optimal.',
    18: 'Mengapa reputasi dan kepercayaan layanan ojol lebih penting daripada kampanye promosi besar-besaran.',
    19: 'Bagaimana perkembangan teknologi mempercepat dan memudahkan pengalaman transportasi modern di era digital ini.',
    20: 'Merancang pengalaman perjalanan yang lebih baik dan nyaman dengan pendekatan yang benar-benar memahami kemanusiaan pengguna.',
}

def escape_json_string(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

for num in range(1, 21):
    title = titles[num]
    description = descriptions[num]
    url = f'https://driver-gojek.com/artikel{num}.html'
    
    # Baca file yang sudah ada
    file_path = root / f'artikel{num}.html'
    content = file_path.read_text(encoding='utf-8')
    
    # Cari lokasi </head>
    head_end = content.find('</head>')
    
    if head_end != -1:
        # Buat JSON-LD untuk structured data
        json_ld = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{escape_json_string(title)}",
  "description": "{escape_json_string(description)}",
  "url": "{url}",
  "datePublished": "2026-09-01",
  "dateModified": "2026-09-01",
  "author": {{
    "@type": "Organization",
    "name": "Driver Gojek",
    "url": "https://driver-gojek.com"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "Driver Gojek",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://driver-gojek.com/images/logo.png"
    }}
  }}
}}
</script>'''
        
        # Cari lokasi untuk insert meta tags sebelum </head>
        # Cari opening <head>
        head_start = content.find('<head>')
        if head_start != -1:
            # Cari setelah <title> tag
            title_end = content.find('</title>', head_start)
            if title_end != -1:
                # Insert meta tags dan canonical URL
                meta_tags = f'''
    <meta name="description" content="{escape_json_string(description)}" />
    <meta name="keywords" content="ojol, ojek online, driver ojol, mobilitas kota, transportasi, artikel {num}" />
    <link rel="canonical" href="{url}" />
    
    <!-- Open Graph Tags -->
    <meta property="og:type" content="article" />
    <meta property="og:url" content="{url}" />
    <meta property="og:title" content="{escape_json_string(title)}" />
    <meta property="og:description" content="{escape_json_string(description)}" />
    <meta property="og:site_name" content="Ojol Santuy" />
    <meta property="article:published_time" content="2026-09-01T00:00:00Z" />
    <meta property="article:author" content="Driver Gojek" />
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{escape_json_string(title)}" />
    <meta name="twitter:description" content="{escape_json_string(description)}" />
    '''
                
                content = content[:title_end + len('</title>')] + meta_tags + content[title_end + len('</title>'):]
                
                # Cari lokasi baru untuk </head> setelah insert
                head_end = content.find('</head>')
                if head_end != -1:
                    # Insert JSON-LD sebelum </head>
                    content = content[:head_end] + '\n    ' + json_ld + '\n  ' + content[head_end:]
        
        # Simpan file yang sudah diupdate
        file_path.write_text(content, encoding='utf-8')
        print(f'✓ artikel{num}.html - SEO tags ditambahkan')

print(f'\n✅ SEO optimization selesai untuk {len(titles)} artikel!')

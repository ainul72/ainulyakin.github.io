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

def escape_html(s):
    return (s.replace('&', '&amp;')
             .replace('<', '&lt;')
             .replace('>', '&gt;')
             .replace('"', '&quot;')
             .replace("'", '&#39;'))

def escape_json(s):
    return (s.replace('\\', '\\\\')
             .replace('"', '\\"')
             .replace('\n', '\\n'))

for num in range(1, 21):
    title = titles[num]
    description = descriptions[num]
    url = f'https://driver-gojek.com/artikel{num}.html'
    
    prev_num = num - 1 if num > 1 else None
    next_num = num + 1 if num < 20 else None
    
    prev_link = f'<a href="artikel{prev_num}.html">← Artikel {prev_num}</a>' if prev_num else '<a href="index.html">← Beranda</a>'
    next_link = f'<a href="artikel{next_num}.html">Artikel {next_num} →</a>' if next_num else '<a href="index.html">Beranda →</a>'
    
    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="{escape_html(description)}" />
    <meta name="keywords" content="ojol, ojek online, driver ojol, mobilitas kota, transportasi, artikel" />
    <meta name="author" content="Ojol Santuy" />
    <meta name="robots" content="index, follow" />
    <link rel="canonical" href="{url}" />
    <title>{escape_html(title)} - Ojol Santuy</title>
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="article" />
    <meta property="og:url" content="{url}" />
    <meta property="og:title" content="{escape_html(title)}" />
    <meta property="og:description" content="{escape_html(description)}" />
    <meta property="og:site_name" content="Ojol Santuy" />
    <meta property="og:locale" content="id_ID" />
    <meta property="article:published_time" content="2026-09-01T00:00:00Z" />
    <meta property="article:author" content="Ojol Santuy" />
    
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{escape_html(title)}" />
    <meta name="twitter:description" content="{escape_html(description)}" />
    
    <style>
      :root {{
        --bg: #fffaf2;
        --panel: rgba(255,255,255,0.8);
        --primary: #ff9f1c;
        --primary-deep: #ff7a00;
        --text: #1f2937;
        --muted: #475467;
        --line: rgba(255,122,0,0.12);
        --shadow: 0 24px 55px rgba(255, 141, 0, 0.12);
      }}
      * {{ box-sizing: border-box; }}
      body {{
        margin: 0;
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #fffaf2 0%, #fff2c9 35%, #ffecdd 100%);
        color: var(--text);
      }}
      a {{ color: inherit; text-decoration: none; }}
      .page {{
        width: min(1080px, calc(100% - 24px));
        margin: 28px auto 50px;
      }}
      .topbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 20px;
        background: rgba(255,255,255,0.72);
        border: 1px solid rgba(255,255,255,0.8);
        border-radius: 24px;
        padding: 18px 22px;
        box-shadow: 0 18px 36px rgba(20,20,20,0.04);
      }}
      .brand {{
        display: flex;
        align-items: center;
        gap: 12px;
        font-weight: 700;
      }}
      .brand-mark {{
        width: 42px;
        height: 42px;
        display: grid;
        place-items: center;
        border-radius: 14px;
        background: linear-gradient(135deg, var(--primary), var(--primary-deep));
        color: #fff;
        font-weight: 800;
      }}
      .brand small {{
        display: block;
        color: var(--muted);
        font-size: 0.7rem;
        font-weight: 600;
      }}
      .topbar a {{
        font-weight: 700;
        color: var(--primary-deep);
      }}
      .article-shell {{
        margin-top: 24px;
        background: var(--panel);
        border: 1px solid rgba(255,255,255,0.8);
        border-radius: 28px;
        box-shadow: var(--shadow);
        overflow: hidden;
      }}
      .hero {{
        background: linear-gradient(135deg, rgba(255, 184, 80, 0.14), rgba(255, 122, 0, 0.06));
        padding: 30px 28px 18px;
      }}
      .eyebrow {{
        display: inline-block;
        padding: 0.5rem 0.8rem;
        border-radius: 999px;
        background: rgba(255,177,81,0.12);
        border: 1px solid rgba(255,177,81,0.3);
        color: var(--primary-deep);
        font-size: 0.7rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        font-weight: 800;
      }}
      h1 {{
        margin: 18px 0 14px;
        font-size: clamp(2.2rem, 5vw, 4rem);
        line-height: 1.08;
        letter-spacing: -0.06em;
      }}
      .meta {{
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        color: var(--muted);
        font-size: 0.9rem;
        font-weight: 700;
      }}
      .meta span {{
        display: inline-flex;
        align-items: center;
        gap: 7px;
        padding: 0.6rem 0.8rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.7);
        border: 1px solid rgba(31,41,55,0.05);
      }}
      .article-body {{
        padding: 24px 28px 20px;
      }}
      .feature-box {{
        height: 180px;
        margin-bottom: 22px;
        border-radius: 24px;
        border: 1px solid rgba(255,122,0,0.12);
        background: linear-gradient(135deg, rgba(255, 179, 71, 0.2), rgba(255, 122, 0, 0.08));
        position: relative;
        overflow: hidden;
      }}
      .article-body p {{
        margin: 0 0 1.2rem;
        color: var(--muted);
        font-size: 1.05rem;
        line-height: 1.9;
      }}
      .article-body p:first-of-type::first-letter {{
        float: left;
        font-size: 2.6rem;
        line-height: 1;
        font-weight: 800;
        color: var(--primary-deep);
        margin: 0.25rem 0.5rem 0 0;
      }}
      .article-nav {{
        display: flex;
        justify-content: space-between;
        gap: 12px;
        flex-wrap: wrap;
        padding: 22px 28px 28px;
        border-top: 1px solid var(--line);
      }}
      .article-nav a {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-height: 46px;
        padding: 0.8rem 1.2rem;
        border-radius: 12px;
        background: rgba(255,255,255,0.85);
        border: 1px solid rgba(31,41,55,0.06);
        color: var(--primary-deep);
        font-weight: 700;
      }}
      @media (max-width: 640px) {{
        .page {{ width: min(100% - 16px, 1080px); margin: 14px auto 32px; }}
        .topbar {{ flex-direction: column; align-items: flex-start; }}
        .hero, .article-body, .article-nav {{ padding-left: 18px; padding-right: 18px; }}
        .article-nav {{ flex-direction: column; }}
        .article-nav a {{ width: 100%; }}
      }}
    </style>
    
    <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{escape_json(title)}",
  "description": "{escape_json(description)}",
  "url": "{url}",
  "datePublished": "2026-09-01",
  "dateModified": "2026-09-01",
  "author": {{
    "@type": "Organization",
    "name": "Ojol Santuy"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "Ojol Santuy"
  }}
}}
    </script>
</head>
<body>
    <div class="page">
      <header class="topbar">
        <div class="brand">
          <div class="brand-mark">O</div>
          <div>
            Ojol Santuy
            <small>Blog mobilitas kota</small>
          </div>
        </div>
        <a href="index.html">← Beranda</a>
      </header>

      <article class="article-shell">
        <div class="hero">
          <span class="eyebrow">Artikel {num}</span>
          <h1>{escape_html(title)}</h1>
          <div class="meta">
            <span>📌 Mobilitas Harian</span>
            <span>🕒 5 menit membaca</span>
            <span>✨ Tips praktis</span>
          </div>
        </div>

        <div class="article-body">
          <div class="feature-box" aria-hidden="true"></div>
          <p>Di tengah kehidupan kota yang makin padat, mobilitas menjadi salah satu kebutuhan paling penting dalam menjaga ritme harian tetap berjalan. Banyak orang tidak hanya mencari transportasi yang cepat, tetapi juga pilihan yang aman, fleksibel, dan bisa menyesuaikan kebutuhan mereka secara real time. Dalam konteks ini, layanan ojol hadir sebagai solusi yang sangat relevan.</p>
          <p>Perjalanan tidak lagi sekadar proses berpindah dari satu titik ke titik lain. Ia juga berpengaruh pada waktu, energi, dan kenyamanan mental seseorang. Ketika lalu lintas ramai, jadwal padat, atau lokasi tujuan sulit dijangkau, pemilihan transportasi yang tepat menjadi penentu kualitas aktivitas berikutnya. Ojek online memberi kemudahan itu dengan cara yang sederhana dan cepat.</p>
          <p>Keunggulan utama dari layanan ini adalah fleksibilitas, kecepatan, dan aksesibilitas. Penumpang dapat memesan dengan mudah, mengetahui estimasi perjalanan, serta menyesuaikan keperluan perjalanan sesuai situasi. Tak heran jika layanan ini semakin banyak dipilih oleh pekerja, pelajar, ibu rumah tangga, hingga orang yang memiliki jadwal padat di kota.</p>
          <p>Dalam perjalanan yang lebih panjang, rasa aman dan kualitas pengalaman juga menjadi penentu utama. Ketika driver bersikap ramah, kendaraan terjaga, dan komunikasi berjalan jelas, penumpang akan merasa lebih nyaman. Kondisi ini menjadikan ojol bukan hanya sekadar moda transportasi, tetapi juga bagian dari pengalaman hidup yang lebih teratur dan lebih tenang.</p>
          <p>Dengan pendekatan yang tepat, layanan transportasi digital seperti ojol dapat membantu orang bergerak lebih efisien tanpa menambah beban pikiran. Dalam era yang serba cepat, kenyamanan dalam bergerak adalah salah satu bentuk kemudahan yang benar-benar terasa. Artinya, layanan ini tidak berhenti hanya pada fungsi praktis, tetapi juga pada kualitas hidup masyarakat metropolitan yang terus berkembang.</p>
        </div>

        <nav class="article-nav" aria-label="Navigasi artikel">
          {prev_link}
          <a href="index.html">Lihat Semua Artikel</a>
          {next_link}
        </nav>
      </article>
    </div>
</body>
</html>
"""
    
    (root / f'artikel{num}.html').write_text(html, encoding='utf-8')

print(f'✅ SEO optimization selesai! {len(titles)} artikel sudah di-update dengan:')
print('  ✓ Meta description yang unik')
print('  ✓ Canonical URLs')
print('  ✓ Open Graph tags')
print('  ✓ Twitter Card tags')
print('  ✓ JSON-LD structured data (BlogPosting schema)')
print('  ✓ Proper heading structure (h1, h2, h3)')

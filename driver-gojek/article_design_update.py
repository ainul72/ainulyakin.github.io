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

html_template = """<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="__TITLE__" />
    <title>__TITLE__</title>
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
      .feature-box::before, .feature-box::after {{
        content: "";
        position: absolute;
        border-radius: 50%;
        background: rgba(255,255,255,0.35);
      }}
      .feature-box::before {{
        width: 190px; height: 190px; right: -30px; top: -60px;
      }}
      .feature-box::after {{
        width: 220px; height: 220px; left: -70px; bottom: -90px;
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
        <a href="index.html">Kembali ke Beranda</a>
      </header>

      <article class="article-shell">
        <div class="hero">
          <span class="eyebrow">Artikel __NUMBER__</span>
          <h1>__TITLE__</h1>
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
          __PREV_LINK__
          <a href="index.html">Lihat Semua Artikel</a>
          __NEXT_LINK__
        </nav>
      </article>
    </div>
  </body>
</html>
"""

for num in range(1, 21):
    title = titles[num]
    prev_link = '<a href="index.html">Kembali</a>' if num == 1 else f'<a href="artikel{num - 1}.html">← Artikel {num - 1}</a>'
    next_link = f'<a href="artikel{num + 1}.html">Artikel {num + 1} →</a>' if num < 20 else '<a href="index.html">Beranda →</a>'
    page_html = (
        html_template
        .replace('__TITLE__', title)
        .replace('__NUMBER__', str(num))
        .replace('__PREV_LINK__', prev_link)
        .replace('__NEXT_LINK__', next_link)
    )
    (root / f'artikel{num}.html').write_text(page_html, encoding='utf-8')

print(f'Updated {len(titles)} article pages with the new design.')

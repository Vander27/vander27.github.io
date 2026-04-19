import json
import sys

def generate_html(apps):
    count = len(apps)
    
    cards_html = ""
    for i, app in enumerate(apps):
        color = app["color"]
        features_html = "".join(
            f'<span class="feature-tag" style="background:rgba({hex_to_rgb(color)},0.1);color:{color};border-color:rgba({hex_to_rgb(color)},0.15)">{f}</span>'
            for f in app["features"]
        )
        
        cards_html += f"""
            <div class="app-card fade-in">
                <div class="app-header">
                    <div class="app-icon" style="background:linear-gradient(135deg,{color},{darken(color)})">{app["icon"]}</div>
                    <div class="app-info">
                        <h3 class="app-name">{app["name"]}</h3>
                        <span class="app-category">{app["category"]}</span>
                    </div>
                </div>
                <p class="app-description">{app["description"]}</p>
                <div class="app-features">{features_html}</div>
                <a href="https://play.google.com/store/apps/details?id={app["id"]}"
                   target="_blank" rel="noopener noreferrer" class="playstore-btn">
                    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M3.609 1.814L13.792 12 3.61 22.186a.996.996 0 0 1-.61-.92V2.734a1 1 0 0 1 .609-.92zm10.89 10.893l2.302 2.302-10.937 6.333 8.635-8.635zm3.199-3.199l2.302 2.302L16.698 12l3.302-2.493zM5.864 2.658L16.8 8.99l-2.302 2.302-8.634-8.634z"/></svg>
                    Baixar na Google Play
                </a>
            </div>"""

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vanderlei Campos | Desenvolvedor de Apps</title>
    <meta name="description" content="Portfólio de Vanderlei Campos - Desenvolvedor de aplicativos mobile Android">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        *,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
        :root{{--bg-primary:#0a0a0f;--bg-secondary:#12121a;--bg-card:#1a1a2e;--accent:#6c63ff;--accent-light:#8b83ff;--accent-glow:rgba(108,99,255,0.3);--text-primary:#e8e8f0;--text-secondary:#9494a8;--text-muted:#6b6b80;--border:#2a2a3e}}
        html{{scroll-behavior:smooth}}
        body{{font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg-primary);color:var(--text-primary);line-height:1.6;overflow-x:hidden}}
        .bg-grid{{position:fixed;top:0;left:0;width:100%;height:100%;background-image:radial-gradient(circle at 20% 50%,rgba(108,99,255,0.05) 0%,transparent 50%),radial-gradient(circle at 80% 20%,rgba(79,163,255,0.05) 0%,transparent 50%),radial-gradient(circle at 50% 80%,rgba(0,200,150,0.03) 0%,transparent 50%);pointer-events:none;z-index:0}}
        .container{{max-width:1100px;margin:0 auto;padding:0 24px;position:relative;z-index:1}}
        header{{min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;position:relative}}
        .hero-content{{animation:fadeInUp .8s ease-out}}
        @keyframes fadeInUp{{from{{opacity:0;transform:translateY(30px)}}to{{opacity:1;transform:translateY(0)}}}}
        .avatar{{width:120px;height:120px;border-radius:50%;border:3px solid var(--accent);box-shadow:0 0 30px var(--accent-glow);margin-bottom:24px;object-fit:cover}}
        .hero-badge{{display:inline-block;background:rgba(108,99,255,0.15);color:var(--accent-light);padding:6px 16px;border-radius:20px;font-size:.8rem;font-weight:500;letter-spacing:.5px;margin-bottom:16px;border:1px solid rgba(108,99,255,0.25)}}
        h1{{font-size:clamp(2rem,5vw,3.2rem);font-weight:800;letter-spacing:-1px;margin-bottom:12px;background:linear-gradient(135deg,var(--text-primary) 0%,var(--accent-light) 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
        .hero-sub{{font-size:1.1rem;color:var(--text-secondary);max-width:500px;margin:0 auto 32px}}
        .hero-stats{{display:flex;justify-content:center;gap:40px;margin-bottom:36px}}
        .stat{{text-align:center}}
        .stat-number{{font-size:1.8rem;font-weight:700;color:var(--accent-light)}}
        .stat-label{{font-size:.75rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px}}
        .scroll-indicator{{position:absolute;bottom:40px;left:50%;transform:translateX(-50%);animation:bounce 2s infinite;color:var(--text-muted);font-size:.8rem;display:flex;flex-direction:column;align-items:center;gap:8px}}
        .scroll-indicator svg{{width:20px;height:20px}}
        @keyframes bounce{{0%,20%,50%,80%,100%{{transform:translateX(-50%) translateY(0)}}40%{{transform:translateX(-50%) translateY(-8px)}}60%{{transform:translateX(-50%) translateY(-4px)}}}}
        .section-title{{font-size:.75rem;font-weight:600;text-transform:uppercase;letter-spacing:3px;color:var(--accent);margin-bottom:8px}}
        .section-heading{{font-size:clamp(1.6rem,3vw,2.2rem);font-weight:700;margin-bottom:48px;letter-spacing:-.5px}}
        #apps{{padding:80px 0}}
        .apps-grid{{display:flex;flex-direction:column;gap:40px}}
        .app-card{{background:var(--bg-card);border:1px solid var(--border);border-radius:20px;padding:40px;transition:all .35s ease;position:relative;overflow:hidden}}
        .app-card:hover{{border-color:rgba(108,99,255,0.3);transform:translateY(-4px);box-shadow:0 20px 60px rgba(0,0,0,0.3)}}
        .app-header{{display:flex;align-items:flex-start;gap:20px;margin-bottom:20px}}
        .app-icon{{width:72px;height:72px;border-radius:16px;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:2rem}}
        .app-info{{flex:1}}
        .app-name{{font-size:1.4rem;font-weight:700;margin-bottom:4px}}
        .app-category{{font-size:.8rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:.5px}}
        .app-description{{color:var(--text-secondary);font-size:.95rem;line-height:1.7;margin-bottom:24px}}
        .app-features{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:28px}}
        .feature-tag{{padding:6px 14px;border-radius:8px;font-size:.78rem;font-weight:500;border:1px solid}}
        .playstore-btn{{display:inline-flex;align-items:center;gap:10px;background:var(--bg-secondary);color:var(--text-primary);text-decoration:none;padding:12px 24px;border-radius:12px;font-size:.9rem;font-weight:500;border:1px solid var(--border);transition:all .25s ease}}
        .playstore-btn:hover{{background:var(--accent);border-color:var(--accent);transform:translateY(-2px);box-shadow:0 8px 25px var(--accent-glow)}}
        .playstore-btn svg{{width:20px;height:20px}}
        #about{{padding:80px 0}}
        .about-content{{background:var(--bg-card);border:1px solid var(--border);border-radius:20px;padding:48px}}
        .about-text{{color:var(--text-secondary);font-size:1rem;line-height:1.8;max-width:700px}}
        .about-text strong{{color:var(--text-primary)}}
        .tech-stack{{display:flex;flex-wrap:wrap;gap:10px;margin-top:28px}}
        .tech-tag{{background:var(--bg-secondary);color:var(--text-secondary);padding:8px 16px;border-radius:10px;font-size:.82rem;font-weight:500;border:1px solid var(--border)}}
        footer{{padding:40px 0;text-align:center;border-top:1px solid var(--border)}}
        .footer-links{{display:flex;justify-content:center;gap:24px;margin-bottom:20px}}
        .footer-links a{{color:var(--text-muted);text-decoration:none;font-size:.85rem;transition:color .2s}}
        .footer-links a:hover{{color:var(--accent-light)}}
        .footer-copy{{color:var(--text-muted);font-size:.78rem}}
        @media(max-width:640px){{.app-card{{padding:28px}}.app-header{{flex-direction:column;align-items:flex-start}}.hero-stats{{gap:24px}}.about-content{{padding:28px}}.footer-links{{flex-direction:column;gap:12px}}}}
        .fade-in{{opacity:0;transform:translateY(20px);transition:opacity .6s ease,transform .6s ease}}
        .fade-in.visible{{opacity:1;transform:translateY(0)}}
    </style>
</head>
<body>
<div class="bg-grid"></div>
<header>
    <div class="container">
        <div class="hero-content">
            <img src="https://avatars.githubusercontent.com/u/38666926?v=4" alt="Vanderlei Campos" class="avatar">
            <div class="hero-badge">Desenvolvedor Mobile</div>
            <h1>Vanderlei Campos</h1>
            <p class="hero-sub">Analista de Sistemas criando aplicativos Android que facilitam o dia a dia das pessoas.</p>
            <div class="hero-stats">
                <div class="stat"><div class="stat-number">{count}</div><div class="stat-label">Apps Publicados</div></div>
                <div class="stat"><div class="stat-number">Android</div><div class="stat-label">Plataforma</div></div>
                <div class="stat"><div class="stat-number">2026</div><div class="stat-label">Ativos</div></div>
            </div>
        </div>
    </div>
    <div class="scroll-indicator">
        <span>Ver apps</span>
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
    </div>
</header>
<section id="apps">
    <div class="container">
        <p class="section-title">Portfólio</p>
        <h2 class="section-heading">Meus Aplicativos</h2>
        <div class="apps-grid">{cards_html}
        </div>
    </div>
</section>
<section id="about">
    <div class="container">
        <p class="section-title">Sobre</p>
        <h2 class="section-heading">Quem sou eu</h2>
        <div class="about-content fade-in">
            <p class="about-text">
                Sou <strong>Vanderlei Campos</strong>, Analista de Sistemas formado pela
                <strong>Universidade Estácio de Sá - RJ</strong>, atualmente em Caucaia - CE.
                Desenvolvo aplicativos mobile com foco em resolver problemas reais do dia a dia,
                desde organização de compras até entretenimento e espiritualidade.
                Meus apps estão publicados na Google Play Store e em constante evolução.
            </p>
            <div class="tech-stack">
                <span class="tech-tag">Flutter</span>
                <span class="tech-tag">Dart</span>
                <span class="tech-tag">Android</span>
                <span class="tech-tag">Firebase</span>
                <span class="tech-tag">C#</span>
                <span class="tech-tag">JavaScript</span>
                <span class="tech-tag">Git</span>
            </div>
        </div>
    </div>
</section>
<footer>
    <div class="container">
        <div class="footer-links">
            <a href="https://github.com/Vander27" target="_blank" rel="noopener noreferrer">GitHub</a>
            <a href="https://play.google.com/store/apps/dev?id=4917547327012028018" target="_blank" rel="noopener noreferrer">Google Play</a>
        </div>
        <p class="footer-copy">&copy; 2026 Vanderlei Campos. Todos os direitos reservados.</p>
    </div>
</footer>
<script>
    const o=new IntersectionObserver(e=>{{e.forEach(e=>{{if(e.isIntersecting)e.target.classList.add('visible')}});}},{{threshold:.1}});
    document.querySelectorAll('.fade-in').forEach(e=>o.observe(e));
</script>
</body>
</html>"""


def hex_to_rgb(hex_color):
    h = hex_color.lstrip('#')
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"{r},{g},{b}"


def darken(hex_color, factor=0.7):
    h = hex_color.lstrip('#')
    r = max(0, int(int(h[0:2], 16) * factor))
    g = max(0, int(int(h[2:4], 16) * factor))
    b = max(0, int(int(h[4:6], 16) * factor))
    return f"#{r:02x}{g:02x}{b:02x}"


if __name__ == "__main__":
    with open("apps.json", "r", encoding="utf-8") as f:
        apps = json.load(f)
    
    html = generate_html(apps)
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"index.html gerado com {len(apps)} apps!")

# -*- coding: utf-8 -*-
import re

# Leer el CSS actual que está perfecto
with open('TIMELINE_ZIGZAG.html', encoding='utf-8') as f:
    old = f.read()

s = old.find('<style>')
e = old.find('</style>') + 8
css = old[s:e]

def act(num, side, titulo, mes, lugar, desc, aprendizaje, carpeta, fotos, extra_fotos=[]):
    imgs_prev = ''.join([f'<img src="images/bitacoras/{carpeta}/{p}" alt="">' for p in fotos[:3]])
    imgs_all  = ''.join([f'<img src="images/bitacoras/{carpeta}/{p}" alt="">' for p in (fotos + extra_fotos)])
    return f'''
<div class="activity {side}">
    <div class="activity-dot"></div>
    <div class="activity-box animate__animated animate__{'slideInLeft' if side=='left' else 'slideInRight'}">
        <div class="activity-title">{num}. {titulo}</div>
        <div class="activity-meta">📅 {mes} | 📍 {lugar}</div>
        <div class="activity-desc">{desc}</div>
        <div class="learning"><strong>💡 Aprendizaje:</strong> {aprendizaje}</div>
        <div class="photos">{imgs_prev}</div>
        <button class="btn" onclick="var g=this.nextElementSibling;g.classList.toggle('show');this.textContent=g.classList.contains('show')?'Ocultar fotos ▲':'Ver todas las fotos ▼'">Ver todas las fotos ▼</button>
        <div class="gallery">{imgs_all}</div>
    </div>
</div>'''

def badge(emoji, titulo):
    return f'''
<div class="chapter-badge animate__animated animate__zoomIn">
    <div class="chapter-badge-content">
        <span class="chapter-emoji">{emoji}</span>
        <span class="chapter-title">{titulo}</span>
    </div>
</div>'''

may = 'may'
feb = 'feb'
mar = 'mar'
abr = 'abr'
jun = 'jun'

timeline = (
    badge('🎓', 'Capítulo 1: Formación SSP · Mayo 2026') +
    act(1,'left','Formación Intensiva: Aprendizajes para la Vida','Mayo 2026','ASOJUNTAS Cartagena del Chairá',
        'Adquirí herramientas de Pedagogía Social, Cultura de Paz y Cuidado de la Naturaleza a través de módulos teóricos y prácticos.',
        'La formación técnica y humana son igualmente importantes para el servicio.',
        may,['MAYO_01.png','MAYO_02.jpeg','MAYO_03.jpeg','MAYO_04.jpeg','MAYO_05.jpeg']) +
    act(2,'right','Estrategia Alerta por mi Ambiente','Mayo 2026','Universidad de la Amazonia',
        'Socialización de estrategia ambiental articulando el SSP con la academia universitaria.',
        'La articulación entre programas amplifica el impacto territorial.',
        may,['MAYO_06.jpeg','MAYO_07.jpeg','MAYO_08.jpeg','MAYO_09.jpeg','MAYO_10.jpeg']) +
    act(3,'left','Veeduría Electoral','Mayo 2026','El Paujil / Cartagena del Chairá',
        'Veeduría ciudadana garantizando transparencia en la jornada electoral.',
        'La veeduría es un acto supremo de ciudadanía y democracia.',
        may,['MAYO_11.jpeg','MAYO_12.jpeg','MAYO_13.jpeg','MAYO_14.jpeg','MAYO_15.jpeg']) +

    badge('📅', 'Capítulo 2: Primeros Pasos · Febrero y Marzo 2026') +
    act(4,'right','Actividades JAC — Febrero','Febrero 2026','ASOJUNTAS Cartagena del Chairá',
        'Fortalecimiento de Juntas de Acción Comunal. Primeros pasos en territorio comunitario.',
        'El primer acercamiento con la comunidad es fundamental para construir confianza.',
        feb,['FEBRERO_01.png','FEBRERO_02.jpeg','FEBRERO_03.jpeg','FEBRERO_04.jpeg','FEBRERO_05.jpeg']) +
    act(5,'left','Fortalecimiento PRAE — Febrero','Febrero 2026','I.E. Agroecológico Amazónico',
        'Acompañamiento al Proyecto Ambiental Escolar identificando oportunidades de intervención.',
        'La educación ambiental es la herramienta más poderosa de cambio generacional.',
        feb,['FEBRERO_01.png','FEBRERO_02.jpeg','FEBRERO_03.jpeg','FEBRERO_04.jpeg','FEBRERO_05.jpeg']) +
    act(6,'right','Actividades JAC — Marzo','Marzo 2026','ASOJUNTAS Cartagena del Chairá',
        'Fortaleciendo participación ciudadana y cultura de paz en el territorio.',
        'La constancia en el trabajo comunitario construye credibilidad y liderazgo.',
        mar,['MARZO_01.png','MARZO_02.jpeg','MARZO_03.jpeg','MARZO_04.jpeg','MARZO_05.jpeg']) +
    act(7,'left','Diagnóstico Técnico PRAE','Marzo 2026','I.E. Agroecológico Amazónico',
        'Diagnóstico del nacimiento de agua, frutales nativos y áreas del PRAE institucional.',
        'La institución posee un escenario ambiental único que debe ser protegido.',
        mar,['MARZO_01.png','MARZO_02.jpeg','MARZO_03.jpeg','MARZO_04.jpeg','MARZO_05.jpeg']) +
    act(8,'right','Desarrollo de Plataforma Web — Software PRAE','Marzo 2026','I.E. Agroecológico Amazónico',
        'Diseño e implementación de plataforma web para filtrar indicadores de desarrollo municipal.',
        'La tecnología puede ser un puente entre educación y gestión pública territorial.',
        mar,['MARZO_01.png','MARZO_02.jpeg','MARZO_03.jpeg','MARZO_04.jpeg','MARZO_05.jpeg']) +

    badge('☮️', 'Capítulo 3: Modalidad Cultura de Paz · Junio 2026') +
    act(9,'left','Diseño de Piezas Gráficas','11 Junio 2026','El Paujil / Cartagena del Chairá',
        'Diseño de flyers informativos con enfoque pedagógico para promover el voto consciente en municipios del Caquetá.',
        'La comunicación visual es una poderosa herramienta de pedagogía política.',
        jun,['JUNIO_01.jpg','JUNIO_02.jpg','JUNIO_03.png','JUNIO_04.jpg','JUNIO_05.jpg']) +
    act(10,'right','Pedagogía Electoral en Territorio','13 Junio 2026','Cartagena del Chairá',
        'Salidas de campo para pedagogía puerta a puerta explicando la importancia de la segunda vuelta presidencial.',
        'La pedagogía presencial crea puentes de confianza que ningún medio digital puede reemplazar.',
        jun,['JUNIO_06.jpg','JUNIO_07.jpg','JUNIO_08.jpg','JUNIO_09.jpg','JUNIO_10.jpg']) +
    act(11,'left','Mesa Técnica con Superintendencia','26 Junio 2026','El Paujil',
        'Participación en espacio institucional de control social, presentando observaciones comunitarias sobre el servicio eléctrico.',
        'Los servicios públicos son un derecho fundamental que la juventud debe defender.',
        jun,['JUNIO_11.jpg','JUNIO_12.jpg','JUNIO_13.jpg','JUNIO_14.jpg','JUNIO_15.jpg']) +
    act(12,'right','Capacitación en Veeduría Electoral','17 Junio 2026','El Paujil',
        'Formación como testigo electoral para garantizar transparencia. Aprendí sobre el Código Electoral y formularios electorales.',
        'La transparencia electoral se construye con ciudadanos capacitados y comprometidos.',
        jun,['JUNIO_16.png','JUNIO_17.jpg','JUNIO_18.jpg','JUNIO_19.jpg','JUNIO_20.jpg']) +
    act(13,'left','Testigo Electoral — Segunda Vuelta','21 Junio 2026','I.E. Agroecológico Amazónico',
        'Ejercicio formal como testigo electoral vigilando desde las 7:30am hasta las 4:00pm la transparencia total del proceso.',
        'Presenciar cómo la voluntad popular se expresa democráticamente fue una experiencia inolvidable.',
        jun,['JUNIO_21.jpg','JUNIO_22.jpg','JUNIO_23.jpg','JUNIO_24.jpg','JUNIO_25.jpg']) +

    badge('🌿', 'Capítulo 4: Cuidado de la Naturaleza · Junio 2026') +
    act(14,'right','Pedagogía de Paz Infantil','12 Junio 2026','El Paujil',
        'Co-facilité taller lúdico con niños y niñas sobre reconciliación y cuidado del entorno con la Fundación Red Caquetá Paz.',
        'La lúdica y el arte son herramientas poderosas para sembrar paz desde la primera infancia.',
        jun,['JUNIO_26.jpg','JUNIO_27.jpg','JUNIO_28.jpg','JUNIO_29.jpg','JUNIO_30.jpg']) +
    act(15,'left','Liderazgo en Infraestructura Comunitaria','29 Junio 2026','Barrio Primero de Mayo',
        'Lideré construcción de bancas comunitarias, recuperación de cancha deportiva y organización de olla comunitaria.',
        'Una olla comunitaria puede construir más tejido social que mil discursos políticos.',
        jun,['JUNIO_31.jpg','JUNIO_32.jpg','JUNIO_33.jpg','JUNIO_34.jpg','JUNIO_35.jpg']) +

    badge('📚', 'Capítulo 5: Sector Educativo PRAE · Mayo 2026') +
    act(16,'right','Entrega de Software PRAE','12 Mayo 2026','I.E. Agroecológico Amazónico',
        'Desarrollé y entregué software para analizar planes de desarrollo e identificar indicadores estratégicos de gestión.',
        'La tecnología al servicio de la comunidad potencia las capacidades de incidencia institucional.',
        may,['MAYO_16.png','MAYO_17.png','MAYO_18.png','MAYO_19.png','MAYO_20.jpeg']) +
    act(17,'left','Jornada Recreativa y Deportiva','12 Mayo 2026','I.E. Agroecológico Amazónico',
        'Articulé con Campamentos Juveniles "Bosque Mitu Salvini" jornada de deporte y recreación con juegos cooperativos.',
        'El deporte y la recreación son estrategias efectivas de prevención y construcción de paz.',
        may,['MAYO_21.jpeg','MAYO_22.jpeg','MAYO_23.jpeg','MAYO_24.jpeg','MAYO_25.png']) +
    act(18,'right','Formación Ambiental Intensiva','Mayo 2026','ASOJUNTAS',
        'Taller profundo sobre gestión ambiental y sostenibilidad territorial conectando educación con participación comunitaria.',
        'La conciencia ambiental es el fundamento de cualquier proceso de transformación social.',
        may,['MAYO_26.jpeg','MAYO_27.png','MAYO_28.jpeg','MAYO_29.png','MAYO_30.jpeg']) +
    act(19,'left','Integración Comunitaria','Mayo 2026','Espacios Comunitarios del Territorio',
        'Actividad de integración cerrando el ciclo de trabajo y consolidando lazos de confianza con la comunidad.',
        'El servicio no es una actividad puntual, es una forma de vida que trasciende los programas.',
        may,['MAYO_31.jpeg','MAYO_32.jpeg','MAYO_33.jpeg','MAYO_34.jpeg','MAYO_35.jpeg']) +
    act(20,'right','Cierre del Proceso SSP — Producto Final','Julio 2026','Territorio Caquetá',
        'Reflexión y cierre consolidando 6 meses de aprendizajes, transformaciones y compromisos con el territorio.',
        'El SSP terminó, pero mi servicio al territorio del Caquetá continúa cada día.',
        jun,['JUNIO_36.jpg','JUNIO_37.jpg','JUNIO_38.jpg','JUNIO_39.jpg','JUNIO_40.jpg'],
        ['JUNIO_41.jpg','JUNIO_42.jpg'])
)

html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Trayectoria en el SSP - Kevin Alexis Aragon Zapata</title>
    <link rel="stylesheet" href="css/styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    {css}
</head>
<body>

<nav class="nav">
    <div class="nav-brand">🌿 SSP - Kevin Aragon</div>
    <div class="nav-links">
        <a href="#inicio">Inicio</a>
        <a href="#videos">Videos</a>
        <a href="#historia">Historia</a>
        <a href="#impacto">Impacto</a>
    </div>
</nav>

<!-- HERO -->
<section class="hero" id="inicio">
    <div class="hero-content animate__animated animate__fadeInDown animate__slow">
        <h1>🌿 MI TRAYECTORIA EN EL SERVICIO SOCIAL PARA LA PAZ</h1>
        <h2>Una Historia de Transformación Territorial en el Caquetá</h2>
        <div class="hero-info">
            <p><strong>Promotor:</strong> Kevin Alexis Aragon Zapata</p>
            <p><strong>Organización:</strong> ASOJUNTAS Cartagena del Chairá</p>
            <p><strong>Periodo:</strong> Febrero - Julio 2026</p>
        </div>
    </div>
</section>

<!-- CARRUSEL -->
<section style="background: var(--dark); padding: 3rem 2rem;">
    <div style="max-width: 800px; margin: 0 auto;">
        <h2 style="color: white; text-align: center; margin-bottom: 2rem; font-size: 1.5rem;">📸 Galería de Evidencias</h2>
        <div class="carousel-section">
            <div class="carousel-container">
                <div class="carousel-track" id="carousel">
                    <div class="carousel-slide"><img src="images/inicial.jpeg" alt="Inicio SSP"></div>
                    <div class="carousel-slide"><img src="images/formacion1.jpg" alt="Formación 1"></div>
                    <div class="carousel-slide"><img src="images/formacion2.jpg" alt="Formación 2"></div>
                    <div class="carousel-slide"><img src="images/formacion3.jpg" alt="Formación 3"></div>
                    <div class="carousel-slide"><img src="images/pedagogia1.jpg" alt="Pedagogía 1"></div>
                    <div class="carousel-slide"><img src="images/pedagogia2.jpg" alt="Pedagogía 2"></div>
                    <div class="carousel-slide"><img src="images/grupo-barrio.jpg" alt="Grupo Barrio"></div>
                    <div class="carousel-slide"><img src="images/ninos1.jpg" alt="Niños 1"></div>
                    <div class="carousel-slide"><img src="images/ninos2.jpg" alt="Niños 2"></div>
                    <div class="carousel-slide"><img src="images/ninos3.jpg" alt="Niños 3"></div>
                    <div class="carousel-slide"><img src="images/obra1.jpg" alt="Obra"></div>
                    <div class="carousel-slide"><img src="images/cancha.jpg" alt="Cancha"></div>
                    <div class="carousel-slide"><img src="images/olla.jpg" alt="Olla comunitaria"></div>
                    <div class="carousel-slide"><img src="images/flyer1.jpg" alt="Flyer 1"></div>
                    <div class="carousel-slide"><img src="images/flyer2.jpg" alt="Flyer 2"></div>
                    <div class="carousel-slide"><img src="images/testigo.jpg" alt="Testigo Electoral"></div>
                    <div class="carousel-slide"><img src="images/votacion1.jpg" alt="Votación"></div>
                    <div class="carousel-slide"><img src="images/acta.jpg" alt="Acta"></div>
                </div>
            </div>
            <button class="carousel-nav carousel-prev" onclick="carouselMove(-1)">❮</button>
            <button class="carousel-nav carousel-next" onclick="carouselMove(1)">❯</button>
        </div>
    </div>
    <script>
        var ci = 0, total = 18;
        function carouselMove(dir) {{
            ci = (ci + dir + total) % total;
            document.getElementById('carousel').style.transform = 'translateX(' + (-ci * 100) + '%)';
        }}
        setInterval(function(){{ carouselMove(1); }}, 4000);
    </script>
</section>

<!-- VIDEOS -->
<section class="video-section" id="videos">
    <div class="section-content">
        <h2 class="section-title">🎥 Videos de mi Experiencia SSP</h2>
        <div class="video-grid">
            <div class="video-item">
                <div class="video-wrapper">
                    <iframe src="https://drive.google.com/file/d/1VhuyI1LovbHjvCDl_kJ8ADFfEX9ZMKcG/preview" allowfullscreen></iframe>
                </div>
                <p style="text-align:center; padding:1rem; font-weight:600; background:var(--light);">Presentación del SSP</p>
            </div>
            <div class="video-item">
                <div class="video-wrapper">
                    <iframe src="https://drive.google.com/file/d/1Oj0PpDhLtIPqAgomShzpa3t2FJOEYIge/preview" allowfullscreen></iframe>
                </div>
                <p style="text-align:center; padding:1rem; font-weight:600; background:var(--light);">Sinchi en Cartagena</p>
            </div>
            <div class="video-item">
                <div class="video-wrapper">
                    <iframe src="https://drive.google.com/file/d/1EjlQZBgZEoyZZajasPM9LGmQk3Azbg5O/preview" allowfullscreen></iframe>
                </div>
                <p style="text-align:center; padding:1rem; font-weight:600; background:var(--light);">Rap del PRAE</p>
            </div>
            <div class="video-item">
                <div class="video-wrapper">
                    <iframe src="https://drive.google.com/file/d/187ZHn7DN1FUfOC5KnyYnAZzNOr3js3d-/preview" allowfullscreen></iframe>
                </div>
                <p style="text-align:center; padding:1rem; font-weight:600; background:var(--light);">Reflexión Ambiental</p>
            </div>
        </div>
    </div>
</section>

<!-- TIMELINE -->
<section class="section" id="historia" style="background: var(--light);">
    <div class="section-content">
        <h2 class="section-title">📅 Mi Historia en el SSP — 20 Actividades</h2>
        <p style="text-align:center; color:#555; margin-bottom:3rem;">Haz clic en <strong>"Ver todas las fotos"</strong> para expandir la galería de cada actividad</p>
        <div class="timeline">
            {timeline}
        </div>
    </div>
</section>

<!-- IMPACTO -->
<section class="impact-section" id="impacto">
    <div class="section-content">
        <h2 style="font-size:2.5rem; margin-bottom:3rem; color:white;">📊 Impacto del SSP</h2>
        <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:2rem; max-width:900px; margin:0 auto; text-align:center;">
            <div style="background:rgba(255,255,255,0.15); padding:2rem; border-radius:15px; backdrop-filter:blur(10px);">
                <div style="font-size:3.5rem; font-weight:900;">20</div>
                <div style="margin-top:0.5rem; opacity:0.9;">Actividades</div>
            </div>
            <div style="background:rgba(255,255,255,0.15); padding:2rem; border-radius:15px; backdrop-filter:blur(10px);">
                <div style="font-size:3.5rem; font-weight:900;">96</div>
                <div style="margin-top:0.5rem; opacity:0.9;">Evidencias Fotográficas</div>
            </div>
            <div style="background:rgba(255,255,255,0.15); padding:2rem; border-radius:15px; backdrop-filter:blur(10px);">
                <div style="font-size:3.5rem; font-weight:900;">6</div>
                <div style="margin-top:0.5rem; opacity:0.9;">Meses de Servicio</div>
            </div>
            <div style="background:rgba(255,255,255,0.15); padding:2rem; border-radius:15px; backdrop-filter:blur(10px);">
                <div style="font-size:3.5rem; font-weight:900;">5</div>
                <div style="margin-top:0.5rem; opacity:0.9;">Capítulos</div>
            </div>
            <div style="background:rgba(255,255,255,0.15); padding:2rem; border-radius:15px; backdrop-filter:blur(10px);">
                <div style="font-size:3.5rem; font-weight:900;">∞</div>
                <div style="margin-top:0.5rem; opacity:0.9;">Compromisos</div>
            </div>
        </div>
    </div>
</section>

<!-- QUOTE -->
<section class="quote-section">
    <p class="quote-text">"La paz no se construye desde arriba, se construye desde los barrios, las veredas, las escuelas y los corazones de las personas."</p>
    <p style="margin-top:2rem; opacity:0.85; font-size:1.1rem; position:relative; z-index:1;">— Kevin Alexis Aragon Zapata · El Paujil, Caquetá · Julio 2026</p>
</section>

<!-- FOOTER -->
<footer class="footer">
    <h3>🌿 Mi Trayectoria en el Servicio Social para la Paz</h3>
    <p>Kevin Alexis Aragon Zapata | ASOJUNTAS Cartagena del Chairá | Febrero - Julio 2026</p>
    <p style="margin-top:1rem; opacity:0.7; font-size:0.9rem;">Transformando el Caquetá desde la base comunitaria</p>
</footer>

</body>
</html>'''

with open('TIMELINE_ZIGZAG.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('HTML generado:', len(html), 'chars,', html.count('\\n'), 'lineas')
print('Actividades:', html.count('activity-title'))
print('Fotos preview:', html.count('class="photos"'))
print('Galerías:', html.count('class="gallery"'))

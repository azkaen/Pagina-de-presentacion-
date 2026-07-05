# GUÍA DE FOTOS - PRODUCTO FINAL SSP
## Recomendaciones para completar tu experiencia web interactiva

**Instrucciones:**
- Coloca tus fotos en la misma carpeta que el archivo HTML
- Nombra las fotos exactamente como se indica abajo
- Formato recomendado: JPG o PNG
- Resolución recomendada: Mínimo 800x600 píxeles
- Las fotos se mostrarán automáticamente cuando las agregues

---

## 📸 FOTO DE PERFIL (HERO SECTION)

**Nombre del archivo:** `tu-foto-perfil.jpg`
**Ubicación:** Sección de inicio (círculo grande)
**Recomendación:** Foto tuya formal, sonriendo, preferiblemente con fondo neutro o relacionado con el SSP

---

## 📸 CAPÍTULO 1: EL INICIO DEL CAMINO

### Inscripción y Selección
**Archivos necesarios:**
- `inscripcion.jpg` - Foto del proceso de inscripción (formulario, captura de pantalla, etc.)
- `seleccion.jpg` - Foto de notificación de selección o documento de aceptación

### Formación Intensiva
**Archivos necesarios:**
- `formacion1.jpg` - Foto de ti en una sesión de formación
- `formacion2.jpg` - Foto de un taller o módulo formativo
- `formacion3.jpg` - Foto grupal con otros promotores del SSP

---

## 📸 CAPÍTULO 2: MODALIDAD CULTURA DE PAZ

### Diseño de Piezas Gráficas (11 junio 2026)
**Archivos necesarios:**
- `flyer1.jpg` - Captura de uno de los flyers que diseñaste
- `flyer2.jpg` - Otro flyer diferente o versión final
- `diseño-trabajo.jpg` - Foto de ti trabajando en el diseño (pantalla de computador, etc.)

### Pedagogía Electoral en Territorio (13 junio 2026)
**Archivos necesarios:**
- `pedagogia1.jpg` - Foto de ti haciendo pedagogía en la calle
- `pedagogia2.jpg` - Foto dialogando con líderes comunitarios o habitantes

### Mesa Técnica con Superintendencia (26 julio 2026)
**Archivos necesarios:**
- *Opcional:* Si tienes fotos de esta reunión, agrégalas manualmente editando el HTML

### Capacitación en Veeduría Electoral (17 junio 2026)
**Archivos necesarios:**
- *Opcional:* Si tienes fotos de la capacitación, agrégalas manualmente

### Testigo Electoral (21 junio 2026)
**Archivos necesarios:**
- `votacion1.jpg` - Foto del puesto de votación (I.E. Agroecológico Amazónico)
- `testigo.jpg` - Foto de ti ejerciendo como testigo electoral (con credencial si es posible)
- `acta.jpg` - Foto del acta de escrutinio que firmaste (puedes borrar datos sensibles)

---

## 📸 CAPÍTULO 3: MODALIDAD 5 - CUIDADO DE LA NATURALEZA

### Pedagogía de Paz con Niños (12 junio 2026)
**Archivos necesarios:**
- `ninos1.jpg` - Foto del taller con niños y niñas
- `ninos2.jpg` - Foto de los dibujos que hicieron los niños sobre paz
- `ninos3.jpg` - Foto grupal con los niños participantes

### Liderazgo en Infraestructura Comunitaria (29 junio 2026)
**Archivos necesarios:**
- `obra1.jpg` - Foto de la construcción de las bancas
- `olla.jpg` - Foto de la olla comunitaria
- `cancha.jpg` - Foto de la cancha recuperada
- `grupo-barrio.jpg` - Foto grupal con habitantes del Barrio Primero de Mayo

---

## 📸 FOTOS ADICIONALES (OPCIONALES)

Si tienes más fotos de otras actividades, puedes agregarlas editando el HTML:

### Mesa Técnica Superintendencia
Agrega este código después del párrafo de aprendizajes:
```html
<div class="photo-gallery">
    <div class="photo-item" onclick="openViewer(this)">
        <div class="photo-placeholder">
            <div class="photo-placeholder-icon">📷</div>
            <div class="photo-placeholder-text">Mesa técnica</div>
            <div class="photo-placeholder-hint">mesa-tecnica.jpg</div>
        </div>
        <img src="mesa-tecnica.jpg" alt="Mesa técnica Superintendencia">
    </div>
</div>
```

### Capacitación Veeduría
Agrega este código después del párrafo de aprendizajes:
```html
<div class="photo-gallery">
    <div class="photo-item" onclick="openViewer(this)">
        <div class="photo-placeholder">
            <div class="photo-placeholder-icon">📷</div>
            <div class="photo-placeholder-text">Capacitación</div>
            <div class="photo-placeholder-hint">capacitacion.jpg</div>
        </div>
        <img src="capacitacion.jpg" alt="Capacitación veeduría">
    </div>
</div>
```

---

## 💡 CONSEJOS PARA LAS FOTOS

1. **Calidad:** Usa fotos claras y bien iluminadas
2. **Horizontal:** Las fotos horizontales se ven mejor en las galerías
3. **Contexto:** Incluye elementos que muestren el entorno (logos SSP, lugares, personas)
4. **Privacidad:** Si aparecen otras personas, asegúrate de tener su consentimiento
5. **Organización:** Mantén todos los archivos de fotos en la misma carpeta que el HTML

---

## 🎯 PRIORIDAD DE FOTOS

Si no tienes todas las fotos, prioriza estas:

**ESSENCIALES (mínimo para impacto visual):**
1. `tu-foto-perfil.jpg` - Tu foto personal
2. `testigo.jpg` - Como testigo electoral (experiencia clave)
3. `ninos1.jpg` - Taller con niños (muy emotivo)
4. `obra1.jpg` - Construcción bancas (tangible)
5. `olla.jpg` - Olla comunitaria (comunidad)

**IMPORTANTES (complementan la historia):**
6. `formacion1.jpg` - Formación SSP
7. `flyer1.jpg` - Flyers electorales
8. `votacion1.jpg` - Puesto de votación
9. `grupo-barrio.jpg` - Grupo del barrio

**DESEABLES (enriquecen la experiencia):**
10. Las demás fotos según disponibilidad

---

## 📱 CÓMO AGREGAR LAS FOTOS

### Opción 1: Arrastrar y soltar
1. Abre la carpeta donde está el archivo HTML
2. Arrastra tus fotos a esa carpeta
3. Asegúrate de que tengan los nombres exactos indicados
4. Abre el HTML en el navegador y las fotos aparecerán automáticamente

### Opción 2: Copiar y pegar
1. Copia tus fotos
2. Pégalas en la carpeta del HTML
3. Renómbralas con los nombres indicados
4. Actualiza el navegador

---

## ⚠️ TROUBLESHOOTING

**Las fotos no aparecen:**
- Verifica que los nombres de archivo sean exactos (incluyendo mayúsculas/minúsculas)
- Asegúrate de que las fotos estén en la MISMA carpeta que el HTML
- Verifica que el formato sea JPG o PNG
- Limpia el caché del navegador (Ctrl+F5)

**Las fotos se ven borrosas:**
- Usa fotos de mayor resolución (mínimo 800x600)
- Evita usar capturas de pantalla de baja calidad

**Quiero cambiar el orden de las fotos:**
- Edita el HTML y cambia el orden de los elementos `<div class="photo-item">`

---

## 🎨 PERSONALIZACIÓN ADICIONAL

Si quieres agregar más fotos o cambiar las descripciones:

1. Abre el archivo HTML en un editor de texto
2. Busca las secciones `<div class="photo-gallery">`
3. Copia y pega elementos `<div class="photo-item">` para agregar más fotos
4. Cambia el texto en `photo-placeholder-text` para personalizar descripciones

---

**¿Necesitas ayuda para agregar las fotos o editar el HTML?**

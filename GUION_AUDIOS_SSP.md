# GUION DE AUDIOS - PRODUCTO FINAL SSP
## Para grabar y añadir a tu experiencia web interactiva

**Instrucciones:**
- Graba cada audio en formato MP3 (puedes usar tu celular)
- Nombra los archivos como: audio1.mp3, audio2.mp3, etc.
- Duración sugerida: 30-60 segundos por audio
- Habla con naturalidad, como si le contaras a un amigo

---

## 🎙️ AUDIO 1: INTRODUCCIÓN PERSONAL
**Ubicación en la web:** Sección Hero (inicio)
**Duración sugerida:** 45 segundos

```
"Hola, soy Kevin Alexis Aragón Zapata, y quiero compartirles mi experiencia 
en el Servicio Social para la Paz. Este viaje transformó mi vida y mi visión 
del Caquetá. Acompáñenme en esta historia de servicio, aprendizaje y 
construcción de paz desde nuestros territorios."
```

---

## 🎙️ AUDIO 2: EL INICIO DEL CAMINO
**Ubicación en la web:** Capítulo 1 - Formación
**Duración sugerida:** 40 segundos

```
"Cuando me inscribí al SSP, no imaginaba lo que vendría. Ser seleccionado 
como promotor fue un honor. La formación me dio herramientas que nunca 
imaginé que tendría: pedagogía social, cultura de paz, participación ciudadana. 
Fue el inicio de una nueva forma de ver mi rol en la comunidad."
```

---

## 🎙️ AUDIO 3: DISEÑO DE FLYERS ELECTORALES
**Ubicación en la web:** Capítulo 2 - Actividad 1
**Duración sugerida:** 35 segundos

```
"Diseñar esos flyers fue más que hacer gráficos. Era crear puentes de 
comunicación con la gente. En territorios donde el abstencionismo es alto, 
una imagen bien diseñada puede motivar a alguien a ir a votar. Fue mi primera 
experiencia usando la comunicación visual para la paz."
```

---

## 🎙️ AUDIO 4: PEDAGOGÍA PUERTA A PUERTA
**Ubicación en la web:** Capítulo 2 - Actividad 2
**Duración sugerida:** 40 segundos

```
"Salir a las calles de Cartagena del Chairá fue una experiencia increíble. 
Hablar cara a cara con la gente, explicarles sus derechos, ver cómo agradecían 
que alguien les tomara el tiempo... Eso me enseñó que la pedagogía presencial 
crea confianza. La democracia se construye en esos diálogos."
```

---

## 🎙️ AUDIO 5: MESA TÉCNICA CON LA SUPERINTENDENCIA
**Ubicación en la web:** Capítulo 2 - Actividad 3
**Duración sugerida:** 45 segundos

```
"Estar en esa mesa técnica con la Superintendencia fue intenso. Representar 
a mi comunidad, presentar sus quejas sobre el servicio eléctrico, exigir 
justicia tarifaria... Me di cuenta de que la juventud tiene un rol importante 
en la defensa de los derechos. No somos el futuro, somos el presente."
```

---

## 🎙️ AUDIO 6: TESTIGO ELECTORAL
**Ubicación en la web:** Capítulo 2 - Actividad 5
**Duración sugerida:** 50 segundos

```
"Ese día como testigo electoral fue inolvidable. Desde las 7:30 AM hasta las 
4:00 PM, vigilando cada voto, cada procedimiento. Ver cómo la voluntad popular 
se expresa de manera ordenada fue emocionante. Sentí que estaba protegiendo 
algo sagrado: la democracia de mi territorio."
```

---

## 🎙️ AUDIO 7: TALLER CON NIÑOS
**Ubicación en la web:** Capítulo 3 - Actividad 1
**Duración sugerida:** 40 segundos

```
"El taller con los niños de la Fundación Red Caquetá Paz fue mágico. Verlos 
dibujar su visión de la paz, escuchar sus ideas... Los niños entienden la 
reconciliación de una forma que nosotros a veces olvidamos. Sembrar paz desde 
la infancia es la mejor inversión que podemos hacer."
```

---

## 🎙️ AUDIO 8: PROYECTO DE INFRAESTRUCTURA
**Ubicación en la web:** Capítulo 3 - Actividad 2
**Duración sugerida:** 45 segundos

```
"Liderar ese proyecto de 12 millones en el Barrio Primero de Mayo fue un reto 
gigante. Construir bancas, recuperar la cancha, organizar la olla comunitaria... 
Pero lo más importante fue ver cómo la comunidad se unió. Transformamos el 
entorno físico y, al mismo tiempo, el tejido social."
```

---

## 🎙️ AUDIO 9: APRENDIZAJES SOBRE LIDERAZGO
**Ubicación en la web:** Capítulo 4 - Card 1
**Duración sugerida:** 35 segundos

```
"El SSP me enseñó que el liderazgo no es sobre posición, es sobre servicio. 
Mi rol era facilitar, acompañar, potenciar a otros. Cuando la comunidad se 
fortalece, el líder se hace invisible. Eso es lo que significa realmente 
servir."
```

---

## 🎙️ AUDIO 10: TRANSFORMACIÓN PERSONAL
**Ubicación en la web:** Capítulo 5 - Impacto
**Duración sugerida:** 50 segundos

```
"Antes del SSP, el servicio comunitario era algo externo. Hoy es mi forma de 
vida. Desarrollé habilidades que usaré siempre: comunicación, gestión, 
análisis de políticas. Pero lo más importante es mi visión: ya no soy un 
beneficiario, soy un agente de cambio en el Caquetá."
```

---

## 🎙️ AUDIO 11: CIERRE Y COMPROMISO
**Ubicación en la web:** Sección final (antes del footer)
**Duración sugerida:** 40 segundos

```
"El SSP ha terminado, pero mi servicio al territorio continúa. Mi compromiso 
con la paz y el desarrollo del Caquetá es para siempre. La paz no es un destino, 
es un camino que recorro cada día. Gracias por ser parte de esta historia."
```

---

## 📋 CÓMO INTEGRAR LOS AUDIOS EN LA WEB

### Opción 1: Reemplazar los placeholders existentes

1. **Graba los audios** y guárdalos como:
   - audio1.mp3, audio2.mp3, ..., audio11.mp3

2. **Coloca los archivos** en la misma carpeta que el HTML

3. **Edita el archivo HTML** y reemplaza las secciones de audio:

```html
<!-- Ejemplo para AUDIO 3 (Flyers) -->
<div class="audio-section">
    <p style="margin-bottom: 0.5rem; font-weight: bold;">🎙️ Mi experiencia diseñando flyers</p>
    <div class="audio-player">
        <button class="audio-btn" onclick="toggleAudio('audio3')">
            <span>▶️</span> Reproducir
        </button>
        <audio id="audio3" src="audio3.mp3"></audio>
    </div>
</div>
```

4. **Actualiza el JavaScript** para manejar los audios reales:

```javascript
function toggleAudio(audioId) {
    const audio = document.getElementById(audioId);
    const btn = audio.parentElement.querySelector('.audio-btn');
    const icon = btn.querySelector('span');
    
    if (audio.paused) {
        audio.play();
        icon.textContent = '⏸️';
        btn.classList.add('playing');
    } else {
        audio.pause();
        icon.textContent = '▶️';
        btn.classList.remove('playing');
    }
}
```

### Opción 2: Usar una plataforma de audio

Si prefieres no editar el código HTML:

1. **Sube tus audios** a SoundCloud, Google Drive, o cualquier plataforma
2. **Obtén los enlaces** de compartir
3. **Reemplaza los placeholders** en el HTML con los reproductores embed de la plataforma

---

## 💡 CONSEJOS PARA LA GRABACIÓN

- **Ambiente:** Graba en un lugar silencioso
- **Voz:** Habla claro, con entusiasmo y naturalidad
- **Tono:** Sé auténtico, no intentes sonar "profesional"
- **Pausas:** Tómate tu tiempo, respira entre frases
- **Emoción:** Transmite lo que sentiste en cada experiencia
- **Longitud:** No te extiendas demasiado, mejor corto y contundente

---

## 🎯 PRIORIDAD DE AUDIOS

Si no puedes grabar todos, te recomiendo este orden de importancia:

1. **Audio 1** (Introducción) - Esencial
2. **Audio 6** (Testigo electoral) - Muy impactante
3. **Audio 10** (Transformación personal) - Conclusión fuerte
4. **Audio 8** (Proyecto infraestructura) - Experiencia tangible
5. **Audio 7** (Taller niños) - Emotivo

Con estos 5 audios ya tendrás una experiencia muy completa y personal.

---

**¿Necesitas ayuda para integrar los audios una vez que los grabes?**

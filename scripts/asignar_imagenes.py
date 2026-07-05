import os
import shutil

# Mapeo de imágenes según bitácoras
# Basado en el análisis cronológico:

# 11 de junio - Diseño de flyers
flyer_images = [
    "03_Bitácora_Fecha-_11_de_junio_2_image2.jpeg",
    "04_Bitácora_Fecha-_11_de_junio_2_image3.jpeg",
    "05_Bitácora_Fecha-_11_de_junio_2_image4.jpeg"
]

# 13 de junio - Pedagogía electoral
pedagogia_images = [
    "18_Bitácora_Fecha-_13_de_junio_2_image6.jpeg",
    "19_Bitácora_Fecha-_13_de_junio_2_image7.jpeg"
]

# 21 de junio - Testigo electoral
votacion_images = [
    "66_Bitácora_Fecha-_21_de_junio_2_image19.jpeg",
    "67_Bitácora_Fecha-_21_de_junio_2_image20.jpeg",
    "68_Bitácora_Fecha-_21_de_junio_2_image21.jpeg"
]

# 12 de junio - Taller niños
ninos_images = [
    "87_Bitácora_Fecha-_12_de_junio_2_image25.jpeg",
    "88_Bitácora_Fecha-_12_de_junio_2_image26.jpeg",
    "89_Bitácora_Fecha-_12_de_junio_2_image27.jpeg"
]

# 29 de junio - Infraestructura
obra_images = [
    "99_Bitácora_Fecha-_29_de_junio_2_image28.jpeg",
    "100_Bitácora_Fecha-_29_de_junio_2_image29.jpeg",
    "101_Bitácora_Fecha-_29_de_junio_2_image30.jpeg",
    "102_Bitácora_Fecha-_29_de_junio_2_image31.jpeg"
]

# 17 de junio - Capacitación veeduría
capacitacion_images = [
    "54_Bitácora_Fecha-_17_de_junio_2_image16.jpeg",
    "55_Bitácora_Fecha-_17_de_junio_2_image17.jpeg"
]

# 26 de junio - Mesa técnica
mesa_images = [
    "36_Bitácora_Fecha-_26_de_junio_2_image11.jpeg",
    "37_Bitácora_Fecha-_26_de_junio_2_image12.jpeg"
]

# Función para copiar imagen
def copy_image(source_dir, source_name, dest_name):
    source_path = os.path.join(source_dir, source_name)
    dest_path = dest_name
    if os.path.exists(source_path):
        shutil.copy(source_path, dest_path)
        print(f"✓ {source_name} -> {dest_name}")
        return True
    else:
        print(f"✗ No encontrada: {source_name}")
        return False

print("=== ASIGNANDO IMÁGENES A SECCIONES DEL HTML ===\n")

source_dir = "imagenes_organizadas"

# Copiar imágenes de flyers
print("\n📄 FLYERS ELECTORALES (11 junio):")
copy_image(source_dir, flyer_images[0], "flyer1.jpg")
copy_image(source_dir, flyer_images[1], "flyer2.jpg")
copy_image(source_dir, flyer_images[2], "diseño-trabajo.jpg")

# Copiar imágenes de pedagogía
print("\n📣 PEDAGOGÍA ELECTORAL (13 junio):")
copy_image(source_dir, pedagogia_images[0], "pedagogia1.jpg")
copy_image(source_dir, pedagogia_images[1], "pedagogia2.jpg")

# Copiar imágenes de votación
print("\n🗳️ TESTIGO ELECTORAL (21 junio):")
copy_image(source_dir, votacion_images[0], "votacion1.jpg")
copy_image(source_dir, votacion_images[1], "testigo.jpg")
copy_image(source_dir, votacion_images[2], "acta.jpg")

# Copiar imágenes de niños
print("\n👨‍👩‍👧‍👦 TALLER NIÑOS (12 junio):")
copy_image(source_dir, ninos_images[0], "ninos1.jpg")
copy_image(source_dir, ninos_images[1], "ninos2.jpg")
copy_image(source_dir, ninos_images[2], "ninos3.jpg")

# Copiar imágenes de obra
print("\n🏗️ INFRAESTRUCTURA (29 junio):")
copy_image(source_dir, obra_images[0], "obra1.jpg")
copy_image(source_dir, obra_images[1], "olla.jpg")
copy_image(source_dir, obra_images[2], "cancha.jpg")
copy_image(source_dir, obra_images[3], "grupo-barrio.jpg")

# Copiar imágenes de formación (usar capacitación)
print("\n🎓 FORMACIÓN (17 junio - Capacitación):")
copy_image(source_dir, capacitacion_images[0], "formacion1.jpg")
copy_image(source_dir, capacitacion_images[1], "formacion2.jpg")

# Copiar imágenes de inscripción/selección (usar primera imagen disponible)
print("\n📝 INSCRIPCIÓN/SELECCIÓN:")
copy_image(source_dir, "01_Bitácora_Fecha-_11_de_junio_2_image1.png", "inscripcion.jpg")
copy_image(source_dir, "02_Bitácora_Fecha-_11_de_junio_2_image1.png", "seleccion.jpg")

# Foto de perfil (buscar imagen que parezca ser foto de persona)
print("\n👤 FOTO DE PERFIL:")
# Usar una de las imágenes de capacitación o pedagogía que pueda ser foto personal
copy_image(source_dir, "18_Bitácora_Fecha-_13_de_junio_2_image6.jpeg", "tu-foto-perfil.jpg")

print("\n=== IMÁGENES ASIGNADAS ===")
print("Las imágenes están listas para usar en el HTML")

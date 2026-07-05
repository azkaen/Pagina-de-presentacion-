import os
import shutil

# Rutas
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(script_dir)
images_path = os.path.join(base_dir, 'images')

# Mapeo de imágenes según el orden de extracción y contexto
# Basado en el análisis de los documentos y el HTML

# Imágenes de JAC Junio (documento más reciente con actividades principales)
# Orden aproximado según cronología de bitácoras
mapeo_junio = {
    # Inscripción y selección (primeras imágenes)
    'temp_rId7.png': 'inscripcion.jpg',
    'temp_rId8.jpg': 'seleccion.jpg',
    
    # Formación (imágenes de capacitación)
    'temp_rId9.jpg': 'formacion1.jpg',
    'temp_rId10.jpg': 'formacion2.jpg',
    'temp_rId11.jpg': 'formacion3.jpg',
    
    # PRAE - Software y acta
    'temp_rId12.jpg': 'prae-software.jpg',
    'temp_rId13.jpg': 'prae-acta.jpg',
    
    # PRAE - Deportes
    'temp_rId14.jpg': 'prae-deporte1.jpg',
    'temp_rId15.jpg': 'prae-deporte2.jpg',
    'temp_rId16.jpg': 'prae-deporte3.jpg',
    
    # Flyers electorales
    'temp_rId17.jpg': 'flyer1.jpg',
    'temp_rId18.jpg': 'flyer2.jpg',
    'temp_rId19.jpg': 'diseño-trabajo.jpg',
    
    # Pedagogía electoral
    'temp_rId20.jpg': 'pedagogia1.jpg',
    'temp_rId21.jpg': 'pedagogia2.jpg',
    
    # Testigo electoral y votación
    'temp_rId22.jpg': 'testigo.jpg',
    'temp_rId23.jpg': 'votacion1.jpg',
    'temp_rId24.jpg': 'acta.jpg',
    
    # Niños
    'temp_rId25.jpg': 'ninos1.jpg',
    'temp_rId26.jpg': 'ninos2.jpg',
    'temp_rId27.jpg': 'ninos3.jpg',
    
    # Infraestructura
    'temp_rId28.jpg': 'obra1.jpg',
    'temp_rId29.jpg': 'olla.jpg',
    'temp_rId30.jpg': 'cancha.jpg',
    'temp_rId31.jpg': 'grupo-barrio.jpg',
}

def asignar_nombres():
    """Asigna nombres correctos a las imágenes extraídas"""
    print("=== ASIGNANDO NOMBRES A IMÁGENES ===\n")
    
    # Cambiar a carpeta images
    os.chdir(images_path)
    
    asignadas = 0
    no_encontradas = []
    
    for temp_name, final_name in mapeo_junio.items():
        if os.path.exists(temp_name):
            # Si el destino ya existe, eliminarlo primero
            if os.path.exists(final_name):
                os.remove(final_name)
            
            shutil.move(temp_name, final_name)
            print(f"✓ {temp_name} -> {final_name}")
            asignadas += 1
        else:
            print(f"✗ No encontrada: {temp_name}")
            no_encontradas.append(temp_name)
    
    print(f"\n=== RESUMEN ===")
    print(f"Imágenes asignadas: {asignadas}")
    print(f"No encontradas: {len(no_encontradas)}")
    
    if no_encontradas:
        print("\nImágenes no encontradas:")
        for name in no_encontradas:
            print(f"  - {name}")
    
    # Limpiar archivos temporales restantes
    print("\n=== LIMPIEZA DE ARCHIVOS TEMPORALES ===")
    temp_files = [f for f in os.listdir('.') if f.startswith('temp_')]
    for temp_file in temp_files:
        os.remove(temp_file)
        print(f"Eliminado: {temp_file}")
    
    print(f"\nImágenes finales en carpeta:")
    for f in sorted(os.listdir('.')):
        if not f.startswith('temp_') and not os.path.isdir(f):
            size = os.path.getsize(f) / 1024  # KB
            print(f"  {f} ({size:.1f} KB)")

if __name__ == "__main__":
    asignar_nombres()

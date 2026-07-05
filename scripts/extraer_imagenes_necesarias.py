from docx import Document
import os
import shutil

# Lista de imágenes necesarias según el HTML
imagenes_necesarias = [
    'inscripcion.jpg',
    'seleccion.jpg',
    'formacion1.jpg',
    'formacion2.jpg',
    'formacion3.jpg',
    'prae-software.jpg',
    'prae-acta.jpg',
    'prae-deporte1.jpg',
    'prae-deporte2.jpg',
    'prae-deporte3.jpg',
    'flyer1.jpg',
    'flyer2.jpg',
    'diseño-trabajo.jpg',
    'pedagogia1.jpg',
    'pedagogia2.jpg',
    'testigo.jpg',
    'votacion1.jpg',
    'acta.jpg',
    'ninos1.jpg',
    'ninos2.jpg',
    'ninos3.jpg',
    'obra1.jpg',
    'olla.jpg',
    'cancha.jpg',
    'grupo-barrio.jpg'
]

# Rutas
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(script_dir)
docs_path = os.path.join(base_dir, 'docs')
images_path = os.path.join(base_dir, 'images')

# Documentos a revisar
documentos = [
    'JAC Junio BITACORA DE ACTIVIDADES.docx',
    'JAC Mayo BITACORA  DE ACTIVIDADES.docx',
    'PRAE Junio FORMATO DE BITACORA.docx'
]

def extraer_imagenes_documento(doc_path):
    """Extrae todas las imágenes de un documento Word"""
    try:
        doc = Document(doc_path)
        image_rels = {}
        
        # Obtener relaciones de imágenes
        for rel in doc.part.rels.values():
            if "image" in rel.target_ref:
                image_rels[rel.rId] = rel.target_ref
        
        # Extraer imágenes
        imagenes_extraidas = []
        for rel_id, target_ref in image_rels.items():
            try:
                image_part = doc.part.rels[rel_id].target_part
                image_data = image_part.blob
                
                # Determinar extensión
                if target_ref.endswith('.png'):
                    ext = '.png'
                elif target_ref.endswith('.jpeg') or target_ref.endswith('.jpg'):
                    ext = '.jpg'
                else:
                    ext = '.jpg'  # default
                
                # Guardar imagen temporal
                temp_name = f"temp_{rel_id}{ext}"
                temp_path = os.path.join(images_path, temp_name)
                
                with open(temp_path, 'wb') as f:
                    f.write(image_data)
                
                imagenes_extraidas.append(temp_path)
                print(f"  Extraída: {temp_name}")
                
            except Exception as e:
                print(f"  Error extrayendo imagen {rel_id}: {e}")
        
        return imagenes_extraidas
        
    except Exception as e:
        print(f"Error procesando {doc_path}: {e}")
        return []

def main():
    print("=== EXTRACCIÓN DE IMÁGENES NECESARIAS ===\n")
    
    # Crear carpeta images si no existe
    os.makedirs(images_path, exist_ok=True)
    
    # Extraer imágenes de cada documento
    todas_imagenes = []
    for doc_name in documentos:
        doc_path = os.path.join(docs_path, doc_name)
        if os.path.exists(doc_path):
            print(f"Procesando: {doc_name}")
            imagenes = extraer_imagenes_documento(doc_path)
            todas_imagenes.extend(imagenes)
            print()
        else:
            print(f"No encontrado: {doc_path}\n")
    
    print(f"\nTotal imágenes extraídas: {len(todas_imagenes)}")
    print(f"Imágenes guardadas en: {os.path.abspath(images_path)}")
    print("\nImágenes necesarias:")
    for img in imagenes_necesarias:
        print(f"  - {img}")
    
    print("\n⚠️  NOTA: Las imágenes extraídas tienen nombres temporales.")
    print("   Debes renombrarlas manualmente según corresponda.")
    print("   O usa el script asignar_imagenes.py para mapearlas.")

if __name__ == "__main__":
    main()

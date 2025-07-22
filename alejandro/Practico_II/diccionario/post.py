post_red_social = {
    "id_post": "A123X",  
    "autor": {
        "usuario": "Alejandro-X-911",
        "nombre_completo": "José Alejandro Zabala Romero"
    }, 
    "contenido_texto": "¡Hoy aprendí a usar diccionarios en Python!  #programacion",
    "lista_de_likes": ["ana_s", "marco99", "coder_girl", "python_fan"], 
    "fecha_publicacion": "2025-07-19",  
    "comentarios": [  
        {"usuario": "ana_s", "texto": "¡Qué buena onda! "},
        {"usuario": "marco99", "texto": "Python es genial "},
    ],
    "es_publico": True  
}
print("--- Detalles del Post ---")
print(f"Autor: {post_red_social['autor']['nombre_completo']}")
print(f"Publicado el: {post_red_social['fecha_publicacion']}")
print(f"Contenido: {post_red_social['contenido_texto']}")
print(f"Likes: {len(post_red_social['lista_de_likes'])} usuarios")
print(f"Comentarios: {len(post_red_social['comentarios'])} comentarios")
print("\nFin del programa ----- jose alejandro zabala romero")
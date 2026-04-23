meme_dict = {
            "COMER": "ingerir alimentos sólidos o líquidos por la boca, masticándolos y tragándolos para nutrirse",
            "CORRER": "desplazarse rápidamente a pie, alternando los pasos de modo que ambos pies quedan en el aire por un instante",
            "LLORAR": "acción de derramar lágrimas, a menudo acompañada de sollozos, como respuesta a emociones intensas como tristeza, dolor, alegría o frustración",
            "BAILAR": "mover el cuerpo y las extremidades rítmicamente al compás de la música, sirviendo como forma de expresión, entretenimiento o ejercicio",
            "CAMINAR": "acción de trasladarse a pie de un lugar a otro, moviendo las piernas de forma alterna"
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("No esta")

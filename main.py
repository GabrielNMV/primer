for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    meme_dict = {
                "CRINGE": "Algo excepcionalmente raro o embarazoso",
                "LOL": "Una respuesta común a algo gracioso",
                "ROFL": "una respuesta a una broma",
                "SHEESH": "ligera desaprobación",
                "CREEPY": "aterrador, siniestro",
                "AGGRO": "ponerse agresivo/enojado",
                }
    if word in meme_dict.keys():
        # Si se encuentra la palabra, mostramos el significado.
        print(meme_dict[word])
    else:
        # Si no se encuentra la palabra, mostramos un mensaje.
        print("No hemos encontrado esa palabra.")

En base a los elementos entregados pude ver dos soluciones:

        la primera es hacer un juego que permita reproducir las opciones del juego.
        
        la segunda diseccionar el archivo json en base, por ejemplo a un for loop, para posteriormente mediante un if, ir assiganandoles valores string o int
        a los comandos que se incluian en el json. 
        
        la segunda opcion es la que mas se acerca al resultado esperado
        
        
        import os
        import json

        folder = "./input"
        files = os.listdir(folder)

        for fn in files:
            if fn.endswith("json"): #Esta condición solo permitirá entrada de ficheros que terminen en json
                with open(os.path.join(folder, fn), 'r') as f:
                    dict = {}
                    content = f.read()
                    f_dict = json.loads(content)
                    dict['file']=fn #Este campo del diccionario lo reemplazarías por tu campo texto
                    dict['golpes']= f_dict['golpes']
                    dict['movimientos']= f_dict['movimientos']
                    print (dict)

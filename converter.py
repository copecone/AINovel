import json, os

series = input("Series Directory: ")
with open(f'novel/{series}/info.json'.format(series), "r", encoding="utf-8") as info_file:
    series_info = json.load(info_file)
    print(f'Name: {series_info["name"]}')
    print(f'Writer: {series_info["writer"]}')
    print(f'Concept: {series_info["concept"]}')
    print(f'Tags: {", ".join(series_info["tags"])}\n')

    print(f'Searching Texts...\n\n{"=" * 50}\n')
    texts = os.listdir(f'novel/{series}/texts')
    for text in texts:
        if text[-4:] == ".txt":
            text_file = open("novel/{}/texts/{}".format(series, text), "r", encoding="utf-8")
            text_str = text_file.read()
            text_file.close()

            ep_name = text[:-4]
            print(f'{ep_name.capitalize()}\n')
            print(f'{text_str}\n{"=" * 50}\n')

            font_import = "<link href=\"https://cdn.jsdelivr.net/gh/sunn-us/SUIT/fonts/static/woff2/SUIT.css\" rel=\"stylesheet\">"
            
            text_export_str = text_str.replace("\n", "\n<br>")

            font_import_str = "\n        ".join(font_import.split("\n"))
            converted_str = f'<!DOCTYPE HTML>\n<html>\n    <head>\n        {font_import_str}\n    </head>\n\n    <body>\n'
            converted_str += f'        <h1>{ep_name.capitalize()}</h1><br>\n        <h3 style="font-family: \'SUIT\', sans-serif; font-weight: 600; font-size: 18pt;">{text_export_str}</h4>\n    </body>\n</html>'

            converted_file = open("novel/{}/{}.html".format(series, ep_name), "w", encoding="utf-8")
            converted_file.write(converted_str)
            converted_file.close()

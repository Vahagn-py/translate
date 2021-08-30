from deep_translator import GoogleTranslator


def translate_file_ru_en(file_path: str, destination_path: str,
                         source_language: str = 'ru', target_language: str = 'en'):
    with open(file_path, "r") as original_file:
        original_txt = original_file.read()
    google_translator = GoogleTranslator(source=source_language, target=target_language)
    translated_txt = google_translator.translate(original_txt)
    with open(destination_path, "w") as translated_file:
        translated_file.write(translated_txt)


translate_file_ru_en(file_path="txt1.txt", destination_path="txt2.txt", source_language="auto")
import PyPDF2
from gtts import gTTS
import os
from pydub import AudioSegment

def pdf_to_audio():
    # Kullanıcıdan PDF dosyasının yolu al
    pdf_path = input("Lütfen PDF dosyasının yolunu girin: ")

    # Kullanıcıdan ses dosyalarının kaydedileceği klasörün yolu al
    audio_path = input("Lütfen ses dosyalarının kaydedileceği klasörün yolunu girin: ")

    # PDF dosyasını aç
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # PDF içeriğini döngü ile oku
        audio_files = []
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            # Metni ses dosyasına dönüştür
            tts = gTTS(text, lang='tr')

            # Ses dosyasını kaydet
            audio_file = f"{audio_path}/page_{page_num + 1}.mp3"
            tts.save(audio_file)
            audio_files.append(audio_file)
            print(f"Sayfa {page_num + 1} ses dosyasına dönüştürüldü.")

        # Ses dosyalarını tek bir dosyaya birleştir
        merge_option = input("Ses dosyalarını tek bir dosyaya birleştirmek istiyor musunuz? (E/H): ")
        if merge_option.lower() == 'e':
            combined_audio = AudioSegment.empty()
            for audio_file in audio_files:
                combined_audio += AudioSegment.from_mp3(audio_file)
            combined_audio.export(f"{audio_path}/combined_audio.mp3", format="mp3")
            print("Ses dosyaları başarıyla birleştirildi.")
        else:
            print("Ses dosyaları birleştirilmedi.")

# Örnek kullanım
pdf_to_audio()

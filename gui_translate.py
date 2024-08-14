import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def translate_text():
    src_lang_code = lang_codes[source_lang.get()]
    dest_lang_code = lang_codes[destination_lang.get()]
    text_to_translate = source_text.get("1.0", tk.END)
    
    try:
        translation = translator.translate(text_to_translate, src=src_lang_code, dest=dest_lang_code)
        translated_text.delete("1.0", tk.END)
        translated_text.insert(tk.END, translation.text)
    except Exception as e:
        translated_text.delete("1.0", tk.END)
        translated_text.insert(tk.END, f"Fehler: {str(e)}")

# Initialisiert das Tool
translator = Translator()

# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Übersetzungstool")


lang_codes = {v: k for k, v in LANGUAGES.items()}

# die Liste der Sprachennamen in Landessprache
language_names = {
    'afrikaans': 'Afrikaans',
    'albanian': 'Shqip',
    'arabic': 'العربية',
    'armenian': 'Հայերեն',
    'azerbaijani': 'Azərbaycan dili',
    'basque': 'Euskara',
    'belarusian': 'Беларуская',
    'bengali': 'বাংলা',
    'bosnian': 'Bosanski',
    'bulgarian': 'Български',
    'catalan': 'Català',
    'cebuano': 'Cebuano',
    'chinese (simplified)': '中文 (简体)',
    'chinese (traditional)': '中文 (繁體)',
    'corsican': 'Corsu',
    'croatian': 'Hrvatski',
    'czech': 'Čeština',
    'danish': 'Dansk',
    'dutch': 'Nederlands',
    'english': 'English',
    'esperanto': 'Esperanto',
    'estonian': 'Eesti',
    'finnish': 'Suomi',
    'french': 'Français',
    'frisian': 'Frysk',
    'galician': 'Galego',
    'georgian': 'ქართული',
    'german': 'Deutsch',
    'greek': 'Ελληνικά',
    'gujarati': 'ગુજરાતી',
    'haitian creole': 'Kreyòl Ayisyen',
    'hausa': 'Hausa',
    'hawaiian': 'ʻŌlelo Hawaiʻi',
    'hebrew': 'עברית',
    'hindi': 'हिन्दी',
    'hmong': 'Hmoob',
    'hungarian': 'Magyar',
    'icelandic': 'Íslenska',
    'igbo': 'Igbo',
    'indonesian': 'Bahasa Indonesia',
    'irish': 'Gaeilge',
    'italian': 'Italiano',
    'japanese': '日本語',
    'javanese': 'Jawa',
    'kannada': 'ಕನ್ನಡ',
    'kazakh': 'Қазақ тілі',
    'khmer': 'ខ្មែរ',
    'korean': '한국어',
    'kurdish (kurmanji)': 'Kurdî (Kurmanji)',
    'kyrgyz': 'Кыргызча',
    'lao': 'ລາວ',
    'latin': 'Latine',
    'latvian': 'Latviešu',
    'lithuanian': 'Lietuvių',
    'luxembourgish': 'Lëtzebuergesch',
    'macedonian': 'Македонски',
    'malagasy': 'Malagasy',
    'malay': 'Bahasa Melayu',
    'malayalam': 'മലയാളം',
    'maltese': 'Malti',
    'maori': 'Te Reo Māori',
    'marathi': 'मराठी',
    'mongolian': 'Монгол',
    'myanmar (burmese)': 'မြန်မာ (ဗမာ)',
    'nepali': 'नेपाली',
    'norwegian': 'Norsk',
    'nyanja (chichewa)': 'Nyanja (Chichewa)',
    'odia': 'ଓଡ଼ିଆ',
    'pashto': 'پښتو',
    'persian': 'فارسی',
    'polish': 'Polski',
    'portuguese': 'Português',
    'punjabi': 'ਪੰਜਾਬੀ',
    'romanian': 'Română',
    'russian': 'Русский',
    'samoan': 'Gagana Sāmoa',
    'scots gaelic': 'Gàidhlig',
    'serbian': 'Српски',
    'sesotho': 'Sesotho',
    'shona': 'ChiShona',
    'sindhi': 'سنڌي',
    'sinhala (sinhalese)': 'සිංහල',
    'slovak': 'Slovenčina',
    'slovenian': 'Slovenščina',
    'somali': 'Soomaali',
    'spanish': 'Español',
    'sundanese': 'Basa Sunda',
    'swahili': 'Kiswahili',
    'swedish': 'Svenska',
    'tagalog (filipino)': 'Tagalog (Filipino)',
    'tajik': 'Тоҷикӣ',
    'tamil': 'தமிழ்',
    'tatar': 'Татарча',
    'telugu': 'తెలుగు',
    'thai': 'ไทย',
    'turkish': 'Türkçe',
    'turkmen': 'Türkmen',
    'ukrainian': 'Українська',
    'urdu': 'اردو',
    'uyghur': 'ئۇيغۇرچە',
    'uzbek': 'Oʻzbek',
    'vietnamese': 'Tiếng Việt',
    'welsh': 'Cymraeg',
    'xhosa': 'isiXhosa',
    'yiddish': 'ייִדיש',
    'yoruba': 'Yorùbá',
    'zulu': 'isiZulu'
}

lang_list = [language_names.get(lang, lang) for lang in lang_codes.keys()]

# Standardsprache auf Deutsch (German) und Englisch (English)
source_lang = tk.StringVar(value='Deutsch')  # Standard: Deutsch
destination_lang = tk.StringVar(value='English')  # Standard: Englisch

# GUI-Elemente erstellen
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Originaltext:").grid(row=0, column=0, sticky=tk.W)
source_text = tk.Text(frame, height=10, width=50)
source_text.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Originalsprache:").grid(row=2, column=0, sticky=tk.W)
source_lang_combo = ttk.Combobox(frame, textvariable=source_lang, values=lang_list)
source_lang_combo.grid(row=2, column=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Zielsprache:").grid(row=3, column=0, sticky=tk.W)
destination_lang_combo = ttk.Combobox(frame, textvariable=destination_lang, values=lang_list)
destination_lang_combo.grid(row=3, column=1, sticky=(tk.W, tk.E))

translate_button = ttk.Button(frame, text="Übersetzen", command=translate_text)
translate_button.grid(row=4, column=0, columnspan=2)

ttk.Label(frame, text="Übersetzter Text:").grid(row=5, column=0, sticky=tk.W)
translated_text = tk.Text(frame, height=10, width=50)
translated_text.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E))

root.mainloop()

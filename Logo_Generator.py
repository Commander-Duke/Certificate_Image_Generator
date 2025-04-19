from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# Bildgröße und Hintergrund
width, height = 900, 800
bg_color = (255, 255, 250)
certificate = Image.new("RGB", (width, height), bg_color)
draw = ImageDraw.Draw(certificate)

# Schriften definieren
try:
    font_title = ImageFont.truetype("/Library/Fonts/Verdana.ttf", 36)
    font_content = ImageFont.truetype("/Library/Fonts/Verdana.ttf", 20)
    font_small = ImageFont.truetype("/Library/Fonts/Verdana.ttf", 18)
except:
    font_title = font_content = font_small = ImageFont.load_default()

# EU-Logo laden
eu_logo = Image.open("eu_logo.png").resize((150, 100))
certificate.paste(eu_logo, (50, 50), eu_logo.convert("RGBA"))

# Siegel erstellen (Beispiel rot)
#draw.ellipse((width-200, height-200, width-50, height-50), outline='red', width=5)

# Titel und Text hinzufügen
draw.text((width / 2, 120), "Europäische Union", fill='black', font=font_title, anchor="mm")
draw.text((width / 2, 180), "Offizielles Zertifikat", fill='black', font=font_content, anchor="mm")
draw.text((width / 2, 230), "zur professionellen Anwendung von Künstlicher Intelligenz für Frauenheilkunde", fill='black', font=font_content, anchor="mm")

# Empfänger
draw.text((width / 2, 320), "Verliehen an:", fill='black', font=font_content, anchor="mm")
draw.text((width / 2, 360), "Herrn Dr. Landvoigt", fill='black', font=font_title, anchor="mm")

# Beschreibungstext
text = ("Dieses Zertifikat bestätigt, dass der Inhaber befähigt ist,\n"
        "Künstliche Intelligenz für Frauenheilkunde gemäß den Standards und ethischen\n"
        "Richtlinien der Europäischen Union professionell einzusetzen.")
draw.multiline_text((width / 2, 450), text, fill='black', font=font_small, anchor="mm", align='center')

# Datum und Ort
date_str = f"Brüssel, {datetime.now().strftime('%d.%m.%Y')}"
draw.text((width / 2, 550), date_str, fill='black', font=font_small, anchor="mm")

# Unterschriften laden und einfügen
signature_vdl = Image.open("signature_vdl.png").resize((200, 80))
certificate.paste(signature_vdl, (int(width / 4 - 100), 600), signature_vdl.convert("RGBA"))

signature_breton = Image.open("schiwago_sign.jpg").resize((200, 80))
certificate.paste(signature_breton, (int(3 * width / 4 - 100), 600), signature_breton.convert("RGBA"))

signature_siegel = Image.open("notarsiegel-800.jpg").resize((100, 100))
certificate.paste(signature_siegel, (int(width / 2 + 150),500), signature_siegel.convert("RGBA"))



# Namen unter Unterschriften
draw.text((width / 4, 690), "Ursula von der Leyen\nPräsidentin der EU-Kommission", fill='black', font=font_small, anchor="mm", align="center")
draw.text((3 * width / 4, 690), "Dr. Schiwago\nEU-Kommissar für Frauen", fill='black', font=font_small, anchor="mm", align="center")

# Rahmen zeichnen
draw.rectangle([10, 10, width-10, height-10], outline=(0, 51, 153), width=5)

# Speichern des Zertifikats
certificate.save("Offizielles_Zertifikat_Langvoigt.png")
import tkinter as tk
from tkinter import filedialog
from tkhtmlview import HTMLLabel

class HTMLFileGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("HTML File Generator")

        # Variables pour le titre, le chemin du fichier, l'image, le texte alternatif et les paragraphes
        self.title_var = tk.StringVar()
        self.file_path = tk.StringVar()
        self.image_path_var = tk.StringVar()
        self.alt_text_var = tk.StringVar()
        self.intro_var = tk.StringVar()
        self.content_var = tk.StringVar()
        self.thanks_var = tk.StringVar()
        self.signature_var = tk.StringVar()

        # Frame pour le contenu
        self.content_frame = tk.Frame(root)
        self.content_frame.pack(pady=20)

        # Zone de texte pour le titre
        self.title_label = tk.Label(self.content_frame, text="Titre du HTML:")
        self.title_label.grid(row=0, column=0, padx=10, pady=10)

        self.title_entry = tk.Entry(self.content_frame, textvariable=self.title_var, width=30)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        # Zone de texte pour le chemin de l'image
        image_label = tk.Label(self.content_frame, text="Chemin de l'image:")
        image_label.grid(row=1, column=0, padx=10, pady=10)

        self.image_entry = tk.Entry(self.content_frame, textvariable=self.image_path_var, width=30)
        self.image_entry.grid(row=1, column=1, padx=10, pady=10)

        # Bouton pour sélectionner l'image
        select_image_button = tk.Button(self.content_frame, text="Sélectionner Image", command=self.select_image)
        select_image_button.grid(row=1, column=2, padx=10, pady=10)

        # Zone de texte pour le texte alternatif
        alt_text_label = tk.Label(self.content_frame, text="Texte alternatif de l'image:")
        alt_text_label.grid(row=2, column=0, padx=10, pady=10)

        self.alt_text_entry = tk.Entry(self.content_frame, textvariable=self.alt_text_var, width=30)
        self.alt_text_entry.grid(row=2, column=1, padx=10, pady=10)

        # Zone de texte pour l'introduction de l'article
        intro_label = tk.Label(self.content_frame, text="Introduction de l'article:")
        intro_label.grid(row=3, column=0, padx=10, pady=10)

        self.intro_text = tk.Text(self.content_frame, width=30, height=4)
        self.intro_text.grid(row=3, column=1, padx=10, pady=10)

        # Zone de texte pour le contenu de l'article
        content_label = tk.Label(self.content_frame, text="Contenu de votre article:")
        content_label.grid(row=4, column=0, padx=10, pady=10)

        self.content_text = tk.Text(self.content_frame, width=30, height=8)
        self.content_text.grid(row=4, column=1, padx=10, pady=10)

        # Zone de texte pour le remerciement
        thanks_label = tk.Label(self.content_frame, text="Remerciement:")
        thanks_label.grid(row=5, column=0, padx=10, pady=10)

        self.thanks_text = tk.Text(self.content_frame, width=30, height=2)
        self.thanks_text.grid(row=5, column=1, padx=10, pady=10)

        # Zone de texte pour la signature
        signature_label = tk.Label(self.content_frame, text="Signature:")
        signature_label.grid(row=6, column=0, padx=10, pady=10)

        self.signature_text = tk.Text(self.content_frame, width=30, height=2)
        self.signature_text.grid(row=6, column=1, padx=10, pady=10)

        # Bouton pour créer le dossier et le fichier HTML
        self.create_button = tk.Button(self.content_frame, text="Créer HTML", command=self.create_folder)
        self.create_button.grid(row=7, column=0, columnspan=3, pady=20)

        # Bouton "Avancé"
        self.advanced_button = tk.Button(self.content_frame, text="Avancé", command=self.show_advanced_editor)
        self.advanced_button.grid(row=8, column=0, columnspan=3, pady=20)

        # Label pour afficher le chemin du fichier créé
        self.result_label = tk.Label(root, textvariable=self.file_path)
        self.result_label.pack()

        # Frame pour l'aperçu HTML
        self.preview_frame = tk.Frame(root)
        self.preview_frame.pack(pady=20)

        # HTMLLabel pour l'aperçu
        self.html_preview_label = HTMLLabel(self.preview_frame, html="")
        self.html_preview_label.pack(expand=True, fill='both')

    def show_advanced_editor(self):
        # Création d'une nouvelle fenêtre pour l'éditeur HTML avancé
        editor_window = tk.Toplevel(self.root)
        editor_window.title("Éditeur HTML Avancé")

        # Création de l'éditeur HTMLLabel dans la nouvelle fenêtre
        html_label = HTMLLabel(editor_window, html=self.generate_advanced_html_content(), editable=True)
        html_label.pack(expand=True, fill='both')

    def generate_advanced_html_content(self):
        # Générez ici le contenu HTML avancé en fonction de vos besoins
        # Vous pouvez utiliser les variables actuelles comme self.title_var, self.image_path_var, etc.
        advanced_html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>{self.title_var.get()}</title>
          <style>
            /* Vos styles CSS avancés ici */
          </style>
        </head>
        <body>
          <div>
            <h1>{self.title_var.get()}</h1>
            <p>{self.intro_text.get("1.0", tk.END)}</p>
            <p>{self.content_text.get("1.0", tk.END)}</p>
            <a href="https://example.com">Découvrir</a>
            <p>{self.thanks_text.get("1.0", tk.END)}</p>
            <p>{self.signature_text.get("1.0", tk.END)}</p>
          </div>
        </body>
        </html>
        """

        return advanced_html_content

    def create_html_file(self, folder_path):
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>{self.title_var.get()}</title>
          <style>
            /* Utilisez des styles en ligne autant que possible */
            body {{
              font-family: Arial, sans-serif;
              margin: 0;
              padding: 0;
            }}
            .container {{
              width: 100%;
              max-width: 600px;
              margin: 0 auto;
              background-color: #b7e2ec;
              padding: 20px;
            }}
            h1 {{
              color: #333;
            }}
            p {{
              color: #555;
            }}
            .cta-button {{
              display: inline-block;
              padding: 10px 20px;
              background-color: #007BFF;
              color: #fff;
              text-decoration: none;
              border-radius: 5px;
            }}
          </style>
        </head>
        <body>
          <div class="container">
            <div style="text-align: center">
              <header>
                <img src="{self.image_path_var.get()}" alt="{self.alt_text_var.get()}" width="550" height="auto">
              </header>
            </div>
            <h1>{self.title_var.get()}</h1>
            <p>{self.intro_text.get("1.0", tk.END)}</p>
            <p>{self.content_text.get("1.0", tk.END)}</p>
            <a href="https://example.com" class="cta-button">Découvrir</a>
            <p>{self.thanks_text.get("1.0", tk.END)}</p>
            <p>{self.signature_text.get("1.0", tk.END)}</p>
          </div>
        </body>
        </html>
        """

        file_path = folder_path + "/index.html"
        with open(file_path, "w") as html_file:
            html_file.write(html_content)

        self.file_path.set(f"HTML file created at:\n{file_path}")

        # Mettez à jour l'aperçu HTML
        self.html_preview_label.set_html(html_content)

    def create_folder(self):
        folder_path = filedialog.askdirectory(title="Select Folder to Create HTML File")

        if folder_path:
            self.create_html_file(folder_path)

    def select_image(self):
        image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if image_path:
            self.image_path_var.set(image_path)

# Création de la fenêtre principale
root = tk.Tk()
app = HTMLFileGenerator(root)

# Lancement de la boucle principale
root.mainloop()

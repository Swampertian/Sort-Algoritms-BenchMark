"""
Packages the complete project into a .zip file ready for AVA submission.
"""
import os
import zipfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ZIP_FILENAME = os.path.join(BASE_DIR, "entrega_trabalho_ordenacao_uft.zip")

INCLUDE_DIRS = [
    "src",
    "bench",
    "docs",
    "tests",
    "relatorio",
    "apresentacao",
]

INCLUDE_FILES = [
    "README.md",
    "generate_pdf_deliverables.py",
]

EXCLUDE_EXTS = {".pyc"}
EXCLUDE_DIRS = {"__pycache__", ".git"}


def make_delivery_zip():
    print(f"Creating delivery zip: {ZIP_FILENAME}")
    with zipfile.ZipFile(ZIP_FILENAME, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Include top-level files
        for filename in INCLUDE_FILES:
            filepath = os.path.join(BASE_DIR, filename)
            if os.path.exists(filepath):
                zipf.write(filepath, arcname=filename)
                print(f"  + Added: {filename}")

        # Include directories
        for dirname in INCLUDE_DIRS:
            dirpath = os.path.join(BASE_DIR, dirname)
            if not os.path.exists(dirpath):
                continue
            for root, dirs, files in os.walk(dirpath):
                dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
                for file in files:
                    if any(file.endswith(ext) for ext in EXCLUDE_EXTS):
                        continue
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, BASE_DIR)
                    zipf.write(full_path, arcname=rel_path)
                    print(f"  + Added: {rel_path}")

    print(f"\n[SUCESSO] Pacote de entrega gerado: {ZIP_FILENAME} ({os.path.getsize(ZIP_FILENAME):,} bytes)")


if __name__ == "__main__":
    make_delivery_zip()

from pypdf import PdfReader, PdfWriter
from pathlib import Path

def split_pdf(pdf_path:Path, out_dir_path:Path):
    pdf_path = pdf_path.resolve()
    out_dir_path = out_dir_path.resolve()
    
    if not isinstance(pdf_path, Path) or not isinstance(out_dir_path, Path):
        raise TypeError("Invalid path type recieved.")
    
    if not pdf_path.exists():
        raise ValueError("input pdf does not exist.")
    
    if not pdf_path.is_file():
        raise ValueError("input pdf is not a file.")
    
    if not out_dir_path.exists():
        raise ValueError("Output path does not exist.")
    
    if not out_dir_path.is_dir():
        raise ValueError("Output path is not a directory.")
    
    try:
        reader = PdfReader(pdf_path)
    except:
        raise RuntimeError("Failed to open pdf")
    
    field_width = len(str(len(reader.pages)))
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        writer.write(Path(f"{out_dir_path}/{pdf_path.stem}_{str(i+1).zfill(field_width)}.pdf"))

if __name__ == '__main__':
    CURRENT_DIR = Path(__file__).resolve().parent
    file_path = CURRENT_DIR / "../../test/sample_document.pdf"
    out_dir_path = CURRENT_DIR / "../../test"
    
    split_pdf(file_path, out_dir_path)
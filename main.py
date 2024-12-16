import fitz  # PyMuPDF
import os

def extract_images_from_pdf(pdf_path, output_dir):
    """Extracts all images from a PDF and saves them in the output directory."""
    os.makedirs(output_dir, exist_ok=True)
    pdf_document = fitz.open(pdf_path)

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        images = page.get_images(full=True)
        
        if not images:
            print(f"No images found on page {page_num + 1}")
            continue
        
        for img_index, img in enumerate(images, start=1):
            xref = img[0]  # Image reference index
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]  # Image format (e.g., jpg, png)
            img_path = os.path.join(output_dir, f"page_{page_num + 1}_img_{img_index}.{image_ext}")
            
            with open(img_path, "wb") as img_file:
                img_file.write(image_bytes)
            print(f"Saved image: {img_path}")

# Example usage
pdf_path = r"  "  # Replace with the path to your PDF
output_dir = r" "  # Replace with your desired output directory
extract_images_from_pdf(pdf_path, output_dir)

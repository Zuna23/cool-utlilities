from pypdf import PdfReader, PdfWriter

# Input/output file paths
input_pdf_path = "28072025113647.pdf"
output_pdf_path = "unlocked.pdf"
password = ""  # Replace with your actual password

# Load and decrypt the PDF
reader = PdfReader(input_pdf_path)
if reader.is_encrypted:
    reader.decrypt(password)

# Create a new writer and copy pages
writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)

# Save the unlocked PDF
with open(output_pdf_path, "wb") as f:
    writer.write(f)

print(f"Unlocked PDF saved as: {output_pdf_path}")

import PyPDF2

# Open the PDF file in read-binary mode
with open("form.pdf", 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # Check if the PDF is encrypted
    if reader.is_encrypted:
        try:
            reader.decrypt("")  # Provide the password if required, or leave empty for no password
        except Exception as e:
            print(f"Failed to decrypt the PDF: {e}")
            exit()

    # Read and print the content of each page
    for page in reader.pages:
        print(page.extract_text())

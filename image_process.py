import pytesseract
from PIL import Image
from summa import summarizer

def upload_image():
    """Prompts the user to select an image file and returns its path."""
    while True:
        image_path = input("Enter the path to your image (or 'q' to quit): ")
        if image_path.lower() == 'q':
            return None
        if not image_path:
            print("Please enter a valid image path.")
            continue
        try:
            Image.open(image_path)
            return image_path
        except FileNotFoundError:
            print("File not found. Please try again.")

def extract_text(image_path):
    """Uses Tesseract OCR to extract text from the image."""
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update Tesseract path if needed
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text.strip()  # Remove extra newlines

def summarize_text(text):
    """Uses Summa summarizer to generate a summary of the extracted text."""
    try:
        summary = summarizer(text, ratio=0.2)  # Adjust ratio for desired summary length (0.2 for 20%)
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "Summary unavailable."

def main():
    """Main function to handle image upload, text extraction, and summarization."""
    image_path = upload_image()
    if not image_path:
        return

    extracted_text = extract_text(image_path)
    if not extracted_text:
        print("No text found in the image.")
        return

    summary = summarize_text(extracted_text)
    print("\nExtracted Text:")
    print(extracted_text)
    print("\nSummary:")
    print(summary)

if __name__ == "__main__":
    main()

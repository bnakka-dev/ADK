import re

def extract_upc_from_image_text(text_from_invoice: str) -> dict:
    """
    Analyzes the text extracted from an invoice image to find 12-digit UPC codes.
    
    Args:
        text_from_invoice: The text content Gemini 'sees' in the uploaded image.
    """
    # Regex to find 12-digit sequences, often found near 'UPC' or 'SKU' labels
    upc_pattern = r"\b\d{12}\b"
    found_codes = re.findall(upc_pattern, text_from_invoice)
    
    return {
        "status": "success" if found_codes else "not_found",
        "upc_count": len(found_codes),
        "codes": list(set(found_codes)) # Remove duplicates
    }
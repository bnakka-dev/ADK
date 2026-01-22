from __future__ import annotations
import os
import logging
import json
from dotenv import load_dotenv
from google.adk.agents import Agent
from .tools import extract_upc_from_image_text
from .schema import InvoiceSchema

load_dotenv()
model_name = os.getenv("ADK_MODEL")

# Configure logging to display responses in CLI
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

root_agent = Agent(
    name="ProInvoiceScanner",
    model=model_name,
    # Updated: use output_schema and add an output_key
    output_schema=InvoiceSchema,
    output_key="invoice_data", 
    tools=[extract_upc_from_image_text],
    instruction="""
    You are a professional Data Extraction Agent. 
    1. Analyze the uploaded invoice image with high precision.
    2. Extract all fields required by the schema.
    3. For dates, use MM-DD-YYYY format. 
    4. If a value is missing, use 'NA' for strings and 0 for numbers.
    5. Ensure the 'items' list contains every product found on the invoice.
    6. Return the data ONLY in the requested JSON format.
    
    IMPORTANT: After extracting the data, always log your findings by stating:
    "EXTRACTED DATA: [your extracted JSON data here]"
    """
)

# Log agent initialization
logger.info("=== Invoice Parser Agent Initialized ===")
logger.info(f"Agent Name: {root_agent.name}")
logger.info(f"Model: {model_name}")
logger.info("Agent ready to process invoices!")
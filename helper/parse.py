from google.generativeai import GenerativeModel
from dotenv import load_dotenv

load_dotenv()

model = GenerativeModel("gemini-1.5-flash")

# Parsing template
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Only extract the data that directly matches the provided description: {parse_description}. "
    "If no information matches, return an empty string ('')."
)


def parse_with_google_gemini(dom_chunks, parse_description):
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        # Construct the prompt
        prompt = template.format(dom_content=chunk, parse_description=parse_description)

        # Generate response using Google Gemini
        response = model.generate_content(contents=[{"parts": [{"text": prompt}]}])

        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(response.text)

    return "\n".join(parsed_results)

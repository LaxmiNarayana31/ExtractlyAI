# WebScribe-AI

An AI-powered web scraper and content parser that extracts, cleans, and analyzes web content efficiently. WebScribe simplifies data retrieval from websites, making it customizable, fast, and intuitive.

## Features

- **Web Scraping**: Automatically fetch and extract content from any website using Selenium.
- **Content Cleaning**: Removes unnecessary elements like scripts and styles, leaving only meaningful data.
- **AI-Powered Parsing**: Uses Google Gemini to analyze and extract specific information based on user input.
- **Streamlit UI**: A user-friendly interface to input websites, parse content, and display results interactively.

## How It Works

1. **Input Website URL**: Enter the URL of the website you want to scrape.
2. **Scrape Content**: Extract and clean the content using powerful scraping logic.
3. **Describe Your Query**: Provide instructions for the type of information you need.
4. **Get Results**: AI processes the content and delivers the requested information.

## Technologies Used

- **Python**: The primary programming language used for development.
- **Streamlit**: For building the user-friendly web interface.
- **Selenium**: Utilized for web scraping to fetch and automate browser interactions.
- **BeautifulSoup**: Employed for parsing HTML and extracting content.
- **Google Gemini API**: Provides AI-powered parsing capabilities for analyzing and extracting specific information.
- **LangChain**: Integrated for large language model (LLM) operations and advanced AI functionalities.

## Installation

To set up WebScribe-AI on your local machine:

1. Clone the repository: `git clone https://github.com/LaxmiNarayana31/WebScribe-AI.git`
2. Create a virtual environment: `pipenv shell`
3. Install dependencies: `pipenv install`
4. Run the Streamlit app: `streamlit run main.py` or `pipenv run main`

# ExtractlyAI

An AI-powered web scraper and content parser that extracts, cleans, and analyzes web content efficiently. ExtractlyAI simplifies data retrieval from websites, making it customizable, fast, and intuitive.

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

## Project Setup

- Clone the repository:
  ```bash
  git clone https://github.com/LaxmiNarayana31/ExtractlyAI.git
  ```
- Create a virtual environment using pipenv. If you don't have pipenv installed, you can install it by running `pip install pipenv` in your terminal.
  ```bash
  pipenv shell # Create a virtual environment
  pipenv install # Install dependencies
  ```
- Run the application:
  ```bash
  pipenv run main

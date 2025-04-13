# Modular AI Agent - Lead Qualification Chatbot

This project implements a lead qualification chatbot using FastAPI, LangChain, OpenAI, and Qdrant. The chatbot is designed to assist users with inquiries about retreats, such as Ayahuasca, location, and pricing, while also capturing leads for further engagement.

## Project Structure

```
modular-ai-agent
├── src
│   ├── embed.py          # Functions for loading, chunking, embedding documents, and storing embeddings
│   ├── retriever.py      # Functions for querying Qdrant and retrieving context for GPT-4
│   ├── lead_logger.py    # Functions for logging leads and extracting user information
│   └── main.py           # FastAPI server setup and chat endpoint
├── requirements.txt      # List of project dependencies
├── README.md             # Project documentation
└── .env                  # Environment variables for API keys and database connections
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/modular-ai-agent.git
   cd modular-ai-agent
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and add your API keys and database connection strings:
   ```
   OPENAI_API_KEY=your_openai_api_key
   QDRANT_URL=your_qdrant_url
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   ```

5. Install Playwright browsers: (for webscraping)
   ```bash
   playwright install
   ```

3. Run the scraper:
   ```bash
   python src/scrape_site.py

## Usage

To start the FastAPI server, run the following command:
```
uvicorn src.main:app --reload
```

You can then access the chatbot at `http://localhost:8000/chat`. Send a POST request with a JSON body containing the user message to receive a response from the chatbot.

## Key Features

- **Document Embedding:** Load and embed retreat documents using OpenAI's embeddings and store them in Qdrant for efficient retrieval.
- **Contextual Responses:** Utilize LangChain to query Qdrant and provide context-based answers using GPT-4.
- **Lead Detection:** Automatically detect user interest and log leads to Supabase or Airtable for follow-up.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

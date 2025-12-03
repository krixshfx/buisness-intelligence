
# MSPCC Analytical Dashboard (Streamlit) ⚙☁

## Overview

This project transforms a Flask-based analytical dashboard into a modern, interactive Streamlit application. Leveraging the power of Streamlit for a responsive user interface and integrating Google's Gemini AI for advanced analytics, this dashboard provides small retail business owners with actionable insights into product performance, marketing strategies, sales forecasting, and compliance. The goal is to offer a robust, easy-to-deploy tool that mirrors the effectiveness and operation of the original application.

## Features

The Streamlit dashboard offers the following key functionalities:

*   **Dashboard**: Visualize overall business performance, including total weekly profit, revenue, and average margin. Displays top products by profit and a live AI-generated business overview.
*   **Data Upload**: Easily upload product data (CSV/text) for AI-powered parsing, metric calculation, and integration into the dashboard.
*   **AI Insights**: Ask natural language questions about your product data and receive AI-driven textual insights and supporting visualizations.
*   **Marketing Simulator**: Simulate the impact of discounts and sales lift on individual product profitability, accompanied by AI-generated marketing advice and comparison charts.
*   **Sales Forecast**: Obtain AI-powered sales forecasts for products and receive intelligent reorder suggestions to optimize inventory.
*   **Compliance Checklist**: Generate a general business compliance checklist tailored to specific locations and business types using AI.
*   **Web Data Extractor**: Utilize AI to extract and structure real-time, publicly available data from the web based on user queries, providing source information for verification.
*   **Report Generator**: Create comprehensive, multi-page PDF audit reports summarizing business performance, data quality, market analysis, and strategic recommendations.

## Setup and Installation

Follow these steps to get the Streamlit application up and running locally:

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd mspcc-analytical-dashboard-streamlit
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scriptsctivate`
```

### 3. Install Dependencies

All required Python packages are listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Google Gemini API Key

Many of the core analytical features rely on the Google Gemini API. You will need an API key to enable these features.

1.  **Obtain an API Key**: Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and create a new API key.
2.  **Set as Environment Variable**: It's recommended to set your API key as an environment variable named `GOOGLE_API_KEY`. Streamlit applications can securely access this.

    *   **For local development**: Create a `.env` file in the root directory of your project and add:
        ```
        GOOGLE_API_KEY="your-api-key-here"
        ```
        Then, install `python-dotenv` (`pip install python-dotenv`) and add `from dotenv import load_dotenv; load_dotenv()` at the very top of your `app.py`.
    *   **For Streamlit Cloud deployment**: Add `GOOGLE_API_KEY` to your app's secrets management (`Settings > Secrets`).

## Running the Application

Once the dependencies are installed and your API key is configured, you can run the Streamlit application:

```bash
streamlit run app.py
```

This command will open the application in your web browser.

## Deployment

This application is designed for easy deployment to platforms that support Streamlit applications:

*   **Streamlit Cloud**: Simply push your code to a GitHub repository, and connect it to Streamlit Cloud for instant deployment.
*   **Hugging Face Spaces**: Upload your files to a new Space, ensuring `app.py` and `requirements.txt` are in the root directory.
*   **GitHub Pages / Other Static Hosting (with custom setup)**: While Streamlit is dynamic, it can be containerized and deployed. For simpler cases, Streamlit Cloud or Hugging Face Spaces are recommended.

## Project Structure

```
.  # Root directory
├── app.py             # Main Streamlit application file
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation (this file)
└── .streamlit/          # (Optional) Streamlit configuration files
    └── config.toml
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details (if applicable, otherwise state 'No License Specified').


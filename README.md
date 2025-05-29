# Web Scraper for Titles and Prices with Streamlit GUI

A Python project that utilizes `requests` to fetch web content and `BeautifulSoup` to parse HTML via `base.py`. The extracted data (titles and prices) is then displayed in a user-friendly web interface powered by Streamlit in `run.py`.

## Features

* Fetches live web content using the `requests` library (`base.py`).
* Parses HTML structure using `BeautifulSoup4` (`base.py`).
* Extracts desired data elements (e.g., product titles and prices) based on HTML tags and attributes.
* Performs basic text cleaning.
* Stores extracted data efficiently in a Python dictionary.
* **User-friendly Graphical User Interface (GUI)** built with Streamlit to display the scraped data (`run.py`).

## Project Structure

* `base.py`: Contains the core web scraping logic. It uses `requests` to fetch web pages and `BeautifulSoup` to parse HTML and extract data (titles and prices). This script is typically imported by `run.py`.
* `run.py`: Implements the Streamlit web application. It imports data fetching/processing functions from `base.py` and presents the scraped information in the GUI.
* `requirements.txt`: Lists all Python dependencies for the project.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.7+ installed.
* `pip` (Python package installer) installed.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    Your `requirements.txt` file should look something like this:
    ```txt
    requests
    beautifulsoup4
    streamlit
    ```
    Then install them:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Application

1.  **Configure the Scraper (`base.py`):**
    * Open the `base.py` script.
    * **Set the `TARGET_URL`:** Modify the variable holding the URL to point to the webpage you want to scrape.
        ```python
        # Inside base.py
        TARGET_URL = "YOUR_TARGET_URL_HERE" # e.g., "[https://www.example.com/products](https://www.example.com/products)"
        ```
    * **Adjust BeautifulSoup Selectors:** This is the most crucial step and is **highly dependent on the structure of the target website**. You need to inspect the HTML of the target webpage in `base.py` to find the correct tags, classes, or IDs for the titles and prices.
        For example, if titles are in `<h2>` tags with class `product-title` and prices are in `<span>` tags with class `price-tag`, your code in `base.py` to find these elements might look like this:
        ```python
        # Inside base.py, within your scraping function:
        # response = requests.get(TARGET_URL)
        # soup = BeautifulSoup(response.content, 'html.parser')

        # Example: Find all title elements
        title_elements = soup.find_all('h2', class_='product-title')
        # Example: Find all price elements
        price_elements = soup.find_all('span', class_='price-tag')

        # Your script will then process these elements
        ```
        **You MUST update these selectors in `base.py` to match the website you are scraping.** Use your browser's developer tools (usually by right-clicking an element and selecting "Inspect") to find the appropriate selectors.
        Ensure `base.py` has a function that `run.py` can call to get the scraped data (e.g., a function that returns the dictionary of titles and prices).

2.  **Run the Streamlit Application (`run.py`):**
    Once `base.py` is configured, execute the `run.py` script using Streamlit from your terminal:
    ```bash
    streamlit run run.py
    ```

3.  **View the Application:**
    Streamlit will typically open the application automatically in your default web browser. If not, it will provide a local URL (e.g., `http://localhost:8501`) that you can navigate to. You should see the scraped titles and prices displayed in the Streamlit interface.

## Example Data Display (Illustrative)

The Streamlit application (`run.py`) might display the data in a table, as list items, or in any other format you define using Streamlit components. For example:

* A table showing "Product Title" and "Price".
* A series of cards, each displaying a title and its price.

## Disclaimer

* Web scraping can be against the terms of service of some websites. Always check a website's `robots.txt` file and its terms of service before scraping.
* Website structures change frequently. If the target website's HTML structure changes, the selectors in `base.py` will need to be updated.
* Be a responsible scraper: don't send too many requests in a short period to avoid overloading the website's server. Implement delays in `base.py` if necessary.

## Contributing (Optional)

Contributions are welcome! If you have suggestions for improvements:
1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## License (Optional)

Distributed under the MIT License. See `LICENSE.txt` for more information.
(If you choose to add a license, create a `LICENSE.txt` file with the MIT license text, or your chosen license).

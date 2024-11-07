# LoopNet Scraper

This project is a Python-based web scraping tool designed to collect data from [LoopNet](https://www.loopnet.com). The tool is divided into two scripts: one for extracting property URLs and another for gathering detailed property information from those URLs.

## Project Structure

- `urlscrap.py`: This script scrapes the URLs of industrial properties from LoopNet.
- `infoscrap.py`: This script takes the URLs collected by `urlscrap.py` and scrapes detailed information from each property page.

## Setup and Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**

   ```sh
   git clone https://github.com/vkostiuk450/loopnet-scrap.git
   cd loopnet-scrap
   ```

2. **Create a Virtual Environment**

   To prevent potential conflicts with other packages, it's recommended to create a virtual environment.

   ```sh
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```sh
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```sh
     source venv/bin/activate
     ```

4. **Install Required Packages**

   Install the necessary Python packages using the provided `requirements.txt` file.

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run `urlscrap.py`**

   This script extracts URLs of industrial properties from LoopNet.

   ```sh
   python urlscrap.py
   ```

   Output: A list of URLs, typically saved to a file for further processing.

2. **Run `infoscrap.py`**

   Once you have your URLs, use this script to scrape detailed information from each URL.

   ```sh
   python infoscrap.py
   ```

   Output: Harvested data, typically stored in a structured format such as JSON or CSV.

## Notes

- Ensure you have the necessary permissions to scrape LoopNet as per their terms of service.
- Consider handling requests responsibly to avoid overloading LoopNet's servers with continuous requests.

## Contributing

Contributions are welcome. Please create a branch for any substantial changes and submit a pull request for review.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or issues, please contact vkostiuk450@gmail.com.
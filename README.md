# RedBus Bus Route Scraping Project

This project is a Python-based web scraper designed to extract bus route and service information from the RedBus website. It navigates through different state-specific pages, extracts details such as bus routes, names, timings, ratings, ticket prices, and seat availability, and then stores this data in a CSV file for further analysis. The project uses `Selenium` for web scraping and `Pandas` for data handling and manipulation.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [How It Works](#how-it-works)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Limitations and Improvements](#limitations-and-improvements)

## Features
- Scrapes bus routes and service details from the RedBus website for different states in India.
- Extracts key bus details such as:
  - **Bus Name**
  - **Bus Type**
  - **Departure Time**
  - **Reaching Time**
  - **Duration**
  - **Bus Ratings**
  - **Ticket Price**
  - **Seat Availability**
- Scrolls through multiple pages of bus routes and services.
- Handles pagination and dynamic loading of content.
- Data is stored in a CSV file (`Bus_Details_data.csv`), ready for further processing or analysis.

## Technologies
- **Python** for the scripting logic.
- **Selenium** for web automation and scraping.
- **Pandas** for data handling and processing.
- **Chrome WebDriver** for interacting with the web browser.
- **Regular Expressions (re)** for text cleaning and extraction.

## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- Google Chrome Browser
- Chrome WebDriver
- Required Python libraries: 
  - `selenium`
  - `pandas`
  - `re`

You can install the required Python packages using:

```bash
pip install selenium pandas
```

## How It Works
1. **URL Generation**: The project dynamically generates URLs for scraping by adjusting the date in the URL to scrape routes for a specific day. You can modify the day offset as needed (e.g., scrape for tomorrow, day after tomorrow, etc.).
2. **Web Navigation and Scrolling**: It navigates to the RedBus website, searches for bus routes based on the state, and scrolls down to load more data dynamically.
3. **Data Extraction**: It collects information from elements like bus name, type, departure/reaching times, ticket prices, and seat availability using `Selenium`'s `find_elements` method.
4. **Pagination Handling**: It iterates through multiple pages of results (up to 5 pages) to scrape all available data.
5. **Data Cleaning**: It cleans the scraped data (e.g., removing unwanted characters, splitting route information into departure and destination places).
6. **Saving Data**: The collected data is stored in a CSV file (`Bus_Details_data.csv`).

## File Structure
- `bus_scraper.py`: The main script that handles scraping and data extraction.
- `Bus_Details_data.csv`: The CSV file that contains the final extracted bus details.
- `chromedriver.exe`: Chrome WebDriver executable (required for Selenium to interact with Chrome).

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/redbus-bus-scraping.git
   cd redbus-bus-scraping
   ```

2. **Install Dependencies**:
   ```bash
   pip install selenium pandas
   ```

3. **Set up Chrome WebDriver**:
   - Download Chrome WebDriver matching your Chrome browser version from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Place the `chromedriver.exe` in your project directory or ensure it's in your system's PATH.

4. **Update the Script**:
   - If needed, modify the date offset in the `generate_url` function to adjust the date for which you want to scrape bus services.

## Usage
1. Open your terminal or command prompt in the project directory.
2. Run the scraper script:
   ```bash
   python bus_scraper.py
   ```
3. The script will open a Chrome browser window, navigate to the RedBus website, and start scraping bus routes and details for different states.
4. The data will be saved in `Bus_Details_data.csv`.

## Output
The final output will be a CSV file `Bus_Details_data.csv` containing the following columns:
- **Route_Name**: The bus route (From Place to Destination).
- **BusName**: Name of the bus service.
- **BusType**: Type of the bus (e.g., AC, Sleeper).
- **BusDepartureTime**: The departure time of the bus.
- **BusReachingTime**: The estimated arrival time at the destination.
- **Bus_Duration**: The total journey duration.
- **BusRating**: User rating of the bus.
- **TicketPrice**: Ticket price for the bus.
- **SeatAvailability**: The number of seats available.
- **From_Place**: The starting location of the bus.
- **To_Place**: The destination of the bus.

## Limitations and Improvements
- **Dynamic Content Loading**: The website uses dynamic content loading, which can sometimes cause the scraper to miss elements. Handling these cases with more robust waiting mechanisms could improve the scraping process.
- **Error Handling**: Currently, the script continues execution even if an error occurs for a particular state or bus route. Adding more granular error logging and handling can improve robustness.
- **Captcha and Anti-Scraping**: RedBus or other similar websites might introduce Captcha or other anti-scraping mechanisms, which could block the scraper. Using proxies or browser automation tools like `Selenium` with headless mode can help overcome this.


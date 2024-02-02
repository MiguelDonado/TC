# TC1 Data Extraction Project
This Python application is designed to extract data from TC1, an official document of the "seguridad social" in Spain, which is in PDF format. The extracted data is then written to an Excel file.

## Project Structure

- `definitive.py`: This is the main script that orchestrates the processing of the PDF files. It uses functions from `logic.py` and `output.py`.

- `logic.py`: This script contains functions for reading and extracting data from PDF files. It uses the `pdfplumber` library to read the PDF files and regular expressions from `support_regex.py` to extract the data.

- `output.py`: This script contains a function for writing the extracted data to an Excel file using the `openpyxl` library.

- `support_regex.py`: This script contains a collection of regular expressions that are used to extract specific data from the text of the PDF files.

## How to Run the Project
To run the project, execute the definitive.py file. This will extract data from the PDF files that are on the same directory that the source code and write the data to an Excel file.

## Dependencies
This project uses the pdfplumber library to read PDF files and the openpyxl library to write to Excel files. Make sure to install these libraries before running the project.

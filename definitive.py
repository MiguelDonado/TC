import output
import logic
import os


def main():
    pdf_files = get_files()
    progress(pdf_files)


def get_files():
    pdf_files = [f for f in os.listdir(".") if f.endswith(".pdf")]
    return pdf_files


def progress(pdf_files):
    # List that will contain the data of each row
    data_file = []
    # List that will contain the data of all rows
    data_files = []
    for file in pdf_files:
        data_file = logic.extract_file(file)
        for row in data_file:
            data_files.append(row)
    output.write_to_xlsx(data_files)


if __name__ == "__main__":
    main()

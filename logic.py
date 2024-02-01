import pdfplumber
from support_regex import (
    mes,
    fecha,
    numero_trabajad,
    liq_conting_com,
    liq_acc_trabajo,
    liq_otras_cotiz,
    bonif_inem,
    bonif_continua,
    demora,
    codigo_cta_cotizacion,
    calificador_liquidacion,
)


def read_pdf(file):
    # It'll return the text from the PDF file as one string
    with pdfplumber.open(file) as pdf:
        text_file = [page.extract_text() for page in pdf.pages]
    return text_file


def to_number(number):
    # Transform a string in the format 25.000,20 to a float in the format 25000.20
    if number:
        return float(number.group(1).replace(".", "").replace(",", "."))
    else:
        return 0.00


def extract_file(file):
    # Extract the data from the PDF file and return a list of lists
    text_pages = read_pdf(file)
    rows = []  # Will store the data from each page (each row is a list of 12 elements)
    for page in text_pages:
        # If the pdf is an img, or if the the pdf returns strange characters, it'll return an "ERROR" row
        if "Recibo de" not in page:
            row = ["ERROR"] * 12
        else:
            mes_field = mes.search(page).group(1)
            fecha_field = fecha.search(page).group(1)
            banco = ""  # We want to return nothing right here
            numero_trabajad_field = to_number(numero_trabajad.search(page))
            liq_conting_com_field = to_number(liq_conting_com.search(page))
            liq_acc_trabajo_field = to_number(liq_acc_trabajo.search(page))
            liq_otras_cotiz_field = to_number(liq_otras_cotiz.search(page))
            demora_field = to_number(demora.search(page))
            bonif_inem_field = to_number(bonif_inem.search(page))
            bonif_continua_field = to_number(bonif_continua.search(page))
            total_field = (
                liq_conting_com_field
                + liq_acc_trabajo_field
                + liq_otras_cotiz_field
                + demora_field
            )
            total_bonif_field = bonif_inem_field + bonif_continua_field
            codigo_cta_cotizacion_field = codigo_cta_cotizacion.search(page).group(1)
            calificador_liquidacion_field = calificador_liquidacion.search(page).group(
                1
            )
            row = (
                mes_field,
                fecha_field,
                banco,
                numero_trabajad_field,
                liq_conting_com_field,
                liq_acc_trabajo_field,
                liq_otras_cotiz_field,
                demora_field,
                total_field,
                total_bonif_field,
                codigo_cta_cotizacion_field,
                calificador_liquidacion_field,
            )
        rows.append(row)
    return rows

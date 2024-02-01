from openpyxl import Workbook


def write_to_xlsx(cuentas_cotizacion_total):
    # The argument is a list of tuples that contains all the parsed data.
    # It creates a xlsx with the desired format.
    # Example: [('01234567F','Ana Peryz Garcia','A', 1520.00, 12320.75, 2987.00),
    # ('00000000F','Pablo Alvaryz Garcia','A', 520.00, 22620.95, 497.00)...]

    wb = Workbook()
    ws = wb.active

    fieldnames = (
        "Mes",
        "Fecha",
        "Banco",
        "Nº",
        "General",
        "Accidente",
        "Otras",
        "Demora",
        "Total",
        "Bonificaciones",
        "Cuenta Cotizacion",
        "Calificador Liquidacion",
    )
    ws.append(fieldnames)

    for cuenta_cotizacion_mes in cuentas_cotizacion_total:
        ws.append(cuenta_cotizacion_mes)

    wb.save("TC.xlsx")

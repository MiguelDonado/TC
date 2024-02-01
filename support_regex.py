import re

mes = re.compile(r"^Per.*?n:\s(.*?)\sN", re.MULTILINE)
fecha = re.compile(r"Fecha:\s(.*?)\sHora", re.MULTILINE)
numero_trabajad = re.compile(
    r"mero\sde\strabajadores\sconfirmados:\s(\d+)$", re.MULTILINE
)
liq_conting_com = re.compile(
    r"^(?:LIQUIDO\sCONTINGENCIAS\sCOMUNES\s)(-?[0-9\.]+,\d\d)", re.MULTILINE
)
liq_acc_trabajo = re.compile(
    r"^(?:LIQUIDO\s(?:DE\s)?ACCIDENTES\sDE\sTRABAJO\s)(-?[0-9\.]+,\d\d)", re.MULTILINE
)
liq_otras_cotiz = re.compile(
    r"(?:LIQUIDO\s(?:DE\s)?OTRAS\sCOTIZACIONES\s)(-?[0-9\.]+,\d\d)", re.MULTILINE
)

bonif_continua = re.compile(
    "BONIFICACION FORMACION CONTINUA\s(-?[0-9\.]+,\d\d)", re.MULTILINE
)
bonif_inem = re.compile(
    "BONIF.Y SUBVENC.CON CARGO AL INEM\s(-?[0-9\.]+,\d\d)", re.MULTILINE
)
demora = re.compile(r"RECARGO\s\(\d+,\d\d%\)\s(-?[0-9\.]+,\d\d)", re.MULTILINE)
codigo_cta_cotizacion = re.compile(
    r"digo\sde\sCuenta\sde\sCotiza.*?:\s(.*?)\sC.digo\sde\sEmpresario", re.MULTILINE
)
calificador_liquidacion = re.compile(r"^Calificador.*?:\s(.*?)\sEntidad", re.MULTILINE)

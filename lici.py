from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def gerar_pdf(servidor, itens):
    # Nome do arquivo
    data_arquivo = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    nome_pdf = f"Licitacao_{data_arquivo}.pdf"

    # Criação do documento
    doc = SimpleDocTemplate(nome_pdf)
    styles = getSampleStyleSheet()
    elementos = []

    # Cabeçalho
    elementos.append(Paragraph("<b>IFCIENCIA PODCAST - PVA</b>", styles["Title"]))
    elementos.append(Spacer(1, 20))

    # Texto principal
    texto = (
        f"Por meio desta, a equipe do <b>IFCIENCIA PODCAST - PVA</b>, "
        f"cujo Servidor Responsável é: <b>{servidor}</b>, "
        f"solicita os seguintes objetos/serviços:"
    )

    elementos.append(Paragraph(texto, styles["BodyText"]))
    elementos.append(Spacer(1, 15))

    # Lista dos objetos
    for i, (objeto, quantidade) in enumerate(itens, start=1):
        elementos.append(
            Paragraph(
                f"{i}. Objeto/Serviço: <b>{objeto}</b><br/>"
                f"Quantidade: <b>{quantidade}</b>",
                styles["BodyText"]
            )
        )
        elementos.append(Spacer(1, 10))

    # Data e assinatura
    elementos.append(Spacer(1, 30))
    elementos.append(Paragraph("Data: ____________________________", styles["BodyText"]))
    elementos.append(Spacer(1, 20))
    elementos.append(Paragraph("Assinatura: _______________________", styles["BodyText"]))

    # Gerar PDF
    doc.build(elementos)

    print(f"\nPDF gerado com sucesso: {nome_pdf}\n")


while True:
    servidor = input("Digite o nome do Servidor Responsável >>> ")

    quantidade_itens = int(input("Quantos objetos/serviços serão solicitados? "))

    itens = []

    for i in range(quantidade_itens):
        print(f"\nObjeto {i+1}")
        objeto = input("Digite o objeto/serviço solicitado >>> ")
        quantidade = input("Digite a quantidade solicitada >>> ")

        itens.append((objeto, quantidade))

    input("\nAperte ENTER para confirmar a licitação...")

    gerar_pdf(servidor, itens)

    continuar = input("Deseja gerar outra licitação? (S/N): ").strip().upper()
    if continuar != "S":
        print("Programa encerrado.")
        break
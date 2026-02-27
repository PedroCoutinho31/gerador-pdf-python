from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from datetime import datetime

def gerar_pdf(nome_cliente: str, valor: str, descricao: str, saida="recibo.pdf"):
    c = canvas.Canvas(saida, pagesize=A4)
    largura, altura = A4

    # Cabeçalho
    c.setFont("Helvetica-Bold", 18)
    c.drawString(2*cm, altura - 2*cm, "RECIBO")

    c.setFont("Helvetica", 11)
    c.drawString(2*cm, altura - 2.8*cm, f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

    # Linha
    c.line(2*cm, altura - 3.2*cm, largura - 2*cm, altura - 3.2*cm)

    # Corpo
    c.setFont("Helvetica", 12)
    y = altura - 4.2*cm
    c.drawString(2*cm, y, f"Recebemos de: {nome_cliente}")
    y -= 0.9*cm
    c.drawString(2*cm, y, f"Valor: R$ {valor}")
    y -= 0.9*cm
    c.drawString(2*cm, y, "Referente a:")
    y -= 0.7*cm

    # Quebra de linha básica (wrap)
    largura_max = 90
    linhas = []
    while len(descricao) > largura_max:
        corte = descricao.rfind(" ", 0, largura_max)
        if corte == -1:
            corte = largura_max
        linhas.append(descricao[:corte].strip())
        descricao = descricao[corte:].strip()
    linhas.append(descricao)

    c.setFont("Helvetica-Oblique", 12)
    for linha in linhas:
        c.drawString(2*cm, y, f"- {linha}")
        y -= 0.7*cm

    # Rodapé / assinatura
    y -= 1.2*cm
    c.setFont("Helvetica", 11)
    c.drawString(2*cm, y, "Assinatura: ________________________________")

    c.showPage()
    c.save()
    print(f"PDF gerado: {saida}")

if __name__ == "__main__":
    nome = input("Nome do cliente: ").strip()
    valor = input("Valor (ex: 150,00): ").strip()
    desc = input("Descrição do serviço/produto: ").strip()

    if not nome or not valor or not desc:
        print("Preencha nome, valor e descrição.")
    else:
        gerar_pdf(nome, valor, desc)
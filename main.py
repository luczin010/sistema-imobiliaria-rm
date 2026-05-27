from classes.imovel import Imovel
from classes.contrato import Contrato
from classes.orcamento import Orcamento
from classes.arquivo_csv import ArquivoCSV

print("===== SISTEMA IMOBILIÁRIA R.M =====")

tipo = input("Digite o tipo do imóvel (apartamento/casa/estudio): ")

while tipo.lower() not in ["apartamento", "casa", "estudio"]:
    tipo = input("Tipo inválido! Digite apartamento, casa ou estudio: ")

quartos = 1

if tipo.lower() != "estudio":
    quartos = int(input("Quantidade de quartos (1 ou 2): "))

vagas = int(input("Quantidade de vagas/garagem: "))

criancas = False

if tipo.lower() == "apartamento":
    resposta = input("Possui crianças? (s/n): ")

    if resposta.lower() == "s":
        criancas = True

parcelas = int(input("Digite o número de parcelas do contrato (1 a 5): "))

while parcelas < 1 or parcelas > 5:
    parcelas = int(input("Valor inválido! Digite entre 1 e 5: "))

imovel = Imovel(tipo, quartos, vagas, criancas)

contrato = Contrato(2000, parcelas)

orcamento = Orcamento(imovel, contrato)

valor_final = orcamento.mostrar_orcamento()

valor_parcela = contrato.calcular_parcelas()

arquivo = ArquivoCSV()
arquivo.gerar_csv(valor_final, valor_parcela)

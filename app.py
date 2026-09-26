# -*- coding: utf-8 -*-
"""
Base de dados de manutenção de equipamentos (winders B1/B2).
Cada entrada representa um problema/código de erro, com:
  - "titulo": nome/código original do problema
  - "sintoma": descrição curta do sintoma (quando identificável no texto original)
  - "passos": lista de passos/verificações, em ordem, para diagnóstico e correção

Uso básico:
    from manutencao_db import MANUTENCAO_DB, buscar, listar_titulos, imprimir_passos

    imprimir_passos("b2 - erro 74")
"""

MANUTENCAO_DB = {

    "b2 - cinta": {
        "titulo": "B2 - Cinta",
        "sintoma": None,
        "passos": [
            "Verificar vibração do BH para ver se há empenamento (testar em manutenção).",
            "Verificar subida/descida do VTC se estiver trepidando ou travando. Se travar em processo, acionar elétrica.",
            "Verificar correia T/R, motor, polias e midle shaft.",
            "Verificar assentamento do C/A.",
            "Verificar pressão C/A avanço/retorno: fazer pressão com a mão. Se estiver leve, verificar manômetro ou cilindro ruim.",
            "Com o winder em processo, verificar assentamento do C/A. Se retornar ao acoplar no holder, trocar o cilindro.",
            "Verificar holders com ferrugem ou desgaste; se necessário, trocar o conjunto inteiro. Holders removidos devem ser ELIMINADOS, não recondicionados.",
        ],
    },

    "b2 - f/r b2": {
        "titulo": "B2 - F/R B2",
        "sintoma": "F/R em processo",
        "passos": [
            "Verificar C/R pesado.",
            "Verificar Holder B/H pesado.",
            "Verificar correias C/R e T/R.",
            "Verificar sensor de velocidade (acionar elétrica e checar os plugs embaixo do motor C/R).",
            "Verificar guide plates frouxas.",
            "Fazer verificação externa na parte superior, checando peças frouxas.",
        ],
    },

    "b2 - erro 74": {
        "titulo": "B2 - Erro 74",
        "sintoma": None,
        "passos": [
            "Verificar se o C/A voltou à posição do sensor.",
            "Verificar bucha plástica derretida.",
            "Verificar pressão de retorno do C/A.",
            "Se o cilindro avança/retorna normalmente, verificar se o sensor está aceso.",
            "Teste da tampa: acionar C/A e colocar a tampa atrás do cilindro. Se o sensor apagar, acionar elétrica para troca.",
            "Sempre verificar holder gasto.",
        ],
    },

    "b2 - erro 88": {
        "titulo": "B2 - Erro 88",
        "sintoma": "Velocidade / speed sensor",
        "passos": [
            "Verificar se pode ser C/R pouco pesado ou fio preso no housing.",
            "TESTE: ligar 2 máquinas, atingir velocidade, desligar as duas juntas e observar qual para primeiro.",
            "Verificar BH pesado ou holder travado.",
            "Verificar plugs do sensor.",
        ],
    },

    "b2 - erro 85": {
        "titulo": "B2 - Erro 85",
        "sintoma": "Falta alimentação de fase, correia rompida ou problema elétrico",
        "passos": [
            "Verificar plugs da tomada VTC.",
            "Verificar correia.",
            "Acionar elétrica.",
            "Verificar contatora.",
        ],
    },

    "b2 - erro 84": {
        "titulo": "B2 - Erro 84",
        "sintoma": "Sobrecarga de motor",
        "passos": [
            "Verificar se pode ser contatora ruim.",
            "Verificar se o fuso do VTC está sujo ou pesado.",
            "Se ocorrer em mais de uma manutenção com este alarme, substituir o VTC.",
        ],
    },

    "b2 - erro 88-87": {
        "titulo": "B2 - Erro 88-87",
        "sintoma": "Ao fazer doff, o BH desarma (geralmente por C/R pesado ou com fio)",
        "passos": [
            "Verificar sensor de posição atrás do winder.",
            "Verificar rolamentos traseiros com fios na base.",
            "Verificar holder pesado.",
        ],
    },

    "b2 - erro 90 swin guide": {
        "titulo": "B2 - Erro 90 (Swing Guide)",
        "sintoma": None,
        "passos": [
            "Verificar parte mecânica caída.",
            "Verificar sensor do cilindro.",
            "TESTE: entrar em Manutenção, segurar o botão amarelo até piscar, girar o revolving dran e apertar ARM (T azul).",
            "Após o teste, segurar o amarelo novamente para voltar.",
        ],
    },

    "b2 - erro 81": {
        "titulo": "B2 - Erro 81",
        "sintoma": None,
        "passos": [
            "Acionar elétrica.",
            "Testar giro do revolving dran pelo botão vermelho várias vezes.",
            "Verificar sensores do B/H.",
            "Verificar base do motor frouxa.",
            "Verificar stopper do RD e porca de travamento.",
        ],
    },

    "b2 - motor desarmado": {
        "titulo": "B2 - Motor Desarmado",
        "sintoma": "Alarme aponta B/H, mas problema geralmente é C/R travado",
        "passos": [
            "Remover correias e verificar ruído, vibração e temperatura.",
            "Lembrar que um motor pode desarmar no lugar de outro.",
            "Testar repetidas vezes.",
        ],
    },

    "b2 - b/h nao solta tubete": {
        "titulo": "B2 - B/H Não Solta Tubete",
        "sintoma": None,
        "passos": [
            "Se acontecer nos dois lados: trocar o booster (BH em posição de travamento).",
            "Se acontecer em apenas um lado: testar os 2 BHs.",
            "Verificar nipel do BH quebrado na frente do winder.",
            "Verificar fio na última sleeve.",
            "Verificar nipel amarelo de alta pressão vazando.",
        ],
    },

    "b2 - vtc sensor cima nao acende": {
        "titulo": "B2 - VTC Sensor de Cima Não Acende",
        "sintoma": None,
        "passos": [
            "Acionar elétrica para verificar contatora.",
            "Regulagem da base do sensor: remover a tampa.",
            "Colocar em modo manual (branco + azul).",
            "Afrouxar a base lateral.",
            "Subir o slide-box (botão vermelho).",
            "Reapertar alinhado.",
            "O sensor deve piscar na descida do VTC.",
            "Ajustar folga em 0,50 com calibrador e chave T4.",
            "Tempo de ativação: L5 = 15 min, L6 = 30 s.",
        ],
    },

    "b1 - cinta": {
        "titulo": "B1 - Cinta",
        "sintoma": None,
        "passos": [
            "Verificar vibração do BH, C/A e T/R.",
            "Verificar anel elástico do T/R solto ou sujo.",
            "Se BH estiver vibrando: trocar e verificar o cap holder C/A.",
            "Verificar pushing body cap gasto (bucha de bronze suja).",
            "Verificar holders gastos ou com ferrugem; trocar o conjunto.",
        ],
    },

    "b1 - bobina gorda": {
        "titulo": "B1 - Bobina Gorda",
        "sintoma": None,
        "passos": [
            "Verificar paralelismo.",
            "Verificar se o C/A está acoplando corretamente.",
        ],
    },

    "b1 - pusher": {
        "titulo": "B1 - Pusher",
        "sintoma": None,
        "passos": [
            "Inspecionar se o pusher está funcionando ou se encontra travado por peças embaixo ou pela mangueira pneumática.",
            "Verificar se o mesmo pode estar travado embaixo do B/H.",
            "ATENÇÃO: sempre acionar a operação para a tarefa antes de manusear a linha.",
        ],
    },

    "b2 - pusher": {
        "titulo": "B2 - Pusher",
        "sintoma": "Não para no sensor",
        "passos": [
            "Abrir a tampa pneumática e inspecionar as conexões da solenoide 6 (referente ao pusher), verificando se não está entupida com fio. Trocar caso esteja entupida.",
            "Se a opção anterior estiver OK, fazer a troca da solenoide.",
            "Se nenhuma das alternativas resolver, substituir o pusher.",
            "Para a troca: remover o S/G para melhor alcance, remover o parafuso M8 da parte superior, remover o sensor e os engates pneumáticos.",
            "Instalar o carrinho no novo pusher e instalá-lo no local. Para ajustar o sensor, colocar apenas os parafusos frontais e removê-los se precisar reajustar. Velocidade de referência: 3 segundos de acionamento para o carro chegar até a frente da máquina.",
        ],
    },

    # OBS: o texto original termina truncado em '"B2 - ' — não há conteúdo
    # suficiente para reconstruir essa última entrada. Se você tiver o
    # restante desse trecho, me envie que eu completo o dicionário.
}


def listar_titulos():
    """Retorna a lista de chaves (códigos/problemas) disponíveis na base."""
    return list(MANUTENCAO_DB.keys())


def buscar(chave):
    """
    Busca um item pela chave (case-insensitive).
    Retorna o dicionário do item ou None se não encontrado.
    """
    chave_normalizada = chave.strip().lower()
    return MANUTENCAO_DB.get(chave_normalizada)


def imprimir_passos(chave):
    """Imprime o passo a passo de um item de forma legível no terminal."""
    item = buscar(chave)
    if item is None:
        print(f"Nenhum item encontrado para: '{chave}'")
        return

    print(f"\n=== {item['titulo']} ===")
    if item.get("sintoma"):
        print(f"Sintoma: {item['sintoma']}")
    print("Passos:")
    for i, passo in enumerate(item["passos"], start=1):
        print(f"  {i}. {passo}")


if __name__ == "__main__":
    print("Itens disponíveis na base de manutenção:\n")
    for titulo in listar_titulos():
        print(f" - {titulo}")

    # Exemplo de uso:
    imprimir_passos("b2 - erro 74")

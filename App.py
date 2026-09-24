import streamlit as st

st.set_page_config(page_title="IA Winder B1/B2", page_icon="🏭")

BASE = {
  "b2 - cinta": "1. Verificar vibração BH para ver empenamento (testar em manutenção)\n2. Verificar subida/descida VTC se trepidando/travando. Se travar em processo, acionar elétrica.\n3. Verificar correia T/R, motor, polias e midle shaft\n4. Verificar assentamento do C/A\n5. Verificar pressão C/A avanço/retorno: fazer pressão com a mão. Se leve, verificar manômetro ou cilindro ruim.\n6. Com winder em processo, verificar assentamento C/A. Se retornar ao acoplar no holder, trocar cilindro.\n7. Verificar holders com ferrugem/gastos -> troca conjunto inteiro. Holders removidos devem ser ELIMINADOS, não recondicionar.",
  "b2 - f/r b2": "F/R em processo: Verificar C/R pesado, Holder B/H pesado, correias C/R e T/R, sensor velocidade (acionar elétrica e verificar plugs embaixo motor C/R), guide plates frouxas, verificação externa parte superior para peças frouxas.",
  "b2 - erro 74": "1. Verificar se C/A voltou posição sensor\n2. Verificar bucha plástica derretida\n3. Verificar pressão retorno C/A\n4. Se cilindro avança/retorna normal, verificar sensor aceso\n5. Teste tampa: acionar C/A e colocar tampa atrás cilindro. Se sensor apagar, acionar elétrica para troca.\n6. Sempre verificar holder gasto.",
  "b2 - erro 88": "Velocidade / speed sensor. Pode ser C/R pouco pesado ou fio nos housing. TESTE: ligar 2 máquinas, atingir velocidade, desligar juntas e ver qual para primeiro. Verificar BH pesado ou holder travado e plugs sensor.",
  "b2 - erro 85": "Falta alimentação fase, correia rompida ou problema elétrico. Verificar plugs tomada VTC, correia, acionar elétrica e verificar contatora.",
  "b2 - erro 84": "Sobrecarga motor. Pode ser contatora ruim ou fuso VTC sujo/pesado. Se >1 manutenção neste alarme, substituir VTC.",
  "b2 - erro 88-87": "Geralmente ao fazer doff BH desarma devido C/R pesado ou com fio. Verificar sensor posição atrás winder, rolamentos traseiros com fios na base, holder pesado.",
  "b2 - erro 90 swin guide": "Verificar parte mecânica caída e sensor cilindro. TESTE: Manutenção + segurar amarelo até piscar e girar revolving dran, apertar ARM (T azul). Após, segurar amarelo para voltar.",
  "b2 - erro 81": "Acionar elétrica. Testar giro revolving dran botão vermelho várias vezes. Verificar sensores B/H, base motor frouxa, stopper RD e porca travamento.",
  "b2 - motor desarmado": "Remover correias e verificar ruído, vibração e temperatura. Um motor pode desarmar no lugar de outro. Testar repetidas vezes. Geralmente alarme B/H mas problema é C/R travado.",
  "b2 - b/h nao solta tubete": "Se ambos os lados: trocar booster (BH em posição travamento). Se um lado: testar 2 BHs. Verificar nipel BH quebrado frente winder, fio última sleeve, nipel amarelo alta pressão vazando.",
  "b2 - vtc sensor cima nao acende": "Acionar elétrica verificar contatora. Regulagem base sensor: remover tampa, manual (branco+azul), afrouxar base lateral, subir slid-box (botão vermelho), reapertar alinhado. Sensor deve piscar na descida VTC. Ajuste folga 0,50 com calibrador e chave T4. L5: 15min p/ ativar, L6: 30s.",
  "b1 - cinta": "Verificar vibração BH, C/A e T/R. Verificar anel elástico T/R solto/sujo. BH vibrando: trocar e verificar cap holder C/A. Verificar pushing body cap gasto (bucha bronze suja) e holders gastos/ferrugem. Trocar conjunto.",
  "b1 - bobina gorda": "Verificar paralelismo e verificar C/A se está acoplando certo."
}

st.title("🏭 IA Winder - B1 / B2")
st.caption("Consulta rápida para manutenção - Equipe Winder")

busca = st.text_input("🔍 Digite: Ex: 'b2 erro 74' ou 'cinta b2'").lower()

if busca:
    resultados = {k:v for k,v in BASE.items() if all(p in k for p in busca.split())}
    if not resultados:
        resultados = {k:v for k,v in BASE.items() if any(p in k for p in busca.split())}
    
    if resultados:
        for chave, solucao in resultados.items():
            st.success(f"**{chave.upper()}**")
            st.write(solucao)
            st.divider()
    else:
        st.error("Não encontrei. Tente: 'erro 74', 'cinta', 'vtc', 'bh'")

st.sidebar.header("➕ Ensinar novo defeito")
with st.sidebar.form("novo"):
    maq = st.text_input("Máquina (B1/B2)")
    cod = st.text_input("Defeito / Erro")
    sol = st.text_area("Solução completa")
    if st.form_submit_button("Salvar"):
        st.sidebar.success(f"Para salvar definitivo, adicione no código: '{maq} - {cod}': '{sol}'")
        st.sidebar.code(f'"{maq.lower()} - {cod.lower()}": "{sol}"')

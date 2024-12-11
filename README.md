# fluxo-caixa-api
Um comerciante precisa controlar o seu fluxo de caixa diário com os lançamentos (débitos e créditos), também precisa de um relatório que disponibilize o saldo diário consolidado.


Vamos estruturar a solução desse desafio com os passos necessários para atender aos requisitos descritos. Para facilitar, utilizarei Python com o framework FastAPI para desenvolver os serviços, e utilizarei SQLite como banco de dados para simplificar a instalação e execução local. Abaixo está a descrição da solução:

<h4> Mapeamento de domínios funcionais e capacidades de negócio </h4>

<h5>O sistema terá dois domínios principais:</h5>

<i>Lançamentos:</i>
Inserir débitos e créditos no fluxo de caixa diário.
Recuperar os lançamentos do dia.
<i>Consolidado Diário:</i>
Calcular o saldo diário consolidado com base nos lançamentos do dia.
Retornar os dados consolidados para um relatório.

<b>Levantamento de requisitos funcionais e não funcionais</b>

<b>Funcionais</b>
Criar, listar, editar e excluir lançamentos (créditos/débitos).
Retornar o saldo consolidado diário.
Validar entradas de dados, como valores positivos e tipos de lançamentos.

<b>Não Funcionais</b>
Arquitetura simples e escalável.
Uso de testes unitários para garantir a qualidade do código.
Fornecer instruções claras para execução local.
Uso de dependências leves para facilitar a instalação.

<b>Desenho da solução</b>
Arquitetura Alvo
Frontend: Não necessário para o desafio (API-based).
Backend:
Framework: FastAPI (rápido, leve e amigável para APIs REST).
Banco de Dados: SQLite (para armazenamento local e simplificado).
Testes: Pytest para testes unitários.

<b>Estrutura do projeto</b>
<code>

<ul><li>- app/
<li>- main.py            # Entrada principal da aplicação
<li>- models.py          # Modelos de banco de dados
<li>- schemas.py         # Validações e esquemas de entrada/saída
<li>- database.py        # Configuração do banco de dados
<li>- routers/
<li>- transactions.py  # Rotas relacionadas a lançamentos
<li>- summary.py       # Rotas relacionadas ao saldo consolidado
</ul>
<ul><li>- tests/
<li>- test_transactions.py
<li>- test_summary.py
<li>- README.md
<li>- requirements.txt
<li>- Dockerfile           # Para containerização (opcional)
</ul>
</code>



<h5><b>Justificativa de escolhas</b></h5>
 <ul><b>FastAPI:</b> Um dos frameworks mais eficientes e amigáveis para desenvolvimento de APIs REST. Possui validação automática com Pydantic.
<b>SQLite:</b> Banco de dados leve, ideal para ambientes de desenvolvimento e testes.
 
<b>Pytest:</b> Ferramenta robusta para automação de testes.
<b>Docker:</b> Opcional para execução em ambientes controlados.
 </ul>


<h5><b># Fluxo de Caixa API</b></h5>
## Requisitos
- Python 3.9+
- FastAPI
- SQLite

## Instalação
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

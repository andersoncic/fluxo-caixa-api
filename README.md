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

<h5><b>## Instalação</b></h5>
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

<h5><b>Endpoints</b></h5>
POST /transactions/: Criar lançamentos.
GET /summary/: Obter saldo consolidado.

#############################################

<h3><b>Infraestrutura</b></h3>
Hospedagem
AWS
EC2 Instance (t2.micro): R$ 45/mês (se fora do Free Tier).
RDS (PostgreSQL): R$ 75/mês.
Storage: R$ 25/mês.
Total AWS: R$ 145/mês.

<b>Ferramentas Gratuitas:</b>

Prometheus + Grafana: Gratuito (self-hosted).
AWS CloudWatch Free Tier: Gratuito.

<b>Ferramentas Pagas:</b>
Datadog: R$ 75/mês por host.
New Relic: Gratuito para até 100 GB/mês.
Total Monitoramento: R$ 0 - R$ 75/mês.

<h5><b>Critérios de Segurança</h5></b>
Infraestrutura
Certificado SSL/TLS:
Gratuito com Let's Encrypt.
R$ 50/ano (~R$ 4/mês) para opções comerciais.
Web Application Firewall (WAF):

AWS WAF: R$ 25/mês.
Cloudflare: Plano gratuito disponível.
Total Segurança: R$ 4 - R$ 25/mês.

<h5><b>Custo Total Estimado (Médio)</h5></b>
Infraestrutura: R$ 35 - R$ 145/mês.
Monitoramento: R$ 0 - R$ 75/mês.
Segurança: R$ 4 - R$ 25/mês.
Custo Geral
Total Geral em Reais: R$ 39 - R$ 245/mês.





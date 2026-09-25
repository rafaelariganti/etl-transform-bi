# Exercício 1 — Teórico-Conceitual: ELT vs. ETL no Contexto de Big Data

**Dupla:** Maria Julia Loureiro e Rafaela Riganti

Com o surgimento de Data Lakes e Data Warehouses modernos em nuvem (como Snowflake, BigQuery e Databricks), a arquitetura ELT (Extract, Load, Transform) ganhou amplo destaque em relação ao tradicional ETL.

## 1. Qual é a diferença fundamental no local e momento de processamento da fase de transformação entre ETL e ELT?

No ETL, a transformação acontece antes da carga, em um servidor intermediário (staging), e só o dado já limpo entra no repositório final. No ELT, o dado bruto é carregado primeiro no Data Lake/Warehouse (exemplo: Snowflake, BigQuery) e a transformação acontece depois, usando o poder de processamento do próprio repositório em nuvem.

## 2. Em qual dos dois cenários a governança de dados e a anonimização prévia (LGPD) tornam-se mais críticas antes do pouso inicial dos dados no repositório? Justifique.

No ETL, porque a anonimização já precisa estar pronta antes de os dados chegarem ao destino — nada sensível é persistido em bruto. No ELT o dado bruto (com CPF, nome etc.) fica armazenado no Data Lake mesmo que temporariamente, o que exige controles de acesso extras para compensar essa exposição.

## 3. Cite dois casos em que o pipeline clássico ETL ainda é preferível a um pipeline ELT.

- Quando há restrições regulatórias rígidas (LGPD, setor financeiro/saúde) que proíbem armazenar dados sensíveis em texto puro, mesmo que por pouco tempo.
- Quando o volume de dados é pequeno/médio e o destino não tem poder de processamento (exemplo: bancos on-premise), tornando mais barato transformar antes de carregar.
# Engenharia de Pipelines e a Fase de Transformação (ETL)

**Matéria:** Business Intelligence e Big Data
**Professor:** Bruno Aguilar da Cunha
**Dupla:** Maria Julia Loureiro e Rafaela Riganti

## Sobre a atividade

Trabalho sobre a fase de **Transform** do pipeline ETL (Extract, Transform, Load), abordando limpeza, padronização, anonimização (LGPD) e enriquecimento de dados. A atividade tem duas partes:

- **Exercício 1** — teórico-conceitual sobre a diferença entre ETL e ELT.
- **Exercício 2** — prático em Python, tratando dados de sensores IoT com pandas.

## Estrutura do repositório

```
etl-transform-bi/
├── exercicio1.md      # respostas do exercício teórico
├── transform_iot_data.py         # solução do exercício prático
└── README.md
```

## Exercício 1 — ETL vs. ELT

Resposta teórica sobre onde e quando a transformação acontece em cada arquitetura, quando a governança/LGPD é mais crítica, e casos em que o ETL clássico ainda é preferível ao ELT. Ver `exercicio1.md`.

## Exercício 2 — Tratamento de Dados de Sensor IoT

A função `transform_iot_data(df)` recebe leituras brutas de sensores e aplica:

1. Remoção de duplicados exatos por `(sensor_id, timestamp)`
2. Padronização do timestamp para datetime
3. Limpeza da temperatura (remove a unidade " C" e converte para float)
4. Preenchimento de nulos de temperatura pela mediana do próprio sensor
5. Conversão da pressão para float
6. Filtro de outliers (temperatura entre -20°C e 100°C; pressão > 0.5 bar)

### Como rodar

1. Instale as dependências:
   ```bash
   pip install pandas numpy
   ```
2. Rode o script na pasta onde ele está salvo:
   ```bash
   python transform_iot_data.py
   ```
3. A saída mostra o DataFrame já limpo, com as leituras inválidas (duplicadas, com outlier ou sem temperatura válida) filtradas.
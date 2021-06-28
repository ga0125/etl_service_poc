DROP TABLE IF EXISTS purchase_data;

CREATE TABLE purchase_data (
  id                   SERIAL PRIMARY KEY,
  cpf                  VARCHAR (11),
  private              INTEGER,
  incomplete           INTEGER,
  last_purchase_date   DATE,
  average_ticket       VARCHAR (8),
  last_purchase_ticket VARCHAR (8),
  most_frequent_store  VARCHAR (14),
  last_purchase_store  VARCHAR (14)
);
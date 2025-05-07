# Getting Started

Let design a retail data pipeline that exist in the common case worldwide.

- I have 3 data sources that store source data
  - Customer master
  - Product master
  - Order transaction
- I want to ETL these sources to the bronze zone.
  - Customer should load with Full-Dump extract
  - Product master should load with Delta extract
  - Order transaction should load with Transaction extract
- I will clean and create data model for these sources
  - Customer dimension
  - Product dimension
  - Order fact
  - Store dimension
- Finally, I will create serving table to be monthly reports
  - Store selling report
  - Product revenue report

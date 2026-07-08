# Turbo DataForge

Turbo DataForge is a collaborative Python-based ETL (Extract, Transform, Load) pipeline designed to automate the extraction, transformation, and loading of business datasets from Excel workbooks into PostgreSQL.

The pipeline processes multiple Excel workbooks, converts them into standardized CSV files, performs data cleaning and transformation, and loads the processed datasets into PostgreSQL for centralized storage and analysis.

The project follows a modular ETL architecture that separates extraction, transformation, storage, and database loading, making it scalable, maintainable, and suitable for real-world data engineering workflows.

---

# Architecture

Excel Workbooks
        │
        ▼
Workbook Discovery
        │
        ▼
Sheet Extraction
        │
        ▼
Data Transformation
        │
        ▼
CSV Generation
        │
        ▼
CSV Cleaning
        │
        ▼
PostgreSQL Loading
        │
        ▼
Analytics & Reporting

---

# Turbo DataForge

Turbo DataForge is a collaborative Python-based ETL (Extract, Transform, Load) pipeline designed to automate the extraction, transformation, and loading of business datasets from Excel workbooks into PostgreSQL.

The pipeline processes multiple Excel workbooks, converts them into standardized CSV files, performs data cleaning and transformation, and loads the processed datasets into PostgreSQL for centralized storage and analysis.

The project follows a modular ETL architecture that separates extraction, transformation, storage, and database loading, making it scalable, maintainable, and suitable for real-world data engineering workflows.

---

# Project Overview

Turbo DataForge processes multiple business datasets stored in Excel workbooks and automatically loads them into PostgreSQL.

The pipeline currently processes four datasets:

- DATA
- GEARBOX
- Innovation Pipeline
- Protein Actual

The ETL workflow performs the following operations:

- Automatically discovers Excel workbooks
- Extracts required worksheets
- Converts Excel worksheets into CSV files
- Cleans and standardizes business data
- Generates meaningful CSV filenames
- Consolidates DATA and GEARBOX datasets
- Loads Innovation Pipeline and Protein Actual datasets independently
- Stores processed data inside PostgreSQL

---

# ETL Workflow

The ETL pipeline consists of four stages:

1. Extract
2. Transform
3. Save
4. Load

---

# 1. Extract

The extraction stage automatically scans the raw data directory and processes every Excel workbook.

The pipeline extracts only the required worksheets.

For Turbo workbooks:

- DATA
- MBR
- GEARBOX

For additional business datasets:

- Innovation Pipeline
- Protein Actual

The extraction module is completely configuration-driven and supports processing multiple workbooks automatically.

---

# 2. Transform

The transformation stage prepares the extracted data for analysis and database loading.

The transformation process includes:

- Cleaning unnecessary rows
- Cleaning unnecessary columns
- Standardizing column names
- Preparing analytical datasets
- Unpivoting DATA worksheets
- Preserving GEARBOX datasets
- Cleaning Product Code values
- Removing unnecessary quotes
- Removing embedded line breaks
- Standardizing CSV formatting
- Preparing datasets for PostgreSQL loading

The cleaned datasets are stored as CSV files before being loaded into the database.

---

# 3. Save

Each processed workbook generates its own cleaned folder inside:

```text
data/
└── cleaned_data/
```

Example structure:

```text
data/
└── cleaned_data/
    ├── turbo_atyab_2025/
    │   ├── turbo_atyab_2025_Data.csv
    │   └── turbo_atyab_2025_GEARBOX.csv
    │
    ├── turbo_atyab_fy_2024/
    │   ├── turbo_atyab_fy_2024_Data.csv
    │   └── turbo_atyab_fy_2024_GEARBOX.csv
    │
    ├── innovation_pipeline/
    │   └── innovation_pipeline.csv
    │
    ├── protein_actual/
    │   └── protein_actual.csv
    │
    └── ...
```

### Naming Convention

Turbo workbook outputs follow the naming convention:

```text
<workbook_name>_Data.csv
<workbook_name>_GEARBOX.csv
```

Examples:

```text
turbo_atyab_2025_Data.csv
turbo_atyab_2025_GEARBOX.csv

turbo_atyab_fy_2024_Data.csv
turbo_atyab_fy_2024_GEARBOX.csv
```

Additional datasets retain their original business names:

```text
innovation_pipeline.csv
protein_actual.csv
```

This naming convention improves traceability by allowing every generated file to be immediately associated with its original workbook or business dataset.

---

# Project Structure

```text
turbo-dataforge/
│
├── config/
│   ├── database.py
│   └── settings.json
│
├── data/
│   ├── raw_data/
│   └── cleaned_data/
│
├── scripts/
│   ├── extract.py
│   ├── workbook_loader.py
│   ├── transform.py
│   ├── save.py
│   ├── load.py
│   ├── clean_csvs.py
│   ├── logger.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Technologies Used

## Programming Language

- Python

## Data Processing

- Pandas

## Database

- PostgreSQL
- SQLAlchemy
- Psycopg2
- pgAdmin 4

## Configuration

- JSON

## Version Control

- Git
- GitHub

---

# Features

- Modular ETL architecture
- Automatic workbook discovery
- Configuration-driven workflow
- Excel worksheet extraction
- Excel-to-CSV conversion
- Business data transformation
- Data unpivoting
- Product Code standardization
- Automatic CSV cleaning
- Standardized file naming convention
- Consolidated DATA table generation
- Consolidated GEARBOX table generation
- Dedicated Innovation Pipeline table generation
- Dedicated Protein Actual table generation
- Automatic PostgreSQL loading
- Source file tracking for consolidated datasets
- Execution logging
- Scalable folder structure
- GitHub collaboration support

---

# PostgreSQL Output

After execution, PostgreSQL contains four production-ready tables.

## 1. data

Contains the consolidated records from every processed Turbo DATA workbook.

Each row includes a `source_file` column that identifies the workbook from which the record originated.

Example:

```text
data
├── turbo_atyab_2025
├── turbo_atyab_fy_2023
├── turbo_atyab_fy_2024
├── turbo_atyab_bud_2026_finalversion
├── turbo_data_act_ytd_mar_fc_fy
└── ...
```

---

## 2. gearbox

Contains the consolidated records from every processed Turbo GEARBOX workbook.

Each row includes a `source_file` column for complete traceability.

Example:

```text
gearbox
├── turbo_atyab_2025
├── turbo_atyab_fy_2023
├── turbo_atyab_fy_2024
├── turbo_atyab_bud_2026_finalversion
├── turbo_data_act_ytd_mar_fc_fy
└── ...
```

---

## 3. innovation_pipeline

Contains the complete Innovation Pipeline dataset loaded directly into PostgreSQL.

```text
innovation_pipeline
```

---

## 4. protein_actual

Contains the complete Protein Actual dataset loaded directly into PostgreSQL.

```text
protein_actual
```

---

The ETL pipeline creates only these four database tables, ensuring a clean and scalable database design while preserving complete traceability for the consolidated Turbo datasets.

---

# How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/adityamsr2606/turbo-dataforge.git
cd turbo-dataforge
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure PostgreSQL

Update your PostgreSQL connection details inside:

```text
config/database.py
```

Configure the following fields:

- Database Host
- Database Port
- Database Name
- Username
- Password

---

## 5. Add Source Excel Files

Place all raw Excel workbooks inside:

```text
data/raw_data/
```

The pipeline automatically discovers every workbook available in this directory.

---

## 6. Execute the Pipeline

Run the ETL pipeline using:

```bash
python main.py
```

The pipeline automatically performs the following tasks:

1. Discovers Excel workbooks
2. Extracts required worksheets
3. Cleans and transforms the data
4. Converts datasets into CSV files
5. Cleans generated CSV files
6. Loads processed datasets into PostgreSQL

---

# Output

After successful execution:

- Cleaned CSV files are generated inside `data/cleaned_data`
- Turbo workbook outputs follow the naming convention:
  - `<workbook_name>_Data.csv`
  - `<workbook_name>_GEARBOX.csv`
- Additional datasets are exported as:
  - `innovation_pipeline.csv`
  - `protein_actual.csv`
- DATA worksheets are consolidated into the `data` table
- GEARBOX worksheets are consolidated into the `gearbox` table
- Innovation Pipeline is loaded into the `innovation_pipeline` table
- Protein Actual is loaded into the `protein_actual` table
- Execution progress is displayed through logging
- Source workbook information is preserved using the `source_file` column for consolidated datasets

---

# Team Contribution

This project was completed collaboratively, with responsibilities divided across different stages of the ETL pipeline.

## Aditya

- Designed the overall ETL architecture
- Planned the project folder structure
- Developed the application entry point (`main.py`)
- Implemented the PostgreSQL loading module (`load.py`)
- Configured PostgreSQL database connectivity
- Integrated the complete ETL workflow
- Implemented consolidated loading for DATA and GEARBOX datasets
- Implemented dedicated loading for Innovation Pipeline and Protein Actual datasets
- Added source file tracking using the `source_file` column
- Updated the cleaned CSV naming convention for improved traceability
- Validated PostgreSQL tables using SQL queries in pgAdmin 4
- Managed Git version control, repository setup, collaborator access, branching, commits, and GitHub deployment
- Performed end-to-end testing and pipeline integration

## Bhumika

- Implemented workbook discovery
- Developed worksheet extraction logic
- Contributed to data cleaning and preprocessing
- Implemented transformation logic
- Assisted in generating standardized CSV outputs
- Contributed to the modular ETL implementation
- Assisted in validating processed datasets before database loading

---

# Future Improvements

The current implementation provides a complete ETL workflow for processing multiple business datasets. Future enhancements can further improve scalability, maintainability, and production readiness.

## Planned Enhancements

### Database

- Incremental data loading
- Automatic schema evolution
- Database indexing for faster queries
- Data versioning
- Partitioned tables for large datasets

### ETL Pipeline

- Environment variable support for database credentials
- Automated data validation
- Data quality reporting
- Exception handling and retry mechanisms
- Parallel processing for multiple workbooks
- Configurable transformation rules
- Duplicate record detection
- Automated backup of processed datasets

### Automation

- Pipeline scheduling using Windows Task Scheduler or Cron
- Apache Airflow integration
- Automated notifications on pipeline completion
- Automated log archival

### Deployment

- Docker containerization
- Docker Compose support
- Cloud PostgreSQL integration
- AWS deployment
- Azure deployment
- CI/CD pipeline using GitHub Actions

### Monitoring

- Pipeline execution metrics
- Performance monitoring
- Database load statistics
- ETL execution dashboard

### Reporting

- Power BI integration
- Tableau integration
- Automated business reports
- Interactive dashboards connected directly to PostgreSQL

---

# Repository

```
Turbo DataForge
│
├── Modular Python ETL Pipeline
├── PostgreSQL Integration
├── Automated Excel Processing
├── CSV Standardization
├── Multi-Dataset Processing
├── Data Cleaning
├── Source File Tracking
└── GitHub Collaboration
```

---

# Contributors

| Name | Role |
|------|------|
| Aditya | Project Architecture, PostgreSQL Integration, ETL Pipeline Integration, Database Loading, GitHub Management |
| Bhumika | Data Extraction, Transformation, CSV Generation, Data Processing |

---

# Acknowledgements

This project was developed as a collaborative data engineering project to demonstrate industry-standard ETL practices using Python and PostgreSQL.

The implementation focuses on modular software design, automated data processing, standardized file generation, and scalable database loading suitable for analytical workflows.

---

# License

This project is intended for educational, academic, and portfolio purposes.

The datasets used in this repository remain the property of their respective owners and are used solely for demonstrating ETL concepts and data engineering workflows.

Unauthorized commercial use of proprietary datasets is not permitted.

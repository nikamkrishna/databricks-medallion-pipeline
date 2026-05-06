# End-to-End Incremental Data Pipeline using Databricks

## Overview

This project implements an end-to-end batch data pipeline using Databricks and Delta Lake following the Medallion Architecture pattern.

The pipeline processes NYC Yellow Taxi trip data through Bronze, Silver, and Gold layers while implementing:

- Incremental processing
- Delta Lake merge operations
- Workflow orchestration
- Partition optimization
- Business aggregations

---

# Architecture

Raw Taxi Data
       ↓
Bronze Layer
       ↓
Silver Layer
       ↓
Incremental Merge
       ↓
Gold Layer

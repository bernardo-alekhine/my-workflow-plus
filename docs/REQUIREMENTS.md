# My WorkFlow+ (ERP)

## Author: Bernardo Alekhine

## Status: In Development

## Tech Stack

- Languages - Python, JavaScript, TypeScript, HTML, CSS

- Frameworks & Libraries - Django, Tailwindcss

- Databases - PostgreSQL (via Neon)

- Key tools - Git, Docker

- Hosting & Infrastructure - Render (Web Service & Static Assets)

## 1. Overview

Placeholder.

## 2. Actors  

| Actor         | Description                                                                              | Permissions                         |
| ------------- | ---------------------------------------------------------------------------------------- | ----------------------------------- |
| Administrator | Manage configurations of user, system, database and troubleshooting errors.              | Full access to system settings only |
| Stakeholder   | Access to all dashboards and audit logs of the system. But no controls to updating data. | Full read access to all audit logs  |
| Manager       | Participation in all apps, bridge between employee and stakeholders.                     | Full CRUD                           |
| Employee      | App/domain specific participation.                                                       | Limited CRUD                        |

## 3.0 Requirements

### 3.1 Core

#### 3.1.1 Functional Requirements

| ID         | Requirement                                                                                             | Priority | Status |
| ---------- | ------------------------------------------------------------------------------------------------------- | -------- | ------ |
| FR-CORE-01 | System must provide a unified navigation sidebar and top bar layout.                                    | High     | Todo   |
| FR-CORE-02 | Provide base abstract base models for timestamps fields.                                                | High     | Todo   |
| FR-CORE-03 | Provide global UI assets for other apps.                                                                | High     | Todo   |
| FR-CORE-04 | Provide utility functions for formatting currency, dates and validation of documents.                   | High     | Todo   |
| FR-CORE-05 | System must provide a global search bar to find Records (Products, Customers, Employees) from any page. | High     | Todo   |

#### 3.1.1 Core Non Functional Requirements

- Must provide all base functions models and any required utility to the other apps.
- Must be fast efficient and reliable.
- Must be thoroughly tested.

### 3.2 Accounts

#### 3.2.1 Accounts Functional Requirements

| ID             | Requirement                                                                                     | Priority | Status |
| -------------- | ----------------------------------------------------------------------------------------------- | -------- | ------ |
| FR-ACCOUNTS-01 | System must allow administrators to create new users.                                           | High     | Todo   |
| FR-ACCOUNTS-02 | Users should have fields for name, documents, picture and other identification fields.          | High     | Todo   |
| FR-ACCOUNTS-03 | Users have a special field for type. This field determines the role of each user in the system. | High     | Todo   |

#### 3.2.2 Accounts Non Functional Requirements

- Must be safe and reliable.
- Robust authentication.
- Provide any required methods to uses on external apps.

### 3.3 Inventory

#### 3.3.1 Inventory Functional Requirements

| ID              | Requirement                                                                          | Priority | Status |
| --------------- | ------------------------------------------------------------------------------------ | -------- | ------ |
| FR-INVENTORY-01 | System must allow for registering products and warehouses.                           | High     | Todo   |
| FR-INVENTORY-02 | System must provide CRUD interface for external apps.                                | High     | Todo   |
| FR-INVENTORY-03 | System must provide interface displaying all available products and their locations. | High     | Todo   |
| FR-INVENTORY-04 | System must log all CRUD operations.                                                 | High     | Todo   |

#### 3.3.2 Inventory Non Functional Requirements

- System should have a fancy UI that displays information about all registered products and their specific warehouses.
- System should allow for registering products or warehouses. Including prices possibly or addresses.

### 3.4 Sales

#### 3.4.1 Sales Functional Requirements

| ID          | Requirement                                                                                   | Priority | Status |
| ----------- | --------------------------------------------------------------------------------------------- | -------- | ------ |
| SALES-FR-01 | System must provide an interface for selling products.                                        | High     | Todo   |
| SALES-FR-02 | System must allow for employees to initiate orders for selling products.                      | High     | Todo   |
| SALES-FR-03 | The orders have different states throughout its lifecycle. As in creating, open, closed, etc. | High     | Todo   |

#### 3.4.2 Sales Non Functional Requirements

- Must be integrated with audit logs and inventory, as changes in stock and operations are recorded and reflected on databases.
- Must have fancy intuitive UI for managing orders or selling products directly. Not limited only to orders.

### 3.5 Purchases

#### 3.5.1 Purchases Functional Requirements

| ID              | Requirement                                                                                       | Priority | Status |
| --------------- | ------------------------------------------------------------------------------------------------- | -------- | ------ |
| PURCHASES-FR-01 | System must provide an interface for managing purchases and purchases orders.                     | High     | Todo   |
| PURCHASES-FR-02 | Lower privilege users can perform requests through orders or directly to higher privileges users. | High     | Todo   |
| PURCHASES FR-03 | System allow to perform purchases of products or services.                                        | High     | Todo   |

#### 3.5.2 Purchases non Functional Requirements

- Integration with services and inventory. Including audit_log which is also related to human resources.
- Intuitive UI for starting order requests changing states and direct purchases.

### 3.6 Todo Services

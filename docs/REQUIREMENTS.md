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

#### 3.1.1Functional Requirements

| ID         | Requirement                                                                                             | Priority | Status |
| ---------- | ------------------------------------------------------------------------------------------------------- | -------- | ------ |
| FR-CORE-01 | System must provide a unified navigation sidebar and top bar layout.                                    | High     | Todo   |
| FR-CORE-02 | Provide base abstract base models for timestamps fields.                                                | High     | Todo   |
| FR-CORE-03 | Provide global UI assets for other apps.                                                                | High     | Todo   |
| FR-CORE-04 | Provide utility functions for formatting currency, dates and validation of documents.                   | High     | Todo   |
| FR-CORE-05 | System must provide a global search bar to find Records (Products, Customers, Employees) from any page. | High     | Todo   |

#### 3.1.2 Core Non Functional Requirements

- Must provide all base functions models and any required utility to the other apps.
- Must be fast efficient and reliable.
- Must be thoroughly tested.

### 3.2 Users

#### 3.2.1 Users Functional Requirements

| ID             | Requirement                                                                                     | Priority | Status |
| -------------- | ----------------------------------------------------------------------------------------------- | -------- | ------ |
| FR-USERS-01 | System must allow administrators to create new users.                                           | High     | Todo   |
| FR-USERS-02 | Users should have fields for name, documents, picture and other identification fields.          | High     | Todo   |
| FR-USERS-03 | Users have a special field for type. This field determines the role of each user in the system. | High     | Todo   |

#### 3.2.2 Users Non Functional Requirements

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

#### 3.5.2 Purchases Non Functional Requirements

- Integration with services and inventory. Including audit_log which is also related to human resources.
- Intuitive UI for starting order requests changing states and direct purchases.

### 3.6 Services

#### 3.6.1 Services Functional Requirements

| ID             | Requirement                                                                                                 | Priority | Status |
| -------------- | ----------------------------------------------------------------------------------------------------------- | -------- | ------ |
| SERVICES-FR-01 | System must allow CRUD of services.                                                                         | High     | Todo   |
| SERVICES-FR-02 | Services have fields of base price, name and date created.                                                  | High     | Todo   |
| SERVICES-FR-03 | System provides interface for setting up service orders. As in created, working, finished, etc.             | High     | Todo   |
| SERVICES-FR-04 | Must have interface to communicate with purchases. As in starting purchase orders and request confirmation. | High     | Todo   |

#### 3.6.2 Services Non Functional Requirements

- Fast and efficient intuitive UI.
- Integrates with purchases and sales interface so services can be purchased or sold elsewhere too.

### 3.7 Financial

#### 3.7.1 Financial Functional Requirements

| ID              | Requirement                                                                                                                  | Priority | Status |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------- | -------- | ------ |
| FINANCIAL-FR-01 | System must provide an interface that displays thoroughly all financial movements of the system. Obtained through audit_log. | High     | Todo   |
| FINANCIAL-FR-02 | Include relevant dashboards, insights and dynamic data analysis driven charts or sortings by date.                           | High     | Todo   |
| FINANCIAL-FR-03 | Integrate thoroughly with audit_log for acquiring data.                                                                      | High     | Todo   |

#### 3.7.2 Financial non Functional Requirements

- Fancy dynamic UI reliable and can provide dynamic charts given date parameters or related requests.

### 3.8 Human Resources

#### 3.8.1 Human Resources Functional Requirements

| ID       | Requirement                                                                                                      | Priority | Status |
| -------- | ---------------------------------------------------------------------------------------------------------------- | -------- | ------ |
| HR-FR-01 | System must provide interface for managing registered users (employees) and their types.                         | High     | Todo   |
| HR-FR-02 | System must provide insights on registered user profits and participation in operations.                         | High     | Todo   |
| HR-FR-03 | System must provide interface for registering payroll for employees and setting salaries or handling comissions. | High     | Todo   |

#### 3.8.2 Human Resources Non Functional Requirements

- Efficient fancy UI and integration with audit_log.
- Safe and protected sensitive data.
- Access control specific to human resources employees.

### 3.9 Audit Log

#### 3.9.1 Audit Log Functional Requirements

| ID              | Requirement                                                                                            | Priority | Status |
| --------------- | ------------------------------------------------------------------------------------------------------ | -------- | ------ |
| AUDIT-LOG-FR-01 | System must provide models (tables) templates or base functionality to other apps.                     | High     | Todo   |
| AUDIT-LOG-FR-02 | System must provide interface for external apps to register logs of sales, purchases, operations, etc. | High     | Todo   |
| AUDIT-LOG-FR-03 | System must contain all audit log tables.                                                              | High     | Todo   |
| AUDIT-LOG-FR-04 | System must perform data validation and sanitiztion.                                                   | High     | Todo   |

#### 3.9.2 Audit Log Non Functional Requirements

- Robust and must process and validate accordingly all requests sent to write logs of operations.
- Reliable work as an API for log registering.

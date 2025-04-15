# Diplom_2 project

## Table of contents

* [General info](#general-info)
* ['api' directory](#api-directory)
    * [1. order_api](#1-order_api)
    * [2. user_api](#2-user_api)
* [Test files](#test-files)
    * [1. test_order](#1-test_order-files)
    * [2. test_user](#2-test_user-files)
* [Additional files](#additional-files)
    * [1. helper](#1-helper)
    * [2. data](#2-data)
    * [3. urls](#3-urls)
    * [4. requirements](#4-requirements)
    * [5. allure_results directory](#5-allure_results-directory)

## General info

This project is created to test the API for the service ["Stellar Burgers"](https://stellarburgers.nomoreparties.site/).

API documentation: ["Документация API"](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89)

## 'api' directory

You can find api methods for related endpoints ['api'](../blob/main/api) directory

### 1. order_api

Includes api methods for endpoints related to the 'Order' object.

### 2. user_api

Includes api methods for endpoints related to the 'User' object.

## Test files

You can find all files with the tests for specific page in ['tests'](../blob/main/tests) directory.

### 1. 'test_order' files

Each file includes the set of tests for each 'Order' endpoint: creation, get for user.

### 2. 'test_user' files

Each file includes the set of tests for each 'User' endpoint: registration, login, change user data.

## Additional files

There are several auxiliary files in the project

### 1. helper

Created to store additional methods.

### 2. data

Created to store test data.

### 3. urls

Created to store urls.

### 4. requirements

Contains the list of packages or libraries needed to work on a project.

### 5. allure_results directory

Include the Allure reports with the test results.

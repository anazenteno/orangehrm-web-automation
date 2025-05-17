# OrangeHRM Automation Project

This repository contains automated test cases for the [OrangeHRM demo site](https://opensource-demo.orangehrmlive.com/) using:

- ✅ Selenium WebDriver
- ✅ Pytest
- ✅ Page Object Model (POM)
- ✅ Parametrized tests
- ✅ Pytest-html reports

## Description

The goal of this project is to validate form fields, employee creation, login flow, and more, as part of a QA Automation portfolio.

Tests are grouped into:
- `test_login.py`: Login functionality
- `test_personal_form.py`: Employee creation and field validation

## Run tests

```bash
pytest --html=report.html

# Bloom Credit Sample Applications: Official Documentation

## Overview

[Bloom Credit](https://bloomcredit.io/) offers a SaaS platform that enables seamless interfacing with the predominant US credit bureaus. The platform allows both the retrieval of consumer credit data (known as an inquiry) and the submission of consumer payment histories to these bureaus. Interaction with the Bloom platform is facilitated through a mix of RESTful APIs and GraphQL.

To aid developers in their integration journey, this repository offers a range of sample applications, all written in the Python language for its wide acceptance and ease of use. Detailed documentation on Bloom Credit's APIs can be accessed through the developer portal: [developers.bloomcredit.io](https://developers.bloomcredit.io).

## Sample Directory

### Data Access Sample Applications:

1. [**Manual Report Viewer**](./manual-report-viewer/): A straightforward web application that initiates an inquiry, presenting the results in a user-friendly format.
2. **Internet Loan Application**: _Anticipated soon_
3. [**Account Review Report**](./account-review): A tool designed to analyze key credit metrics across a set of existing customers.

### Furnishment Sample Applications:

- _Anticipated soon_

## Setup

### API Credentials

To successfully utilize Bloom Credit APIs, an API key is indispensable. Additionally, access to the sandbox environment is needed. For access requests, please email: [inquiries@bloomcredit.io](mailto:inquiries@bloomcredit.io).

### System Prerequisites

- Python version `^3.8` or higher

### Essential Tools

- [Poetry](https://python-poetry.org/docs/): This tool handles dependency management and packaging.
  - For installation guidance, consult the [Poetry Installation Documentation](https://python-poetry.org/docs/#installation).

To install _poetry_, execute one of the following commands in your terminal:

```bash
pip install poetry
```

OR

```bash
pip3 install poetry
```

Afterward, other tools and dependencies can be accessed using `poetry` and installed with `poetry install`. Further details are elaborated below.

### Configuration

Three sample applications are available for exploration:

- /manual-report-viewer
- /internet-loan-application
- /account-review

**Navigational Tip**: From the root directory, use the following command to enter a desired sub-directory:

```bash
cd desired_directory_name
```

Inside **[/samples-data-access](./)**, create a `.env` file with the ensuing variables:

```bash
CLIENT_ID=
CLIENT_SECRET=
```

> **Note**: The `CLIENT_ID` and `CLIENT_SECRET` should be provisioned by Bloom Credit.

Once the **System Prerequisites** and **Essential Tools** listed above are in place, adopt the ensuing workflow for local development:

```bash
poetry install
```

Comprehensive documentation regarding each application is available within its respective directory.

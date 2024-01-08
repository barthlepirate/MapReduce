# MapReduce Implementation

This repository contains the implementation of a MapReduce framework using Azure Durable Functions and Azure Blob Storage. This project was created as a part of Azure Lab 2, which focuses on cloud computing concepts covered in lectures 3 and 4.

## Project Structure

- `Mapper`: Contains the code for the Mapper activity function which processes input data into key-value pairs.
- `Reducer`: Houses the Reducer activity function code that aggregates the results.
- `Shuffler`: The Shuffler activity function that organizes the output from the Mapper.
- `Fetcher`: Implementation of the GetInputDataFn activity function that retrieves input data from Azure Blob Storage.
- `HttpStart`: The HTTP trigger function that initiates the orchestration.
- `Orchestrator`: The Durable Functions orchestrator that coordinates the MapReduce tasks.

## How It Works

The framework is designed to perform word count operations on a set of documents. It follows these steps:
1. `HttpStart` triggers the `Orchestrator`.
2. `Orchestrator` invokes `GetInputDataFn` to fetch and prepare data from Azure Blob Storage.
3. `Mapper` functions process the data into intermediate key-value pairs.
4. `Shuffler` organizes the Mapper output.
5. `Reducer` functions aggregate the results.

## Running the Project

Detailed instructions on setting up the environment, deploying, and running the solution can be found in the accompanying `Azure-Lab2.pdf` document, which also includes guidelines for load testing and performance analysis.

## Prerequisites

- An Azure subscription with access to Azure Functions and Azure Blob Storage.
- Familiarity with Azure Durable Functions, as documented [here](https://learn.microsoft.com/en-us/azure/azure-functions/durable/quickstart-python-vscode).
- Understanding of the MapReduce programming model.

## Input Data

The input data for this project is a collection of text files stored in Azure Blob Storage. These files contain paragraphs from the "Saving Mr. Banks" song played in class.

## Contributions

As this project is part of a lab assignment, contributions are not currently being accepted. However, feedback on the implementation is welcome.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

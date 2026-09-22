# Mystery Delivery System

## Overview

This project is a solution for the Nexgensis Technologies Python Developer Assignment.

The program simulates a delivery system involving warehouses, delivery agents, and packages. It assigns each package to the nearest available agent, calculates delivery distances, and generates a performance report.

## Features

* Parse JSON input data
* Assign packages to the nearest delivery agent
* Calculate delivery distances using Euclidean distance
* Track packages delivered by each agent
* Calculate agent efficiency
* Identify the best-performing agent
* Generate report.json output

## Assumptions

1. Packages are assigned to the nearest available agent.

2. If two agents are at the same distance, the first matching agent is selected.

3. Efficiency is calculated as:

   efficiency = total_distance / packages_delivered

4. Agents can deliver multiple packages.

5. The solution supports both JSON formats provided in the assignment files.

## How to Run

```bash
python3 solution.py
```

## Output

The program generates a report.json file containing:

* packages_delivered
* total_distance
* efficiency
* best_agent

## Testing

The solution was successfully tested using:

* base_case.json
* test_case_1.json
* test_case_2.json
* test_case_3.json
* test_case_4.json
* test_case_5.json
* test_case_6.json
* test_case_7.json
* test_case_8.json
* test_case_9.json
* test_case_10.json

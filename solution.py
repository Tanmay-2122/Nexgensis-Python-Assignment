import json
import math

# Calculate Euclidean distance between two coordinate points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate delivery report from input JSON data
def generate_report(data):

    # Handle both JSON formats provided in assignment files
    if isinstance(data["warehouses"], list):

        # Convert warehouse list into dictionary format
        warehouses = {
            w["id"]: w["location"]
            for w in data["warehouses"]
        }

        # Convert agent list into dictionary format
        agents = {
            a["id"]: a["location"]
            for a in data["agents"]
        }

        warehouse_key = "warehouse_id"

    else:

        warehouses = data["warehouses"]
        agents = data["agents"]
        warehouse_key = "warehouse"

    # Initialize report for each agent
    report = {
        agent_id: {
            "packages_delivered": 0,
            "total_distance": 0.0,
            "efficiency": 0.0
        }
        for agent_id in agents
    }

    # Process every package
    for package in data["packages"]:

        warehouse_loc = warehouses[package[warehouse_key]]

        # Find nearest agent to package warehouse
        nearest_agent = min(
            agents,
            key=lambda a: distance(
                agents[a],
                warehouse_loc
            )
        )

        # Calculate total delivery distance
        trip_distance = (
            distance(
                agents[nearest_agent],
                warehouse_loc
            )
            +
            distance(
                warehouse_loc,
                package["destination"]
            )
        )

        # Update delivery statistics
        report[nearest_agent]["packages_delivered"] += 1
        report[nearest_agent]["total_distance"] += trip_distance

    best_agent = None
    best_efficiency = float("inf")

    # Calculate efficiency for each agent
    for agent in report:

        delivered = report[agent]["packages_delivered"]

        if delivered > 0:
            efficiency = report[agent]["total_distance"] / delivered
        else:
            efficiency = 0

        report[agent]["total_distance"] = round(
            report[agent]["total_distance"], 2
        )

        report[agent]["efficiency"] = round(
            efficiency, 2
        )

        # Select the most efficient agent
        if delivered > 0 and efficiency < best_efficiency:
            best_efficiency = efficiency
            best_agent = agent

    # Store best agent in final report
    report["best_agent"] = best_agent

    return report

# Read input JSON file
# Change file name if needed
with open("base_case.json", "r") as f:
    data = json.load(f)

# Generate report
report = generate_report(data)

# Display report on console
print(json.dumps(report, indent=4))

# Save report to report.json
with open("report.json", "w") as f:
    json.dump(report, f, indent=4)

print("report.json generated successfully")

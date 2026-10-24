# AquaRoot-X Software Simulation

dry_threshold = 600

test_values = [720, 480, 520, 680, 400]

print("AquaRoot-X Simulation")
print("---------------------")

for moisture in test_values:
    if moisture > dry_threshold:
        decision = "IRRIGATE"
    else:
        decision = "MONITOR"

    print(f"Soil Moisture: {moisture} -> Decision: {decision}")

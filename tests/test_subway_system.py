# test_cases.py

from src.subway_system import SubwaySystem

# Initialize system
system = SubwaySystem()

# Test 1: Normal trip from A to B
system.check_in("001", "A", 5)
system.check_out("001", "B", 10)

# Test 2: Another trip on same route
system.check_in("002", "A", 3)
system.check_out("002", "B", 8)

# Test 3: Invalid checkout (no check-in)
system.check_out("003", "B", 12)

# Test 4: Average from A to B
system.get_average_distance("A", "B")

# Test 5: No data for C to D
system.get_average_distance("C", "D")

# Test 6: Double check-in error
system.check_in("004", "X", 1)
system.check_in("004", "X", 2)

# Test 7: Valid check-out after fix
system.check_out("004", "Y", 6)
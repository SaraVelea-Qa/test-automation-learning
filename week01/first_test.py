# variable declaration
test_name = "Login with invalid user"
steps = 5
duration = 2.75
passed = True
expected_title = "Dashboard"
actual_title = "Login"

# print the test result
print("Test:", test_name)

# f-string
print(f"Steps: {steps}, Duration: {duration}s")

# if/else
if passed:
     print(f"✅ {test_name} PASSED")
else:
     print(f"❌ {test_name} FAILED")

# exercise 1
if expected_title == actual_title:
     print(f"✅ Title matched: {actual_title}")
else:
     print(f"❌ Title mismatch: expected {expected_title}, but got {actual_title}")
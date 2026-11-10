# variable declaration
testName = "Login with invalid user"
steps = 5
duration = 2.75
passed = True
expectedTitle = "Dashboard"
actualTitle = "Login"

# print the test result
print("Test:", testName)

# f-string
print(f"Steps: {steps}, Duration:  {duration}s")

# if/else
if passed:
     print(f"✅ {testName} PASSED")

else:
    print(f"❌ {testName} FAILED")

# exercise 1
if expectedTitle == actualTitle:
     print(f"✅ Title matched: {actualTitle}")

else:
     print(f"❌ Title mismatch: expected {expectedTitle}, but got {actualTitle}")
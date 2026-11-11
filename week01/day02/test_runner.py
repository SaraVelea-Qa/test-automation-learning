test_names = [
    "Login valid user", 
    "Login invalid user", 
    "Login invalid password", 
    "Login empty fields", 
    "Login session timeout"
    ]
results = [True, False, False, False, True]
failed_tests = []
passed_count = 0
failed_count = 0

for i in range(len(test_names)):
    print(f"Test Name: {test_names[i]}, Result: {'Passed' if results[i] else 'Failed'}")
    if results[i]:
        passed_count += 1
    else:
        failed_count += 1
        failed_tests.append(test_names[i])

print(f"Total Tests: {len(test_names)}, Passed: {passed_count}, Failed: {failed_count}")
print(f"Failed Tests: {failed_tests}")

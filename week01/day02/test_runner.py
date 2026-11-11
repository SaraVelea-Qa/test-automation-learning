test_names = ["Login valid user", "Login invalid user", "Login invalid password", "Login empty fields", "Login session timeout"]
results = [True, False, False, False, True]
failed_tests_list = []
passed_tests = 0
failed_tests = 0

for i in range(len(test_names)):
    print(f"Test Name: {test_names[i]}, Result: {'Passed' if results[i] else 'Failed'}")
    if results[i]:
        passed_tests = passed_tests + 1
    else:
        failed_tests = failed_tests + 1
        failed_tests_list.append(test_names[i])

print(f"Total Tests: {len(test_names)}, Passed: {passed_tests}, Failed: {failed_tests}")
print(f"Failed Tests: {failed_tests_list}")
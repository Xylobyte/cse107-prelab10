COURSE = cse107
GROUP_NAME = group3
ASSIGNMENT = prelab10
TARGETS = password.py sieve.py
zip: $(TARGETS)
	zip $(COURSE)_$(GROUP_NAME)_$(ASSIGNMENT).zip $(TARGETS)
	@echo "\n--- zip archive created ---\n"
	zipinfo $(COURSE)_$(GROUP_NAME)_$(ASSIGNMENT).zip
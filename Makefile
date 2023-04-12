test:
	NERGE_ADDITIONAL_PERSON_NAMES_AND_SURNAMES_FILE_PATH=tests/NERGE_ADDITIONAL_PERSON_NAMES_AND_SURNAMES_FILE_PATH_file_example.txt pytest .
test_cov_html:
	NERGE_ADDITIONAL_PERSON_NAMES_AND_SURNAMES_FILE_PATH=tests/NERGE_ADDITIONAL_PERSON_NAMES_AND_SURNAMES_FILE_PATH_file_example.txt coverage run --source=. -m pytest .
	coverage html
	python3 -m webbrowser "htmlcov/index.html"
test_cov_report:
	NERGE_ADDITIONAL_PERSON_NAMES_AND_SURNAMES_FILE_PATH=tests/NERGE_ADDITIONAL_PERSON_NAMES_AND_SURNAMES_FILE_PATH_file_example.txt coverage run --source=. -m pytest .
	coverage report -m

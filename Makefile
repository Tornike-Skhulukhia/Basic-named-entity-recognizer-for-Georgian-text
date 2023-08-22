test:
	NERGE_ADDITIONAL_PERSON_NAMES_AND_SURNAMES_FILE_PATH=tests/NERGE_ADDITIONAL_PERSON_NAMES_AND_SURNAMES_FILE_PATH_file_example.txt python3 -m coverage run -m pytest .
	python3 -m coverage report -m
YEAR ?= 2022

deps:
	pip3 install --upgrade autopep8

pretty:
	autopep8 --in-place --recursive .

copy:
	@cp -r day_temp ./${YEAR}/day_${DAY}

run:
	@python3 ${YEAR}/day_${DAY}/solution.py input.txt

test:
	@python3 ${YEAR}/day_${DAY}/solution.py test_input.txt

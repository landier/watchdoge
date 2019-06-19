clean:
	python3 -m pipenv --clear --rm

init:
	python3 -m pipenv --python 3
	python3 -m pipenv install --dev

run:
	# python3 -m pipenv run python exchange_puller.py
	# python3 -m pipenv run python events.py
	# python3 -m pipenv run python pubsub.py
	python3 -m pipenv run python data.py

shell:
	python3 -m pipenv shell

build:
	python3 -m pipenv lock --pre

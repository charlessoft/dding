install:
	python setup.py install --record files.txt
sdist:
	python setup.py sdist bdist_wheel
publish:
	twine upload dist/*
clean:
	cat files.txt | xargs rm -rf
	rm -fr ./dding.egg-info
	rm -fr ./dist
	rm -fr ./build

resetconfig:
	rm -fr ~/.dding/config.json

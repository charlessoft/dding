install:
	python setup.py install --record files.txt
sdist:
	cd dding && python setup.py sdist
clean:
	cat files.txt | xargs rm -rf
	rm -fr ./dding.egg-info
	rm -fr ./dist
	rm -fr ./build

resetconfig:
	rm -fr ~/.dding/config.json

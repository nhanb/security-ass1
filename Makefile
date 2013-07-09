zip: ceasar.py subst.py coltrans.py vernam.py 
	zip COSC2539_A1_ciphers_s3360610.zip ceasar.py subst.py coltrans.py vernam.py 

test: tests.py
	python tests.py

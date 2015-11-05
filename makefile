FILES :=                              \
    model.html                      \
    IDB1.log                       \
    apiary.apib						  \
    models.py 						\
    tests.py 						\
    UML.pdf 						\

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

config:
	git config -l

scrub:
	make clean
	rm -f  model.html
	rm -f  IDB1.log

status:
	make clean
	@echo
	git branch
	git remote -v
	git status


model.html: models.py
	pydoc3 -w models

models.log:
	git log > IDB1.log

test: tests.py
	coverage2 run    --branch tests.py >  tests.out 2>&1
	coverage2 report --omit=*site-packages* -m  >> tests.out
	cat tests.out

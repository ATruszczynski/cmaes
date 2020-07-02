FROM python:3

ADD my_script.py /
ADD cec17_python/cec17_functions.py /
ADD cec17_python/input_data ./input_data
ADD cec17_python/cec17_test_func.so /
ADD cec17_python/__init__.py /

RUN pip install cma

CMD [ "python", "./__init__.py" ]

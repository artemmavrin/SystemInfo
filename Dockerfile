FROM python:3.7
ENV HOME /home/py_info
COPY . $HOME
WORKDIR $HOME
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install --upgrade numpy scipy pandas scikit-learn tensorflow matplotlib
RUN make install
CMD py_info

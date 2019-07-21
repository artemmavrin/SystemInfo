FROM python:3.7
ENV HOME /home/py_info
COPY . $HOME
WORKDIR $HOME
RUN pip install numpy scipy pandas scikit-learn tensorflow matplotlib seaborn
RUN make install
CMD py_info

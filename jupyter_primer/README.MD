# Jupyter notebook primer
Starting from [Jupyter Notebook: An Introduction](
https://realpython.com/jupyter-notebook-introduction/), the notebook sample uses basic functions of Jupyter notebooks.

## Install Jupyter Notebook]

Pre-requisite: `pip install --upgrade setuptools`

Found at http://discuss.codingblocks.com/t/jupyter-notebook/23251, https://janakiev.com/blog/jupyter-virtual-envs/


`pip install notebook`

`pip install --user virtualenv`

To use virtualenv in the Jupyter notebook:

`python -m ipykernel install --user --name=fastaienv`

Further commands to list and uninstall virtual environments:

`jupyter kernelspec list`

`jupyter kernelspec uninstall myenv`

Start jupyter from project directory: `jupyter notebook`

*As of Python 3.8.1 on Windows, there is a bug, that prevents rendering the content.*

To work around this, change C:\Users\<user>\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\tornado\platform\asyncio.py


    # https://github.com/jupyter/notebook/issues/5094 Start
    import sys
    # https://github.com/jupyter/notebook/issues/5094 Stop
    import asyncio

    # https://github.com/jupyter/notebook/issues/5094 Start
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # https://github.com/jupyter/notebook/issues/5094 Stop
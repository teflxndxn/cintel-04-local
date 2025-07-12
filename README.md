# cintel-04-local

## Python Installation and Setup

I installed Python 3.12.1 on my macOS machine using the official installer from python.org.  
During installation, I ran the `Install Certificates.command` as instructed.

To ensure my terminal uses the official Python instead of Anaconda, I updated my PATH by adding:

```bash
export PATH="/Library/Frameworks/Python.framework/Versions/3.12/bin:$PATH"
```
After updating the PATH and restarting my terminal, I verified the Python and pip versions with the following commands:
```bash
which python3
python3 --version
python3 -m pip --version
```
Output:
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
Python 3.12.1
pip 23.2.1 from /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pip (python 3.12)


# SCPI Script Instructions

These instructions assume Windows 10.

## Install Python for Windows

The latest releases can be found here:

[Python Releases for Windows | Python.org](https://www.python.org/downloads/windows/)

Choose the following installation options:

![Python install options](images/python-install-options.png)

A User Access Control dialog may pop up asking for access privileges; click Ok to accept.

## Install Python Package(s)

The script uses the python package (library) `rohdeschwarz`. Python comes with a package manager, `pip`, which can be used from the command line.

Open your terminal of choice from the start menu (e.g. `cmd.exe` or Powershell).

If you are off-VPN, type in:

```shell
pip install rohdeschwarz
```

This will fail behind VPN unless we add proxy information. Try again with your username and proxy (internet) password:

```shell
pip install --proxy "https://<username>:<password>@<proxy>:<port>"
```

Note that the port is optional; the default value is 80.

Here is an example:

```shell
pip install --proxy "https://elmo:OpenSesame@proxy.sesame-street.org"
```

**Note that any special characters in your password will have to be [url encoded](https://www.w3schools.com/tags/ref_urlencode.ASP).**

## Run Script

The python installer associates file extension `.py` with python; you can double-click the script to run it.

If the window disappears too quickly (e.g. due to an error), run the script from the command line instead:

```shell
cd path/to/scpi_script.py
python scpi_script.py
```

## Errors

The most common error is due to connection timeout, for example when the instrument cannot be reached.

```shell
> python .\scpi_script.py
Traceback (most recent call last):
  File ".\scpi_script.py", line 6, in <module>
    instr.open_tcp('localhost')
  File "C:\Users\VM\AppData\Local\Programs\Python\Python38\lib\site-packages\rohdeschwarz\instruments\genericinstrument.py", line 32, in open_tcp
    self.bus.open(ip_address, socket)
  File "C:\Users\VM\AppData\Local\Programs\Python\Python38\lib\site-packages\rohdeschwarz\bus\tcp.py", line 86, in open
    self.__socket.connect((address, port))
socket.timeout: timed out
```

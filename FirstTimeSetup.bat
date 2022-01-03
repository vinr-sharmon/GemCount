py -m pip install -r requirements.txt
pip install pipupgrade
pipupgrade --verbose --latest --yes
del requirements.txt
del FirstTimeSetup.bat
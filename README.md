# PII_PCI_Redactor

## Quick Usage
install using   
`pip install git+https://github.com/AlbinRaven/PII_PCI_Redactor.git#egg=PII_PCI_Redactor`  
  
then import it to your code  
```
from PII_PCI_Redactor import redactor
... 
redactor.redact_pii_pci(json_str)
```
  
Testing if the pacakge is working properly  
```
test_res_id, test_res_text = redactor.test_redact_pii_pci()
if test_res_id == 1:
    print("Test Passed")
```

## Adding Custom PCI/PII Regex to the library

In order to add custom regex pattern, you will have to  
1. Clone the repository locally  
2. Edit the PII_regex and PCI_regex to add your pattern
3. Run setup.py

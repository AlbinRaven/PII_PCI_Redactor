import re

PII_REGEX = [
    {"email_address": r"\b[a-z0-9._%+\-—|]+@[a-z0-9.\-—|]+\.[a-z|]{2,6}\b"}
]

PCI_REGEX = [
    {"credit_card": r"4\d{3}(\s+|-)?\d{4}(\s+|-)?\d{4}(\s+|-)?\d{4}"},
    {"loosened_credit_card": r"^4(?:\D*\d){15}$"}
]

def redact_pii_pci(json_str):
    for pattern_set in (PII_REGEX, PCI_REGEX):
        for pattern_dict in pattern_set:
            for key, pattern in pattern_dict.items():
                json_str = re.sub(pattern, "[REDACTED]", json_str)
    return json_str

def test_redact_pii_pci():
    test_input = '{"name": "John", "email_address": "john@example.com", "credit_card": "4123 4567 8901 2345"}'
    expected_output = '{"name": "John", "email_address": "[REDACTED]", "credit_card": "[REDACTED]"}'
    assert redact_pii_pci(test_input) == expected_output, "Redaction failed"
    return 1, "test passed"

if __name__ == "__main__":
    test_redact_pii_pci()
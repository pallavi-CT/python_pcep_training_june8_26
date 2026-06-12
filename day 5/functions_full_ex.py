#Scenario: Build a mini event processing pipeline using functions:
# 1. Write pipeline(*functions) that returns a function which chains all functions left-to-right (output of one feeds next)
# 2. Write transformation functions: normalize_keys(record) (lowercase all keys), add_timestamp(record) (adds current timestamp), validate_required(record, *required_fields) (raises if missing), mask_sensitive(record, *fields) (replaces values with "***")
# 3. Using pipeline(), compose a data processing chain for user registration events
# 4. Write process_batch(records, transform_fn, *args, on_error="skip", **kwargs) — applies transform to each record; on error either "skip" or "raise"
# 5. Test with sample registration events including one with missing fields

from datetime import datetime
from functools import reduce

# 1. Pipeline composer
def pipeline(*functions):
    """Compose functions left-to-right into a single function."""
    def composed(data):
        return reduce(lambda v, f: f(v), functions, data)
    return composed

# 2. Transformation functions
def normalize_keys(record: dict) -> dict:
    return {k.lower().strip(): v for k, v in record.items()}

def add_timestamp(record: dict) -> dict:
    return {**record, "processed_at": datetime.now().isoformat()}

def make_validator(*required_fields):
    """Closure: returns a validator for the given required fields."""
    def validate(record: dict) -> dict:
        missing = [f for f in required_fields if f not in record]
        if missing:
            raise ValueError(f"Missing required fields: {missing}")
        return record
    return validate

def make_masker(*sensitive_fields):
    """Closure: returns a masker for specified fields."""
    def mask(record: dict) -> dict:
        return {k: ("***" if k in sensitive_fields else v)
                for k, v in record.items()}
    return mask

# 3. Build registration pipeline
process_registration = pipeline(
    normalize_keys,
    make_validator("email", "name", "password"),
    make_masker("password"),
    add_timestamp,
)

# 4. Batch processor
def process_batch(records, transform_fn, on_error="skip"):
    results, errors = [], []
    for i, record in enumerate(records):
        try:
            results.append(transform_fn(record))
        except Exception as e:
            if on_error == "raise":
                raise
            errors.append({"index": i, "record": record, "error": str(e)})
    return {"processed": results, "errors": errors}

# 5. Test
registrations = [
    {"Name": "Alice", "Email": "alice@example.com", "Password": "s3cr3t"},
    {"name": "Bob",   "email": "bob@example.com"},   # Missing password!
    {"NAME": "Carol", "EMAIL": "carol@ex.com", "PASSWORD": "abc123"},
]

output = process_batch(registrations, process_registration, on_error="skip")
print(f"Processed: {len(output['processed'])} | Errors: {len(output['errors'])}")
for r in output["processed"]:
    print("OK", {k: v for k, v in r.items() if k != "processed_at"})
for e in output["errors"]:
    print(f" Wrong Record {e['index']}: {e['error']}")
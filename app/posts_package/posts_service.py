def validate_keys(payload: dict, expected_keys: set):
    body_keys = set(payload.keys())

    invalid_keys = body_keys - expected_keys

    if invalid_keys:
        raise KeyError(
            {
                "error": "invalid_keys",
                "expected": list(expected_keys),
                "received": list(body_keys),
            }
        )
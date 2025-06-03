def extract_features(email):
    headers = email['Content']['Headers']
    return {
        "spf_result": headers.get("Received-SPF", ["none"])[0],
        "dkim_result": headers.get("DKIM-Signature", ["missing"])[0],
        "from_vs_return_path": headers.get("From", [""])[0] != headers.get("Return-Path", [""])[0],
        "reply_to_mismatch": headers.get("From", [""])[0] != headers.get("Reply-To", [""])[0],
        "subject_entropy": len(set(headers.get("Subject", [""])[0]))  # crude entropy
    }

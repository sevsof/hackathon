class Email:
    def __init__(self, filename, subject="", sender="", body="",
                 status="ok", reason=""):
        self.filename = filename
        self.subject = subject
        self.sender = sender
        self.body = body
        self.status = status    
        self.reason = reason

    def __repr__(self):
        return (f"Email(filename={self.filename!r}, status={self.status!r}, "
                f"subject={self.subject!r})")
        
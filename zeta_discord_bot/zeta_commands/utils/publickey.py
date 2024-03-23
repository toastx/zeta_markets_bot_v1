import base58

class PublicKey:
    LENGTH = 32
    def __init__(self, value: str | list[int]):
        if isinstance(value, str):
            try:
                self.byte_value = base58.b58decode(value)
            except ValueError:
                raise ValueError("Invalid public key.")
        else:
            self.byte_value = bytes(value)

        if len(self.byte_value) != self.LENGTH:
            raise ValueError("error")

    def __bytes__(self) -> bytes:
        return (
            self.byte_value
            if len(self.byte_value) == self.LENGTH
            else self.byte_value.rjust(self.LENGTH, b"\0")
        )

    def __str__(self) -> str:
        return self.base58_encode().decode("utf-8")

    def base58_encode(self) -> bytes:
        return base58.b58encode(bytes(self))

    def base58_decode(self) -> bytes:
        return base58.b58decode(self.byte_value)

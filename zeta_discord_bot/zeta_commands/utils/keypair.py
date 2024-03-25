from __future__ import annotations
import base58
from typing import List
from nacl.signing import SigningKey
from nacl.public import PrivateKey as NaclPrivateKey



class Keypair:
    def __init__(self, keypairnacl: NaclPrivateKey | None = None) -> None:
            self.key_pair = keypairnacl
            verify_key: bytes = bytes(
                                SigningKey(bytes(self.key_pair)).verify_key
                                )
            self.public_key = PubKey(verify_key)
            self.private_key = bytes(self.key_pair) + bytes(self.public_key)

            

    @classmethod
    def from_private_key(cls, private_key: str | List[int]) -> Keypair:
        if isinstance(private_key, list):
            private_key = bytes(private_key)
        elif isinstance(private_key, str):
            
            try:
                private_key = base58.b58decode(private_key)
            except Exception as e:
                raise ValueError(f"Error decoding private key: {str(e)}")
        
        seed = private_key[:32]
        return cls(NaclPrivateKey(seed))
    
   
        
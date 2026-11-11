import hmac

class CryptoService:

    supported_algs = {
        "sha256": ("HMAC", "sha256"),
        "sha512": ("HMAC", "sha512")
    }

    @classmethod
    def execute(cls, alg):
        function, algorithm = cls.supported_algs[alg]

        result = hmac.new(
            b"secret",
            b"message",
            digestmod=algorithm
        )

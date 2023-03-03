"""
Определите исключение OopsException. Сгенерируйте его и посмотрите, что
произойдет. Затем напишите код, позволяющий поймать это исключение и вывести строку 'Caught an oops'.
"""


class OopsException(Exception):
    pass


words = ["oops", "OOPS", "oOPs", "OOPS", "Oops"]
for word in words:
    if word == "Oops":
        # raise OopsException(word)

        try:
            raise OopsException('Caught an oops')

        except OopsException as exc:
            print(exc)
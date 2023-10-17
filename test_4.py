import tempfile


class Resource:

    def __init__(self):
        self.__file = tempfile.TemporaryFile(mode='a+', buffering=- 1, encoding=None,
                                             newline=None, suffix=None, prefix=None,
                                             dir=None, errors=None)
    def repeat(self):
        self.__file.seek(0)
        content = self.__file.read()
        self.__file.write(content)

    def write(self, msg):
        self.__file.seek(0)
        content = self.__file.read()
        self.__file.seek(0)
        self.__file.write(msg + "\n" + content)

    def show(self):
        self.__file.seek(0)
        print(self.__file.read())

    def close(self):
        self.__file.close()


class ContextManager:
    def __init__(self):
        self.__resource = Resource()

    def __enter__(self):
        return self.__resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__resource:
            self.__resource.close()


if __name__ == '__main__':
    with ContextManager() as cm:
        cm.write('wow how do you do?')
        cm.write('your next line will be "wow how do you do?"')
        cm.write('i\'m from future')
        cm.repeat()
        cm.repeat()
        cm.show()
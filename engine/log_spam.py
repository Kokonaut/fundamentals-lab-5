class LogSpam:

    def __init__(self):
        self.mem = dict()

    def check(self, character_id, message):
        if (character_id in self.mem
                and message == self.mem[character_id]):
            return False
        self.mem[character_id] = message
        return True

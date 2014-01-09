def say(statement):
    print statement

def shout(statement):
    say(statement.upper())

class QuietTalker:
    def say(self, statement):
        say('Quiet Talker: {}'.format(statement))

    def shout(self, statement):
        self.say('Pardon, my loudness, but {}'.format(
            statement.upper())
        )
        say('Ahem.')

class LoudTalker:
    def say(self, statement):
        shout('LoudTalker: {}'.format(statement))

say('hello')
quietTalker = QuietTalker()
loudTalker = LoudTalker()

quietTalker.say('I am quiet talker.')
loudTalker.say('I am loud talker!!')
quietTalker.shout('Why are you yelling?')

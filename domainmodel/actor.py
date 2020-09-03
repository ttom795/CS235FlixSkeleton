class Actor:
    def __init__(self, actorName):
        self.actor = actorName
        self.colleagueList = []
    def __repr__(self):
        actorReturn = self.actor
        boolean = True
        if str(self.actor).isnumeric() or self.actor == "":
            return "<Actor None>"
        return f'<Actor {self.actor}>'
    def __eq__(self, toCompare):
        return self.actor == toCompare.actor
    def __lt__(self, toCompare):
        return self.actor < toCompare.actor
    def __hash__(self):
        return hash(self.actor)
    def add_actor_colleague(self, colleague):
        self.colleagueList.append(colleague.actor)
    def check_if_this_actor_worked_with(self, colleague):
        return colleague.actor in self.colleagueList
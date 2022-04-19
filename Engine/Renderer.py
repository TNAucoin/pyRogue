import tcod

from Actors import Entity


class Render:
    def __init__(self, console):
        self.console = console

    def render(self, entities):
        for entity in entities:
            self.draw_entity(entity)

    def draw_entity(self, entity: Entity):
        tcod.console_set_default_foreground(self.console, entity.color)
        print(entity.x)
        tcod.console_put_char(self.console, entity.x, entity.y, entity.char, tcod.BKGND_NONE)

    def clear_entity(self, entity: Entity):
        tcod.console_put_char(self.console, entity.x, entity.y, ' ', tcod.BKGND_NONE)

    def clear_all(self, entities):
        for entity in entities:
            self.clear_entity(entity)

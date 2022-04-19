#!/usr/bin/python
import tcod
from tcod import Console
from tcod.tileset import Tileset

from globals import SCREEN_WIDTH, SCREEN_HEIGHT
from Engine.Renderer import Render
from Actors.Entity import Entity


def init() -> tuple[Console, Tileset, Render]:
    font_path = './Assets/dejavu10x10_gs_tc.png'
    tile_set = tcod.tileset.load_tilesheet(font_path, 32, 8, tcod.tileset.CHARMAP_TCOD)
    console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, "F")
    renderer = Render(console)
    return console, tile_set, renderer


def game_loop(console: tcod.Console, tileset: Tileset, renderer: Render) -> None:
    with tcod.context.new(columns=console.width, rows=console.height, tileset=tileset) as context:
        player = Entity("@", tcod.white)\
            .set_position((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        while True:
            console.clear()
            console.print(x=0, y=0, string="Hello PyRogue")
            renderer.draw_entity(player)
            context.present(console)

            for event in tcod.event.wait():
                context.convert_event(event)
                print(event)
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()


def main() -> None:
    console, tile_set, renderer = init()
    game_loop(console, tile_set, renderer)


if __name__ == "__main__":
    main()

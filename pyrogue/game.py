from typing import Tuple

import tcod
from tcod import Console
from tcod.tileset import Tileset

import globals


def init() -> tuple[Console, Tileset]:
    font_path = 'dejavu10x10_gs_tc.png'
    tile_set = tcod.tileset.load_tilesheet(font_path, 32, 8, tcod.tileset.CHARMAP_TCOD)
    console = tcod.Console(globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT, "F")
    return console, tile_set


def game_loop(console: tcod.Console, tileset: Tileset) -> None:
    with tcod.context.new(columns=console.width, rows=console.height, tileset=tileset) as context:
        while True:
            console.clear()
            console.print(x=0, y=0, string="Hello PyRogue")
            context.present(console)

            for event in tcod.event.wait():
                context.convert_event(event)
                print(event)
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()


def main() -> None:
    console, tile_set = init()
    game_loop(console, tile_set)


if __name__ == "__main__":
    main()

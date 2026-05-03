from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, nickname: str,
                 musical_instrument: str, favorite_spell: str) -> None:
        self._favorite_spell = favorite_spell
        super().__init__(nickname, musical_instrument)

    def player_info(self) -> str:
        name = self.nickname
        spell = self._favorite_spell
        return f"Druid {name}. {name} has a favourite spell: {spell}"

    def get_rating(self) -> int:
        return len(self._favorite_spell)

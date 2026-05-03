from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, nickname: str,
                 _musical_instrument: str, _favorite_spell: str) -> None:
        self._favorite_spell = _favorite_spell
        super().__init__(nickname, _musical_instrument)

    def player_info(self) -> str:
        name = self.nickname
        spell = self._favorite_spell
        return f"Druid {name}. {name} has a favourite spell: {spell}"

    def get_rating(self) -> int:
        return len(self._favorite_spell)

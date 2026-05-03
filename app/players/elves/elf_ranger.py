from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname: str, _musical_instrument:
                 str, _bow_level: int) -> None:
        self._bow_level = _bow_level
        super().__init__(nickname, _musical_instrument)

    def player_info(self) -> str:
        name = self.nickname
        bow = self._bow_level
        return f"Elf ranger {name}. {name} has bow of the {bow} level"

    def get_rating(self) -> int:
        return self._bow_level * 3

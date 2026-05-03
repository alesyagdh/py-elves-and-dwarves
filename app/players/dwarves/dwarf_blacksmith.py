from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str,
                 _favorite_dish: str, _skill_level: int) -> None:
        self._skill_level = _skill_level
        super().__init__(nickname, _favorite_dish)

    def player_info(self) -> str:
        name = self.nickname
        skill = self._skill_level
        return f"Dwarf blacksmith {name} with skill of the {skill} level"

    def get_rating(self) -> int:
        return self._skill_level

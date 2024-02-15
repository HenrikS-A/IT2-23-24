class Pokemon:
    def __init__(self, pokemon_info) -> None:
        self.navn: str = pokemon_info["name"]["english"]
        self.typer: list[str] = pokemon_info["type"]
        self.stats: dict[str, int] = pokemon_info["base"]

    def __str__(self) -> str:
        return f"{self.navn} - HP: {self.stats['HP']}"

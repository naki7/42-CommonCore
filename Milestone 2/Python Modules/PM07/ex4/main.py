from ex4.TournamentCard import TournamentCard as TournCard
from ex4.TournamentPlatform import TournamentPlatform as TournPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")

    drag_card: TournCard = TournCard("Fire Dragon", 5, "Legendary")
    wiz_card: TournCard = TournCard("Ice Wizard", 3, "Common")
    main_platform: TournPlatform = TournPlatform()

    drag_stats: str = main_platform.register_card(drag_card)
    print(drag_stats)

    wiz_stats: str = main_platform.register_card(wiz_card)
    print(wiz_stats)

    print("Creating tournament match...")
    match_result = main_platform.create_match('dragon_001', 'wizard_001')
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard: list = main_platform.get_leaderboard()
    for ranking in leaderboard:
        print(ranking)

    print("\nPlatform Report:")
    report: dict = main_platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()

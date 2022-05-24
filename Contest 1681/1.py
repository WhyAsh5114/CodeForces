for _ in range(int(input())):
    n = int(input())
    alice_cards = [int(x) for x in input().split()]
    m = int(input())
    bob_cards = [int(x) for x in input().split()]
    alice_max = max(alice_cards)
    bob_max = max(bob_cards)

    if alice_max > bob_max:
        alice_winner, bob_winner = "Alice", "Alice"
    elif alice_max < bob_max:
        alice_winner, bob_winner = "Bob", "Bob"
    else:
        alice_winner, bob_winner = "Alice", "Bob"

    print(alice_winner)
    print(bob_winner)
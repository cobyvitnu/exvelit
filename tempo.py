def approve_delegation(address_wallet: str, error: str) -> None:
    """Approve delegation to the wallet address.

    Args:
        address_wallet (str): The wallet address to approve delegation to.
        error (str): The error message to display if the delegation approval fails.
    """
    try:
        # Approve delegation to the wallet address.
        approve_delegation_response = client.approve_delegation(address_wallet)

        # Check if the delegation approval was successful.
        if approve_delegation_response.status_code == 200:
            cprint(f'\n>>> approve_delegation radiant | {address_wallet} | success', 'green')
        else:
            cprint(f'\n>>> approve_delegation radiant | {address_wallet} | {error}', 'red')
    except Exception as e:
        cprint(f'\n>>> approve_delegation radiant | {address_wallet} | {error}', 'red')
        raise e


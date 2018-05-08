def current_user(request):
    return dict(
        current_user=dict(
            login='Nikita Rubinov',
            id=1,
            logged=1
        ),
    )
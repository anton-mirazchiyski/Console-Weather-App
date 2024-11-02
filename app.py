def validate_user_input(city_name):
    return city_name.isalpha()


def get_user_input(text='Enter city name: '):
    city_name = input(text)
    result = validate_user_input(city_name)
    return get_user_input(text='Enter a valid city name: ') if not result else city_name


def main():
    user_input = get_user_input()


if __name__ == '__main__':
    main()

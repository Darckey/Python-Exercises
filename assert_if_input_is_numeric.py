def assert_if_input_is_numeric(u_input):
    try:
        value = int(u_input)
        print(f'Correct, you gave numeric valua => {value}')
    except ValueError:
        try:
            value = float(u_input)
            print(f'Correct, you gave numeric valua with decimals => {value}')
        except ValueError:
            print(input(f'Enterad value "{u_input}" is not numeric!'))


user_input = input("Enter numeric value! ")
assert_if_input_is_numeric(user_input)

#comment